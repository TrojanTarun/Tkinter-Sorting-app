import os,shutil
folders={
    'videos' :['.mp4'],
    'audios' :['.mp3'],
    'images' :['.jpg','.png'],
    'documents' :['.docx','.xlsx','.xls','.pdf','.txt'],

}
# print(folders)
# for folder_names in folders:
#     print(folder_names,folders[folder_names])
def rename_folder():
    for folder in os.listdir(dir):
        if os.path.isdir(os.path.join(dir,folder))==True:
            os.rename(os.path.join(dir,folder),os.path.join(dir,folder.lower()))


def create_move(ext,filename):
    find=False
    for folder_name in folders:
        if "."+ext in folders[folder_name]:
            # print(" found "+ folder_name)
            if folder_name not in os.listdir(dir):
                os.mkdir(os.path.join(dir,folder_name))
            shutil.move(os.path.join(dir,filename),os.path.join(dir,folder_name))
            find=True
            break
    if find!=True:
        if other_name not in os.listdir(dir):
            os.mkdir(os.path.join(dir,other_name))
        shutil.move(os.path.join(dir,filename),os.path.join(dir,other_name))

        
    #print(ext,filename)


dir = "G:\\PyGUI\\files"#input("Enter the Location:")
other_name = input("Enter the folder name for unknown files:")
rename_folder()
all_files = os.listdir(dir)
length = len(all_files)
count=1
for i in all_files:
    if os.path.isfile(os.path.join(dir,i))==True:
        create_move(i.split(".")[-1],i)
    print(f"Total Files:{length}| Done: {count} | Left:{length-count}")
    count+=1
        #print("YES")

