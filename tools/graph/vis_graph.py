import numpy as np
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.cm as cm

sns.set(font_scale=1.2)
plt.rcParams['font.family'] = 'Noto Sans CJK JP'#支持中文标签显示
graph_r = pickle.load(open('/home/mrduan/projects/RRCNN/Reasoning-RCNN/tools/graph/aluminum_cooccur_matrix.pkl', 'rb'))
graph_r = np.float32(graph_r)
# graph_r = np.around(graph_r.astype(np.float32), decimals=3)
# aluminum数据集
CLASSES = ['针孔', '擦伤', '脏污', '褶皱']
# textfile平纹数据集
'''
CLASSES = ['错经', '错纹织', '断纬', '纬缩', '糙皮档', '档子', '缺经', '稀弄',
           '破边', '边带纬（拖纬）', '双纬', '引纬错序', '跳纱', '破洞',
           '扭结', '边撑磨痕', '细节', '污渍纱', '粗纬', '松吊经',
           '紧经', '松边', '卷边', '紧边', '异物织入', '污迹',
           '云织（隐档）', '异常斜纹', '棉球', '断疵', '浆斑', '结子',
           '双经', '错纬', '穿错', '粗经', '大肚纱', '模糊',
           '筘路', '断经', '不确定', '拖纬', '飞花', '异物']

# textfile斜纹细分类数据集
CLASSES = ['异物12', '纬向破边11', '经向破边10', '拖纱9', '断疵8', '污迹7', '污渍纱6', '破洞5',
           '异物织入4', '点状3', '纬向2', '经向1', '密档', '线头',
           '异物', '飞花', '拖纬', '不确定', '断经', '筘路',
           '模糊', '大肚纱', '粗经', '穿错', '错纬', '双经',
           '结子', '浆斑', '断疵', '棉球', '异常斜纹', '云织（隐档）',
           '污迹', '异物织入', '紧边', '卷边', '松边', '紧经',
           '松吊经', '粗纬', '污渍纱', '细节', '边撑磨痕', '扭结',
           '破洞', '跳纱', '引纬错序', '双纬', '边带纬（拖纬）', '破边',
           '稀弄', '缺经', '档子', '糙皮档', '纬缩', '断纬',
           '错纹织', '错经']
'''
# textfile斜纹粗分类数据集
# CLASSES = ['经向', '纬向', '点状', '异物织入', '破洞', '污渍纱', '污迹', '断疵',
           #'拖纱', '经向破边', '纬向破边', '异物']
# coco2017数据集
'''
CLASSES = ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus',
               'train', 'truck', 'boat', 'traffic_light', 'fire_hydrant',
               'stop_sign', 'parking_meter', 'bench', 'bird', 'cat', 'dog',
               'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe',
               'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee',
               'skis', 'snowboard', 'sports_ball', 'kite', 'baseball_bat',
               'baseball_glove', 'skateboard', 'surfboard', 'tennis_racket',
               'bottle', 'wine_glass', 'cup', 'fork', 'knife', 'spoon', 'bowl',
               'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot',
               'hot_dog', 'pizza', 'donut', 'cake', 'chair', 'couch',
               'potted_plant', 'bed', 'dining_table', 'toilet', 'tv', 'laptop',
               'mouse', 'remote', 'keyboard', 'cell_phone', 'microwave',
               'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock',
               'vase', 'scissors', 'teddy_bear', 'hair_drier', 'toothbrush']
'''
#graph_r = 1 - graph_r
start = 0
end = 4
f, ax1 = plt.subplots(figsize=(4,4), ncols=1)

sns.heatmap(graph_r[start:end,start:end], cmap=cm.Blues, annot=True, annot_kws={'size':8}, cbar_kws={"shrink":0.2}, ax=ax1, linewidths = 0.02, xticklabels=CLASSES[start:end], yticklabels=CLASSES[start:end], square=True)
labelx = ax1.get_xticklabels()
plt.setp(labelx, rotation=30, horizontalalignment='right')
ax1.set_title("铝皮缺陷类别共现关系可视化")
plt.savefig('/home/mrduan/projects/RRCNN/Reasoning-RCNN/work_dirs/vis/aluminum_r_graph.png')
plt.show()