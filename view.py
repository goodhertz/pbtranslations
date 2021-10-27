from util import * #INLINE

HEREDIR = Path(__FILE__).parent

c = "{:04d}".format(int(__inputs__[0])) # inputs
layout_dps = eval((HEREDIR / f"layouts/{c}_layout.py").read_text())
matches = list(HEREDIR.glob(f"**/{c}.py"))
src = run_path(matches[0])
ts = src["ts"]

@ui(rect=layout_dps.ambit()
, watch=GENERICS
, timeline=len(LANGS))
def plugin(u):
    lang = LANGS[u.i]
    dps = layout_dps
    labels = PS()

    for l in dps.fft("labels"):
        l.f(None)
        if l.tag() == "options":
            if l.data.get("string_count", 0) > 1 and not l.data.get("shows_all_strings"):
                l.s(hsl(0.05, s=1))
        if p := to_pen(u.ch, ts, l, lang):
            labels += p
    
    return dps.copy() + labels


def adjacent(direction):
    idx = RELEASES.index(c)
    adj = idx+direction
    __inputs__[0] = RELEASES[adj%len(RELEASES)]
    return Action.PreviewStoryboardReload