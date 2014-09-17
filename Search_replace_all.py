import os
import  fileinput
tosearch = raw_input("enter word to search:")
toreplace = raw_input("enter word to replace:")

def get_filepaths(directory):
    file_paths = []  # List which will store all of the full filepaths.

    
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath) 

    return file_paths 
   
full_file_paths = get_filepaths(os.getcwd())
for i in range (len(full_file_paths)):   
        tempFile = open(full_file_paths[i],'r+')
        for line in fileinput.input( full_file_paths[i] ):
                if word in line :
                        tempFile.write( line.replace(tosearch,toreplace))
                        tempFile.close()


        


