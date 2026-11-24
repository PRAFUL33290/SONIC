"""Assemble src/game.html + assets/chars.json -> index.html (fichier unique, jouable hors-ligne sauf la police)."""
import pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent
body = (ROOT / "src/game.html").read_text()
data = (ROOT / "assets/chars.json").read_text()
body = body.replace("/*CHARS*/[]", data)
head = ('<!doctype html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no, viewport-fit=cover">\n'
        '<meta name="apple-mobile-web-app-capable" content="yes">\n')
(ROOT / "index.html").write_text(head + body.replace("<style>", "<style>\n:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px);box-sizing:border-box}", 1) + "\n</html>\n")
if len(sys.argv) > 1:
    pathlib.Path(sys.argv[1]).write_text(body)
print("ok")
