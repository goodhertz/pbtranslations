from pbt.translations import *


ts = TranslationSet()

ts.append(T(tag="Parameter/option",
    text="""
        D
        O
        T""")
    # Referring to note length; set vertically in a very tight spot
    .es("""
        P
        U
        N
        T
        O""")
    .pt("""
        P
        O
        N
        T
        O""")
    .fr("""
        P
        O
        I
        N
        T
        É""")
    .ja("""
        付
        点""")
    .ko(0)
    .zhHans(0)
    .zhHant(0)
    .ar('نقطة')
    .he(0)
)

ts.append(T(tag="Parameter/option",
    text='DOT')
    # Referring to note length
    .es('PUNTO')
    .pt('PONTO')
    .fr('POINTÉ')
    .ja('付点')
    .ko(0)
    .zhHans(0)
    .zhHant(0)
    .ar('نقطة')
    .he(0)
)

ts.append(T(tag="Parameter/option",
    text='Ext.')
    # Short for `External`
    .es(1)
    .pt(1)
    .fr(1)
    .ja('外部')
    .ko(0)
    .zhHans(0)
    .zhHant(0)
    .ar(1)
    .he(0)
)

ts.append(T(tag="Parameter/option",
    text='Int.')
    # Short for `Internal`
    .es(1)
    .pt(1)
    .fr(1)
    .ja('内部')
    .ko(0)
    .zhHans(0)
    .zhHant(0)
    .ar(1)
    .he(0)
)

ts.append(T(tag="Parameter/option",
    text="""
        N
        O
        T
        E""")
    # Referring to note length; set vertically in a very tight spot
    .es("""
        N
        O
        T
        A""")
    .pt("""
        N
        O
        T
        A""")
    .fr(1)
    .ja("""
        音
        符""")
    .ko(0)
    .zhHans(0)
    .zhHant(0)
    .ar('النوتة')
    .he(0)
)

ts.append(T(tag="Parameter/option",
    text='NOTE')
    # Referring to note length
    .es('NOTA')
    .pt('NOTA')
    .fr(1)
    .ja('音符')
    .ko(0)
    .zhHans(0)
    .zhHant(0)
    .ar('النوتة')
    .he(0)
)

ts.append(T(tag="Parameter/option",
    text='Off')
    # Default for booleans
    .es(1)
    .pt('Des.')
    .fr(1)
    .ja('オフ')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar(1)
    .he('אוף')
)

ts.append(T(tag="Parameter/option",
    text='On')
    # Default for booleans
    .es(1)
    .pt('Lig.')
    .fr(1)
    .ja('オン')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar(1)
    .he('און')
)

ts.append(T(tag="Parameter/option",
    text="""
        T
        I
        M
        E""")
    # Referring to note length; set vertically in a very tight spot
    .es("""
        T
        I
        E
        M
        P
        O""")
    .pt("""
        T
        E
        M
        P
        O""")
    .fr("""
        T
        E
        M
        P
        S""")
    .ja("""
        時
        間""")
    .ko(0)
    .zhHans(0)
    .zhHant(0)
    .ar('الوقت')
    .he(0)
)

ts.append(T(tag="Parameter/option",
    text="""
        T
        R
        I
        P""")
    # Referring to note length; set vertically in a very tight spot
    .es("""
        T
        R
        S
        I
        L
        L
        O""")
    .pt("""
        T
        E
        R
        C
        I
        N
        A""")
    .fr("""
        T
        R
        I
        O
        L
        E
        T""")
    .ja("""
        三
        連
        符""")
    .ko(0)
    .zhHans(0)
    .zhHant(0)
    .ar('المسيرة')
    .he(0)
)

ts.append(T(tag="Parameter/option",
    text='TIME')
    # Referring to note length
    .es('TIEMPO')
    .pt('TEMPO')
    .fr('TEMPS')
    .ja('時間')
    .ko(0)
    .zhHans(0)
    .zhHant(0)
    .ar('الوقت')
    .he(0)
)

ts.append(T(tag="Parameter/option",
    text='TRIP')
    # Referring to note length
    .es('TRSILLO')
    .pt('TERCINA')
    .fr('TRIOLET')
    .ja('三連符')
    .ko(0)
    .zhHans(0)
    .zhHant(0)
    .ar('المسيرة')
    .he(0)
)

