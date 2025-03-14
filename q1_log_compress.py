import os
import zipfile
from datetime import date
import datetime

def list_file_properties(directory_path):
    if not os.path.isdir(directory_path):
        print(f"Error: {directory_path} is not a valid directory")
        return

    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path)
            if file_size / (1024 * 1024 ) >=100 and os.path.splitext(file_path)[1] != ".zip":
                output_zip_name = os.path.basename(file_path) + '.zip'
                with zipfile.ZipFile(output_zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
                    zipf.write(file_path, os.path.basename(file_path + '/archive'))

            created_timestamp = os.path.getctime(file_path)
            created_date = datetime.datetime.fromtimestamp(created_timestamp)
            if (datetime.datetime.now() - created_date).days >= 30 and os.path.splitext(file_path)[1] == ".zip":
                os.remove(file_path)



if __name__ == "__main__":
    list_file_properties("/var/log")
    print(f"Script Execution Completed")