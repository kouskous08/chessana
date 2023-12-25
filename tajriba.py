import cv2
import numpy as np

# Chemin de l'image
image_path = 'C:\\Users\\hp\\Desktop\\connectmobile\\image'
output_path = 'C:\\Users\\hp\\Desktop\\connectmobile\\image'

def compter_carreaux_blancs(nom_image):
    # Charger l'image depuis le fichier
    image = cv2.imread(f"{image_path}\\{nom_image}")

    # Convertir l'image en niveaux de gris
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Définir les plages de couleurs que vous souhaitez détecter (noir et blanc)
    lower_black = 0
    upper_black = 100

    lower_white = 150
    upper_white = 255

    # Créer les masques pour chaque plage de couleurs
    mask_black = cv2.inRange(gray, lower_black, upper_black)
    mask_white = cv2.inRange(gray, lower_white, upper_white)

    # Appliquer les masques à l'image d'origine
    result_black = cv2.bitwise_and(gray, gray, mask=mask_black)
    result_white = cv2.bitwise_and(gray, gray, mask=mask_white)

    # Trouver les contours dans les images résultantes
    contours_black, _ = cv2.findContours(mask_black, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_white, _ = cv2.findContours(mask_white, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Dessiner les contours sur l'image d'origine
    image_with_contours = image.copy()
    cv2.drawContours(image_with_contours, contours_white, -1, (255, 0, 0), 2)  # Bleu pour les contours blancs
    cv2.drawContours(image_with_contours, contours_black, -1, (0, 0, 255), 2)  # Rouge pour les contours noirs
    # Enregistrer l'image avec les contours
    cv2.imwrite(f'{output_path}\\contours_{nom_image}', image_with_contours)

    # Compter le nombre de carreaux blancs
    nombre_carreaux_blancs = len(contours_white)
    print(f"Nombre de carreaux blancs : {nombre_carreaux_blancs}")
    nombre_carreaux_noirs = len(contours_black)
    print(f"Nombre de carreaux blancs : {nombre_carreaux_noirs}")

compter_carreaux_blancs("copy_b.jpg")
#yaaaa dakiiiii mchi 3adl wahd image bwa7da wu chof coordonne diala wu menba3d ayi moraba3 3ay kon 3ando coordonne dialo mhn htan chi nhar wu 3adla wu hada ghir tadye3 d lwa9t  ana n 3tik mital:
#db 3ana A1 Fiha A wu fiha 1 wu 3an 3adlo le carre fayn kayn l intersection entre le rectangle de A wu 1
#wu menba3d 3ad super posihom bach d chof teswira mhm hin i kon 3andk wa9t khawi 3adla
