import os

path=input("请输入参考同名文件夹路径:\n")
path=path.replace("\\","/")
path=os.path.join(path+"/")
dist=input("请输入待删除文件夹路径:\n")
dist=dist.replace("\\","/")
dist=os.path.join(dist+"/")
if(os.path.exists(path)):
    names=os.listdir(path)
else:
    print("输入参考路径不存在，请检查路径！")

if(os.path.exists(dist)):
    names1=os.listdir(dist)
else:
    print("输入删除路径不存在，请检查路径！")

del_list=[n for n in names1 if n not in names]
for n in del_list:
    filename=os.path.join(dist,n)
    os.remove(filename)
    print("目标文件夹无对应文件{}已删除！".format(n))
print("目标文件夹无对应文件已删除成功！")
print("重复文件个数: {}".format(len(del_list)))
try:
    input("Press any key  to end")
except SyntaxError:
    pass
