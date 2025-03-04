from functools import wraps
from textwrap import dedent

LANGUAGE_SORT_ORDER = order = ["en", "es", "pt", "fr", "it", "ja", "ko", "zhHans", "zhHant", "ar", "he"]

def strip_whitespace(s):
    if isinstance(s, str):
        return dedent("\n".join([l.strip() for l in s.strip().split("\n")])).strip()
    else:
        return s

def translation(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        t = args[0]
        translation = strip_whitespace(args[1])
        if t.en == translation:
            t.warnings.append(["redundant", f.__name__])
        if translation == 0:
            t.warnings.append(["untranslated", f.__name__])
        if translation == 1:
            pass
        
        return f(t, translation, **kwds)
    return wrapper


class T():
    def __init__(self, tag=None, context=None, text=None):
        self.tag = tag
        self.text = strip_whitespace(text)
        self.context = context or None
        self.warnings = []
        
        # special formatting flags
        self._ja_vertical = False
        
        self.en(self.text)
    
    def __repr__(self):
        t = f"<T({self.tag})—{self.text}"
        #t += "".join(["("+str(getattr(self, lang))+")" for lang in LANGUAGE_SORT_ORDER[1:]])
        t += ">"
        return t
    
    def __getitem__(self, lang):
        l = "_" + lang.replace("-", "")
        if hasattr(self, l):
            res = getattr(self, l)
            if res == 0 or res == 1:
                return self._en
            else:
                return res
        else:
            return self._en
    
    def get_raw_value(self, lang):
        l = "_" + lang.replace("-", "")
        if hasattr(self, l):
            return getattr(self, l)
        else:
            return -1

    def en(self, translation):
        self._en = translation
        return self
    
    @translation
    def es(self, translation):
        self._es = translation
        return self
    
    @translation
    def fr(self, translation):
        self._fr = translation
        return self

    @translation
    def it(self, translation):
        self._it = translation
        return self
    
    @translation
    def pt(self, translation):
        self._pt = translation
        return self
    
    @translation
    def ja(self, translation, vertical=False):
        self._ja = translation
        self._ja_vertical = vertical
        return self
    
    @translation
    def ko(self, translation):
        self._ko = translation
        return self
    
    @translation
    def zhHans(self, translation):
        self._zhHans = translation
        return self
    
    @translation
    def zhHant(self, translation):
        self._zhHant = translation
        return self
    
    @translation
    def ar(self, translation):
        self._ar = translation
        return self
    
    @translation
    def he(self, translation):
        self._he = translation
        return self
    

class TranslationSet():
    def __init__(self):
        self.strings = {}

    def append(self, item):
        self.strings["_".join([item.tag, dedent(item.text).strip(), item.context or "None"])] = item

    def lookup(self, tag, text, context):
        return self.strings.get("_".join([tag, dedent(text).strip(), context or "None"]))