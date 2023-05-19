import pandas as pd
import os

# 指定文件夹路径
folder_path = "D:\\Ori\\数据处理\\excel合并"  # 替换为实际的文件夹路径

# 获取文件夹下的所有xlsx文件的文件名
files = [f for f in os.listdir(folder_path) if f.endswith('.xlsx')]

# 创建一个空的DataFrame作为基础数据
df_base = pd.DataFrame()

# 循环读取每个xlsx文件，并纵向拼接到基础数据上
for file in files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_excel(file_path)
    df_base = pd.concat([df_base, df], axis=0)

# 保存纵向拼接后的数据到CSV文件
output_path = "D:\\Ori\\数据处理\\excel合并\\元素.csv"  # 替换为实际的输出路径和文件名
df_base.to_csv(output_path, index=False)

print("成功保存CSV文件到指定路径:", output_path)
