import os
from pathlib import Path
import shutil
from textnode import TextNode, TextType

def main():

    public_dir_path = os.path.abspath("public")
    static_dir_path = os.path.abspath("static")

    empty_public_dir(public_dir_path, static_dir_path)
    copy_static_to_public(source_path=static_dir_path, destination_path=public_dir_path)



#Function to delete all the contents of the public directory.
def empty_public_dir(public_dir_path, static_dir_path):
    try:
        if os.listdir(public_dir_path):
            print("Existing content found in public directory. Deleting all contents..")
            for item in os.listdir(public_dir_path):
                if os.path.isdir(os.path.join(public_dir_path, item)):
                    shutil.rmtree(os.path.join(public_dir_path, item))
                else:
                    os.remove(os.path.join(public_dir_path, item))
            print("Deleted all contents in public directory")
    except Exception as e:
        print(f"Creating a public folder in the root directory. More details: {e}")
        os.mkdir(public_dir_path)
    

#Function to copy all assets from static dir to public dir. 
def copy_static_to_public(source_path, destination_path):
    try:
        if os.listdir(source_path):
            for item in os.listdir(source_path):
                if os.path.isdir(os.path.join(source_path, item)):
                    os.mkdir(os.path.join(destination_path, item))
                    copy_static_to_public(os.path.join(source_path, item), os.path.join(destination_path, item))
                else:
                    shutil.copy(os.path.join(source_path, item), destination_path)
                    print(f"{item} moved to {destination_path}")
    except Exception as e:
        print(f"Static assets are not present. More details: {e}")







if __name__ == "__main__":
    main()