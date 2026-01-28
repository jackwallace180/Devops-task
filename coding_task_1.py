import os

def FileTyper(path, rec):
    ## find all files and directories in path ##
    ## originally used os.listdir here but was unable to get subdirectories ##
    for root, dirs, files in os.walk(path):
        ## iterate through file name ends ##
        for filename in files:
            if filename.endswith(".cpp") or filename.endswith(".hpp"):
                print(f' {filename} This is a c++ file!')
            elif filename.endswith(".c") or filename.endswith(".h"):
                print(f' {filename} This is a c file!')
            elif filename.endswith(".py"):
                print(f' {filename} This is a python file!')
            elif filename.endswith(".java"):
                print(f' {filename} This is a java file!')
            elif filename.endswith(".m"):
                print(f' {filename} This is a matlab file!')
            else:
                continue
        ## os.walk looks through directory files first, break will stop it looking through subdirectories ##
        if rec != "True":
            break

if __name__ == '__main__':
    ## enter path as string followed by ,"True" if you want to search subdirectories ##
    FileTyper("path/to/dir", "False")
