import os
import re
import requests
import upyun
from urllib.parse import urlparse
from dotenv import load_dotenv

# 从.env文件中加载环境变量
load_dotenv()

# 从环境变量中获取又拍云配置信息
BUCKET_NAME = os.getenv('BUCKET_NAME')
OPERATOR_NAME = os.getenv('OPERATOR_NAME')
OPERATOR_PWD = os.getenv('OPERATOR_PWD')
DIR_PATH = os.getenv('DIR_PATH')

up = upyun.UpYun(BUCKET_NAME, OPERATOR_NAME, OPERATOR_PWD)

# 获取当前目录下的所有md文件
md_files = [f for f in os.listdir() if os.path.isfile(f) and f.endswith('.md')]

for md_file in md_files:
    # 读取md文件内容
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 匹配所有图片链接
    img_urls = re.findall('!\[.*?\]\((.*?)\)', content)

    for img_url in img_urls:
        # 判断图片链接是否为本地链接
        if img_url.startswith('http'):
            # 判断图片链接是否为upyun.xuqiming.tech的链接
            if 'upyun.xuqiming.tech' in img_url:
                continue 
            # 如果是网络图片，将其转存到又拍云
            response = requests.get(img_url)
            img_name = os.path.basename(urlparse(img_url).path)
            img_path = DIR_PATH + img_name
            up.put(img_path, response.content)
            # 替换md文件中的图片链接
            content = content.replace(img_url, f'https://upyun.xuqiming.tech{img_path}')
            print(f'{img_name}已上传')
        else:
            # 如果是本地图片，直接上传到又拍云
            with open(img_url, 'rb') as f:
                img_name = os.path.basename(img_url)
                img_path = DIR_PATH + img_name
                up.put(img_path, f.read())
                # 替换md文件中的图片链接
                content = content.replace(img_url, f'https://upyun.xuqiming.tech{img_path}')
                print(f'{img_name}已上传')

    # 将更新后的md文件内容写回文件
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'{md_file}已处理完毕')
