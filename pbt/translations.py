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
    def __init__(self, tag, context, text):
        self.tag = tag
        self.text = text
        self.context = context or None
        self.warnings = []
    
    def __repr__(self):
        t = f"<T({self.tag})—{self.text}"
        t += "".join(["("+str(getattr(self, lang))+")" for lang in LANGUAGE_SORT_ORDER[1:]])
        t += ">"
        return t

    def en(self, translation):
        self.en = translation
        return self
    
    @translation
    def es(self, translation):
        self.es = translation
        return self
    
    @translation
    def fr(self, translation):
        self.fr = translation
        return self
    
    @translation
    def pt(self, translation):
        self.pt = translation
        return self
    
    @translation
    def ja(self, translation):
        self.ja = translation
        return self
    
    @translation
    def ko(self, translation):
        self.ko = translation
        return self
    
    @translation
    def zhHans(self, translation):
        self.zhHans = translation
        return self
    
    @translation
    def zhHant(self, translation):
        self.zhHant = translation
        return self
    
    @translation
    def ar(self, translation):
        self.ar = translation
        return self
    
    @translation
    def he(self, translation):
        self.he = translation
        return self
    

class TranslationSet(list):
    pass