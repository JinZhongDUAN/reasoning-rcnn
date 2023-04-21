import os

# 指定图像文件所在目录
image_dir = '/root/textfile/data/xiewen_multiple/images'

# 遍历目录下的所有文件
for root, dirs, files in os.walk(image_dir):
    for filename in files:
        # 如果文件是JPEG图像文件，则修改扩展名
        if filename.endswith('.jpg'):
            src_path = os.path.join(root, filename)
            dst_path = os.path.join(root, os.path.splitext(filename)[0] + '.jpeg')
            os.rename(src_path, dst_path)
