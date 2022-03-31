import json
import http.client as httplib
import os
import mimetypes
import time
import urllib.parse as urlparse
import urllib

def get_credentials():
    creds_file_name = "sharefile_credentials"
    creds_file_path = os.path.join(os.getcwd(), creds_file_name)
    file = open(creds_file_path, 'r')
    lines = file.readlines()
    if len(lines) != 5:
        raise Exception("Credentials file: sharefile_credentials is invalid")
    hostname, client_id, client_secret, username, password = lines
    hostname = hostname.strip()
    client_id = client_id.strip()
    client_secret = client_secret.strip()
    username = username.strip()
    password = password.strip()
    return hostname, client_id, client_secret, username, password


def authenticate(hostname, client_id, client_secret, username, password):
    uri_path = '/oauth/token'
    headers = {'Content-Type':'application/x-www-form-urlencoded'}
    params = {'grant_type':'password'
                    , 'client_id':client_id
                    , 'client_secret':client_secret
                    , 'username':username
                    , 'password':password}
    http = httplib.HTTPSConnection(hostname)
    http.request('POST'
                    , uri_path, urlparse.urlencode(params)
                    , headers=headers)
    response = http.getresponse()
    token = None
#     print(response.read())
    if response.status == 200:
        token = json.loads(response.read())
    http.close()
    return token


def get_authorization_header(token):
    return {'Authorization':'Bearer %s'%(token['access_token'])}


def get_hostname(token):
    return '%s.sf-api.com'%(token['subdomain'])


def get_dir_list(token, get_children=True, fid="allshared"):
    """ Get the root level Item for the provided user. To retrieve Children the $expand=Children
    parameter can be added.

    Args:
    dict json token acquired from authenticate function
    boolean get_children - retrieve Children Items if True, default is False"""

    uri_path = '/sf/v3/Items({})'.format(fid)
    if get_children:
        uri_path = '%s?$expand=Children' % (uri_path)
    #     print ('GET %s%s'%(get_hostname(token), uri_path))
    http = httplib.HTTPSConnection(get_hostname(token))
    http.request('GET', uri_path, headers=get_authorization_header(token))
    response = http.getresponse()

    #     print (response.status, response.reason)
    items = json.loads(response.read())
    #     print (items['Id'], items['CreationDate'], items['Name'])
    context = {"id": items['Id']}
    all_children = []
    if 'Children' in items:
        children = items['Children']
        for child in children:
            #             print(child['Id'], items['CreationDate'], child['Name'])
            all_children.append([child['Id'], items['CreationDate'], child['Name']])
    context["children"] = all_children
    return context


def download_item(token, item_id, local_path):
    """ Downloads a single Item. If downloading a folder the local_path name should end in .zip.

    Args:
    dict json token acquired from authenticate function
    string item_id - the id of the item to download
    string local_path - where to download the item to, like "c:\\path\\to\\the.file" """

    uri_path = '/sf/v3/Items(%s)/Download' % (item_id)
    # print('GET %s%s' % (get_hostname(token), uri_path))
    http = httplib.HTTPSConnection(get_hostname(token))
    http.request('GET', uri_path, headers=get_authorization_header(token))
    response = http.getresponse()
    location = response.getheader('location')
    redirect = None
    if location:
        redirect_uri = urlparse.urlparse(location)
        redirect = httplib.HTTPSConnection(redirect_uri.netloc)
        redirect.request('GET', '%s?%s' % (redirect_uri.path, redirect_uri.query))
        response = redirect.getresponse()

    with open(local_path, 'wb') as target:
        b = response.read(1024 * 8)
        while b:
            target.write(b)
            b = response.read(1024 * 8)

    # print(response.status, response.reason)
    http.close()
    if redirect:
        redirect.close()


def multipart_form_post_upload(url, filepath):
    """ Does a multipart form post upload of a file to a url.

    Args:
    string url - the url to upload file to
    string filepath - the complete file path of the file to upload like, "c:\path\to\the.file

    Returns:
    the http response """

    #     print(url)

    newline = b'\r\n'
    filename = os.path.basename(filepath)
    data = []
    headers = {}
    boundary = '----------%d' % int(time.time())
    headers['content-type'] = 'multipart/form-data; boundary=%s' % boundary
    data.append(('--%s' % boundary).encode('utf-8'))
    data.append(('Content-Disposition: form-data; name="%s"; filename="%s"' % ('File1'
                                                                               , filename)).encode('utf-8'))
    data.append(('Content-Type: %s' % get_content_type(filename)).encode('utf-8'))
    data.append(('').encode('utf-8'))
    data.append(open(filepath, 'rb').read())
    data.append(('--%s--' % boundary).encode('utf-8'))
    data.append(('').encode('utf-8'))
    data_str = newline.join(data)
    headers['content-length'] = len(data_str)
    uri = urlparse.urlparse(url)
    http = httplib.HTTPSConnection(uri.netloc)
    http.putrequest('POST', '%s?%s' % (uri.path, uri.query))
    for hdr_name, hdr_value in headers.items():
        http.putheader(hdr_name, hdr_value)
    http.endheaders()
    http.send(data_str)
    return http.getresponse()


def get_content_type(filename):
    return mimetypes.guess_type(filename)[0] or 'application/octet-stream'


def upload_file(token, folder_id, local_path):
    """ Uploads a File using the Standard upload method with a multipart/form mime encoded POST.

    Args:
    dict json token acquired from authenticate function
    string folder_id - where to upload the file
    string local_path - the full path of the file to upload, like "c:\\path\\to\\file.name" """

    uri_path = '/sf/v3/Items(%s)/Upload' % (folder_id)
    #     print ('GET %s%s'%(get_hostname(token), uri_path))
    http = httplib.HTTPSConnection(get_hostname(token))
    http.request('GET', uri_path, headers=get_authorization_header(token))

    response = http.getresponse()
    upload_config = json.loads(response.read())
    print(upload_config)
    if 'ChunkUri' in upload_config:
        upload_response = multipart_form_post_upload(upload_config['ChunkUri'], local_path)
        # print("\t\t\t\t", upload_response.status, upload_response.reason)
        print("\t\t\t\t", upload_response.read())
    else:
        print('No Upload URL received')


def delete_file(token, fid):
    #     https://account.sf-api.com/sf/v3/Items(id)

    uri_path = '/sf/v3/Items(%s)' % (fid)
    #     print ('GET %s%s'%(get_hostname(token), uri_path))
    http = httplib.HTTPSConnection(get_hostname(token))
    http.request('DELETE', uri_path, headers=get_authorization_header(token))
    response = http.getresponse()
    # print(response.read())
    return response

hostname, client_id, client_secret, username, password = get_credentials()
TOKEN = authenticate(hostname, client_id, client_secret, username, password)


def get_dir_list_wrapper(get_children=True, fid="allshared"):
    global TOKEN
    return get_dir_list(TOKEN, get_children, fid)


def download_item_wrapper(item_id, local_path):
    global TOKEN
    download_item(TOKEN, item_id, local_path)


def upload_file_wrapper(folder_id, local_path):
    global TOKEN
    upload_file(TOKEN, folder_id, local_path)


def delete_file_wrapper(file_id):
    global TOKEN
    delete_file(TOKEN, file_id)
