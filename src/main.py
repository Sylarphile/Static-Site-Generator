import os
import shutil
import sys
from static_to_public import copy_to_public
from block_markdown import generate_page_recursive

def main():

    basepath = "/"
    basepath = f"{sys.argv[1]}/"

    dst = "./docs"
    src = "./static"
    content = "./content"
    template = "./template.html"

    print("Deleting docs directory...")
    file_list = os.listdir(src)

    if os.path.exists(dst):
        shutil.rmtree(dst)
        os.mkdir(dst)
    else:
        os.mkdir(dst)

    print("Copying static files to public directory...")

    copy_to_public(src, dst, file_list)
   
    generate_page_recursive(
        content,
        template,
        dst,
        basepath
    )
        
main()