# reasoning-rcnn
该项目来源于https://github.com/chanyn/Reasoning-RCNN
Reasoning-RCNN: Unifying Adaptive Global Reasoning into Large-scale Object Detection (CVPR2019 Oral)
# Environments（Ubuntu18.04，python3.7）
addict            2.4.0
certifi           2022.12.7
cycler            0.11.0
fonttools         4.37.1
kiwisolver        1.4.4
matplotlib        3.5.3
mkl-fft           1.3.1
mkl-random        1.2.2
mkl-service       2.4.0
mmcv-full         1.7.1
mmdet             2.28.2    /root/mmdetection
ninja             1.11.1
numpy             1.21.5
opencv-python     4.6.0.66
packaging         23.0
Pillow            9.0.1
pip               22.3.1
psutil            5.9.4
pycocotools       2.0.6
pyparsing         3.0.9
python-dateutil   2.8.2
PyYAML            6.0
scipy             1.7.3
setuptools        65.6.3
six               1.16.0
terminaltables    3.1.10
torch             1.6.0
torchvision       0.7.0
typing_extensions 4.5.0
wheel             0.38.4
yapf              0.32.0
![image](https://user-images.githubusercontent.com/105783906/222870913-1709b253-5593-407e-8b7a-0d36a6143c59.png)
![image](https://user-images.githubusercontent.com/105783906/222870917-bcf28855-88a5-455a-84df-12593b40b4d7.png)
# Detail
上述项目为执行./compile.sh后的，可以直接用，或者你可以在自己的环境下重新执行（安装完需要的库后）
1.安装mmcv-full
pip install mmcv-full=={mmcv_version} -f https://download.openmmlab.com/mmcv/dist/{cu_version}/{torch_version}/index.html
例如pip install mmcv-full -f https://download.openmmlab.com/mmcv/dist/cu101/torch1.6.0/index.html
2.安装mmdetection
git clone https://github.com/open-mmlab/mmdetection.git
cd mmdetection
pip install -v -e .
3.安装上述需要的库，包括torch1.6.0和torchvision0.7.0
4.准备好数据集更改相应文件路径
5.执行训练（reasoning-rcnn目录下）：python ./tools/train.py configs/faster_rcnn_r101_fpn_1x_coco.py
![image](https://user-images.githubusercontent.com/105783906/222870451-20888275-0fa4-4c7b-9f62-b735d226b45f.png)
# 其它
1.如果提示RuntimeError: CUDA error: invalid device function，则很可能是mmcv-full版本问题，可以安装其它版本进行尝试。
2.如果提示某个函数不存在，很可能是由于mmdet版本问题，不过这个用不了作者使用的0.5.7版本的，可以参照mmdetection/tools/里的train.py对reasoning-rcnn里的train.py进行修改。
