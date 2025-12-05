#Libréries
import tkinter as tk
import turtle

#Définition des fonctions
def Afficher_prevention_mode_beta():
    t.clear()
    t.penup()
    t.home()
    t.pendown()
    t.write("Cette version de Quest est une version Beta cela signifie que cette version est temporaire et peut avoire des bug", align="center", font=("Berlin Sans FB Demi", 8, "bold"))

def Connexion_en_cours():
    t.clear()
    t.penup()
    t.home()
    t.pendown()
    t.write("Connexion en cours...", align="center", font=("Arial", 10, "bold"))

#Config fenetre
root = tk.Tk()
root.title("Quest")

# Canvas Turtle intégré dans Tkinter
canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

screen = turtle.TurtleScreen(canvas)
screen.bgcolor("white")
t = turtle.RawTurtle(screen)
t.hideturtle()

# Zone de boutons (n'occupe plus toute la hauteur et fond assorti)
controls = tk.Frame(root, bg="white")
controls.pack(side=tk.RIGHT, anchor='n', padx=10, pady=10)  # pas fill=tk.Y pour éviter la zone grise

# Texte "Login"
lbl_merci = tk.Label(controls, text="Quest BETA", bg="white", font=("Berlin Sans FB Demi", 12))
lbl_merci.pack(pady=(0,8))

#créé le bouton se connecter
btn_se_connecter = tk.Button(controls, text="Tester en BETA", command=Connexion_en_cours, width=12, height=2)
btn_se_connecter.pack(pady=5)

# Frame intermédiaire centré verticalement/horizontalement
middle = tk.Frame(controls, bg="white")
middle.pack(expand=True)  # prend l'espace vertical disponible et centre son contenu

#Afficher l'apprevention du mode BETA
Afficher_prevention_mode_beta()

#Config fenetre
root.mainloop()