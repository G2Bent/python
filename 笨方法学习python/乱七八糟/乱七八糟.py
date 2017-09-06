from PIL import Image
import numpy as np

import pdir,requests

#修改图片的RGB值
a = np.array(Image.open("test.jpg"))
b = [122,222,255]-a
im = Image.fromarray(b.astype("uint8"))
im.save("new.jpg")

#查看对象的全部属性和方法
print(pdir(requests))