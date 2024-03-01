import os


def remove_ds_store(dir_path):
    """
    Removes all .DS_Store files in the given directory and its subdirectories on macOS.
    """
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file == ".DS_Store":
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"Removed file: {file_path}")


def __main__():
    pwd = os.getcwd()

    # find startFolder
    if "startFolder" in os.listdir(pwd):
        print("start searching")
        # rm MacOS-product trash file
        remove_ds_store(pwd)
        # concatenate paths to each namefolder
        allnameFolders = [pwd + '/startFolder/' + each for each in os.listdir("./startFolder/")]

        for folder in allnameFolders:
            numFound = len(os.listdir(folder))
            if numFound == 1:
                treasure = os.listdir(folder)[0]
                if treasure == 'treasure.txt':
                    print("Found it!\nIn folder: " + folder)
                    break
                else:
                    print("hey what is it??", treasure)
            elif numFound > 1:
                print("Hey what is it??", os.listdir(folder))
            else:
                print("Better luck next time!")
    else:
        print("No starting folder in the current directory")
        print("Run 'python3 plantTreasure.py' in the shell first.\nOr, start the search in a different directory.")


if __name__ == "__main__":
    __main__()
