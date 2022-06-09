from pbt.translations import *


ts = TranslationSet()

ts.append(T(tag="ClumpLabel/text",
    text='ADV FILTER')
    .es('FILTRO EXT')
    .pt('FILTRO +')
    .fr('FILTRE EXT')
    .ja('フィルター微調整')
    .ko('세부 필터')
    .zhHans('高級濾波調節')
    .zhHant('進階濾波調節')
    .ar('فلتر مُفصَّل')
    .he('פילטר ועוד')
)

ts.append(T(tag="ClumpLabel/text",
    text='FILTER')
    .es('FILTRO')
    .pt('FILTRO')
    .fr('FILTRE')
    .ja('フィルター')
    .ko('필터')
    .zhHans('滤波')
    .zhHant('濾波')
    .ar('الفلتر')
    .he('פילטר')
)

ts.append(T(tag="ClumpLabel/text",
    text="""
        G
        A
        I
        N""")
    # Set vertically
    .es("""
        GA
        NAN
        CIA""")
    .pt("""
        GA
        NH
        O""")
    .fr(1)
    .ja("""
        ゲ
        イ
        ン""")
    .ko("""
        게
        인""")
    .zhHans("""
        增
        益""")
    .zhHant("""
        增
        益""")
    .ar('الربح')
    .he('גיין')
)

ts.append(T(tag="ClumpLabel/text",
    text='HIGH')
    .es('ALTOS')
    .pt('AGUDO')
    .fr('AIGUS')
    .ja('高域')
    .ko('고역대')
    .zhHans('高频')
    .zhHant('高頻')
    .ar('مرتفع')
    .he('גבוהים')
)

ts.append(T(tag="ClumpLabel/text",
    text='LOW')
    .es('BAJOS')
    .pt('GRAVE')
    .fr('GRAVES')
    .ja('低域')
    .ko('저역대')
    .zhHans('低频')
    .zhHant('低頻')
    .ar('منخفض')
    .he('נמוכים')
)

ts.append(T(tag="ClumpLabel/text",
    text="""
        R
        A
        N
        G
        E""")
    # Set vertically
    .es("""
        R
        A
        N
        G
        O""")
    .pt("""
        EX
        TE
        NS
        ÃO""")
    .fr("""
        G
        A
        M
        M
        E""")
    .ja("""
        範
        囲""")
    .ko("""
        적
        용
        범
        위""")
    .zhHans("""
        范
        围""")
    .zhHant("""
        範
        圍""")
    .ar('المدى')
    .he('טווח')
)

ts.append(T(tag="ClumpLabel/text",
    text='TILT')
    .es('INCLINACIÓN')
    .pt('INCLINAÇÃO')
    .fr('INCLINAISON')
    .ja('チルト')
    .ko('틸트')
    .zhHans('倾斜')
    .zhHant('傾斜')
    .ar('الإمالة')
    .he('טילט')
)

ts.append(T(tag="ParamLabel/text",
    text='Loudness')
    .es('Volumen')
    .pt('Intensidade')
    .fr('Sonie')
    .ja('ラウドネス')
    .ko('음량')
    .zhHans('响度')
    .zhHant('響度')
    .ar('مستوَى الصوت')
    .he('לאודנס')
)

ts.append(T(tag="ParamLabel/text",
    text='Output Gain')
    .es('Ganancia de Salida')
    .pt('Ganho de Saída')
    .fr('Gain de Sortie')
    .ja('アウトプットゲイン')
    .ko('아웃풋 게인')
    .zhHans('输出增益')
    .zhHant('輸出增益')
    .ar('رِبح إشارة الإخراج')
    .he('גיין יציאה')
)

ts.append(T(tag="ParamLabel/text",
    text='Resonance')
    .es('Resonancia')
    .pt('Ressonância')
    .fr('Résonance')
    .ja('レゾナンス')
    .ko('레저넌스')
    .zhHans('谐振')
    .zhHant('諧振')
    .ar('الرنين')
    .he('רסונאנס')
)

ts.append(T(tag="ParamLabel/text",
    text='Slope')
    .es('Pendiente')
    .pt('Declive')
    .fr('Ordre')
    .ja('スロープ')
    .ko('필터 기울기')
    .zhHans('坡度')
    .zhHant('坡度')
    .ar('الميل')
    .he('מדרון')
)

ts.append(T(tag="Parameter/option",
    context="TiltLoudnessMode",
    text='Auto')
    # in the sense of 'automatic'
    .es(1)
    .pt('Automático')
    .fr('Automatique')
    .ja('自動')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('أوتوماتيكي')
    .he('אוטומטי')
)

ts.append(T(tag="Parameter/option",
    context="TiltLoudnessMode",
    text='Bass')
    .es('Graves')
    .pt('Grave')
    .fr('Grave')
    .ja('低域')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('الباس')
    .he('בס')
)

ts.append(T(tag="Parameter/option",
    context="TiltLoudnessMode",
    text='Standard')
    .es('Estándar')
    .pt('Padrão')
    .fr('Normal')
    .ja('普通')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('عادي')
    .he('סטנדרט')
)

ts.append(T(tag="Parameter/option",
    context="TiltLoudnessMode",
    text='Treble')
    .es('Agudos')
    .pt('Agudo')
    .fr('Aigu')
    .ja('高域')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('الصوت العالي')
    .he('טרבל')
)

ts.append(T(tag="Tagline",
    text='Superior tone-shaping, from mix to master')
    .es('Modelado de tonos sensacional, de la mezcla al máster')
    .pt('Modelagem excelente de tonalidade, da mix à master.')
    .fr('Excellent tone-shaping, du mix au master')
    .ja('周波数の鋭利なピックアップとトーンシェーピング')
    .ko('믹싱에서 마스터링까지 아우르는 간결한 톤 쉐이핑')
    .zhHans('从混音到母带的超级音色塑造')
    .zhHant('從混音到母帶的超級音色塑造')
    .ar('تسوية نِغم ممتازة،من الميكس إِلَى الماستر')
    .he('טון-שייפינג קצה עליון, ממיקס למאסטר')
)

