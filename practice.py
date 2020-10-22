# # # from PIL import Image
# # # import os
# # # i="Image_20200825091050781.png"
# # # img=Image.open("D:/Cmian/save_masks/Image_20200825091050781.png")
# # #     # bmp_name = os.path.join(img_path, i)
# # #     # img = Image.open(bmp_name)
# # # w, h = img.size
# # # if h == 4000:
# # #     top = img.crop((0, 0, 2000, 2000))
# # #     down = img.crop((0, 2000, 2000, 4000))
# # #     i_top = i[:-4] + "_top"
# # #     i_down = i[:-4] + "_down"
# # #     top.save(os.path.join("D:/Cmian/save_masks/half_imgs/", str(i_top) + '.png'))
# # #     down.save(os.path.join("D:/Cmian/save_masks/half_imgs/", str(i_down) + '.png'))
# # import numpy as np
# # from PIL import Image
# # import os
# # i="Image_20200825091050781_top.png"
# # img=Image.open("D:/Cmian/save_masks/half_imgs/Image_20200825091050781_top.png")
# # n=int(2000/768)
# # m=np.ceil((2000/768))
# # print(m)
# # # print(n)
# # h_list=[]
# # if(m==n):
# #     for t in range(int(m)):
# #         h_list.append(t*768)
# # else:
# #     for t in range(int(m/2)):
# #         h_list.append(t*768)
# #     h_list.append(int(2000/2-768/2))
# #     for t in range(1,int(m/2)+1):
# #         h_list.append(2000-768*t)
# # w_list=h_list
# # for m in range(len(h_list)):
# #     for n in range(len(w_list)):
# #         img1 = img.crop((w_list[n], h_list[m], w_list[n] + 768, h_list[m] + 768))
# #         i_img1 = i[:-4] + str(m) + "_" + str(n)
# #         img1.save(os.path.join("G:/", str(i_img1) + '.png'))
# # import cv2
# # import numpy as np
# # import torch
# # from torchvision import transforms
# #
# # # x_test = torch.zeros((1, 3, 768, 768), dtype=torch.float)
# # image=cv2.imread("G:/Image_20200825091050921_down1_2_o.png",0)
# # img=cv2.imread("G:/Image_20200825091050921_down1_2.png",0)
# #
# # ret=image*0.8+img*0.2
# #
# # # img = image[..., ::-1]  # RGB
# # # img = transforms.ToPILImage()(img)
# # # img = transforms.ToTensor()(img)
# # # x_test[0:, 0:3, :, :] = im
# # print(img.shape)
# # img=np.expand_dims(img,2)
# # img = img.repeat(3, axis=2)
# # img[:,:,1]=0
# # img[:,:,2]=0
# # print(img.shape)
# # img=cv2.imwrite("G:/Image_20200825091050921_down1_2(1).png",img)
#
# # print(img)
# # print(x_test)
# import os,shutil
# names=os.listdir("//192.168.0.111/视觉检测原图")
# shutil.make_archive("//192.168.0.111/视觉检测原图/c面(已标注)-0825","zip",'//192.168.0.111/视觉检测原图/c面(已标注)-0825')
# print(names)
#
import re


# names=['YX_backup_2020_10_08_010001_4261124.bak','YX_backup_2020_11_06_020001_6435893.bak','YX_backup_2020_09_06_020001_6435893.bak']
# names.sort()
# print(len(names))
# print(names)
# names.pop(0)
# print(len(names))
# print(names)
        # print(n)
# import os
# t=[]
# t.append(os.path.getmtime('G:/gen_train_mask.py'))
# t.append(os.path.getmtime('G:/c面(已标注)-0825.zip'))
# t.append(os.path.getmtime('G:/SegNet_Conv-20200721T065014Z-001.zip'))
# t.sort()
# print(t)
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# from plyfile import PlyData
# plydata = PlyData.read('G:/project/TODO/data/Image_20200919140526288_3204.ply')
# xlist = plydata['vertex']['x']
# ylist = plydata['vertex']['y']
# zlist = plydata['vertex']['z']
# data = plydata.elements[0].data
# print(plydata)
# print(type(data))
# print(data.shape)
# # print(data)
# fig = plt.figure(dpi=120)
# ax = Axes3D(fig)
# # ax.scatter(xlist, ylist, zlist,c='b',marker='.',s=2,linewidth=0,alpha=1,cmap='spectral')
# ax.scatter(xlist, ylist, zlist)
# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')
# plt.show()
# data = plydata.elements[0].data
# print(plydata)
# print(type(data))
# print(data.shape)
# print(data)
