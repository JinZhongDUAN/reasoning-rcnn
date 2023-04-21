本项目来源于https://github.com/chanyn/Reasoning-RCNN
Reasoning-RCNN: Unifying Adaptive Global Reasoning into Large-scale Object Detection (CVPR2019 Oral)
对其进行了相关内容修改使其可以运行，测试环境如下：
# Environments（Ubuntu16.04，python3.6）
addict          2.4.0
certifi         2021.5.30
cffi            1.14.6
cycler          0.11.0
Cython          0.29.33
kiwisolver      1.3.1
matplotlib      3.3.4
mkl-fft         1.0.6
mkl-random      1.0.1
mmcv            0.4.3
mmdet           0.5.7+6d83f89
numpy           1.15.4
olefile         0.46
opencv-python   4.6.0.66
packaging       21.3
pandas          0.25.3
Pillow          8.3.1
pip             21.3.1
pycocotools     2.0.6
pycparser       2.21
pyparsing       3.0.0
python-dateutil 2.8.2
pytz            2023.3
PyYAML          6.0
scipy           1.5.4
seaborn         0.11.2
setuptools      58.0.4
six             1.16.0
TBB             0.2
terminaltables  3.1.10
torch           0.4.1
torchvision     0.2.1
wheel           0.37.1
yapf            0.32.0
# Detail
本项目使用mmdetection0.5.7,需要的话【[在此](https://github.com/Jinzhong-Duan/mmdetection)】下载（已对官方版本内容进行了相关修改，可以直接用于Reasoning-RCNN）

1.创建conda虚拟环境并安装requirements.txt里面的库并激活进入虚拟环境

```pip install -r requirements.txt```

2.安装mmcv（先安装mmcv后安装mmdetection）

```pip install mmcv==0.4.3```

3.安装mmdetection0.5.7

```git clone https://github.com/Jinzhong-Duan/mmdetection.git```

```conda install cython #pip install cython```

```cd mmdetection#如果已经在此目录不需要此条命令```

```./compile.sh```

```python setup.py install #pip install .```

4.执行训练

```python ./tools/train.py configs/faster_rcnn_r101_fpn_1x_coco.py```（reasoning-rcnn目录下）

5.执行测试(根据实际进行修改)

```python test.py configs/coco_faster_rcnn_r101_fpn_1x.py work_dirs/faster_rcnn_r101_fpn_1x/aluminum/epoch_3.pth --json_out work_dirs/test_result/aluminum_rrcnn_result```

```python coco_eval.py work_dirs/test_result/faster_rcnn_result.bbox.json --ann /root/aluminum/annotations/val.json```

# 其它
1.如果执行./compile.sh出现gcc等问题，很可能是由于cuda，cudnn，pytorch，mmcv版本存在不匹配问题。

2.其他环境未测试，谨慎尝试。

3.如果使用官方的mmdetection0.5.7不能直接用，需要修改相应代码。

4.如果非想使用官方的mmdetection，建议使用mmdetection1.0.0,代码改动会少点。
