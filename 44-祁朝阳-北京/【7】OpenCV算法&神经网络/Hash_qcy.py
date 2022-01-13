# -*- coding: utf-8 -*-
"""
Aim：计算Hash算法
Author：祁朝阳
Date：2021.12.29
"""
import numpy as np
import pandas as pd
import cv2 
import os

# =============================================================================
# Define functions:
def aHash(img_arr):
# a-Hash
    img_resize = cv2.resize(img_arr, (8,8), interpolation=cv2.INTER_CUBIC)     #img resize
    img_resize_gray = cv2.cvtColor(img_resize, cv2.COLOR_BGR2GRAY)  #img to gray
    
    # cv2.imshow('original', img)
    # cv2.imshow('resized', img_resize)
    # cv2.waitKey()
    # cv2.destroyAllWindows()
    
    img_avg = img_resize_gray.mean()
    img_hash = ''
    # # method 1:
    # for i in range( img_resize_gray.shape[0]):
    #     for j in range(img_resize_gray.shape[1]):
    #         if img_resize_gray[i][j] > img_avg:
    #             img_hash = img_hash + '1'
    #         else:
    #             img_hash = img_hash + '0'
    
    # method 2:
    img_resize_gray = img_resize_gray.flatten()
    for i in img_resize_gray:
        if i>img_avg:
            img_hash = img_hash + '1'
        else:
            img_hash = img_hash + "0"
    
    # print(img_hash)
    return img_hash


def dHash(img_arr):
# d-Hash
    img_resize = cv2.resize(img_arr, (9,8), interpolation=cv2.INTER_CUBIC) # what the fuck! 8 rows, 9 columns
    img_gray = cv2.cvtColor(img_resize, cv2.COLOR_BGR2GRAY)
       
    # loop
    m,n = img_gray.shape
    img_hash = ''
    for i in range(m):
        for j in range(n-1):
            if img_gray[i][j]>img_gray[i][j+1]:
                img_hash = img_hash +'1'
            else:
                img_hash = img_hash + '0'
    # print(img_hash)
    return img_hash


def cmp_Hash(hash1, hash2):
    if len(hash1) != len(hash2):
        # print('Hash ERROR')
        return 'Hash ERROR'
    else:
        n = 0
        for i in range(len(hash1)):
            if hash1[i] != hash2[i]:
                n = n+1
        return n

# ============================================================================
# Main code
source_path = r'G:\八斗视频\新的课程\【7】OpenCV算法&神经网络\代码'
os.chdir(source_path)

# read images
img1 = cv2.imread('lenna.png', 1)  
img2 = cv2.imread('lenna_noise.png', 1)

# cv2.imshow('img1', img1)
# cv2.imshow('img2', img2)
# cv2.waitKey()
# cv2.destroyAllWindows()

# calculate dHash
img1_ahash = aHash(img1)
img2_ahash = aHash(img2)

# ahash comparision
aHash_diff = cmp_Hash(img1_ahash, img2_ahash)
print(img1_ahash)
print(img2_ahash)
print('a-Hash difference is: {0}'.format(aHash_diff))


# calculate dHash
img1_dhash = dHash(img1)
img2_dhash = dHash(img2)

# dhash comparision
dHash_diff = cmp_Hash(img1_dhash, img2_dhash)
print(img1_dhash)
print(img2_dhash)
print('d-Hash difference is: {0}'.format(dHash_diff))






















