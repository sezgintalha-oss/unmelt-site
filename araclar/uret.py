#!/usr/bin/env python3
"""Yasal sayfaları uygulamadaki Markdown metinlerinden üretir (G113).

Kaynak: masal-terapi-app deposundaki app/lib/features/legal/veri/*.md
(uygulamanın kendi gösterdiği metin). Web sayfası bu metnin birebir HTML
karşılığıdır; metin elle değiştirilmez, önce uygulamadaki .md değişir.

Kullanım: python3 araclar/uret.py <md-klasoru>
Desteklenen Markdown: #, ##, ### başlık; "- " madde (2 boşluk girintili devam
satırı); boş satırla ayrılan paragraf; `kod`. Uygulamadaki basit_markdown.dart
ile aynı alt küme.
"""
import html
import pathlib
import re
import sys

KOK = pathlib.Path(__file__).resolve().parent.parent

SAYFALAR = [
    # (md dosyası, çıktı yolu, dil, öbür dilin yolu)
    ("gizlilik_en.md", "privacy/index.html", "en", "privacy/tr/index.html"),
    ("gizlilik_tr.md", "privacy/tr/index.html", "tr", "privacy/index.html"),
    ("kosullar_en.md", "terms/index.html", "en", "terms/tr/index.html"),
    ("kosullar_tr.md", "terms/tr/index.html", "tr", "terms/index.html"),
]

ETIKET = {
    "en": {
        "home": "Home", "privacy": "Privacy Policy", "terms": "Terms of Use",
        "delete": "Delete your account", "other": "Türkçe",
    },
    "tr": {
        "home": "Ana sayfa", "privacy": "Gizlilik Politikası",
        "terms": "Kullanım Koşulları", "delete": "Hesabını sil",
        "other": "English",
    },
}
YOL = {
    "en": {"home": "index.html", "privacy": "privacy/index.html",
           "terms": "terms/index.html", "delete": "delete-account/index.html"},
    "tr": {"home": "tr/index.html", "privacy": "privacy/tr/index.html",
           "terms": "terms/tr/index.html",
           "delete": "delete-account/tr/index.html"},
}


def satir_ici(metin: str) -> str:
    parcalar = re.split(r"(`[^`]+`)", metin)
    cikti = []
    for p in parcalar:
        if p.startswith("`") and p.endswith("`") and len(p) > 1:
            cikti.append("<code>" + html.escape(p[1:-1]) + "</code>")
        else:
            e = html.escape(p, quote=False)
            e = re.sub(
                r"\b([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,})\b",
                r'<a href="mailto:\1">\1</a>', e)
            cikti.append(e)
    return "".join(cikti)


def md_html(md: str) -> tuple[str, str]:
    """(başlık, gövde HTML) döndürür."""
    satirlar = md.splitlines()
    govde: list[str] = []
    baslik = ""
    paragraf: list[str] = []
    madde: list[str] | None = None
    liste: list[str] = []

    def paragrafi_bitir():
        nonlocal paragraf
        if paragraf:
            govde.append("<p>" + satir_ici(" ".join(paragraf)) + "</p>")
            paragraf = []

    def maddeyi_bitir():
        nonlocal madde
        if madde is not None:
            liste.append("<li>" + satir_ici(" ".join(madde)) + "</li>")
            madde = None

    def listeyi_bitir():
        nonlocal liste
        maddeyi_bitir()
        if liste:
            govde.append("<ul>\n" + "\n".join(liste) + "\n</ul>")
            liste = []

    for ham in satirlar:
        s = ham.rstrip()
        if not s.strip():
            paragrafi_bitir()
            listeyi_bitir()
            continue
        m = re.match(r"^(#{1,3}) (.*)$", s)
        if m:
            paragrafi_bitir()
            listeyi_bitir()
            seviye = len(m.group(1))
            if seviye == 1 and not baslik:
                baslik = m.group(2).strip()
            govde.append(f"<h{seviye}>{satir_ici(m.group(2).strip())}</h{seviye}>")
            continue
        if s.startswith("- "):
            paragrafi_bitir()
            maddeyi_bitir()
            madde = [s[2:].strip()]
            continue
        if madde is not None and ham.startswith("  "):
            madde.append(s.strip())
            continue
        listeyi_bitir()
        paragraf.append(s.strip())
    paragrafi_bitir()
    listeyi_bitir()
    return baslik, "\n".join(govde)


def goreli(cikti: str, hedef: str) -> str:
    derinlik = cikti.count("/")
    return "../" * derinlik + hedef


def sayfa(cikti: str, dil: str, baslik: str, govde: str, oteki: str) -> str:
    e = ETIKET[dil]
    y = YOL[dil]
    nav = " · ".join(
        f'<a href="{goreli(cikti, y[k])}">{e[k]}</a>'
        for k in ("home", "privacy", "terms", "delete"))
    return f"""<!doctype html>
<html lang="{dil}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Unmelt — {html.escape(baslik)}</title>
<link rel="stylesheet" href="{goreli(cikti, 'style.css')}">
<link rel="alternate" hreflang="{'tr' if dil == 'en' else 'en'}" href="{goreli(cikti, oteki)}">
</head>
<body>
<main>
<p class="dil"><a href="{goreli(cikti, oteki)}" hreflang="{'tr' if dil == 'en' else 'en'}">{e['other']}</a></p>
{govde}
</main>
<footer>
<nav>{nav}</nav>
<p>© 2026 Mamonta Dış Ticaret A.Ş.</p>
</footer>
</body>
</html>
"""


def main() -> None:
    kaynak = pathlib.Path(sys.argv[1])
    for md_ad, cikti, dil, oteki in SAYFALAR:
        baslik, govde = md_html((kaynak / md_ad).read_text(encoding="utf-8"))
        hedef = KOK / cikti
        hedef.parent.mkdir(parents=True, exist_ok=True)
        hedef.write_text(sayfa(cikti, dil, baslik, govde, oteki), encoding="utf-8")
        print("yazıldı:", cikti)


if __name__ == "__main__":
    main()
