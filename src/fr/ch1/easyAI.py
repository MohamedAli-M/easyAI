import cv2 
import imutils 
import numpy
import matplotlib


class easyAI: 
    def lireImage(chemin):
        return cv2.imread(chemin)
    
    def afficherImage(nomImage, image):
        cv2.imshow(nomImage, image)
        cv2.waitKey(0)
    
    def lirePixelRGB(image, x, y):
        (B,G,R) = image[y,x]
        print("R={},G={},B={}".format(R,G,B))

    def convertirGris(image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    def seuillerImage(image, val_inf, val_sup):
        return cv2.threshold(image, val_inf, val_sup, cv2.THRESH_BINARY_INV)[1]

    def trouverContours(image):
        contours = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        return imutils.grab_contours(contours)

    def dessinerContours(image, contour, r,g,b):
        cv2.drawContours(image, [contour], -1, (r,g,b), 3)

    def dessinerTexte(image, texte, posX, posY, r,g,b):
        cv2.putText(image, texte, (posX, posY),  cv2.FONT_HERSHEY_SIMPLEX, 0.7, (r, g, b), 2)


# ### Récupérer une partie de l'image qui nous intéresse 
# # En affichant l'image, on voit que la région s'étant de 193:233 à 279:106
# cv2.rectangle(copy, (183, 233), (279, 106), (0, 0, 255), 2)
# cv2.imshow("Rectangle", copy)
# cv2.waitKey(0)

# ### Détecter les bords
# formes = cv2.imread("../lib/shapes.jpg")
# formes_gris = cv2.cvtColor(formes, cv2.COLOR_BGR2GRAY)
# edges = cv2.Canny(formes_gris, 30, 150)
# cv2.imshow("Edges", edges)
# cv2.waitKey(0)

