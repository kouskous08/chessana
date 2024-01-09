import cv2
import numpy as np
def appliquer_toutes_transformations_couleur(image_path):
    # Charger l'image
    image = cv2.imread(image_path)

    # Afficher l'image originale
    cv2.imshow("Image Originale", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Convertir en niveaux de gris
    image_gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Image en Niveaux de Gris", image_gris)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Convertir en espace de couleur HSV
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    cv2.imshow("Image en HSV", image_hsv)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Convertir en espace de couleur LAB
    image_lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    cv2.imshow("Image en LAB", image_lab)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Convertir en échelle de gris avec teinte constante (Luminance en HLS)
    image_luminance = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)[:, :, 1]
    cv2.imshow("Image en Echelle de Gris avec Teinte Constante", image_luminance)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Convertir en sépia
    image_sepia = cv2.transform(image, np.array([[0.393, 0.769, 0.189],
                                                  [0.349, 0.686, 0.168],
                                                  [0.272, 0.534, 0.131]]))
    cv2.imshow("Image en Sépia", image_sepia)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Convertir en espace de couleur XYZ
    image_xyz = cv2.cvtColor(image, cv2.COLOR_BGR2XYZ)
    cv2.imshow("Image en XYZ", image_xyz)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Convertir en espace de couleur Luv
    image_luv = cv2.cvtColor(image, cv2.COLOR_BGR2Luv)
    cv2.imshow("Image en Luv", image_luv)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Exemple d'utilisation avec le chemin de l'image
image_path = "image\\c_de.jpg"  # Remplacez cela par le chemin de votre image
appliquer_toutes_transformations_couleur(image_path)
