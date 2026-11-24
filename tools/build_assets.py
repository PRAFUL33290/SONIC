"""Découpe les 20 cartes de l'affiche et génère assets/chars.json (images en base64)."""
import base64, io, json, pathlib
from PIL import Image, ImageDraw

ROOT = pathlib.Path(__file__).resolve().parent.parent
src = Image.open(ROOT / "assets/source.png").convert("RGB")
cols = [(25, 259), (274, 506), (519, 751), (765, 997)]
rows = [(174, 430), (443, 703), (710, 965), (972, 1220), (1230, 1513)]
chars = [
    ("sonic", "SONIC", "Le hérisson bleu", "#1d5fe0"),
    ("tails", "TAILS", "Le renard", "#f59a1b"),
    ("knuckles", "KNUCKLES", "L'échidné", "#d8232a"),
    ("amy", "AMY ROSE", "La hérissonne rose", "#ff5fa8"),
    ("shadow", "SHADOW", "Le hérisson noir", "#26232b"),
    ("rouge", "ROUGE", "La chauve-souris", "#8a3fd1"),
    ("eggman", "DR. EGGMAN", "Le savant fou", "#c8102e"),
    ("silver", "SILVER", "Le hérisson d'argent", "#20a8b8"),
    ("cream", "CREAM", "La lapine", "#ff8a3d"),
    ("blaze", "BLAZE", "Le chat", "#9b59d6"),
    ("vector", "VECTOR", "Le crocodile", "#2fa83a"),
    ("espio", "ESPIO", "Le caméléon", "#b62fb0"),
    ("charmy", "CHARMY", "L'abeille", "#f3c316"),
    ("mighty", "MIGHTY", "Le tatou", "#e0322e"),
    ("ray", "RAY", "L'écureuil", "#f0b400"),
    ("metal", "METAL SONIC", "Le robot", "#1a3f9e"),
    ("big", "BIG", "Le gros chat", "#6a4fd6"),
    ("omega", "OMEGA", "Robot de combat", "#b5121b"),
    ("zavok", "ZAVOK", "Chef Zeti", "#7d1530"),
    ("chaos", "CHAOS", "Dieu de l'eau", "#18a0e8"),
]

def b64(img, q):
    buf = io.BytesIO(); img.save(buf, "JPEG", quality=q, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()

out = []
(ROOT / "assets/cards").mkdir(exist_ok=True)
for k, (cid, name, sub, color) in enumerate(chars):
    x0, x1 = cols[k % 4]; y0, y1 = rows[k // 4]
    card = src.crop((x0, y0, x1, y1))
    card.save(ROOT / f"assets/cards/{cid}.png")
    w, h = card.size
    s = w - 32
    face = card.crop((16, 4, 16 + s, 4 + s)).resize((168, 168), Image.LANCZOS)
    out.append({"id": cid, "name": name, "sub": sub, "color": color,
                "face": b64(face, 84), "card": b64(card, 88)})
(ROOT / "assets/chars.json").write_text(json.dumps(out, ensure_ascii=False))
print("ok", len(out))
