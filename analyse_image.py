import cv2
import numpy as np
def tracer_rectangles(image_path, output_path, rectangles, color=(0, 100, 0), thickness=1):
    # Charger l'image à partir du fichier
    image = cv2.imread(image_path)

    # Tracer les rectangles sur l'image
    for rect_coords in rectangles:
        x1, y1, x2, y2 = rect_coords
        cv2.rectangle(image, (x1, y1), (x2, y2), color, thickness)

    # Enregistrer l'image modifiée à l'emplacement spécifié
    cv2.imwrite(output_path, image)

    # Afficher l'image avec les rectangles (facultatif)


def intersection(rectangle1, rectangle2):
    x_intersection = max(rectangle1[0], rectangle2[0])
    y_intersection = max(rectangle1[1], rectangle2[1])
    x2_intersection = min(rectangle1[2], rectangle2[2])
    y2_intersection = min(rectangle1[3], rectangle2[3])

    if x_intersection < x2_intersection and y_intersection < y2_intersection:
        # Il y a une intersection
        return (x_intersection, y_intersection, x2_intersection, y2_intersection)
    else:
        # Pas d'intersection
        return None



# Définir le chemin de l'image d'entrée
image_path = "C:\\Users\\hp\\Desktop\\connectmobile\\image"
image_name="\\c_de.jpg"
# Définir le chemin de sortie pour l'image modifiée
output_image_path = "C:\\Users\\hp\\Desktop\\connectmobile\\image\\a_modifiee.jpg"

x0=42
y0=50
xf=850
yf=850
yn=48

c8=(42,y0,145,yf)
c7=(145,y0,250,yf)
c6=(250,y0,350,yf)
c5=(350,y0,450,yf)
c4=(450,y0,550,yf)
c3=(550,y0,650,yf)
c2=(650,y0,750,yf)
c1=(750,y0,850,yf)

ch=(x0,50,xf,150)
cg=(x0,150,xf,250)
cf=(x0,250,xf,350)
ce=(x0,350,xf,450)
cd=(x0,450,xf,550)
cc=(x0,550,xf,650)
cb=(x0,650,xf,750)
ca=(x0,750,xf,850)

# Liste des coordonnées des rectangles à tracer
#rectangles_list_n = [c6]
#rectangles_list_l=[ce]

# Appeler la fonction pour tracer les rectangles et enregistrer l'image
#tracer_rectangles(image_path+image_name, output_image_path, rectangles_list_n)
#tracer_rectangles(output_image_path, output_image_path, rectangles_list_l,(0,0,255))

def bege_en_rouge(image_name):
    image = cv2.imread(image_name)
    couleur_source = np.array([72, 155, 194])
    nouvelle_couleur = np.array([0, 0, 255])
    tolerance = 50
    masque = np.all(np.abs(image - couleur_source) < tolerance, axis=-1)
    image[masque] = nouvelle_couleur
    cv2.imwrite('image_modifiee.jpg', image)


def presence_rouge(image_name,coords):
    image = cv2.imread(image_name) 
    x1, y1 = coords[0], coords[1]
    x2, y2 = coords[2], coords[3]
    region = image[y1:y2, x1:x2]
    couleur_a_detecter = np.array([0, 0, 255]) 
    tolerance = 5
    couleur_basse = couleur_a_detecter - tolerance
    couleur_haute = couleur_a_detecter + tolerance    
    masque = cv2.inRange(region, couleur_basse, couleur_haute)
    presence_couleur_specifique = np.any(masque > 0)
    return presence_couleur_specifique

a=ch 
b=c1  



coords_intersection = intersection(a, b)
bege_en_rouge("image/G.jpg")
presence_rouge('image_modifiee.jpg',coords_intersection)



