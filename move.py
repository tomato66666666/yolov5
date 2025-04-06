import os
import shutil

# 设置路径
train_image_dir = "dataset/images/train"  # 训练图片目录
train_label_dir = "dataset/labels/train"  # 训练标注目录
val_image_dir = "dataset/images/val"      # 验证图片目录
val_label_dir = "dataset/labels/val"      # 验证标注目录

# 确保目标目录存在
os.makedirs(val_image_dir, exist_ok=True)
os.makedirs(val_label_dir, exist_ok=True)

# 获取所有图片文件
image_files = sorted(os.listdir(train_image_dir))  # 按文件名排序
label_files = sorted(os.listdir(train_label_dir))  # 按文件名排序

# 确保图片和标注文件一一对应
assert len(image_files) == len(label_files), "图片和标注文件数量不一致"

# 移动最后 40 张图片和标注文件
for image_file, label_file in zip(image_files[-40:], label_files[-40:]):
    # 移动图片
    shutil.move(os.path.join(train_image_dir, image_file), os.path.join(val_image_dir, image_file))
    # 移动标注
    shutil.move(os.path.join(train_label_dir, label_file), os.path.join(val_label_dir, label_file))

print("移动完成！")