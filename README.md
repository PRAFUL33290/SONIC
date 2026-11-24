# SONIC

Jeu de cartes Sonic jouable dans le navigateur (fichier unique `index.html`).

## Structure

```
index.html        # jeu final généré (à ouvrir dans le navigateur)
src/game.html     # source du jeu (HTML/CSS/JS)
assets/
  source.png      # affiche source 1 (héros)
  source2.png     # affiche source 2 (pouvoirs suprêmes)
  cards/          # cartes découpées (une PNG par personnage)
  chars.json      # cartes encodées en base64 pour le jeu
  misc/           # visuels divers
tools/
  build_assets.py # découpe les affiches -> cards/ + chars.json
  build_html.py   # src/game.html + chars.json -> index.html
```

## Build

```
python tools/build_assets.py   # si les affiches changent
python tools/build_html.py     # régénère index.html
```
