import cv2
import numpy as np

# Charger votre image
image = cv2.imread('image/c_de.jpg')

# Définir la couleur que vous souhaitez remplacer (par exemple, RGB: 194, 155, 72)
couleur_source = np.array([72, 155, 194])

# Définir la nouvelle couleur (par exemple, RGB: 255, 0, 0)
nouvelle_couleur = np.array([0, 0, 255])

# Définir une marge de tolérance pour la comparaison des couleurs
tolerance = 50

# Trouver les pixels dans la plage de couleur spécifiée avec une tolérance
masque = np.all(np.abs(image - couleur_source) < tolerance, axis=-1)

# Remplacer la couleur dans l'image
image[masque] = nouvelle_couleur

# Enregistrer l'image modifiée
cv2.imwrite('image_modifiee.jpg', image)

# Charger votre image
image = cv2.imread('image/c_de.jpg')

# Définir la couleur spécifique que vous souhaitez détecter (par exemple, 0, 0, 255 pour le rouge)
couleur_a_detecter = np.array([0, 0, 255])

# Définir une petite plage de couleurs autour de la couleur spécifique
tolerance = 5
couleur_basse = couleur_a_detecter - tolerance
couleur_haute = couleur_a_detecter + tolerance

# Créer un masque en utilisant la plage de couleurs spécifiée
masque = cv2.inRange(image, couleur_basse, couleur_haute)

# Vérifier si le masque contient des pixels non nuls (c'est-à-dire la présence de la couleur spécifique)
presence_couleur_specifique = np.any(masque > 0)

# Afficher le résultat (True si la couleur spécifique est présente, False sinon)
print("La couleur spécifique est présente :", presence_couleur_specifique)



#hadi machi mohima :
def comparer_image(image1, image2, coords, output_path, seuil=50000):
    # Charger l'image
    image1 = cv2.imread(image1)
    image2 = cv2.imread(image2)

    # Convertir les images en niveaux de gris
    image1_xyz = cv2.cvtColor(image1, cv2.COLOR_BGR2XYZ)
    image2_xyz = cv2.cvtColor(image2, cv2.COLOR_BGR2XYZ)

    # Extraire les coordonnées du coin supérieur gauche et du coin inférieur droit
    x1, y1 = coords[0], coords[1]
    x2, y2 = coords[2], coords[3]

    # Extraire la région spécifiée
    region1 = image1_xyz[y1:y2, x1:x2]
    region2 = image2_xyz[y1:y2, x1:x2]


    # Calculer la différence absolue entre les deux régions
    difference = cv2.absdiff(region1, region2)

    # Calculer la somme des valeurs des pixels de la différence
    somme_diff = np.sum(difference)
    print(somme_diff)
    cv2.imwrite(output_path, difference)




    # Comparer avec le seuil
    if somme_diff > seuil:
        return True
    else:
        return False
