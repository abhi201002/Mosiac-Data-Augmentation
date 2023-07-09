import numpy as np
import cv2
import random
import os
import PIL
from PIL import Image

OUTPUT = 1000
min_scale = 0.3
max_scale = 0.7
def get_label(path):
    labels = []
    with open(path) as f:
        label = f.readlines()
        label = [bb.rstrip('\n') for bb in label]
        label = [bb.split(' ') for bb in label]
        
        for bbox in label:
            labels.append([int(bbox[0]), float(bbox[1]), float(bbox[2]), float(bbox[3]), float(bbox[4])])
    return labels
    
def get_path(label, img_path):
    name,ext = os.path.split(img_path)
    
    path = os.path.join(label, f'{name}.txt')
    return path

def Mosaic(image, label):
    img_list = os.listdir(image)
    # annos = os.listdir(label)
    index = random.sample(range(len(img_list)),4)
    
    x = min_scale + random.random() * (max_scale - min_scale)
    y = min_scale + random.random() * (max_scale - min_scale)
    
    
    res = np.zeros((OUTPUT , OUTPUT , 3),dtype = np.uint8)
    
    h = int(y*OUTPUT)
    w = int(x*OUTPUT)
    
    for i in range(4):
        path = os.path.join(image,img_list[index[i]])
        # path_label = get_path(label,image_list[index[i]])
        # label = get_label(path_label)
        
        img = Image.open(path)
        img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
        
        if(i == 0):
            img = cv2.resize(img, (h,w))
            res[0:w , 0:h ,:] = img
            # with open(path_label,'w') as f:
            #     for bb in label:
            #         X = bb[1] * x
            #         Y = bb[2] * y
            #         W = bb[3] * x
            #         H = bb[4] * y
            #         f.write(str(bb[0]) + ' ' + str(X) + ' ' + str(Y) + ' ' + str(W) + ' ' + str(H) + '\n')
                
        elif(i == 1):
            img = cv2.resize(img, (h,OUTPUT - w))
            res[w:OUTPUT, 0:h ,:] = img
            # with open(path_label,'w') as f:
            #     for bb in label:
            #         X = x + bb[1] * (1 - x)
            #         Y = bb[2] * y
            #         W = bb[3] * (1 - x)
            #         H = bb[4] * y
            #         f.write(str(bb[0]) + ' ' + str(X) + ' ' + str(Y) + ' ' + str(W) + ' ' + str(H) + '\n')
        
        elif(i == 2):
            img = cv2.resize(img, (OUTPUT - h,w))
            res[0:w , h:OUTPUT ,:] = img
            # with open(path_label,'w') as f:
            #     for bb in label:
            #         X = bb[1] * x
            #         Y = y + bb[2] * (1 - y)
            #         W = bb[3] * x
            #         H = bb[4] * (1 - y)
            #         f.write(str(bb[0]) + ' ' + str(X) + ' ' + str(Y) + ' ' + str(W) + ' ' + str(H) + '\n')
        
        elif(i == 3):
            img = cv2.resize(img, (OUTPUT - h,OUTPUT - w))
            res[w:OUTPUT , h:OUTPUT , :] = img
            # with open(path_label,'w') as f:
            #     for bb in label:
            #         X = x + bb[1] * (1 - x)
            #         Y = y + bb[2] * (1 - y)
            #         W = bb[3] * (1 - x)
            #         H = bb[4] * (1 - y)
            #         f.write(str(bb[0]) + ' ' + str(X) + ' ' + str(Y) + ' ' + str(W) + ' ' + str(H) + '\n')
    
    cv2.imwrite(r'C:\Users\pgupt\Videos\Images - 2 seconds\image.jpg',res)
    
Mosaic(r'C:\Users\pgupt\Videos\Images - 2 seconds\Train',r'')