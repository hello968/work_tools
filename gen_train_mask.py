import json
import cv2
from labelme import utils
import os

import numpy as np
import shutil


def build_img_hub(traindata_path):
    if not os.path.exists(os.path.join(traindata_path,'imgs')):
        os.makedirs(os.path.join(traindata_path,'imgs'))
    if not os.path.exists(os.path.join(traindata_path,'masks')):
        os.makedirs(os.path.join(traindata_path,'masks'))
    if not os.path.exists(os.path.join(traindata_path,'save_masks')):
        os.makedirs(os.path.join(traindata_path,'save_masks'))
    for i in os.listdir(traindata_path):
        if i[-4:]=='json':
            if os.path.exists(os.path.join(traindata_path,i[:-4]+'png')):
                shutil.copy(os.path.join(traindata_path,i),os.path.join(traindata_path,'masks',i))
                shutil.copy(os.path.join(traindata_path,i[:-4]+'png'), os.path.join(traindata_path,'imgs',i[:-4]+'bmp'))
            elif os.path.exists(os.path.join(traindata_path,i[:-4]+'bmp')):
                shutil.copy(os.path.join(traindata_path,i),os.path.join(traindata_path,'masks',i))
                shutil.copy(os.path.join(traindata_path,i[:-4]+'bmp'), os.path.join(traindata_path,'imgs',i[:-4]+'bmp'))
            else:
                print('no label:%s......'%i)



def get_masks(traindata_path):
    json_paths=os.path.join(traindata_path,'masks/')
    img_path=os.path.join(traindata_path,'imgs/')
    save_mask_file=os.path.join(traindata_path,'save_masks/')
    index = 0
    for json_file in os.listdir(json_paths):
        if json_file[-4:]=='json':
            json_file=os.path.join(json_paths,json_file)
            # print(json_file)
            try:
                data=json.load(open(json_file))
                # print(json_file)
                imgPath=data['imagePath'].split('/')[-1][:-3]+'bmp'
                print(imgPath)
                imgpath=os.path.join(img_path,imgPath)
                # print(imgpath)

                if os.path.exists(imgpath):
                    img=cv2.imread(imgpath)
                    lbl,lbl_names=utils.labelme_shapes_to_label(img.shape,data['shapes'])
                    index = index + 1
                    # print(len(lbl_names))
                    print("current json index is: ", index)
                    mask = []
                    for i in range(1, len(lbl_names)):

                        # label=label_names.index(i)
                        mask.append((lbl==i).astype(np.uint8))
                    mask=np.transpose(np.asarray(mask,np.uint8),[1,2,0])
                    mask[:,:,0]=mask[:, :, 0]*255
                    for i in range(mask.shape[-1]-1):
                        mask[:,:,0]=mask[:,:,i+1]*255+mask[:,:,0]
                        mask[:,:,0]=np.clip(mask[:,:,0],0,255)

                    # mask=mask*255
                    cv2.imwrite(os.path.join(save_mask_file,str(imgPath[:-3])+'png'),mask[:,:,0])
            except UnicodeDecodeError:
                pass

if __name__=="__main__":
    traindata_path = "D:/406S-A(20201019)/biaozhu/" #修改源文件路径即可
    build_img_hub(traindata_path=traindata_path)
    # label_name=['1', '2', '3', '4', '5', '6', '7', '8', '9']
    get_masks(traindata_path)

# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
# # !H:\Anaconda3\envs\new_labelme\python.exe
# import argparse
# import json
# import os
# import os.path as osp
# import base64
# import warnings
#
# import PIL.Image
# import yaml
#
# from labelme import utils
#
# import cv2
# import numpy as np
# from skimage import img_as_ubyte
#
#
# # from sys import argv
#
# def main():
#     warnings.warn("This script is aimed to demonstrate how to convert the\n"
#                   "JSON file to a single image dataset, and not to handle\n"
#                   "multiple JSON files to generate a real-use dataset.")
#
#     json_file = "/home/jfw/needlabel/6_json/"
#
#     # freedom
#     list_path = os.listdir(json_file)
#     print('freedom =', json_file)
#     for i in range(0, len(list_path)):
#         path = os.path.join(json_file, list_path[i])
#         if os.path.isfile(path):
#
#             data = json.load(open(path))
#             img = utils.img_b64_to_arr(data['imageData'])
#             lbl, lbl_names = utils.labelme_shapes_to_label(img.shape, data['shapes'])
#
#             captions = ['%d: %s' % (l, name) for l, name in enumerate(lbl_names)]
#
#             lbl_viz = utils.draw_label(lbl, img, captions)
#             # out_dir = osp.basename(path).replace('.', '_')
#             out_dir = osp.basename(path).split('.json')[0]
#             save_file_name = out_dir
#             # out_dir = osp.join(osp.dirname(path), out_dir)
#
#             if not osp.exists(json_file + 'mask'):
#                 os.mkdir(json_file + 'mask')
#             maskdir = json_file + 'mask'
#
#             if not osp.exists(json_file + 'mask_viz'):
#                 os.mkdir(json_file + 'mask_viz')
#             maskvizdir = json_file + 'mask_viz'
#
#             out_dir1 = maskdir
#             # if not osp.exists(out_dir1):
#             #     os.mkdir(out_dir1)
#
#             # PIL.Image.fromarray(img).save(out_dir1 + '\\' + save_file_name + '_img.png')
#             PIL.Image.fromarray(lbl).save(out_dir1 + '/' + save_file_name + '.png')
#
#             PIL.Image.fromarray(lbl_viz).save(maskvizdir + '/' + save_file_name +
#                                               '_label_viz.png')
#
#             # if not osp.exists(json_file + '\\' + 'mask_png'):
#             #     os.mkdir(json_file + '\\' + 'mask_png')
#             # mask_save2png_path = json_file + '\\' + 'mask_png'
#             ################################
#             # mask_pic = cv2.imread(out_dir1+'\\'+save_file_name+'_label.png',)
#             # print('pic1_deep:',mask_pic.dtype)
#
#             # mask_dst = img_as_ubyte(lbl)  # mask_pic
#             # print('pic2_deep:', mask_dst.dtype)
#             # cv2.imwrite(mask_save2png_path + '\\' + save_file_name + '_label.png', mask_dst)
#             ##################################
#
#             with open(osp.join(out_dir1, 'label_names.txt'), 'w') as f:
#                 for lbl_name in lbl_names:
#                     f.write(lbl_name + '\n')
#
#             warnings.warn('info.yaml is being replaced by label_names.txt')
#             info = dict(label_names=lbl_names)
#             with open(osp.join(out_dir1, 'info.yaml'), 'w') as f:
#                 yaml.safe_dump(info, f, default_flow_style=False)
#
#             print('Saved to: %s' % out_dir1)
#
#
# if __name__ == '__main__':
#     # base64path = argv[1]
#     main()

# import scipy.misc
# import numpy as np
#
# img=scipy.misc.imread("G:/Image_20200825091050781.png")
# maximg=np.max(img,axis=1)
# print(maximg)
