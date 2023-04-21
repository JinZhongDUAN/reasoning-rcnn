import json
import numpy as np
import pickle
from collections import defaultdict

# 读取COCO标注文件
with open('/root/aluminum/annotations/train.json', 'r') as f:
    data = json.load(f)

# 创建一个字典来存储对象共现频率
cooccur = defaultdict(int)
obj_ids = set()

# 遍历所有图像和它们的对象
for img in data['images']:
    # 获取图像ID和它的对象信息
    img_id = img['id']
    objs = [obj['category_id'] for obj in data['annotations'] if obj['image_id'] == img_id]
    # 对于每对对象，更新它们的共现频率
    for i in range(len(objs)):
        obj_ids.add(objs[i])
        for j in range(i + 1, len(objs)):
            if objs[i] != objs[j]:
                # 如果这对对象不属于同一个类别，则更新共现频率
                cooccur[(objs[i], objs[j])] += 1

# 输出每对对象的共现频率
print(cooccur)
for pair, freq in cooccur.items():
    print(f"对象{pair[0]}和对象{pair[1]}共现了{freq}次。")

# 创建对象共现矩阵
n_objs = len(obj_ids)

cooccur_matrix = np.zeros((n_objs, n_objs))
for obj1 in range(1, n_objs+1):
    for obj2 in range(obj1+1, n_objs+1):
        pair_1 = (obj1, obj2)
        pair_2 = (obj2, obj1)
        if pair_1 in cooccur:
            cooccur_matrix[obj1-1, obj2-1] = cooccur[pair_1] + cooccur[pair_2]
cooccur_matrix = cooccur_matrix + np.transpose(cooccur_matrix)
print(cooccur_matrix)

# 简单行归一化
'''sums = np.sum(cooccur_matrix, axis=1)
for i in range(n_objs):
    if sums[i] > 0:
        cooccur_matrix[i, :] /= sums[i]'''
# 行列归一化
row_sum = np.sum(cooccur_matrix, axis=1)
col_sum = np.sum(cooccur_matrix, axis=0)
divisor = np.sqrt(np.outer(row_sum, col_sum))
cooccur_matrix = cooccur_matrix / divisor
cooccur_matrix[np.arange(n_objs), np.arange(n_objs)] = 1
print(cooccur_matrix)
# 保存矩阵为pkl文件
with open('./graph/aluminum_cooccur_matrix.pkl', 'wb') as f:
    pickle.dump(cooccur_matrix, f)