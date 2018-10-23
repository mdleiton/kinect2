from PIL.ImageMath import eval as im_eval
from freenect2 import Device, FrameType

def guardarprofundidad(depth):
	archivo = open ('depthimage.txt','w')
	arreglo=depth.to_array()
	for i in arreglo:
		for j in i:
			archivo.write(' {:.10f}'.format(j*0.001))
		archivo.write("\n")
	archivo.close()

frames = {}
dispositivo = Device()
with dispositivo.running():
    for frame_type, frame in dispositivo:
	frames[frame_type] = frame
        if frame_type is FrameType.Depth:
            break
depth= frames[FrameType.Depth]
guardarprofundidad(depth)
#normalizar valores de profundidad a rango de 0-255
norm_im = im_eval('convert(I / 16, "L")', I=frame.to_image())
norm_im.save('Depthimage.tiff')



