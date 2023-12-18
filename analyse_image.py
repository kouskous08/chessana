import cv2
import numpy as np
def detecter_echequier(image_path,output_path):
    # Charger l'image
    image = cv2.imread(image_path)
    
    # Convertir l'image en niveaux de gris
    gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Utiliser la détection des coins (Harris corner detection)
    coins = cv2.cornerHarris(gris, 2, 3, 0.04)

    # Dilater les coins pour les rendre plus visibles
    coins = cv2.dilate(coins, None)
    
    # Appliquer un seuillage pour obtenir les coins détectés
    seuil = 0.01 * coins.max()
    coins_detectes = np.where(coins > seuil)
    
	# Dessiner des cercles autour des coins détectés
    image[coins_detectes] = [0, 0, 255]

    # Afficher l'image résultante
    cv2.imshow('Echiquier detecte', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Enregistrer l'image résultante
    cv2.imwrite(output_path, image)
    
detecter_echequier('C:\\Users\\hp\\Desktop\\connectmobile\\image\\setranj.jpg', 'C:\\Users\\hp\\Desktop\\connectmobile\\image\\a.jpg')