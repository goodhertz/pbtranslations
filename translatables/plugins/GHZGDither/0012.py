from pbt.translations import *


ts = TranslationSet()

ts.append(T(tag="ParamLabel/text",
    text="""
        Auto
        Blanking""")
    .es("""
        Desconexión
        Automática""")
    .pt("""
        Desligamento
        Automático""")
    .fr("""
        Silence
        Automatique""")
    .ja('オートブランキング')
    .ko('자동 차단 기능')
    .zhHans('自动空白')
    .zhHant('自動空白')
    .ar('المسح التلقائي')
    .he('אוטו-בלאנקינג')
)

ts.append(T(tag="ParamLabel/text",
    text="""
        Bit
        Depth""")
    .es("""
        Profundidad
        de Bits""")
    .pt("""
        Profundidade
        em Bits""")
    .fr("""
        Niveau de
        Quantification""")
    .ja('ビットデプス')
    .ko('비트 뎁스')
    .zhHans('位元深度')
    .zhHant('位元深度')
    .ar('عمق البِت')
    .he('ביט-דפט׳')
)

ts.append(T(tag="ParamLabel/text",
    text="""
        Dither
        Amount""")
    .es("""
        Nivel de
        Tramado""")
    .pt("""
        Quantidade
        de Dither""")
    .fr("""
        Intensité
        du Dither""")
    .ja('ディザー量')
    .ko('디더 적용 정도')
    .zhHans('抖动量')
    .zhHant('抖動量')
    .ar('كمية الديثر')
    .he('דיט׳ר מיקס')
)

ts.append(T(tag="ParamLabel/text",
    text="""
        Noise
        Shaping""")
    .es("""
        Modelado
        de Ruido""")
    .pt("""
        Modelagem
        do Ruído""")
    .fr("""
        Formage
        de Bruit""")
    .ja('ノイズシェーピング')
    .ko('노이즈 셰이핑')
    .zhHans('杂讯整形')
    .zhHant('雜訊整形')
    .ar('تشكيل الضجيج')
    .he('נויז-שייפינג')
)

ts.append(T(tag="Parameter/option",
    context="BitDepth",
    text='Pass Thru')
    .es('Señal Limpia')
    .pt('Sinal Limpo')
    .fr('Laissez-Passer')
    .ja('パススルー')
    .ko('패스 스루')
    .zhHans('不变')
    .zhHant('不變')
    .ar('تجَاوز')
    .he('ביט-דפט׳')
)

ts.append(T(tag="Parameter/option",
    context="DitherAmount",
    text='High')
    .es('Alto')
    .pt('Alto')
    .fr('Haute')
    .ja('多め')
    .ko('많음')
    .zhHans('高')
    .zhHant('高')
    .ar('مرتفع')
    .he('הרבה')
)

ts.append(T(tag="Parameter/option",
    context="DitherAmount",
    text='Low')
    .es('Bajo')
    .pt('Baixo')
    .fr('Basse')
    .ja('少なめ')
    .ko('적음')
    .zhHans('低')
    .zhHant('低')
    .ar('منخفض')
    .he('מעט')
)

ts.append(T(tag="Parameter/option",
    context="DitherAmount",
    text='None')
    .es('Nulo')
    .pt('Nenhum')
    .fr('Nulle')
    .ja('なし')
    .ko('없음')
    .zhHans('无')
    .zhHant('無')
    .ar('لا شيء')
    .he('בלי')
)

ts.append(T(tag="Parameter/option",
    context="DitherAmount",
    text='Optimal')
    .es('Óptimo')
    .pt('Otimizado')
    .fr('Optimale')
    .ja('最適')
    .ko('최적')
    .zhHans('最佳')
    .zhHant('最佳')
    .ar('مثالي')
    .he('כמה דיט׳ר')
)

ts.append(T(tag="Parameter/option",
    context="NoiseShaping",
    text='High')
    .es('Alto')
    .pt('Alto')
    .fr('Haut')
    .ja('多め')
    .ko('많음')
    .zhHans('高')
    .zhHant('高')
    .ar('مرتفع')
    .he('הרבה')
)

ts.append(T(tag="Parameter/option",
    context="NoiseShaping",
    text='Low')
    .es('Bajo')
    .pt('Baixo')
    .fr('Bas')
    .ja('少なめ')
    .ko('적음')
    .zhHans('低')
    .zhHant('低')
    .ar('منخفض')
    .he('מעט')
)

ts.append(T(tag="Parameter/option",
    context="NoiseShaping",
    text='Medium')
    .es('Medio')
    .pt('Médio')
    .fr('Moyen')
    .ja('普通')
    .ko('보통')
    .zhHans('中')
    .zhHant('中')
    .ar('متوسط')
    .he('מספיק')
)

ts.append(T(tag="Parameter/option",
    context="NoiseShaping",
    text='None')
    .es('Nulo')
    .pt('Nenhum')
    .fr('Nul')
    .ja('なし')
    .ko('없음')
    .zhHans('无')
    .zhHant('無')
    .ar('لا شيء')
    .he('בלי')
)

ts.append(T(tag="Parameter/option",
    context="NoiseShaping",
    text='Optimal')
    .es('Óptimo')
    .pt('Otimizado')
    .fr(1)
    .ja('最適')
    .ko('최적')
    .zhHans('最佳')
    .zhHant('最佳')
    .ar('مثالي')
    .he('אופיטמלי')
)

ts.append(T(tag="Tagline",
    text='World-class dither, simple controls.')
    .es('Tramado de otro nivel, controles sencillos')
    .pt('Dither excepcional, controles simples.')
    .fr('Dither exceptionnel, contrôles simples.')
    .ja('イージーオペレーションディザー')
    .ko('심플한 컨트롤의 월드클래스 디더')
    .zhHans('世界级的抖动处理, 超简易的控制')
    .zhHant('世界級的抖動處理, 超簡易的控制')
    .ar('ديثرعالمي،كنترولز بسيطة')
    .he('.דיט׳ר איכותי, בעיצוב פשוט')
)

