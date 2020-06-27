from functools import wraps

LANGUAGE_SORT_ORDER = order = ["en", "es", "pt", "fr", "ja", "ko", "zhHans", "zhHant", "ar", "he"]

def translation(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        t = args[0]
        translation = args[1]
        if t.en == translation:
            t.warnings.append(["redundant", f.__name__])
        if translation == 0:
            t.warnings.append(["untranslated", f.__name__])
        if translation == 1:
            pass
        
        return f(t, translation)
    return wrapper

class T():
    def __init__(self, tag=None, context=None, text=None):
        self.tag = tag
        self.text = text
        self.context = context or None
        self.warnings = []
        self.en(text)
    
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
    def pt(self, translation):
        self._pt = translation
        return self
    
    @translation
    def ja(self, translation):
        self._ja = translation
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
        self.strings["_".join([item.tag, item.text, item.context or "None"])] = item

    def lookup(self, tag, text, context):
        return self.strings.get("_".join([tag, text, context or "None"]))