from coldtype import *
from runpy import run_path

HEREDIR = Path(__FILE__).parent
NOTO = HEREDIR / "Noto-unhinted"

LANGS = ["en", "es", "pt", "fr", "ja", "ko", "zh-Hans", "zh-Hant", "ar"]
RELEASES = []
NAMES = {}
PATHS = {}

GENERICS = []
GENERICS_TS = {}

for py in (HEREDIR / "translatables/configs").glob("**/*.py"):
    GENERICS.append(py)
    GENERICS_TS[py.stem] = run_path(py)["ts"]

lookup = HEREDIR / "LOOKUP.md"
for idx, l in enumerate(lookup.read_text().split("\n")):
    l = l.strip("- ")
    if idx % 3 == 0:
        if not l: continue
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

def to_pen(ch, ts, l, lang, f=None):
    initial = l.data.get("initialValue")
    if initial is not None:
        if l.data.get("shows_all_strings"):
            return DATPens([to_pen(ch, ts, p, lang, f=hsl(0.75, 1, 0.4)) for p in l._pens])
        else:
            v = int(initial)
            hits = sum([int(c.inside(l.bounds())) for c in ch])
            v = (v + hits)%(len(l._pens))
            p = to_pen(ch, ts, l._pens[v], lang, f=hsl(0.75, 1, 0.4))
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
            found = False
            for _, v in GENERICS_TS.items():
                res = v.lookup(*l.data.get("ts"))
                if res:
                    txt = res[lang]
                    found = True
            if not found:
                print("!", l.data.get("ts"))
                return None
    
    b = l.bounds()

    #print(txt, l.data.get("ts"))
    
    out = (StSt(txt, best_font(actual_lang),
        font_size=28,
        fallback=Style(best_font("en"), 28),
        multiline=True)
        .xalign(b)
        .scaleToWidth(b.inset(5).w, shrink_only=1)
        .scaleToHeight(b.inset(5).h, shrink_only=1)
        .align(b, *align)
        .f(hsl(0.9, s=1) if u else f))
    
    return out