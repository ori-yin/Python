import pandas as pd
import os

# 指定文件夹路径
folder_path = "文件夹路径"

# 获取文件夹下的所有excel文件的文件名
files = [f for f in os.listdir(folder_path) if f.endswith('.xlsx')]

# 读取第一个excel文件作为基础数据
df = pd.read_excel(os.path.join(folder_path, files[0]))

# 循环读取剩下的excel文件，并纵向连接到基础数据上
for file in files[1:]:
    temp_df = pd.read_excel(os.path.join(folder_path, file))
    df = pd.concat([df, temp_df], axis=0)

# 保存纵向连接后的数据到新的excel文件
df.to_excel("纵向连接后的数据.xlsx", index=False)
