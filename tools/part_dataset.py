import os
import cv2
import json
import numpy as np
from pycocotools.coco import COCO
# 加载标注文件
dataset = COCO('/root/textfile/data/xiewen_multiple/xiewen_mult.json')

# 获取所有图像的信息
images = dataset.dataset['images']

# 随机打乱图像的顺序
np.random.shuffle(images)

# 划分比例
split_ratio = 0.8

# 计算划分点
split_idx = int(len(images) * split_ratio)

# 分割图像信息
train_images = images[:split_idx]
val_images = images[split_idx:]

# 创建训练集和验证集的索引
train_dataset = COCO()
train_dataset.dataset['images'] = []
train_dataset.dataset['annotations'] = []
val_dataset = COCO()
val_dataset.dataset['images'] = []
val_dataset.dataset['annotations'] = []

for image_info in train_images:
    # 加载图像文件
    file_path = os.path.join('/root/textfile/data/xiewen_multiple/images', image_info['file_name'])
    image = cv2.imread(file_path)
    # 将图像信息添加到训练集中
    train_dataset.dataset['images'].append(image_info)
    train_dataset.dataset['images'][-1]['file_name'] = file_path
    train_dataset.dataset['images'][-1]['height'] = image.shape[0]
    train_dataset.dataset['images'][-1]['width'] = image.shape[1]
    # 将标注信息添加到训练集中
    annotation_ids = dataset.getAnnIds(imgIds=image_info['id'])
    annotations = dataset.loadAnns(annotation_ids)

    for annotation in annotations:
        train_dataset.dataset['annotations'].append(annotation)

for image_info in val_images:
    # 加载图像文件
    file_path = os.path.join('/root/textfile/data/xiewen_multiple/images', image_info['file_name'])
    image = cv2.imread(file_path)
    # 将图像信息添加到验证集中
    val_dataset.dataset['images'].append(image_info)
    val_dataset.dataset['images'][-1]['file_name'] = file_path
    val_dataset.dataset['images'][-1]['height'] = image.shape[0]
    val_dataset.dataset['images'][-1]['width'] = image.shape[1]
    # 将标注信息添加到验证集中
    annotation_ids = dataset.getAnnIds(imgIds=image_info['id'])
    annotations = dataset.loadAnns(annotation_ids)
    for annotation in annotations:
        val_dataset.dataset['annotations'].append(annotation)

# 创建索引
train_dataset.createIndex()
val_dataset.createIndex()

# 保存训练集和验证集的标注文件
with open('/root/textfile/data/xiewen_multiple/train_xiewen_mult.json', 'w') as f:
    json.dump(train_dataset.dataset, f)
with open('/root/textfile/data/xiewen_multiple/val_xiewen_mult.json', 'w') as f:
    json.dump(val_dataset.dataset, f)