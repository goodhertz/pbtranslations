from coldtype import *
from coldtype.tool import parse_inputs
from coldtype.renderer.reader import SourceReader
from functools import partial
from runpy import run_path

NOTO = __sibling__("Noto-unhinted")

def best_font_name(lang):
    if lang in ["en", "es", "pt", "fr", "it"]:
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

LANGUAGES = ["en", "es", "pt", "fr", "it", "ja", "ko", "zh-Hans", "zh-Hant", "ar"]

args = parse_inputs(__inputs__, dict(
    catalog=[None, str, "Must provide catalog"],
    language=["en", str]))

def __initials__():
    return dict(
        frame_offset=LANGUAGES.index(args["language"]))

# shim
shim = {"DATPenSet":P, "DATPen":P, "bw":bw, "P":P}
def add_data(self:P, data): return self.data(**data)
P.add_data = add_data

pens = eval(__VERSION__["layout"].read_text(), shim)
data = SourceReader(__VERSION__["config"])
ts = data.program["ts"]

for py in (__sibling__("translatables/configs").glob("**/*.py")):
    program = run_path(py)
    for k, s in program["ts"].strings.items():
        ts.append(s)

@animation(pens.ambit(), bg=1, tl=len(LANGUAGES), watch=[__VERSION__["config"]])
def scratch(f):
    lang = LANGUAGES[f.i]

    def label(fill, p:P):
        try:
            t = ts.lookup(*p.data("ts"))
            txt = t[lang]
            _lang = lang
        except TypeError:
            txt = p.data("us")
            _lang = "en"
            fill = hsl(0.9, 0.7)
        
        if not txt:
            return None
        
        x, y = p.data("align")
        return (StSt(txt, best_font(_lang), 30
            , fallback=Style(best_font("en"), 30)
            , multiline=1)
            .align(p.ambit(), Edge(x), Edge(y))
            .scaleToWidth(p.ambit().w, shrink_only=1)
            .scaleToHeight(p.ambit().h, shrink_only=1)
            .f(fill))
    
    return P(
        pens.copy(),
        StSt(lang, best_font("en"), 50).align(f.a.r.inset(5), "SW")
            .f(1)
            .layer(lambda p: P(p.ambit(tx=1, ty=1).inset(-10)).f(0), 1),
        P(map(partial(label, hsl(0.3))
            , pens.find("clump"))),
        P(map(partial(label, hsl(0.6))
            , pens.find("param"))),
        P(map(partial(label, hsl(0.07, 0.8, 0.6))
            , pens.find("value"))))