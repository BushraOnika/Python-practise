import os
for path,_, files in os.walk("Color_Correct_label_pic"):
    for file in files:
        if "Black" in file:
            file_path=os.path.join(path,file)
            print(file_path)
            file_name=file.replace("Black","green")
            print(file_name)
            new_file_path=os.path.join(path,file_name)
            print(new_file_path)
            os.rename(file_path,new_file_path)
        elif 'Blue' in file:
            file_path=os.path.join(path,file)
            file_name=file.replace("Blue","red")
            new_file_path=os.path.join(path,file_name)
            os.rename(file_path,new_file_path)
        elif 'Green' in file:
            file_path=os.path.join(path,file)
            file_name=file.replace("Green","blue")
            new_file_path=os.path.join(path,file_name)
            os.rename(file_path,new_file_path)
        elif 'Red' in file:
            file_path=os.path.join(path,file)
            file_name=file.replace("Red","white")
            new_file_path=os.path.join(path,file_name)
            os.rename(file_path,new_file_path)
        elif 'White' in file:
            file_path=os.path.join(path,file)
            file_name=file.replace("White","black")
            new_file_path=os.path.join(path,file_name)
            os.rename(file_path,new_file_path)
