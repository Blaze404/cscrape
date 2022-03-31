import sharefile as SF
import form_readers as FR
import helper
import pandas as pd
import time

change_sharefile = True
delay1 = 1
delay2 = 6

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
            pdfs = [x for x in pdfs if x[2].split(".")[-1] == "pdf"]
            # print(pdfs)
            pdfs_sorted = sorted(pdfs, key=lambda x: x[1], reverse=True)
            ftype, df = helper.get_form_handler(this_form_name)
            global_df = df
            first = True
            for i, pdf in enumerate(pdfs_sorted):
                # print(pdf)
                current_path = "/home/blaze/Desktop/Cygnus-Datasets/suri/{}.pdf".format(str(i + 1))
                if change_sharefile:
                    SF.download_item_wrapper(pdf[0], current_path)
                # print(ftype)
                if ftype == '480.6 A' and change_sharefile:
                    this_df = FR.read_suri_files_form_a(current_path)
                elif ftype == '480.6 D' and change_sharefile:
                    this_df = FR.read_suri_files_form_d(current_path)
                elif ftype == "480.6 EC" and change_sharefile:
                    this_df = FR.read_suri_files_form_ec(current_path)
                elif ftype == "480.6 SP" and change_sharefile:
                    this_df = FR.read_suri_files_form_sp(current_path)
                else:
                    this_df = None
                if first and change_sharefile:
                    current_excel_path = "/home/blaze/Desktop/Cygnus-Datasets/suri/latest.xlsx"
                    this_df.to_excel(current_excel_path)
                    time.sleep(delay1)
                    print("\t\t\tUploading: ", current_excel_path)
                    print("\t\t\tUploading to folder: ", this_form_folder_id)
                    SF.upload_file_wrapper(this_form_folder_id, current_excel_path)
                    time.sleep(delay2)

                    first = False
                global_df = pd.concat([global_df, this_df], ignore_index=True)
            if change_sharefile:
                history_excel_path = "/home/blaze/Desktop/Cygnus-Datasets/suri/history.xlsx"
                global_df.to_excel(history_excel_path)
                time.sleep(delay1)
                print("\t\t\tUploading:", history_excel_path)
                SF.upload_file_wrapper(this_form_folder_id, history_excel_path)
                print("\t\t\tUploading to folder: ", this_form_folder_id)
                time.sleep(delay1)
                #
                # upload_file(token, this_form, current_excel_path)

                # global_df = pd.concat([a, b], ignore_index=True)