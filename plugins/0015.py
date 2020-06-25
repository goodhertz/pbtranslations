from pbt.translations import *


ts = TranslationSet()

ts.append(T("ClumpLabel/text", "ADV FILTER")
    .es("FILTRO EXT")
    .pt("FILTRO +")
    .fr("FILTRE EXT")
    .ja("フィルター微調整")
    .ko("세부 필터")
    .zhHans("高級濾波調節")
    .zhHant("進階濾波調節")
    .ar("فلتر مُفصَّل")
    .he(0)
)

ts.append(T("ClumpLabel/text", "FILTER")
    .es("FILTRO")
    .pt("FILTRO")
    .fr("FILTRE")
    .ja("フィルター")
    .ko("필터")
    .zhHans("滤波")
    .zhHant("濾波")
    .ar("الفلتر")
    .he(0)
)

ts.append(T("ClumpLabel/text", "G|A|I|N") # Set vertically
    .es("GA|NAN|CIA")
    .pt("GA|NH|O")
    .fr(1)
    .ja("ゲ|イ|ン")
    .ko("게|인")
    .zhHans("增|益")
    .zhHant("增|益")
    .ar("الربح")
    .he(0)
)

ts.append(T("ClumpLabel/text", "HIGH")
    .es("ALTOS")
    .pt("AGUDO")
    .fr("AIGUS")
    .ja("高域")
    .ko("고역대")
    .zhHans("高频")
    .zhHant("高頻")
    .ar("مرتفع")
    .he(0)
)

ts.append(T("ClumpLabel/text", "LOW")
    .es("BAJOS")
    .pt("GRAVE")
    .fr("GRAVES")
    .ja("低域")
    .ko("저역대")
    .zhHans("低频")
    .zhHant("低頻")
    .ar("منخفض")
    .he(0)
)

ts.append(T("ClumpLabel/text", "R|A|N|G|E") # Set vertically
    .es("R|A|N|G|O")
    .pt("EX|TE|NS|ÃO")
    .fr("G|A|M|M|E")
    .ja("範|囲")
    .ko("적|용|범|위")
    .zhHans("范|围")
    .zhHant("範|圍")
    .ar("المدى")
    .he(0)
)

ts.append(T("ClumpLabel/text", "TILT")
    .es("INCLINACIÓN")
    .pt("INCLINAÇÃO")
    .fr("INCLINAISON")
    .ja("チルト")
    .ko("틸트")
    .zhHans("倾斜")
    .zhHant("傾斜")
    .ar("الإمالة")
    .he(0)
)

ts.append(T("ParamLabel/text", "Loudness")
    .es("Sonoridad")
    .pt("Intensidade")
    .fr("Sonie")
    .ja("ラウドネス")
    .ko("음압")
    .zhHans("响度")
    .zhHant("響度")
    .ar("مستوَى الصوت")
    .he(0)
)

ts.append(T("ParamLabel/text", "Output Gain")
    .es("Ganancia salida")
    .pt("Ganho de Saída")
    .fr("Gain de Sortie")
    .ja("アウトプットゲイン")
    .ko("아웃풋 게인")
    .zhHans("输出增益")
    .zhHant("輸出增益")
    .ar("رِبح إشارة الإخراج")
    .he(0)
)

ts.append(T("ParamLabel/text", "Resonance")
    .es("Resonancia")
    .pt("Ressonância")
    .fr("Résonance")
    .ja("レゾナンス")
    .ko("레저넌스")
    .zhHans("谐振")
    .zhHant("諧振")
    .ar("الرنين")
    .he(0)
)

ts.append(T("ParamLabel/text", "Slope")
    .es("Pendiente")
    .pt("Declive")
    .fr("Ordre")
    .ja("スロープ")
    .ko("필터 기울기")
    .zhHans("坡度")
    .zhHant("坡度")
    .ar("الميل")
    .he(0)
)

ts.append(T("Parameter/option", "Auto", "TiltLoudnessMode") # i.e. automatic
    .es("Automático")
    .pt("Automático")
    .fr("Automatique")
    .ja("自動")
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar("أوتوماتيكي")
    .he(0)
)

ts.append(T("Parameter/option", "Bass", "TiltLoudnessMode")
    .es("Bajos")
    .pt("Grave")
    .fr("Grave")
    .ja("低域")
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar("الباس")
    .he(0)
)

ts.append(T("Parameter/option", "Standard", "TiltLoudnessMode")
    .es("Estándar")
    .pt("Padrão")
    .fr("Normal")
    .ja("普通")
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar("عادي")
    .he(0)
)

ts.append(T("Parameter/option", "Treble", "TiltLoudnessMode")
    .es("Altos")
    .pt("Agudo")
    .fr("Aigu")
    .ja("高域")
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar("الصوت العالي")
    .he(0)
)