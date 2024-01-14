import subprocess
import time
import cv2
import numpy as np

#prendre photo
IP_DU_DISPOSITIF = ""

PORT_ADB = 5555

DOSSIER_DESTINATION_PC = "C:\\Users\\hp\\Desktop\\connectmobile\\image"

DOSSIER_DESTINATION_ANDROID = "/sdcard/DCIM/Camera/mobile"

def  prendre_photo(nom_photo):

    debut_chronometre_global = time.time()
    

    commande_capture_photo = f"adb connect {IP_DU_DISPOSITIF}:{PORT_ADB} && adb shell input keyevent KEYCODE_CAMERA"
    subprocess.run(commande_capture_photo, shell=True)
    

    time.sleep(2)
    

    commande_derniere_image = f"adb shell \"ls -t /sdcard/DCIM/Camera/ | head -n 1\""
    derniere_image = subprocess.run(commande_derniere_image, shell=True, capture_output=True, text=True)
    derniere_image = derniere_image.stdout.strip()


    commande_changer = f"adb shell mv /sdcard/DCIM/Camera/{derniere_image} {DOSSIER_DESTINATION_ANDROID}/{nom_photo}"
    subprocess.run(commande_changer, shell=True)
    

    commande_copie_photo = f"adb pull {DOSSIER_DESTINATION_ANDROID}/{nom_photo} {DOSSIER_DESTINATION_PC}/{nom_photo}"
    subprocess.run(commande_copie_photo, shell=True)
    

    duree_ecoulee_global = time.time() - debut_chronometre_global
    afficher_duree(duree_ecoulee_global)
    

def afficher_duree(duree):
    heures, reste = divmod(duree, 3600)
    minutes, secondes = divmod(reste, 60)
    print(f"Durée totale : {int(heures)} heures, {int(minutes)} minutes, {int(secondes)} secondes")

def redemmarer_serveur():
    tuer_serveur = "adb kill-server"
    subprocess.run(tuer_serveur, shell=True)
    lancer_serveur = "adb start-server"
    subprocess.run(lancer_serveur, shell=True)

#couper l image (3la 7asab la taille d echequier)

def crop_image(input_image, output_path):
    img = cv2.imread(input_image)
    cropped_img = img[1000:1000+2260, 0:0+2260]#img[y:y+height, x:x+width]
    cv2.imwrite(output_path, cropped_img)


x = 0
y = 1000
width = 2260
height = 2260
crop_image("image\\c.jpg","image\\c_de.jpg",x,y,width,height)
#ta9sim d la tables n ligne et collone
#mchi chof analyse_image.py
