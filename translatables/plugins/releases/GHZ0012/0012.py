from pbtranslations.translations import *


ts = TranslationSet()

ts.append(T(tag="Parameter/option",
    context="BitDepth",
    text='Pass Thru')
    .es('Señal Limpia')
    .pt('Sinal Limpo')
    .fr('Laissez-Passer')
    .it('Originale')
    .ja('パススルー')
    .ko('패스 스루')
    .zhHans('不变')
    .zhHant('不變')
    .ar('تجَاوز')
    )

ts.append(T(tag="Parameter/option",
    context="DitherAmount",
    text='None')
    .es('Nulo')
    .pt('Nenhum')
    .fr('Nulle')
    .it('Nullo')
    .ja('なし')
    .ko('없음')
    .zhHans('无')
    .zhHant('無')
    .ar('لا شيء')
    )

ts.append(T(tag="Parameter/option",
    context="DitherAmount",
    text='Low')
    .es('Bajo')
    .pt('Baixo')
    .fr('Basse')
    .it('Poco')
    .ja('少なめ')
    .ko('적음')
    .zhHans('低')
    .zhHant('低')
    .ar('منخفض')
    )

ts.append(T(tag="Parameter/option",
    context="DitherAmount",
    text='Optimal')
    .es('Óptimo')
    .pt('Otimizado')
    .fr('Optimale')
    .it('Ottimale')
    .ja('最適')
    .ko('최적')
    .zhHans('最佳')
    .zhHant('最佳')
    .ar('مثالي')
    )

ts.append(T(tag="Parameter/option",
    context="DitherAmount",
    text='High')
    .es('Alto')
    .pt('Alto')
    .fr('Haute')
    .it('Molto')
    .ja('多め')
    .ko('많음')
    .zhHans('高')
    .zhHant('高')
    .ar('مرتفع')
    )

ts.append(T(tag="Parameter/option",
    context="NoiseShaping",
    text='Optimal')
    .es('Óptimo')
    .pt('Otimizado')
    .fr(1)
    .it('Ottimale')
    .ja('最適')
    .ko('최적')
    .zhHans('最佳')
    .zhHant('最佳')
    .ar('مثالي')
    )

ts.append(T(tag="Parameter/option",
    context="NoiseShaping",
    text='None')
    .es('Nulo')
    .pt('Nenhum')
    .fr('Nul')
    .it('Nullo')
    .ja('なし')
    .ko('없음')
    .zhHans('无')
    .zhHant('無')
    .ar('لا شيء')
    )

ts.append(T(tag="Parameter/option",
    context="NoiseShaping",
    text='Low')
    .es('Bajo')
    .pt('Baixo')
    .fr('Bas')
    .it('Poco')
    .ja('少なめ')
    .ko('적음')
    .zhHans('低')
    .zhHant('低')
    .ar('منخفض')
    )

ts.append(T(tag="Parameter/option",
    context="NoiseShaping",
    text='Medium')
    .es('Medio')
    .pt('Médio')
    .fr('Moyen')
    .it('Medio')
    .ja('普通')
    .ko('보통')
    .zhHans('中')
    .zhHant('中')
    .ar('متوسط')
    )

ts.append(T(tag="Parameter/option",
    context="NoiseShaping",
    text='High')
    .es('Alto')
    .pt('Alto')
    .fr('Haut')
    .it('Molto')
    .ja('多め')
    .ko('많음')
    .zhHans('高')
    .zhHant('高')
    .ar('مرتفع')
    )

ts.append(T(tag="Tagline",
    text='World-class dither, simple controls')
    .es('Tramado de otro nivel, controles sencillos')
    .pt('Dither excepcional, controles simples')
    .fr('Dither exceptionnel, contrôles simples')
    .it('Dither di classe mondiale con controlli semplici')
    .ja('イージーオペレーションディザー')
    .ko('심플한 컨트롤의 월드클래스 디더')
    .zhHans('世界级的抖动处理, 超简易的控制')
    .zhHant('世界級的抖動處理, 超簡易的控制')
    .ar('ديثرعالمي،كنترولز بسيطة')
    )

ts.append(T(tag="ParamLabel/text",
    text='Bit\nDepth')
    .es('Profundidad\nde Bits')
    .pt('Profundidade\nem Bits')
    .fr('Niveau de\nQuantification')
    .it('Bit File\nEsportato')
    .ja('ビットデプス')
    .ko('비트 뎁스')
    .zhHans('位元深度')
    .zhHant('位元深度')
    .ar('عمق البِت')
    )

ts.append(T(tag="ParamLabel/text",
    text='Dither\nAmount')
    .es('Nivel de\nTramado')
    .pt('Quantidade\nde Dither')
    .fr('Intensité\ndu Dither')
    .it('Quantità\nDither')
    .ja('ディザー量')
    .ko('디더 적용 정도')
    .zhHans('抖动量')
    .zhHant('抖動量')
    .ar('كمية الديثر')
    )

ts.append(T(tag="ParamLabel/text",
    text='Auto\nBlanking')
    .es('Desconexión\nAutomática')
    .pt('Desligamento\nAutomático')
    .fr('Silence\nAutomatique')
    .it('Auto\nSilenzio')
    .ja('オートブランキング')
    .ko('자동 차단 기능')
    .zhHans('自动空白')
    .zhHant('自動空白')
    .ar('المسح التلقائي')
    )

ts.append(T(tag="ParamLabel/text",
    text='Noise\nShaping')
    .es('Modelado\nde Ruido')
    .pt('Modelagem\ndo Ruído')
    .fr('Formage\nde Bruit')
    .it('Tipo\nDither')
    .ja('ノイズシェーピング')
    .ko('노이즈 셰이핑')
    .zhHans('杂讯整形')
    .zhHant('雜訊整形')
    .ar('تشكيل الضجيج')
    )

