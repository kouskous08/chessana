import cv2
import numpy as np

image_path="image\\b_de.jpg"
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
cv2.imwrite("image\\bab_de.jpg", image_gris)



