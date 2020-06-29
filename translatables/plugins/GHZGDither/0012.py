from pbt.translations import *


ts = TranslationSet()

ts.append(T(tag="ParamLabel/text",
    text='Auto\nBlanking')
    .es('Supresión\nautomática')
    .pt('Desligamento\nAutomático')
    .fr('Silence\nAutomatique')
    .ja('オートブランキング')
    .ko('자동 차단 기능')
    .zhHans('自动消隐')
    .zhHant('自動消隱')
    .ar('المسح التلقائي')
    .he(0)
)

ts.append(T(tag="ParamLabel/text",
    text='Bit\nDepth')
    .es('Profundidad\nde bit')
    .pt('Profundidade\nem Bits')
    .fr('Niveau de\nQuantification')
    .ja('ビットデプス')
    .ko('비트 뎁스')
    .zhHans('比特深度')
    .zhHant('比特深度')
    .ar('عمق البِت')
    .he(0)
)

ts.append(T(tag="ParamLabel/text",
    text='Dither\nAmount')
    .es('Nivel de\ninterpolación')
    .pt('Quantidade\nde Dither')
    .fr('Intensité\ndu Dither')
    .ja('ディザー量')
    .ko('디더 적용 정도')
    .zhHans('抖动量')
    .zhHant('抖動量')
    .ar('كمية الديثر')
    .he(0)
)

ts.append(T(tag="ParamLabel/text",
    text='Noise\nShaping')
    .es('Modelación\nde ruido')
    .pt('Modelagem\ndo Ruído')
    .fr('Formage\nde Bruit')
    .ja('ノイズシェーピング')
    .ko('노이즈 형태')
    .zhHans('噪音整形')
    .zhHant('噪音整形')
    .ar('تشكيل الضجيج')
    .he(0)
)

ts.append(T(tag="Parameter/option",
    context="BitDepth",
    text='Pass Thru')
    .es('Señal limpia')
    .pt('Sinal Limpo')
    .fr('Laissez-Passer')
    .ja('そのまま')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('تجَاوز')
    .he(0)
)

ts.append(T(tag="Parameter/option",
    context="DitherAmount",
    text='High')
    .es('Alto')
    .pt('Alto')
    .fr('Haute')
    .ja('多め')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('مرتفع')
    .he(0)
)

ts.append(T(tag="Parameter/option",
    context="DitherAmount",
    text='Low')
    .es('Bajo')
    .pt('Baixo')
    .fr('Basse')
    .ja('少なめ')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('منخفض')
    .he(0)
)

ts.append(T(tag="Parameter/option",
    context="DitherAmount",
    text='None')
    .es('Nulo')
    .pt('Nenhum')
    .fr('Nulle')
    .ja('なし')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('لا شيء')
    .he(0)
)

ts.append(T(tag="Parameter/option",
    context="DitherAmount",
    text='Optimal')
    .es('Óptimo')
    .pt('Otimizado')
    .fr('Optimale')
    .ja('最適')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('مثالي')
    .he(0)
)

ts.append(T(tag="Parameter/option",
    context="NoiseShaping",
    text='High')
    .es('Alta')
    .pt('Alto')
    .fr('Haut')
    .ja('多め')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('مرتفع')
    .he(0)
)

ts.append(T(tag="Parameter/option",
    context="NoiseShaping",
    text='Low')
    .es('Baja')
    .pt('Baixo')
    .fr('Bas')
    .ja('少なめ')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('منخفض')
    .he(0)
)

ts.append(T(tag="Parameter/option",
    context="NoiseShaping",
    text='Medium')
    .es('Medio')
    .pt('Médio ')
    .fr('Moyen')
    .ja('普通')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('متوسط')
    .he(0)
)

ts.append(T(tag="Parameter/option",
    context="NoiseShaping",
    text='None')
    .es('Nula')
    .pt('Nenhum')
    .fr('Nul')
    .ja('なし')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('لا شيء')
    .he(0)
)

ts.append(T(tag="Parameter/option",
    context="NoiseShaping",
    text='Optimal')
    .es('Óptima')
    .pt('Otimizado')
    .fr(1)
    .ja('最適')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('مثالي')
    .he(0)
)

ts.append(T(tag="Tagline",
    text='World-class dither, simple controls.')
    .es('Interpolación de lujo, controles sencillos')
    .pt('Dither excepcional, controles simples.')
    .fr('Dither exceptionnel, contrôles simples.')
    .ja('イージーオペレーションディザー')
    .ko('심플한 컨트롤의 월드클래스 디더')
    .zhHans('世界级的抖动处理, 超简易的控制')
    .zhHant('世界級的抖動處理, 超簡易的控制')
    .ar('ديثرعالمي،كنترولز بسيطة')
    .he(0)
)

