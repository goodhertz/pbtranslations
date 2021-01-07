#!/usr/bin/env python

from coldtype import *
from coldtype.renderer import Renderer
from runpy import run_path
import pbt
import glfw

HEREDIR = Path(__file__).parent
NOTO = HEREDIR / "Noto-unhinted"

LANGS = ["en", "es", "pt", "fr", "ja", "ko", "zh-Hans", "zh-Hant", "ar", "he"]

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
            return DATPens([to_pen(mh, ts, p, lang, f=hsl(0.75, 1, 0.4)) for p in l.pens])
        else:
            v = int(initial)
            for m in (mh or []):
                if m[-1].inside(l.bounds()):
                    v += 1
                    v = v % len(l.pens)
            p = to_pen(mh, ts, l.pens[v], lang, f=hsl(0.75, 1, 0.4))
            return p
    
    tag = l.getTag()
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

def preview_renderable(dps, ts, lang):
    r = dps.bounds()

    @renderable(r, rstate=1, watch=GENERICS)
    def previewer(r, rs):
        out = DATPens([dps])
        labels = DATPens()

        for l in dps.fft("labels"):
            l.f(None)
            if l.getTag() == "options":
                if l.data.get("string_count", 0) > 1 and not l.data.get("shows_all_strings"):
                    l.s(hsl(0.05, s=1))
            if p := to_pen(rs.mouse_history, ts, l, lang):
                labels += p
        
        return out + labels
    
    return previewer

def cycle(arr, idx):
    if idx < 0:
        return len(arr) - 1
    elif idx >= len(arr):
        return 0
    else:
        return idx

class TranslationPreview(Renderer):
    def before_start(self):
        self.lang = self.args.lang
        self.catalog = None
        self.ts = None
        return not self.switch_to_catalog(self.args.catalog)
        
    def switch_to_catalog(self, catalog):
        """True if found"""
        c = "{:04d}".format(int(catalog))
        matches = list(HEREDIR.glob(f"**/{c}.py"))

        if len(matches) == 0:
            print(f"Could not find a translation file matching catalog >>> {c}")
            return False
        else:
            self.layout_dps = eval((HEREDIR / f"layouts/{c}_layout.py").read_text())
            self.reset_filepath(str(matches[0]))
            self.catalog = c
            return True

    def reload(self, trigger):
        result = super().reload(trigger)
        self.ts = self.program["ts"]

        for py in (HEREDIR / "translatables/configs").glob("**/*.py"):
            program = run_path(py)
            for k, s in program["ts"].strings.items():
                self.ts.append(s)

        return result

    def render(self, trigger, indices=[]):
        self.set_title(NAMES[self.catalog] + " / " + self.lang)
        return super().render(trigger, indices=indices)

    def renderables(self, trigger):
        return [preview_renderable(self.layout_dps, self.ts, self.lang)]
    
    def allow_mouse(self):
        return True
    
    def on_key(self, win, key, scan, action, mods):
        if action == glfw.PRESS:
            cidx = RELEASES.index(self.catalog)
            if key in [glfw.KEY_UP, glfw.KEY_DOWN]:
                if key == glfw.KEY_DOWN:
                    cidx -= 1
                else:
                    cidx += 1
                self.switch_to_catalog(RELEASES[cycle(RELEASES, cidx)])
                self.action_waiting = Action.PreviewStoryboardReload
                return
            elif key in [glfw.KEY_LEFT, glfw.KEY_RIGHT]:
                lidx = LANGS.index(self.lang)
                if key == glfw.KEY_LEFT:
                    lidx -= 1
                else:
                    lidx += 1
                self.lang = LANGS[cycle(LANGS, lidx)]
                self.action_waiting = Action.PreviewStoryboardReload

        return super().on_key(win, key, scan, action, mods)
    
    def on_stdin(self, stdin):
        if stdin in LANGS:
            self.lang = stdin
            self.on_action(Action.PreviewStoryboard)
        else:
            try:
                if self.switch_to_catalog(stdin):
                    self.reload_and_render(Action.Resave)
            except ValueError:
                print("Invalid catalog")


def main():
    pargs, parser = Renderer.Argparser(
        name="translation-preview",
        file=False,
        nargs=[
            ["lang", "en"],
            ["catalog", "0001"]])
    TranslationPreview(parser).main()

if __name__ == "__main__":
    main()