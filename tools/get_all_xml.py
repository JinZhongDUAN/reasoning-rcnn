import os
import xml.etree.ElementTree as ET


#根据xml文件夹生成所有xml文件列表

folder_path = "/root/NEU/annotations"  # 替换为你的文件夹路径
output_file = "output.txt"  # 输出文件名

with open(output_file, "w") as f:
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in sorted(filenames, key=lambda x: int(os.path.splitext(x)[0])):
            #name, ext = os.path.splitext(filename) # 分离文件名和扩展名
            f.write(os.path.basename(filename) + "\n") # 获取文件名并写入文件

#根据实际修改xml文件中各标签的内容
# 指定XML文件所在的目录
'''
xml_dir = "/root/NEU/annotations"

# 遍历目录中所有的XML文件
for filename in os.listdir(xml_dir):
    if filename.endswith(".xml"):
        # 解析XML文件
        tree = ET.parse(os.path.join(xml_dir, filename))
        root = tree.getroot()

        # 获取filename标签的文本内容
        filename_tag = root.find("filename")
        if filename_tag is not None:
            image_filename = filename_tag.text
            image_filename = os.path.splitext(image_filename)[0] + ".jpg"

            # 修改path标签内容
            for path in root.iter("path"):
                path.text = os.path.join(xml_dir, image_filename)

            # 保存修改后的XML文件
            tree.write(os.path.join(xml_dir, filename))
'''