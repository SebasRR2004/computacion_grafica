import numpy as np
import matplotlib.pyplot as plt

def CapaImg (img:np.array, Capa:int)->np.array:
    fil, col, cap = img.shape

    imgCapa = np.zeros((fil, col, 3))
    imgCapa[:, :, Capa] = img[:, :, Capa]

    return imgCapa

def BrilloImg (img:np.array, Brillo:int)->np.array:
    copiaImg:np.array = np.copy(img)
    return (copiaImg+Brillo)

def AjusteCanal (img:np.array, brillo:int, capa:int)->np.array:
    copiaImg:np.array = np.copy(img)
    copiaImg[:, :, capa] =  copiaImg[:, :, capa]+brillo
    return copiaImg

def Contraste (img:np.array, contraste:float, tipo:int)->np.array:
    if (tipo == 0):
        img = contraste*np.log10(1+img)
    else :
        img = contraste*np.exp(img-1)

    return img

#3
def invertirColor (img:np.array)->np.array:
    return 1 - img

#4






# import matplotlib.pyplot as plt
# import numpy as np
# plt.rcParams['image.cmap'] = 'gray'
