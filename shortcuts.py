import sharefile as SF
import form_readers as FR
import helper
import pandas as pd


def remove_all_xlsx():
    change_sharefile = True
    data = SF.get_dir_list_wrapper()
    # print(data['children'])
    for client in data['children']:
        this_client_name = client[2]
        print("Processing client:", this_client_name)
        years = SF.get_dir_list_wrapper(fid=client[0])
        for year in years['children']:
            this_year = year[2]
            forms = SF.get_dir_list_wrapper(fid=year[0])
            print("\tProcessing year:", this_year)
            # print(forms['children'])
            for form in forms['children']:
                this_form_name = form[2]
                print("\t\tProcessing form:", this_form_name)
                this_form_folder_id = form[0]
                pdfs = SF.get_dir_list_wrapper(fid=form[0])['children']
                xlsxs = [x for x in pdfs if x[2].split(".")[-1] == "xlsx"]
                # print(xlsxs)

                for i, xlsx in enumerate(xlsxs):
                    xlsx_id = xlsx[0]
                    xlsx_name = xlsx[2]
                    print("\t\t\tDeleting: ", xlsx_name)
                    SF.delete_file_wrapper(xlsx_id)


def upload_an_excel(folder_id, path):
    print("uploading: ", path)
    print("to folder: ", folder_id)
    SF.upload_file_wrapper(folder_id, path)


remove_all_xlsx()
# upload_an_excel("fo71d0aa-4ea4-408d-ae64-d35df5454cf1", "/home/blaze/Desktop/Cygnus-Datasets/suri/history.xlsx")
