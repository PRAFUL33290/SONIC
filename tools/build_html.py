"""Assemble src/game.html + assets/chars.json + assets/music.mp3 -> index.html (fichier unique, jouable hors-ligne sauf la police)."""
import base64, json, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent
body = (ROOT / "src/game.html").read_text()
data = (ROOT / "assets/chars.json").read_text()
body = body.replace("/*CHARS*/[]", data)
music_path = ROOT / "assets/music.mp3"
music_uri = ("data:audio/mpeg;base64," + base64.b64encode(music_path.read_bytes()).decode("ascii")) if music_path.exists() else ""
body = body.replace('/*MUSIC*/""', json.dumps(music_uri))
head = ('<!doctype html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no, viewport-fit=cover">\n'
        '<meta name="apple-mobile-web-app-capable" content="yes">\n')
(ROOT / "index.html").write_text(head + body.replace("<style>", "<style>\n:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px);box-sizing:border-box}", 1) + "\n</html>\n")
if len(sys.argv) > 1:
    pathlib.Path(sys.argv[1]).write_text(body)
print("ok")
