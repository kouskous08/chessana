import cv2
import numpy as np

def detecter_echequier(image_path, output_path):
    # Charger l'image
    image = cv2.imread(image_path)

    # Convertir l'image en niveaux de gris
    gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Appliquer un flou pour améliorer la détection des contours
    flou = cv2.GaussianBlur(gris, (5, 5), 0)

    # Utiliser la détection de contours Canny
    contours = cv2.Canny(flou, 50, 150)

    # Utiliser la transformée de Hough pour détecter les lignes
    lignes = cv2.HoughLines(contours, 1, np.pi / 180, 100)

    # Dessiner les lignes détectées sur l'image originale
    for ligne in lignes:
        rho, theta = ligne[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

    # Afficher et enregistrer l'image résultante
    cv2.imshow('Echiquier detecte', image)
    cv2.imwrite(output_path, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

detecter_echequier('C:\\Users\\hp\\Desktop\\connectmobile\\image\\setranj.jpg', 'C:\\Users\\hp\\Desktop\\connectmobile\\image\\a.jpg')