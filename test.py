import cv2
import numpy as np

# Chemin de l'image
image_path = 'C:\\Users\\hp\\Desktop\\connectmobile\\image'
output_path = 'C:\\Users\\hp\\Desktop\\connectmobile\\image'
def analyse_carreau(nom_image):
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

	# Enregistrer les images résultantes
	cv2.imwrite(f'{output_path}\\noir_b.jpg', result_black)
	cv2.imwrite(f'{output_path}\\blanc_b.jpg', result_white)

analyse_carreau("copy_b.jpg")

