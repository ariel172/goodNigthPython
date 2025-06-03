# -*- coding: utf-8 -*-
"""
Script Python utilisant le module Turtle pour afficher une scène nocturne
avec une lune, des étoiles clignotantes et un message.

Ce script amélioré inclut :
- Une meilleure structuration du code (fonctions, constantes).
- L'utilisation de `screen.ontimer` pour une animation non bloquante.
- Des commentaires et docstrings pour une meilleure lisibilité.
- Une gestion plus propre des objets Turtle (un par étoile).
- Une lune en forme de croissant.
- Des étoiles qui apparaissent plus vite et clignotent en changeant de couleur.
"""

import turtle
import random

# --- Constantes --- #
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = "black"
COLORS = ["#FFD700", "#ADD8E6", "#FFA07A", "#98FB98", "#F0E68C", "#DDA0DD", "#FFB6C1", "#87CEFA"] # Couleurs pastel étendues

MOON_RADIUS = 50
MOON_COLOR = "lightyellow"
MOON_POSITION = (0, 150)

STAR_SIZE = 15
NUM_STARS = 20 # Augmenté le nombre d'étoiles
STAR_APPEAR_DELAY_MS = 150  # Délai réduit pour une apparition plus rapide
TWINKLE_DELAY_MS = 300     # Délai pour le clignotement

TEXT_COLOR = "white"
TEXT_POSITION = (0, -250)
TEXT_FONT = ("Arial", 20, "normal")
MESSAGE = "Bonne Nuit !"
INITIAL_DELAY_S = 0.5 # Délai initial réduit

# --- Configuration de l'écran --- #
screen = turtle.Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(BACKGROUND_COLOR)
screen.tracer(0)  # Désactiver les mises à jour automatiques

# --- Variables globales --- #
stars_drawn = 0
active_stars = [] # Liste pour stocker les infos des étoiles (turtle, pos, size)
moon_turtle = None
text_turtle = None
twinkle_active = False # Pour s'assurer que twinkle_stars n'est lancé qu'une fois

# --- Fonctions --- #
def create_turtle(shape="classic", speed=0, visible=False):
    """Crée et configure un nouvel objet Turtle."""
    t = turtle.Turtle()
    t.hideturtle()
    t.shape(shape)
    t.speed(speed)
    t.penup()
    if visible:
        t.showturtle()
    return t

def draw_crescent_moon(t, pos, radius, color):
    """Dessine un croissant de lune."""
    x, y = pos
    t.color(color)
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

    t.penup()
    offset = radius * 0.3
    t.goto(x + offset, y - radius + offset*1.5)
    t.color(BACKGROUND_COLOR)
    t.pendown()
    t.begin_fill()
    t.circle(radius * 0.9)
    t.end_fill()
    t.penup()

def draw_star(t, pos, size, color):
    """Dessine une étoile à 5 branches avec une tortue donnée."""
    x, y = pos
    t.clear() # Efface le dessin précédent de cette tortue
    t.penup()
    t.goto(x, y)
    t.color(color)
    t.pendown()
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()
    t.penup()

def display_message(t, message, pos, color, font):
    """Affiche un message texte."""
    x, y = pos
    t.goto(x, y)
    t.color(color)
    t.write(message, align="center", font=font)

def get_random_star_position():
    """Génère une position aléatoire pour une étoile, en évitant la lune et le texte."""
    max_x = SCREEN_WIDTH // 2 - STAR_SIZE
    max_y = SCREEN_HEIGHT // 2 - STAR_SIZE
    min_y_avoid = TEXT_POSITION[1] - TEXT_FONT[1] * 2 # Zone élargie à éviter près du texte
    moon_x, moon_y = MOON_POSITION
    avoid_radius_sq = (MOON_RADIUS * 1.7)**2 # Zone élargie à éviter autour de la lune

    while True:
        star_x = random.randint(-max_x, max_x)
        star_y = random.randint(-max_y, max_y)

        # Vérifier la proximité du texte
        is_near_text = (TEXT_POSITION[0] - 50 < star_x < TEXT_POSITION[0] + 50) and \
                       (min_y_avoid - 50 < star_y < min_y_avoid + 70)

        # Vérifier la proximité de la lune
        dist_sq = (star_x - moon_x)**2 + (star_y - moon_y)**2
        is_near_moon = dist_sq < avoid_radius_sq

        if not is_near_text and not is_near_moon:
            return (star_x, star_y)

def add_star():
    """Ajoute une nouvelle étoile clignotante à l'écran."""
    global stars_drawn, twinkle_active
    if stars_drawn < NUM_STARS:
        star_pos = get_random_star_position()
        star_color = random.choice(COLORS)

        # Créer une tortue dédiée pour cette étoile
        new_star_turtle = create_turtle()
        draw_star(new_star_turtle, star_pos, STAR_SIZE, star_color)

        # Stocker les informations de l'étoile
        active_stars.append({"turtle": new_star_turtle, "pos": star_pos, "size": STAR_SIZE})

        screen.update() # Mettre à jour l'écran pour afficher la nouvelle étoile
        stars_drawn += 1

        # Planifier l'ajout de la prochaine étoile
        screen.ontimer(add_star, STAR_APPEAR_DELAY_MS)

        # Démarrer le clignotement si ce n'est pas déjà fait et qu'il y a des étoiles
        if not twinkle_active and active_stars:
            twinkle_active = True
            twinkle_stars()
    else:
        print(f"{NUM_STARS} étoiles ont été ajoutées.")

def twinkle_stars():
    """Fait clignoter toutes les étoiles actives en changeant leur couleur."""
    if not active_stars: # S'arrêter s'il n'y a plus d'étoiles (au cas où)
        return

    for star_info in active_stars:
        new_color = random.choice(COLORS)
        draw_star(star_info["turtle"], star_info["pos"], star_info["size"], new_color)

    screen.update() # Mettre à jour l'écran pour montrer les nouvelles couleurs

    # Planifier le prochain clignotement
    screen.ontimer(twinkle_stars, TWINKLE_DELAY_MS)

def show_message_and_start_stars():
    """Affiche le message puis commence à ajouter les étoiles."""
    global text_turtle
    text_turtle = create_turtle()
    display_message(text_turtle, MESSAGE, TEXT_POSITION, TEXT_COLOR, TEXT_FONT)
    screen.update()
    # Commencer à ajouter les étoiles
    screen.ontimer(add_star, STAR_APPEAR_DELAY_MS)

def main():
    """Fonction principale du script."""
    global moon_turtle
    try:
        # Créer les tortues principales
        moon_turtle = create_turtle()

        # Dessiner la lune
        draw_crescent_moon(moon_turtle, MOON_POSITION, MOON_RADIUS, MOON_COLOR)
        screen.update() # Afficher la lune

        # Planifier l'affichage du message et le début de l'ajout des étoiles
        screen.ontimer(show_message_and_start_stars, int(INITIAL_DELAY_S * 1000))

        print("Configuration terminée. Lancement de l'animation...")
        screen.mainloop() # Démarrer la boucle d'événements Turtle

    except turtle.Terminator:
        print("Fenêtre Turtle fermée par l'utilisateur.")
    except Exception as e:
        print(f"Une erreur inattendue est survenue : {e}")
        # Essayer de nettoyer en cas d'erreur
        try:
            screen.bye()
        except: # Ignorer les erreurs lors de la fermeture
            pass

if __name__ == "__main__":
    main()