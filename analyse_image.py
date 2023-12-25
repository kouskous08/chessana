from PIL import Image
import cv2
import numpy as np

image_path = "C:\\Users\\hp\\Desktop\\connectmobile\\image"

def decouper_image(image_name):
    # Charger l'image
    img = Image.open(f"{image_path}\\{image_name}")

    # Spécifier les coordonnées du rectangle de découpe (gauche, haut, droite, bas)
    coordinates = (460, 0, 1654, 1160)  # (gauche, haut, droite, bas)

    # Découper l'image en utilisant les coordonnées spécifiées
    cropped_img = img.crop(coordinates)

    # Enregistrer l'image découpée
    cropped_img.save(f"{image_path}\\copy_{image_name}")



def img_noir_blanc(image_name):
    # Charger l'image depuis le fichier
    image = cv2.imread(f"{image_path}\\copy_{image_name}")

    # Convertir l'image en niveaux de gris
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Appliquer un flou gaussien pour réduire le bruit et améliorer la détection des contours
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Utiliser la détection des contours de Canny
    edges = cv2.Canny(blurred, 50, 150)

    # Trouver les contours dans l'image
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filtrer les contours pour obtenir les rectangles
    rectangles = []
    for contour in contours:
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        if len(approx) == 4 and cv2.contourArea(approx) > 1000:
            rectangles.append(approx)

    # Dessiner les rectangles détectés sur l'image originale
    result = image.copy()
    cv2.drawContours(result, rectangles, -1, (0, 255, 0), 2)

    # Enregistrer l'image résultante
    cv2.imwrite(f"{image_path}\\result_{image_name}", result)



img_noir_blanc("b.jpg")
