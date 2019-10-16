import os
import re

dir = r'D:\work\Projects\practice\data\prank'

def rename_files():
    # get file names for a directory 
    file_list = os.listdir(dir)
    print(file_list)
    # for each file rename the file
    for file in file_list:
        os.rename(os.path.join(dir, file), os.path.join(dir, re.sub(r'[0-9]', '',file)))

if __name__ == '__main__':
    rename_files()