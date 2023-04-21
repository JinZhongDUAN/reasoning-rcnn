import mmcv
from mmcv.runner import load_checkpoint
from mmdet.models import build_detector
from mmdet.apis import inference_detector, show_result

cfg = mmcv.Config.fromfile('configs/rrcnn/coco_reasoning_rcnn_r101_fpn_1x.py')
cfg.model.pretrained = None

# construct the model and load checkpoint
model = build_detector(cfg.model, test_cfg=cfg.test_cfg)
_ = load_checkpoint(model, 'work_dirs/coco_rrcnn_fpn_r101_1x/textile/epoch_20.pth')

# test a single image
img = mmcv.imread('data/textile/1.jpeg')
result = inference_detector(model, img, cfg)
show_result(img, result, dataset='textile')

# test a list of images
'''
imgs = ['data/test/66.jpg', 'data/test/88.jpg', 'data/test/100.jpg']
for i, result in enumerate(inference_detector(model, imgs, cfg, device='cuda:0')):
    print(i, imgs[i])
    show_result(imgs[i], result, dataset='aluminum')
'''