from PIL import Image
import cv2
import numpy as np

def traiter_image(chemin_image):
    # Charger l'image
    image = cv2.imread(chemin_image)

    # Convertir en niveaux de gris
    gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Appliquer un flou pour réduire le bruit
    flou = cv2.GaussianBlur(gris, (5, 5), 0)

    return flou

def detecter_mouvement(image_precedente, image_actuelle):
    # Soustraction d'arrière-plan
    difference = cv2.absdiff(image_precedente, image_actuelle)

    # Seuiller l'image pour obtenir les zones de mouvement
    _, seuil = cv2.threshold(difference, 30, 255, cv2.THRESH_BINARY)

    # Trouver les contours des zones de mouvement
    contours, _ = cv2.findContours(seuil, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Dessiner les contours sur l'image d'origine (à des fins de visualisation)
    image_resultante = image_actuelle.copy()
    cv2.drawContours(image_resultante, contours, -1, (0, 255, 0), 2)

    return image_resultante

# Chemin de l'image
chemin_image = 'C:\\Users\\hp\\Desktop\\connectmobile\\image\\copy_b.jpg'

# Traitement de l'image
image_precedente = traiter_image(chemin_image)
image_actuelle = traiter_image(chemin_image)

# Détection des mouvements
image_mouvement = detecter_mouvement(image_precedente, image_actuelle)

# Afficher l'image résultante avec les contours de mouvement
cv2.imshow("Détection de mouvement", image_mouvement)
cv2.waitKey(0)
cv2.destroyAllWindows()
