from easyAI import easyAI

### Importer une image 
image = easyAI.lireImage("../../../lib/rgb.jpg")

### Afficher une image 
easyAI.afficherImage("Couleurs", image)

### Accéder aux pixels d'une image pour comprendre la notation RGB
# Rouge 
easyAI.lirePixelRGB(image, 350, 250)
# Vert
easyAI.lirePixelRGB(image, 100, 500)
# Bleu 
easyAI.lirePixelRGB(image, 600, 400)

### Convertir en tons de gris
image = easyAI.lireImage("../../../lib/shapes.jpg")
gris = easyAI.convertirGris(image)
easyAI.afficherImage("Tons de gris", gris)

### Seuillage d'une image (doit bien être expliqué)
seuil = easyAI.seuillerImage(gris, 225, 255)
easyAI.afficherImage("Seuillage", seuil)

### Trouver les contours d'une image 
contours = easyAI.trouverContours(seuil)

### Dessiner les contours sur une image 
for contour in contours: 
    easyAI.dessinerContours(image, contour, 255,0,160)
    easyAI.afficherImage("Contours", image)

### Écrire sur l'image 
easyAI.dessinerTexte(image, "J'ai trouve {} formes !".format(len(contours)), 10,25, 255, 0, 170)
easyAI.afficherImage("Contours", image)
