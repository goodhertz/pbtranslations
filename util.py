from coldtype import *

HEREDIR = Path(__FILE__).parent
LANGS = ["en", "es", "pt", "fr", "ja", "ko", "zh-Hans", "zh-Hant", "ar"]
RELEASES = []
NAMES = {}
PATHS = {}

GENERICS = []

for py in (HEREDIR / "translatables/configs").glob("**/*.py"):
    GENERICS.append(py)

lookup = HEREDIR / "LOOKUP.md"
for idx, l in enumerate(lookup.read_text().split("\n")):
    l = l.strip("- ")
    if idx % 3 == 0:
        RELEASES.append(l)
    elif idx % 3 == 1:
        NAMES[RELEASES[-1]] = l
    elif l:
        PATHS[RELEASES[-1]] = l

def best_font_name(lang):
    if lang in ["en", "es", "pt", "fr"]:
        return "NotoSans-Bold.ttf"
    elif lang in ["ja"]:
        return "NotoSansCJKjp-Bold.otf"
    elif lang in ["ko"]:
        return "NotoSansCJKkr-Bold.otf"
    elif lang in ["zh-Hans"]:
        return "NotoSansCJKsc-Bold.otf"
    elif lang in ["zh-Hant"]:
        return "NotoSansCJKtc-Bold.otf"
    elif lang in ["he"]:
        return "NotoSansHebrew-Bold.ttf"
    elif lang in ["ar"]:
        return "NotoSansArabic-Bold.ttf"
    else:
        return "NotoSerifDisplay-Italic.ttf"

def best_font(lang):
    return Font.Cacheable(NOTO / best_font_name(lang))

def to_pen(mh, ts, l, lang, f=None):
    initial = l.data.get("initialValue")
    if initial is not None:
        if l.data.get("shows_all_strings"):
            return DATPens([to_pen(mh, ts, p, lang, f=hsl(0.75, 1, 0.4)) for p in l._pens])
        else:
            v = int(initial)
            # for m in (mh or []):
            #     if m[-1].inside(l.bounds()):
            #         v += 1
            #         v = v % len(l._pens)
            p = to_pen(mh, ts, l._pens[v], lang, f=hsl(0.75, 1, 0.4))
            return p
    
    tag = l.tag()
    align = [Edge(e) for e in l.data["align"]]

    if not f:
        if tag == "clump":
            f = hsl(0.5, s=1, l=0.3)
        else:
            f = hsl(0.6, s=1, l=0.4)

    u = l.data.get("us")
    actual_lang = lang

    if u:
        txt = u
        actual_lang = "en"
    else:
        t = ts.lookup(*l.data.get("ts"))
        if t:
            txt = t[lang]
        else:
            print("!", l.data.get("ts"))
            return None
    
    b = l.bounds()
    slugs = []
    for line in txt.split("\n"):
        slugs.append(Slug(line,
            Style(best_font(actual_lang), 32),
            Style(best_font("en"), 32)))
    
    return (Graf(slugs, b.inset(5))
        .pens()
        .xa()
        .scaleToWidth(b.inset(5).w, shrink_only=1)
        .scaleToHeight(b.inset(5).h, shrink_only=1)
        #.align(b, y="mny" if tag == "param" else "mdy")
        .align(b, *align)
        .f(hsl(0.9, s=1) if u else f))