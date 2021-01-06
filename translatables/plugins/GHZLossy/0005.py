from pbt.translations import *


ts = TranslationSet()

ts.append(T(tag="ClumpLabel/text",
    text='FILTER')
    .es('FILTRO')
    .pt('FILTRO')
    .fr('FILTRE')
    .ja('フィルター')
    .ko('필터')
    .zhHans('滤波')
    .zhHant('濾波')
    .ar('فلتر')
    .he('פילטר')
)

ts.append(T(tag="ClumpLabel/text",
    text='LOSS')
    .es('PÉRDIDA')
    .pt('PERDA')
    .fr('PERTE')
    .ja('ロス')
    .ko('손실')
    .zhHans('损失')
    .zhHant('損失')
    .ar('فقدان')
    .he('לוס')
)

ts.append(T(tag="ClumpLabel/text",
    text='VERB')
    .es('REVERB')
    .pt('REVERB')
    .fr('REVERB')
    .ja('リバーブ')
    .ko('리버브')
    .zhHans('混响')
    .zhHant('混響')
    .ar('الصدى')
    .he('וורב')
)

ts.append(T(tag="ParamLabel/text",
    text='Amount')
    .es('Intensidad')
    .pt('Quantidade')
    .fr('Intensité')
    .ja('量')
    .ko('정도')
    .zhHans('量')
    .zhHant('量')
    .ar('الكمية')
    .he('מיקס')
)

ts.append(T(tag="ParamLabel/text",
    text="""
        Auto
        Gain""")
    .es("""
        Ganancia
        Auto.""")
    .pt("""
        Ganho
        Automático""")
    .fr("""
        Gain
        Automatique""")
    .ja("""
        オート
        ゲイン""")
    .ko("""
        오토
        게인""")
    .zhHans('自动增益')
    .zhHant('自動增益')
    .ar("""
        التلقائي
        الربح""")
    .he('אוטו-גיין')
)

ts.append(T(tag="ParamLabel/text",
    text='DRY')
    .es(1)
    .pt(1)
    .fr(1)
    .ja('原音')
    .ko('원음')
    .zhHans('干声')
    .zhHant('乾聲')
    .ar('جاف')
    .he('מיקס')
)

ts.append(T(tag="ParamLabel/text",
    text='Gain')
    .es('Ganancia')
    .pt('Ganho')
    .fr(1)
    .ja('ゲイン')
    .ko('게인')
    .zhHans('增益')
    .zhHant('增益')
    .ar('الربح')
    .he('גיין')
)

ts.append(T(tag="ParamLabel/text",
    text="""
        Gate
        Threshold""")
    .es("""
        Umbral
        de Puerta""")
    .pt("""
        Limite
        do Gate""")
    .fr("""
        Seuil
        du Gate""")
    .ja("""
        ゲート
        スレッショルド""")
    .ko("""
        게이트
        기준 레벨""")
    .zhHans("""
        门限
        域值""")
    .zhHant("""
        門限
        域值""")
    .ar("""
        للبوابة
        حد العتبة""")
    .he('סף גייט')
)

ts.append(T(tag="ParamLabel/text",
    text='LOSSY')
    .es(1)
    .pt(1)
    .fr(1)
    .ja(1)
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar(1)
    .he('לוסי')
)

