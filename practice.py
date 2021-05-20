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
# import re


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



# fig = plt.figure(figsize=(10, 5))  # 创建绘图窗口，并设置窗口大小
# # 画第一张图
# ax1 = fig.add_subplot(211)  # 将画面分割为2行1列选第一个
# ax1.plot(epoch, loss, 'red', label='loss')  # 画dis-loss的值，颜色红
# ax1.legend(loc='upper right')  # 绘制图例，plot()中的label值
# ax1.set_xlabel('epoch')  # 设置X轴名称
# ax1.set_ylabel('loss')  # 设置Y轴名称
# # 画第二张图
# ax2 = fig.add_subplot(212)  # 将画面分割为2行1列选第二个
# ax2.plot(step, gan, 'blue', label='gan')  # 画gan-loss的值，颜色蓝
# ax2.legend(loc='upper right')  # loc为图例位置，设置在右上方，（右下方为lower right）
# ax2.set_xlabel('step')
# ax2.set_ylabel('Generator-loss')
# plt.show()  # 显示绘制的图
# x=np.arange(0,1,0.1)
# y=np.arange(0,7000,500)


# def read_excel():
#     # 打开文件
#     workBook = xlrd.open_workbook('D:/data.xlsx')
#
#     # 1.获取sheet的名字
#     # 1.1 获取所有sheet的名字(list类型)
#     allSheetNames = workBook.sheet_names()
#     print(allSheetNames)

    # 1.2 按索引号获取sheet的名字（string类型）
    # sheet1Name = workBook.sheet_names()[0]
    # print(sheet1Name)
    #
    # # 2. 获取sheet内容
    # ## 2.1 法1：按索引号获取sheet内容
    # sheet1_content1 = workBook.sheet_by_index(0) # sheet索引从0开始
    # ## 2.2 法2：按sheet名字获取sheet内容
    # sheet1_content2 = workBook.sheet_by_name('Sheet1')
    #
    # # 3. sheet的名称，行数，列数
    # print(sheet1_content1.name,sheet1_content1.nrows,sheet1_content1.ncols);
    #
    # # 4. 获取整行和整列的值（数组）
    # rows = sheet1_content1.row_values(3) # 获取第四行内容
    # cols = sheet1_content1.col_values(2) # 获取第三列内容
    # print(rows)
    #
    # # 5. 获取单元格内容(三种方式)
    # print(sheet1_content1.cell(1, 0).value)
    # print(sheet1_content1.cell_value(2, 2))
    # print(sheet1_content1.row(2)[2].value)
    #
    # # 6. 获取单元格内容的数据类型
    # # Tips: python读取excel中单元格的内容返回的有5种类型 [0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error]
