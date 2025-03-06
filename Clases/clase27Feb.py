import numpy as np
import matplotlib.pyplot as plt
import ProceImg as pi
from skimage import io, filters 


MiImagen=np.array(plt.imread("photo.jpg"))/255

plt.figure(1)
plt.subplot(2,2,1)
plt.imshow(MiImagen)
plt.title("Imagen Original")

plt.subplot(2,2,2)
BrilloImg=pi.BrilloImg(MiImagen, 0.5)
plt.imshow(BrilloImg)
plt.title("Ajuste de Brillo")

plt.subplot(2,2,3)
AjusteCanal=pi.AjusteCanal(MiImagen, 100, 0)
plt.imshow(AjusteCanal) 

# plt.subplot(2,2,4)
# Contraste=pi.Contraste(MiImagen, 0.5, 1)    
# plt.imshow(Contraste)

plt.subplot(2,2,4)
invetir=pi.invertirColor(MiImagen)    
plt.imshow(invetir)
plt.title("Color Invertido")
plt.show()

# --------------------------- #
# image_rgb = io.imread("photo.jpg")/255

# plt.subplot(221)
# plt.imshow(image_rgb)
# plt.title("Imagen Original")

# plt.subplot(222)
# plt.imshow(image_rgb[:,:,0])
# plt.title("Canal Rojo")

# plt.subplot(223)
# plt.imshow(image_rgb[:,:,1])
# plt.title("Canal Verde")

# plt.subplot(224)
# plt.imshow(image_rgb[:,:,2])
# plt.title("Canal Azul")

# plt.show()

# print("- Dimensiones de la imagen:")
# print(image_rgb.shape)