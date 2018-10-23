from freenect2 import Device, FrameType
import numpy as np
from PIL import Image

dispositivo = Device()   #inicializar el dispositivo

with dispositivo.running():
    for tipo, frame in dispositivo: 		#por cada frame que reciba
        if tipo is FrameType.Ir: 		#cuando reciba el primer frame de tipo IR se detiene para procesarlo
            break

#proceso para normalizar a un rango de 0,1 los valores recibidos en el frame IR que estan en un rango de 0,65535
#para esto se divide la matriz para el valor maximo y luego se aplica raiz cuadrada(similar a un correccion simple de gamma).
ir_image = frame.to_array()
ir_image /= ir_image.max()
ir_image = np.sqrt(ir_image)

# guardar la imagen
Image.fromarray(256 * ir_image).convert('L').save('IRimage.tiff')