#     # print(sheet1_content1.cell(1, 0).ctype)
# l=["YXdoc_backup_2020_12_21_010000_9275245.bak","YX_backup_2020_12_21_010000_9275245.bak","YX_backup_2020_12_20_094508_7168696.bak",
#                                                                                             "YXdoc_backup_2020_12_20_094508_7168696"]
# print(l)
# l.sort()
# print(l)
#
# import os
#
#
# with open("D:/no/yuedu/在日本当猫的日子.txt", encoding="gb18030") as f:
#     txt=f.read()
# txt.replace("0",)
# with open("D:/no/yuedu/在日本当猫的日子1.txt","w", encoding="gb18030") as f1:
#     for i in range(len(txt.split("☆、"))):
#         t=txt.split("☆、")[i]
#         # d=t.split("作者有话要说：")[0]
#         # print(d)
#         t = "第" + "{}".format(i) + "章 " + t
#         f1.writelines(t)
# print("ok")
# f.close()
# f1.close()
# f1=open(r"G:/210115_A/mosha_surface_flawC_0115.pt","rb")
# # 读取文件数据内容
# data=f1.read()
# print(data)
# import torch
# import io
#
# with open('G:/210115_A/mosha_surface_flawC_0115.pt', 'rb') as f:
#     buffer = io.BytesIO(f.read())
# torch.load(buffer)
# print(torch.load(model))
# txt="12345"
# for i in range(1,5):
#     t=txt.split("{}".format(i))
#     print(t)
# with open("D:/no/yuedu/【焦糖】嫁给陛下后我天天翻车(1).txt", encoding="utf-8") as f:
#     txt = f.read()
# # txt.replace("0",)
# with open("D:/no/yuedu/【焦糖】嫁给陛下后我天天翻车.txt","w", encoding="utf-8") as f1:
#     for i in range(1, 93):
#         if(i<93):
#             print(i)
#             s = str("{}、".format(i))
#             print(s)
#             # t = txt.split(s)[0]
#             # # print(t)
#             # txt = txt.split(s)[1]
#             #
#             # # txt2 = txt.split("{}、".format(i + 1))[0]
#             # tw = "第" + "{}".format(i-1) + "章 " + t
#             # f1.writelines(tw)
#         else:
#             twe = "第" + "{}".format(i) + "章 "+txt
#             f1.writelines(twe)
#
# print("ok")
# import os
# import shutil
#
# traindata_path=r'D:\MA\biaozhu\imgs'
# for i in os.listdir(traindata_path):
#     # print(i)
#     if i[-3:] == 'png' or 'bmp':
#         if os.path.exists(os.path.join(traindata_path, i[:-3] + 'png')):
#             # shutil.copy(os.path.join(traindata_path, i), os.path.join(traindata_path, 'masks', i))
#             print(os.path.join(traindata_path, 'bmpconvert', i[:-3] + 'bmp'))
#             shutil.copy(os.path.join(traindata_path, i[:-3] + 'png'), os.path.join(traindata_path, 'bmpconvert', i[:-3] + 'bmp'))
#         elif os.path.exists(os.path.join(traindata_path, i[:-3] + 'bmp')):
#             # shutil.copy(os.path.join(traindata_path, i), os.path.join(traindata_path, 'masks', i))
#             print(i)
#             print(os.path.join(traindata_path, 'bmpconvert',i[:-3]+'bmp'))
#             shutil.copy(os.path.join(traindata_path, i[:-3] + 'bmp'), os.path.join(traindata_path, 'bmpconvert', i[:-3] + 'bmp'))
# import numpy as np
#
# n=np.zeros((4,4))
# n[3,3]=4
# max=np.max(n,axis=1)
# print(max)
# num=np.sum(max>0)
# print(num)
import urllib.request

from bs4 import BeautifulSoup
from tqdm import tqdm

def get_content(url):
    html=urllib.request.urlopen(url)
    div_bf = BeautifulSoup(html, from_encoding='utf-8', features='html.parser')
    div=div_bf.find_all('div', class_='con')
    # print(div[1])
    para = div[1].find_all('p')
    # print(para)
    w_txt=[]
    for n in div[1].text.split("。"):
        w_n = n+"。\n"
        w_txt.append(w_n)
    return w_txt
if __name__ == '__main__':
    server = "http://www.ggdowns.com/"
    target = 'http://www.ggdowns.com/m/novel/62366.html'     ##小说目录页面
    html = urllib.request.urlopen(url=target)
    dl_bf = BeautifulSoup(html, from_encoding='utf-8', features='html.parser') ## 明确指定解析器，这里我使用了最好的HTML解析器（“html.parser”）
    dl = dl_bf.find('dl', id='g')    ## 寻找存放内容的标签
    # print(dl)
    chapters = dl.find_all('a')
    # print(chapters)
    # print(chapters[0].string)
    # print(chapters[0].get('href'))
    n=1
    with open("D:/no/末世流亡.txt",'w') as f:
        for chap in tqdm(chapters):
            name = "第"+ str(n) +"章          "+chap.string
            f.write(name)
            href = server+chap.get('href')
            w_ch = get_content(href)
            f.writelines(w_ch)
            n=n+1

    print("爬取完成！")
f.close()