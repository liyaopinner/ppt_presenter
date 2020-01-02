import os
import json

from PIL import Image

import oss2


access_key_id = "LTAI4Fgiaw9k5pJSVGQD9e7T"
access_key_secret = "6AdaCS8Yks0t0ML6AT5VAUVrIKLDmB"
bucket_name = "51ppt"
endpoint = "http://oss-cn-hangzhou.aliyuncs.com"


# 确认上面的参数都填写正确了
for param in (access_key_id, access_key_secret, bucket_name, endpoint):
    assert '<' not in param, '请设置参数：' + param

def get_image_info(image_file):
    """获取本地图片信息
    :param str image_file: 本地图片
    :return tuple: a 3-tuple(height, width, format).
    """
    im = Image.open(image_file)
    return im.height, im.width, im.format

# 创建Bucket对象，所有Object相关的接口都可以通过Bucket对象来进行
bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name)

key = 'test/example2.jpg'
new_pic = 'new-example.jpg'

# 上传示例图片
bucket.put_object_from_file(key, '第一范式.png')

#分类-多维度分类，文件名，id对应

"""
单文件
    1. 文本内容
    2. 附件
    3. 图片管理
    4. 封面管理
    5. 分类管理
"""

# 获取图片信息
result = bucket.get_object(key, process='image/info')
a = 1

