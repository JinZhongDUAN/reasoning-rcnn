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
本项目以执行./compile.sh,可以直接用，或者你可以在自己的环境下重新执行（安装完需要的库）
1.安装mmcv-full
pip install mmcv-full=={mmcv_version} -f https://download.openmmlab.com/mmcv/dist/{cu_version}/{torch_version}/index.html
例如pip install mmcv-full -f https://download.openmmlab.com/mmcv/dist/cu101/torch1.6.0/index.html
2.安装mmdetection
git clone https://github.com/open-mmlab/mmdetection.git
cd mmdetection
pip install -v -e .
3.安装上述所需的库，包括torch1.6.0和torchvision0.7.0
4.执行训练（reasoning-rcnn目录下）：python ./tools/train.py configs/faster_rcnn_r101_fpn_1x_coco.py
# 其它
1.如果提示RuntimeError: CUDA error: invalid device function，则很可能是mmcv-full版本问题，可以安装其它版本进行尝试。
2.如果提示train.py里的某个函数不存在，是由于mmdetection版本较新引起的（老版本的某些东西在新版本中已经去除），可以根据mmdetection/tools下的train.py对reasoning-rcnn/tools里的train.py进行修改。
3.如果执行./compile.sh出现gcc等问题，很可能是由于cuda，cudnn，pytorch，mmcv-full版本存在不匹配问题。
4.本项目必须安装mmcv-full，mmcv精简版执行不了。
