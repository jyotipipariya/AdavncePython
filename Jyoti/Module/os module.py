import os
# os.system ('notepad')
# os.system ('calc')
# os.system('mkdir Ram')
# os.system('mkdir Shyam')
# os.system ('rmdir Shyam')
# os.system ('rmdir Ram')

# Making n number of folders inside a folder
'''for i in range (1,11):
    path = 'D:\\Ram\\'
    folder_name='Shyam' + str (i)
    t = path+folder_name
    create_folder='mkdir ' + t
    os.system(create_folder)'''

# to delete a non-empty folder
# shutil deletes the folder permanently
'''import shutil
shutil.rmtree('D:\\Ram')'''

# to see the current working directory
print(os.getcwd())
# to change the working directory
'''os.chdir('D:/Ram')
print(os.getcwd())'''

# to see the stored content inside the folder
'''os.chdir('D:\\')
print(os.listdir())'''

# to explore the contents inside a folder
'''x = os.listdir()
for item in x:
    print(item)'''

# to return the content from a path
'''lst=os.walk('D:\\Bunty altius')
for root_path, dir, files in lst:
    print('root_path=', root_path)
    print('directories=', dir)
    print('files=',files)
    print()'''

# to print hierirachal folder
# os.makedirs('Ram/Shyam/Mohan')
# os.removedirs('Ram/Shyam/Mohan')

# to rename
print(os.getcwd())
os.chdir('D:\\Bunty altius\\bunty')
print(os.getcwd())
os.rename('shyam.txt', 'ram.txt')

# use of shutil








