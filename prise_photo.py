import subprocess
import time
from PIL import Image

# Adresse IP de l'appareil Android
IP_DU_DISPOSITIF = ""

# Port ADB par défaut
PORT_ADB = 5555

# Dossier de destination sur le PC
DOSSIER_DESTINATION_PC = r"C:\Users\hp\Desktop\connectmobile\image"

# Dossier de destination sur l'appareil Android
DOSSIER_DESTINATION_ANDROID = "/sdcard/DCIM/Camera/mobile"

def crop_image(input_image, output_path, x, y, width, height):
    # Charger l'image
    img = cv2.imread(input_image)

    # Découper l'image en utilisant les coordonnées x, y, largeur et hauteur spécifiées
    cropped_img = img[y:y+height, x:x+width]

    # Enregistrer l'image découpée
    cv2.imwrite(output_path, cropped_img)


def  capture_photo(nom_photo):

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
    



    redemmarer_serveur()

def afficher_duree(duree):
    heures, reste = divmod(duree, 3600)
    minutes, secondes = divmod(reste, 60)
    print(f"Durée totale : {int(heures)} heures, {int(minutes)} minutes, {int(secondes)} secondes")

def redemmarer_serveur():
    tuer_serveur = "adb kill-server"
    subprocess.run(tuer_serveur, shell=True)
    lancer_serveur = "adb start-server"
    subprocess.run(lancer_serveur, shell=True)

# Exemple d'utilisation
nom_photo_personnalise = "setranj.jpg"
capture_photo(nom_photo_personnalise)

