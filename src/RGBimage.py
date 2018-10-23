from freenect2 import Device, FrameType
import numpy as np
from PIL import Image

dispositivo = Device()   #inicializar el dispositivo

with dispositivo.running():
    for type_, frame in dispositivo: 		#por cada frame que reciba
        if type_ is FrameType.Color: 		#cuando reciba el primer frame de tipo RGB se detiene para procesarlo
            break
#generar imagen  RGB
rgb_image=frame.to_image()
rgb_image.save("RGBimage.tiff")

#generar imagen  BGR
bgr_image = frame.to_array()
bgr = Image.fromarray(bgr_image)
bgr.save("BGRimage.tiff")

