#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 13:18:40 2024

@author: leijianan
"""

from io import StringIO
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import numpy as np
import matplotlib.pyplot as plt

url="https://www.hko.gov.hk/sc/wxinfo/season/catRF_91-20.htm"
response = requests.get(url)

if response.ok:
    print("Data is ready")
    
    # 使用 BeautifulSoup 解析 HTML
    soup = bs(response.text,'html.parser')
    # 找到包含数据的表格（假设数据在第一个表格中）
    table = soup.find('table') # 根据实际情况选择合适的选择器
    
table_str = str(table)

table_io = StringIO(table_str)

df = pd.read_html(table_io,header=2)[0]
df = df.values
df = df[0::2]
df[0,0]='month1'
df[1,0]='month2'
df[2,0]='month3'
df[3,0]='month4'
df[4,0]='month5'
df[5,0]='month6'
df[6,0]='month7'
df[7,0]='month8'
df[8,0]='month9'
df[9,0]='month10'
df[10,0]='month11'
df[11,0]='month12'
df[:, 1] = [s[2:-2] for s in df[:, 1]]
df[:, 3] = [s[2:-2] for s in df[:, 3]]
df = np.delete(df,2, axis=1)
custom_columns = ['month', 'low rainfall', 'high rainfall']

# 将 NumPy 数组转换为 DataFrame，并设置自定义列标签
df = pd.DataFrame(df, columns=custom_columns)
print(df)
# 绘制折线图
plt.figure(figsize=(10, 5))
plt.plot(df['month'], df['low rainfall'], marker='o', label='Low Rainfall')
plt.plot(df['month'], df['high rainfall'], marker='o', label='High Rainfall')

# 添加标题和标签
plt.title('Rainfall Level')
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
plt.xticks(rotation=45)  # 旋转 x 轴标签以便更好地显示
plt.legend()  # 显示图例

# 显示图形
plt.tight_layout()  # 自动调整布局
plt.show()