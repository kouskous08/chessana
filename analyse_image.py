import cv2
import numpy as np
def tracer_rectangles(image_path, output_path, rectangles, color=(0, 100, 0), thickness=3 ):
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

x0=80
y0=80
xf=2170
yf=2144
yn=48

c8=(80,y0,350,yf)
c7=(350,y0,610,yf)
c6=(610,y0,870,yf)
c5=(870,y0,1130,yf)
c4=(1130,y0,1390,yf)
c3=(1390,y0,1650,yf)
c2=(1650,y0,1910,yf)
c1=(1910,y0,2170,yf)

ch=(x0,80,xf,340)
cg=(x0,340,xf,600)
cf=(x0,600,xf,860)
ce=(x0,860,xf,1120)
cd=(x0,1120,xf,1370)
cc=(x0,1370,xf,1630)
cb=(x0,1630,xf,1890)
ca=(x0,1890,xf,2144)

# Liste des coordonnées des rectangles à tracer
rectangles_list_n = [c8,c7,c6,c5,c4,c3,c2,c1]
rectangles_list_l=[ch,cg,cf,ce,cd,cc,cb,ca]

 #Appeler la fonction pour tracer les rectangles et enregistrer l'image
tracer_rectangles(image_path+image_name, output_image_path, rectangles_list_n)
tracer_rectangles(output_image_path, output_image_path, rectangles_list_l,(0,0,255))

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
    return presence_couleur_specifique >1000

a=cb 
b=c8  



coords_intersection = intersection(a, b)
bege_en_rouge("image/b_de.jpg")
presence_rouge('image_modifiee.jpg',coords_intersection)



