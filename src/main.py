import os
import shutil
from static_to_public import copy_to_public

def main():

    dst = "./public"
    src = "./static"

    print("Deleting public directory...")
    file_list = os.listdir(src)

    if os.path.exists("./public"):
        shutil.rmtree(dst)
        os.mkdir(dst)
    else:
        os.mkdir(dst)

    print("Copying static files to public directory...")

    copy_to_public(src, dst, file_list)
        
main()