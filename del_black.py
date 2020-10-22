import os
import cv2
import numpy as np
import glob

path=input("输入文件路径:\n")
if(os.path.exists(path)):
    for name in glob.glob(os.path.join(path,"*.png")):
        name=name.replace("\\","/")
        img=cv2.imread(name,0)
        print(img.shape)
        max=np.max(img,axis=1)
        num=np.sum(max>40)
        print(num)
        if(num!=768):
            print(name+"已删除")
            os.remove(name)
        else:
            print(name+"已检查，保留")
    print("删除成功！")
else:
    print("文件夹不存在")
