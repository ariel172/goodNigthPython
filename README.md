# Animation Ciel Nocturne avec Turtle

Ce script Python utilise le module `turtle` pour générer une animation simple et agréable d'un ciel nocturne. Il affiche une scène comprenant un croissant de lune, des étoiles qui apparaissent progressivement et scintillent en changeant de couleur, ainsi qu'un message personnalisable.

## Fonctionnalités

Le script présente plusieurs caractéristiques notables pour créer une expérience visuelle dynamique. Un croissant de lune est dessiné de manière distincte, ajoutant un détail réaliste à la scène. Des étoiles apparaissent ensuite une par une à des emplacements aléatoires, en prenant soin d'éviter les zones occupées par la lune et le message affiché en bas de l'écran. L'effet le plus dynamique est le scintillement des étoiles : une fois apparues, elles changent de couleur de manière cyclique, créant une impression de clignotement. L'animation est conçue pour être fluide et non bloquante grâce à l'utilisation de la fonction `screen.ontimer` du module `turtle`, ce qui assure que la fenêtre graphique reste réactive pendant l'exécution. De plus, le script offre une flexibilité appréciable via des constantes définies au début du code. Ces constantes permettent de personnaliser facilement divers aspects de l'animation, tels que les dimensions de la fenêtre, les couleurs utilisées pour les éléments, le nombre total d'étoiles, la vitesse d'apparition et de scintillement, ainsi que le message affiché.

## Prérequis

Pour exécuter ce script, vous avez besoin d'une installation de Python 3 sur votre système. Le module `turtle`, qui est essentiel pour les graphiques, fait partie de la bibliothèque standard de Python. Par conséquent, aucune installation de dépendance supplémentaire n'est généralement nécessaire.

## Utilisation

L'exécution du script est simple. Enregistrez d'abord le code dans un fichier avec une extension `.py`, par exemple `ciel_nocturne.py`. Ensuite, ouvrez un terminal ou une invite de commande, naviguez jusqu'au répertoire où vous avez enregistré le fichier, et lancez le script en utilisant la commande `python ciel_nocturne.py` ou `python3 ciel_nocturne.py`, selon votre configuration Python. Une fenêtre graphique s'ouvrira, affichant d'abord la lune, puis le message, et enfin les étoiles commenceront à apparaître et à scintiller. Pour arrêter l'animation, il suffit de fermer la fenêtre graphique Turtle. Le script est conçu pour se terminer proprement lorsque la fenêtre est fermée par l'utilisateur.

## Personnalisation

Si vous souhaitez modifier l'apparence ou le comportement de l'animation, vous pouvez ajuster les valeurs des constantes définies au début du fichier `twinkling_script.py` (ou le nom que vous lui avez donné). Vous pouvez changer le `MESSAGE`, modifier la palette de `COLORS`, ajuster le `NUM_STARS`, ou encore régler les délais `STAR_APPEAR_DELAY_MS` et `TWINKLE_DELAY_MS` pour contrôler la vitesse de l'animation selon vos préférences.
