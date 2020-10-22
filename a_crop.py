import os
from PIL import Image
import numpy as np

def build_nine_folder(img_path):
    if not os.path.exists(os.path.join(img_path,"nine_imgs")):
        os.makedirs(os.path.join(img_path,"nine_imgs"))

def build_half_folder(img_path):
    if not os.path.exists(os.path.join(img_path,"half_imgs")):
        os.makedirs(os.path.join(img_path,"half_imgs"))

def half_crop(img_path):
    save_img=os.path.join(img_path,"half_imgs")
    for i in os.listdir(img_path):
        if i[-3:]=="bmp" or i[-3:]=="png":
            file_name = os.path.join(img_path, i)
            # print(file_name)
            img = Image.open(file_name)
            w,h=img.size
            if h==4000:
                top=img.crop((0,0,867,2000))
                down=img.crop((0,2000,867,4000))
                i_top=i[:-4]+"_top"
                i_down = i[:-4] + "_down"
                top.save(os.path.join(save_img+"/",str(i_top)+'.png'))
                down.save(os.path.join(save_img+"/", str(i_down) + '.png'))
            print(i+"处理成功！")
def customize_crop(exim_size):
    save_img = os.path.join(nine_path, "nine_imgs")

    for i in os.listdir(nine_path):
        if i[-3:] == "png":
            file_name = os.path.join(nine_path, i)
            # print(file_name)
            img = Image.open(file_name)
            w, h = img.size
            W,H=exim_size
            h_num=np.ceil(h/H)
            w_num=np.ceil(w/W)
            h_list=[]
            w_list=[]
            if(h_num==int(h/H)):
                for t in range(int(h_num)):
                    h_list.append(t*H)
            else:
                for t in range(int(h_num/2)):
                    h_list.append(t*H)
                h_list.append(int(h/2-H/2))
                for t in range(1,int(h_num/2)+1):
                    h_list.append(h-t*H)
            if (w_num == int(w / W)):
                for t in range(int(w_num)):
                    w_list.append(t * W)
            else:
                for t in range(1, int(w_num / 2) + 1):
                    w_list.append(w-t * W)
            for m in range(len(h_list)):
                for n in range(len(w_list)):
                    img1=img.crop((w_list[n],h_list[m],w_list[n]+W,h_list[m]+H))
                    i_img1 = i[:-4] + str(m)+"_"+str(n)
                    img1.save(os.path.join(save_img + "/", str(i_img1) + '.png'))
            print(i+"处理完毕！")

if __name__=="__main__":
    img_path="D:/406S-A(20201019)/biaozhu/save_masks/"

    ########把2000x4000图片裁剪为1/2大小#############
    build_half_folder(img_path=img_path)
    half_crop(img_path)
    ##############################################

    ########把2000x2000图片裁剪为1/9大小#############
    nine_path = "D:/406S-A(20201019)/biaozhu/save_masks/half_imgs/"
    build_nine_folder(img_path=nine_path)
    customize_crop(exim_size=(768,768))
    # exim_siz期望裁剪的尺寸为(w,h)元组
    ##############################################
    print("ok")