"""Build index.html from src/template.html.

Replaces {{LOGO}} and {{FAV}} with inline base64 images and turns
{{wa:message}} into WhatsApp links with a pre-written message.
Run:  python3 build.py
"""
import base64, re, urllib.parse
from pathlib import Path

ROOT = Path(__file__).parent
WA = "https://wa.me/8801346074720?text="

def b64(path):
    return base64.b64encode((ROOT / path).read_bytes()).decode()

t = (ROOT / "src/template.html").read_text(encoding="utf-8")
t = t.replace("{{LOGO}}", b64("src/assets/anchorstack-logo-on-dark.png"))
t = t.replace("{{FAV}}", b64("src/assets/favicon.png"))
t = re.sub(r"\{\{wa:(.*?)\}\}", lambda m: WA + urllib.parse.quote(m.group(1)), t)
assert "{{" not in t, "unreplaced placeholder left in template"
(ROOT / "index.html").write_text(t, encoding="utf-8")
print("index.html built")
