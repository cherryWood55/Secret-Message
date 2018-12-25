import os
file_names = os.listdir(r"D:\Udacity\prank")
print (file_names)
cwd=os.getcwd();
print ("The current working directory:"+cwd)
os.chdir(r"D:\Udacity\prank")

for file in file_names:
    print(file)
    new_name = ''.join([i for i in file if not i.isdigit()])
    
    print (new_name)
    os.rename(file, new_name)
