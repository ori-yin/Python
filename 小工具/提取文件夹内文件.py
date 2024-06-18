import os
import shutil

def move_images(src_dir, dst_dir, image_extensions=None):
    """
    将源文件夹及其子文件夹中的所有图片文件移动到目标文件夹。
    
    参数:
    src_dir (str): 源文件夹路径
    dst_dir (str): 目标文件夹路径
    image_extensions (list): 图片文件扩展名列表（可选）
    """
    
    # 如果没有提供图片扩展名列表，使用默认的图片扩展名
    if image_extensions is None:
        image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']
    
    # 如果目标文件夹不存在，则创建目标文件夹
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    
    # 遍历源文件夹及其所有子文件夹
    for root, _, files in os.walk(src_dir):
        for file in files:
            # 检查文件扩展名是否在图片扩展名列表中
            if any(file.lower().endswith(ext) for ext in image_extensions):
                src_file = os.path.join(root, file)  # 源文件的完整路径
                dst_file = os.path.join(dst_dir, file)  # 目标文件的完整路径
                
                # 确保目标文件夹中不存在同名文件
                if not os.path.exists(dst_file):
                    shutil.move(src_file, dst_file)  # 移动文件到目标文件夹
                else:
                    # 如果目标文件夹中存在同名文件，添加计数器重命名文件
                    base, ext = os.path.splitext(file)
                    counter = 1
                    while os.path.exists(dst_file):
                        new_file_name = f"{base}_{counter}{ext}"  # 新文件名
                        dst_file = os.path.join(dst_dir, new_file_name)  # 新目标文件路径
                        counter += 1
                    shutil.move(src_file, dst_file)  # 移动文件到目标文件夹
                
                # 打印移动的文件信息
                print(f"Moved: {src_file} to {dst_file}")

# 示例用法
src_directory = '你的源文件夹路径'  # 替换为实际的源文件夹路径
dst_directory = '你的目标文件夹路径'  # 替换为实际的目标文件夹路径
move_images(src_directory, dst_directory)
