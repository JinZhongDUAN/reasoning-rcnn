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

# 初始化对象集合和共现频率字典
obj_counts = {cat['id']: 0 for cat in data['categories']}
for ann in data['annotations']:
    obj_counts[ann['category_id']] += 1
for i, cat in enumerate(data['categories']):
    obj_ids.add(cat['id'])
    cooccur[(cat['id'], cat['id'])] = obj_counts[cat['id']]
    for j in range(i + 1, len(data['categories'])):
        cooccur[(cat['id'], data['categories'][j]['id'])] = 0
        cooccur[(data['categories'][j]['id'], cat['id'])] = 0
# print(cooccur)
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
# print(cooccur)
for pair, freq in cooccur.items():
    print(f"对象{pair[0]}和对象{pair[1]}共现了{freq}次。")

# 创建对象共现矩阵
obj_ids = sorted(list(obj_ids))
n_objs = len(obj_ids)

cooccur_matrix = np.zeros((n_objs, n_objs))
for i in range(1, n_objs+1):
    for j in range(1, n_objs+1):
        cooccur_matrix[i-1, j-1] = cooccur[i, j]

print(cooccur_matrix)

# 计算条件概率
for i in range(n_objs):
    for j in range(n_objs):
        if i == j:
            pass
        else:
            cooccur_matrix[i, j] = cooccur_matrix[i, j] / cooccur_matrix[j, j]
for i in range(n_objs):
    cooccur_matrix[i, i] = cooccur_matrix[i, i] / cooccur_matrix[i, i]
np.set_printoptions(precision=3, suppress=True)
print(cooccur_matrix)
# 保存矩阵为pkl文件
with open('./graph/aluminum_cooccur_matrix.pkl', 'wb') as f:
    pickle.dump(cooccur_matrix, f)