import os,shutil

path=input("输入文件路径:\n")
path=path.replace('\\','/')
path=os.path.join(path+'/')
dist_file=input("输入目标文件路径:\n")
dist_file=dist_file.replace('\\','/')
dist_file=os.path.join(dist_file+'/')
if(os.path.exists(path)):
    names=os.listdir(path)
del_name=[]
for i in range(len(names)):
    del_name.append(names[i].split(".")[0])
for n in del_name:
    if(del_name.count(n)>=2):
        filename=os.path.join(path,n+'.bmp')
        jsonname=os.path.join(path,n+'.json')
        newfile=os.path.join(dist_file,n+'.bmp')
        newjson=os.path.join(dist_file,n+'.json')
        del_name.remove(n)
        shutil.move(filename,newfile)
        shutil.move(jsonname,newjson)
        print("已移动标注文件{}！".format(n))
print("标记文件及对应图片移动成功！")
try:
    input("Press any key  to end")
except SyntaxError:
    pass
