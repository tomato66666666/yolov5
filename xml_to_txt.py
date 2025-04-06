import xml.etree.ElementTree as ET
import os


def convert_xml_to_txt(xml_file, output_txt_file, class_mapping):
    """
    将 XML 文件转换为 YOLO 格式的 TXT 文件。

    :param xml_file: XML 文件路径
    :param output_txt_file: 输出的 TXT 文件路径
    :param class_mapping: 类别名称到类别索引的映射字典
    """
    # 解析 XML 文件
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # 获取图片尺寸
    size = root.find('size')
    width = int(size.find('width').text)
    height = int(size.find('height').text)

    # 打开输出的 TXT 文件
    with open(output_txt_file, 'w') as f:
        # 遍历每个对象
        for obj in root.findall('object'):
            # 获取类别名称
            class_name = obj.find('name').text
            if class_name not in class_mapping:
                continue  # 如果类别不在映射中，跳过

            # 获取类别索引
            class_id = class_mapping[class_name]

            # 获取边界框坐标
            bndbox = obj.find('bndbox')
            xmin = float(bndbox.find('xmin').text)
            ymin = float(bndbox.find('ymin').text)
            xmax = float(bndbox.find('xmax').text)
            ymax = float(bndbox.find('ymax').text)

            # 转换为 YOLO 格式
            x_center = (xmin + xmax) / 2 / width
            y_center = (ymin + ymax) / 2 / height
            box_width = (xmax - xmin) / width
            box_height = (ymax - ymin) / height

            # 写入 TXT 文件
            f.write(f"{class_id} {x_center:.6f} {y_center:.6f} {box_width:.6f} {box_height:.6f}\n")


# 输入和输出目录
xml_dir = "D:\python\yolov5-7.0\Annotations"  # XML 文件所在的目录
txt_dir = "D:\python\yolov5-7.0\dataset\labels\\train"  # 输出的 TXT 文件目录
os.makedirs(txt_dir, exist_ok=True)

# 类别名称到索引的映射
class_mapping = {
    "ng": 0,  # 将 "ng" 映射为类别 0
}

# 遍历所有 XML 文件
for xml_file in os.listdir(xml_dir):
    if xml_file.endswith(".xml"):
        xml_path = os.path.join(xml_dir, xml_file)
        txt_file = xml_file.replace(".xml", ".txt")
        txt_path = os.path.join(txt_dir, txt_file)
        convert_xml_to_txt(xml_path, txt_path, class_mapping)

print("批量转换完成！")