ts.append(T(tag="ParamLabel/text",
    text='Range')
    .es('Rango')
    .pt('Extensão')
    .fr('Gamme')
    .ja('範囲')
    .ko('필터 범위')
    .zhHans('范围')
    .zhHant('範圍')
    .ar('المدَى')
    .he('טווח')
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

ts.append(T(tag="ParamLabel/text",
    text='Speed')
    .es('Velocidad')
    .pt('Velocidade')
    .fr('Vitesse')
    .ja('スピード')
    .ko('속도')
    .zhHans('速度')
    .zhHant('速度')
    .ar('السرعة')
    .he('מהירות')
)

ts.append(T(tag="ParamLabel/text",
    text='Stereo Mode')
    .es('Modo Estéreo')
    .pt('Modo Estéreo')
    .fr('Mode Stéréo')
    .ja('ステレオモード')
    .ko('스테레오 모드')
    .zhHans('立体声模式')
    .zhHant('立體聲模式')
    .ar('وضع ستيريو')
    .he('מצב סטריאו')
)

ts.append(T(tag="ParamLabel/text",
    text="""
        Verb
        Decay""")
    .es("""
        Decaimiento
        de Reverb""")
    .pt("""
        Decaimento
        do Reverb""")
    .fr("""
        Decay
        de Reverb""")
    .ja("""
        リバーブ
        ディケイ""")
    .ko("""
        리버브
        디케이""")
    .zhHans("""
        混响
        衰减""")
    .zhHant("""
        混響
        衰減""")
    .ar("""
        الصدى
        تضاؤل""")
    .he('ריוורב דיקאיי')
)

ts.append(T(tag="ParamLabel/text",
    text='Weighting')
    .es('Peso')
    .pt('Peso')
    .fr('Poids')
    .ja('加重')
    .ko('가중치')
    .zhHans('加权')
    .zhHant('加權')
    .ar('ترجيح')
    .he('משקל')
)

ts.append(T(tag="Parameter/option",
    context="FilterMode",
    text='Invert')
    .es('Invert.')
    .pt('Invert.')
    .fr('Inversé')
    .ja('逆')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('عَكّس')
    .he('מצב פילטר')
)

ts.append(T(tag="Parameter/option",
    context="FilterMode",
    text='Norm.')
    .es(1)
    .pt(1)
    .fr('Normal')
    .ja('普通')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('طبيعي')
    .he('נורמאלי')
)

ts.append(T(tag="Parameter/option",
    context="LossMode",
    text='Inverse')
    .es('Inverso')
    .pt('Inverso')
    .fr('Inversée')
    .ja('逆')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('عَكّس')
    .he('מצב לוס')
)

ts.append(T(tag="Parameter/option",
    context="LossMode",
    text='Packet Loss')
    .es('Pérdida de Paquetes')
    .pt('Perda de Packets')
    .fr('Perte de Paquets')
    .ja('パケットロス')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('فقدان الطور')
    .he('פאקט לוס')
)

ts.append(T(tag="Parameter/option",
    context="LossMode",
    text='Packet Repeat')
    .es('Repetición de Paquetes')
    .pt('Repetição de Packets')
    .fr('Répétition de Paquets')
    .ja('パケットリピート')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('تكرير الطور')
    .he('פאקט רפיט')
)

ts.append(T(tag="Parameter/option",
    context="LossMode",
    text='Phase Jitter')
    .es('Fluctuación de Fase')
    .pt('Flutuação de Fase')
    .fr('Jitter de Phase')
    .ja('フェーズジター')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('إرتعاش الطور')
    .he('ג׳יטר פאזה')
)

ts.append(T(tag="Parameter/option",
    context="LossMode",
    text='Standard')
    .es('Estándar')
    .pt('Padrão')
    .fr('Normale')
    .ja('普通')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('عادي')
    .he('סטנדרט')
)

ts.append(T(tag="Parameter/option",
    context="LossMode",
    text='Standard + Packet Loss')
    .es('Estándar + Pérdida de Paquetes')
    .pt('Padrão + Perda de Packets')
    .fr('Normale + Perte de Paquets')
    .ja('普通＋パケットロス')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('عادي + فقدان الطور')
    .he('סטנדרט+פאקט לוס')
)

ts.append(T(tag="Parameter/option",
    context="LossMode",
    text='Standard + Packet Repeat')
    .es('Estándar + Repetición de Paquetes')
    .pt('Padrão + Repetição de Packets')
    .fr('Normale + Répétition de Paquets')
    .ja('普通＋パケットリピート')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('عادي + تكرير الطور')
    .he('סטנדרט+פאקט רפיט')
)

ts.append(T(tag="Parameter/option",
    context="StereoMode",
    text='Joint Stereo')
    .es('Estéreo Conjunto')
    .pt('Estéreo Somado')
    .fr('Stéréo Combiné')
    .ja('ジョイントステレオ')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('مجموعة ستيريو')
    .he('מצב סטריאו')
)

ts.append(T(tag="Parameter/option",
    context="StereoMode",
    text='Mono')
    .es(1)
    .pt(1)
    .fr(1)
    .ja('モノラル')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('مونو')
    .he('מונו')
)

ts.append(T(tag="Parameter/option",
    context="StereoMode",
    text='Stereo')
    .es('Estéreo')
    .pt('Estéreo')
    .fr('Stéréo')
    .ja('ステレオ')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('ستيريو')
    .he('סטריאו')
)

ts.append(T(tag="Parameter/option",
    context="VerbPosition",
    text='Post')
    .es(1)
    .pt('Pós')
    .fr(1)
    .ja('ポスト')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('بعد')
    .he('פוסט')
)

ts.append(T(tag="Parameter/option",
    context="VerbPosition",
    text='Pre')
    .es(1)
    .pt('Pré')
    .fr('Pré')
    .ja('プリ')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('قبل')
    .he('פרה')
)

ts.append(T(tag="Parameter/option",
    context="Weighting",
    text='Flat')
    .es('Plana')
    .pt('Padrão')
    .fr('Uniforme')
    .ja('一定')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('مُسْتَوٍ')
    .he('שטוח')
)

ts.append(T(tag="Parameter/option",
    context="Weighting",
    text='Perceptual')
    .es(1)
    .pt('Psicoacústico')
    .fr('Perceptuel')
    .ja('知覚')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('إدراكي')
    .he('פרספטואל')
)

ts.append(T(tag="Tagline",
    text='Lossy artifacts, on demand.')
    .es('Artefactos de compresión, bajo demanda.')
    .pt('Artefatos digitais, à disposição.')
    .fr('Artefacts numériques, à la demande.')
    .ja('デジタル・サウンド・アート・ファクトリー')
    .ko('예술적 디지털 아티팩트')
    .zhHans('艺品般的复古模拟')
    .zhHant('藝品般的復古模擬')
    .ar('ادوات فقودة، تحت الطلب')
    .he('לו-פיי סאונד, און דימנד')
)

