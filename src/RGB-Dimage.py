from freenect2 import Device, FrameType
import numpy as np

dispositivo = Device()
frames = {}
with dispositivo.running():
    for type_, frame in dispositivo:
        frames[type_] = frame
        if FrameType.Color in frames and FrameType.Depth in frames:
            break

#calibracion para no distortionar el frame de profundidad y registrar el frame RGB juntos.
rgb, depth = frames[FrameType.Color], frames[FrameType.Depth]
undistorted, registered, big_depth = dispositivo.registration.apply(
    rgb, depth, with_big_depth=True)

# unirlos como una nube de puntos.
with open('np.pcd', 'wb') as fobj:
    dispositivo.registration.write_pcd(fobj, undistorted, registered)

with open('np_grande.pcd', 'wb') as fobj:
   dispositivo.registration.write_big_pcd(fobj, big_depth, rgb)
