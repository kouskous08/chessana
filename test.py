from PIL import Image
# Fonction pour obtenir les dimensions d'une image

chemin_image=r"C:\Users\hp\Desktop\connectmobile\image\setranj.jpg"
image = Image.open(chemin_image)
largeur, hauteur = image.size
print (largeur, hauteur)