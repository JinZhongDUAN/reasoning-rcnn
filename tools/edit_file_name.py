import os
import glob
import xml.etree.ElementTree as ET


folder_path = '/root/NEU/annotations'  # 将文件夹路径替换成你要操作的文件夹路径
# 匹配所有crazing_*.xml文件
for filepath in glob.glob(os.path.join(folder_path, "scratches_*.xml")):
    # 获取文件名（包含扩展名）
    filename = os.path.basename(filepath)
    # 将文件名更改为*.xml
    new_filename = ''.join(filter(str.isdigit, filename))#去掉所有非数字字符包括扩展名
    #new_filename = filename.replace("inclusion_", "")
    new_filename = str(1500 + int(new_filename))
    new_filename = new_filename + '.xml'
    # 拼接新的文件路径
    new_filepath = os.path.join(os.path.dirname(filepath), new_filename)
    # 修改文件名
    os.rename(filepath, new_filepath)

'''
# 定义XML文件夹的路径
xml_folder_path = "/root/NEU/annotations"

# 遍历文件夹中的所有XML文件
for xml_file in os.listdir(xml_folder_path):
    if xml_file.endswith(".xml"):
        xml_file_path = os.path.join(xml_folder_path, xml_file)
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        # 遍历所有的filename标签
        for filename_tag in root.iter("filename"):
            filename = filename_tag.text
            # 如果文件名以"crazing_"开头，则将其改为"*."
            if filename.startswith("scratches_"):
                new_filename = ''.join(filter(str.isdigit, filename))
                new_filename = str(1500 + int(new_filename))
                new_filename = new_filename + '.jpg'
                #new_filename = filename.replace("crazing_", "")
                filename_tag.text = new_filename

        # 保存修改后的XML文件
        tree.write(xml_file_path)
'''