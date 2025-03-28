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

# 3. Crear una función que invierta los colores de una imagen
def invertirColor (img:np.array)->np.array:
    return 1 - img

# 4. Crear una función que retorne una imagen con solo el canal rojo
def extraerRojo(img: np.array) -> np.array:
    img_roja = np.zeros_like(img)
    img_roja[:, :, 0] = img[:, :, 0]  # Mantener solo el canal rojo
    return img_roja

# 5. Crear una función que retorne una imagen con solo el canal verde
def extraerVerde(img: np.array) -> np.array:
    img_verde = np.zeros_like(img)
    img_verde[:, :, 1] = img[:, :, 1]  # Mantener solo el canal verde
    return img_verde

# 6. Crear una función que retorne una imagen con solo el canal azul
def extraerAzul(img: np.array) -> np.array:
    img_azul = np.zeros_like(img)
    img_azul[:, :, 2] = img[:, :, 2]  # Mantener solo el canal azul
    return img_azul

# 7. Crear una función que retorne una imagen con color Magenta (rojo y azul)
def extraerMagenta(img: np.array) -> np.array:
    img_magenta = np.zeros_like(img)
    img_magenta[:, :, 0] = img[:, :, 0]  # Mantener el canal rojo
    img_magenta[:, :, 2] = img[:, :, 2]  # Mantener el canal azul
    return img_magenta

# 8. Crear una función que retorne una imagen con color Cyan (verde y azul)
def extraerCyan(img: np.array) -> np.array:
    img_cyan = np.zeros_like(img)
    img_cyan[:, :, 1] = img[:, :, 1]  # Mantener el canal verde
    img_cyan[:, :, 2] = img[:, :, 2]  # Mantener el canal azul
    return img_cyan

# 9. Crear una función que retorne una imagen con color Amarillo (rojo y verde)
def extraerAmarillo(img: np.array) -> np.array:
    img_amarillo = np.zeros_like(img)
    img_amarillo[:, :, 0] = img[:, :, 0]  # Mantener el canal rojo
    img_amarillo[:, :, 1] = img[:, :, 1]  # Mantener el canal verde
    return img_amarillo

# 10. Crear una función que reconstruya una imagen a partir de sus canales de color
def reconstruirImagen(roj: np.array, ver: np.array, azu: np.array) -> np.array:
    return roj + ver + azu  # Suma de los canales para reconstruir la imagen

# 11. Crear una función que fusiona dos imágenes sin ecualizar
def fusionarImagenes(img1: np.array, img2: np.array) -> np.array:
    # Asegurar que ambas imágenes tienen la misma forma
    if img1.shape != img2.shape:
        raise ValueError("Las imágenes deben tener la misma forma para fusionarlas.")

    # Sumar las dos imágenes sin ecualizar
    img_fusionada = img1 + img2

    # Clipping para evitar valores mayores a 1 (si las imágenes están normalizadas)
    img_fusionada = np.clip(img_fusionada, 0, 1)

    return img_fusionada

# 12. Crear una función que fusiona dos imágenes con ecualización
def ecualizarImagen(img: np.array) -> np.array:
    img = (img * 255).astype(np.uint8)  # Convertir a uint8 si estaba normalizada (0-1)
    img_ecualizada = np.zeros_like(img)  # Crear imagen vacía

    for i in range(3):  # Aplicar ecualización a cada canal (R, G, B)
        img_ecualizada[:, :, i] = cv2.equalizeHist(img[:, :, i])  # Ecualizar cada canal

    return img_ecualizada / 255  # Normalizar de vuelta a (0-1)

def fusionarImagenesEcualizadas(img1: np.array, img2: np.array) -> np.array:
    # Asegurar que ambas imágenes tienen la misma forma
    if img1.shape != img2.shape:
        raise ValueError("Las imágenes deben tener la misma forma para fusionarlas.")

    # Fusionar imágenes (suma de píxeles)
    img_fusionada = img1 + img2
    img_fusionada = np.clip(img_fusionada, 0, 1)  # Evitar valores fuera de rango

    # Aplicar ecualización
    img_fusionada_ecualizada = ecualizarImagen(img_fusionada)

    return img_fusionada_ecualizada

# 13. Crear una función que ecualice una imagen con un factor de intensidad
def ecualizarImagenFactor(img: np.array, factor: float) -> np.array:
    if factor < 0 or factor > 1:
        raise ValueError("El factor debe estar en el rango [0, 1]")

    # Convertir la imagen a uint8 (rango 0-255) si está normalizada
    img_uint8 = (img * 255).astype(np.uint8)

    # Aplicar ecualización de histograma en cada canal
    img_ecualizada = np.zeros_like(img_uint8)
    for i in range(3):  # Canales R, G, B
        img_ecualizada[:, :, i] = cv2.equalizeHist(img_uint8[:, :, i])

    # Convertir de vuelta a rango 0-1
    img_ecualizada = img_ecualizada / 255.0

    # Interpolación lineal entre la imagen original y la ecualizada
    img_resultado = (1 - factor) * img + factor * img_ecualizada

    return np.clip(img_resultado, 0, 1)

# 14 y 15. Crear una función que convierta una imagen a escala de grises usando el método promedio (Avarege)
def avarage(img: np.array) -> np.array:
    # Calcular el promedio de los canales RGB
    img_promedio = np.mean(img, axis=2)

    return img_promedio

# 16. Crear una función que convierta una imagen a escala de grises usando el método ponderado (Luminosity)
def luminosity(img: np.array) -> np.array:
    coeficientes = np.array([0.2989, 0.5870, 0.1140])  # Pesos de la luminosidad
    return np.dot(img[..., :3], coeficientes)

# 17. Crear una función que convierta una imagen a escala de grises usando el método de tonalidad (Midgray)
def midgray(img: np.array) -> np.array:
    return (np.max(img, axis=2) + np.min(img, axis=2)) / 2