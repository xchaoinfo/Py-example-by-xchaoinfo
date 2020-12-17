import base64
from io import BytesIO

from PIL import Image


def compress_img_b64(img_path, compress_rate=5):
    """对图片压缩后, 转为 base64编码"""
    with Image.open(img_path) as im:
        w, h = im.size
        im.thumbnail((w / compress_rate, h / compress_rate))
        img_byte = BytesIO()
        im.convert("RGB").save(img_byte, format="jpeg")
        return base64.b64encode(img_byte.getvalue()).decode()
