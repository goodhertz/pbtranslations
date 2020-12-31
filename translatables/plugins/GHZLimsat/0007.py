from pbt.translations import *


ts = TranslationSet()

ts.append(T(tag="ClumpLabel/text",
    text='LINK')
    .es('VÍNCULO')
    .pt(1)
    .fr('COUPLAGE')
    .ja('リンク')
    .ko('링크 설정')
    .zhHans('连结')
    .zhHant('連結')
    .ar('الوصل')
    .he('לינק')
)

ts.append(T(tag="ClumpLabel/text",
    text='OUT')
    .es('SALIDA')
    .pt('SAÍDA')
    .fr('SORTIE')
    .ja('アウト')
    .ko('아웃풋')
    .zhHans('输出')
    .zhHant('輸出')
    .ar('الخرج')
    .he('יציאה')
)

ts.append(T(tag="ClumpLabel/text",
    text='RATIO')
    .es('PROPORCIÓN')
    .pt('PROPORÇÃO')
    .fr(1)
    .ja('比率')
    .ko('비율')
    .zhHans('比率')
    .zhHant('比率')
    .ar('نسبة الضغط')
    .he('יחס')
)

ts.append(T(tag="ClumpLabel/text",
    text='SIDECHAIN')
    .es(1)
    .pt(1)
    .fr(1)
    .ja('サイドチェイン')
    .ko('사이드체인')
    .zhHans('旁链')
    .zhHant('旁鏈')
    .ar('السايدشين')
    .he('סייד-צ׳יין')
)

ts.append(T(tag="ClumpLabel/text",
    text='SPEED')
    .es('VELOCIDAD')
    .pt('VELOCIDADE')
    .fr('VITESSE')
    .ja('スピード')
    .ko('속도')
    .zhHans('速度')
    .zhHant('速度')
    .ar('السرعة')
    .he('מהירות')
)

ts.append(T(tag="ClumpLabel/text",
    text='THRESH')
    .es('UMBRAL')
    .pt('LIMITE')
    .fr('SEUIL')
    .ja('スレッショルド')
    .ko('기준 레벨')
    .zhHans('阈')
    .zhHant('閾')
    .ar('حد العتبة')
    .he('סף')
)

ts.append(T(tag="ClumpLabel/text",
    text='VIBE')
    .es('VIBRA')
    .pt(1)
    .fr('AMBIANCE')
    .ja('バイブ')
    .ko('톤 조정')
    .zhHans('氛围')
    .zhHant('氛圍')
    .ar('الجو')
    .he('וייב')
)

ts.append(T(tag="ParamLabel/text",
    text='Attack')
    .es('Ataque')
    .pt('Ataque')
    .fr('Attaque')
    .ja('アタック')
    .ko('어택 타임')
    .zhHans('起动时间')
    .zhHant('起動時間')
    .ar('زمن التطبيق')
    .he('זמן-התקף')
)

ts.append(T(tag="ParamLabel/text",
    text='Auto Gain')
    .es('Ganancia Auto.')
    .pt('Ganho Autom.')
    .fr('Gain Auto')
    .ja('オートゲイン')
    .ko('오토 게인 설정')
    .zhHans('自动增益')
    .zhHant('自動增益')
    .ar('الربح التلقائي')
    .he('אוטו-גיין')
)

ts.append(T(tag="ParamLabel/text",
    text='Color')
    .es('Coloración')
    .pt('Coloração')
    .fr('Coloration')
    .ja('カラー')
    .ko('컬러')
    .zhHans('色彩')
    .zhHant('色彩')
    .ar('اللون')
    .he('צבע')
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
    text='FRDY')
    .es(1)
    .pt(1)
    .fr(1)
    .ja(1)
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar(1)
    .he(1)
)

ts.append(T(tag="ParamLabel/text",
    text="""
        Link
        Amount""")
    .es("""
        Intensidad
        de Vínculo""")
    .pt("""
        Intensidade
        do Link""")
    .fr("""
        Intensité
        du Couplage""")
    .ja('リンクパーセンテージ')
    .ko('링크 정도')
    .zhHans('连结程度')
    .zhHant('連結程度')
    .ar("""
        الوصل
        كمية""")
    .he('לינק מיקס')
)

ts.append(T(tag="ParamLabel/text",
    text="""
        Link
        Side Gain""")
    .es("""
        Ganancia de
        Vínculo de Side""")
    .pt("""
        Ganho
        Side""")
    .fr("""
        Gain de Side
        du Couplage""")
    .ja('リンクサイドゲイン')
    .ko('링크 사이드 게인')
    .zhHans('连结侧信号增益')
    .zhHant('連結側信號增益')
    .ar("""
        الجانبي
        وصل الربح""")
    .he('לינק גיין')
)

ts.append(T(tag="ParamLabel/text",
    text='Link Mode')
    .es('Modo de Vínculo')
    .pt('Modo do Link')
    .fr('Mode de Couplage')
    .ja('リンクモード')
    .ko('링크 모드')
    .zhHans('连结模式')
    .zhHant('連結模式')
    .ar('وضعُ الوصل')
    .he('מצב לינק')
)

ts.append(T(tag="ParamLabel/text",
    text='Release')
    .es('Relajación')
    .pt('Repouso')
    .fr('Retour')
    .ja('リリース')
    .ko('릴리즈 타임')
    .zhHans('释放时间')
    .zhHant('釋放時間')
    .ar('التحرير')
    .he('זמן-שחרור')
)

ts.append(T(tag="ParamLabel/text",
    text="""
        Sidechain
        HPF""")
    .es("""
        Filtro Paso Altos
        de Sidechain""")
    .pt("""
        Filtro Passa-Altas
        do Sidechain""")
    .fr("""
        Passe-Haut
        du Sidechain""")
    .ja('サイドチェインHPF')
    .ko('사이드체인 HPF')
    .zhHans('旁链高通滤波器')
    .zhHant('旁鏈高通濾波器')
    .ar("""
        العالية للسايدشين
        مرشح الترددا""")
    .he('סייד-צ׳יין היי-פאס פילטר')
)

ts.append(T(tag="ParamLabel/text",
    text="""
        Sidechain
        Trim""")
    .es("""
        Ajuste
        de Sidechain""")
    .pt("""
        Sidechain
        Volume""")
    .fr("""
        Volume
        du Sidechain""")
    .ja('サイドチェイントリム')
    .ko('사이드체인 트림')
    .zhHans('旁链修剪')
    .zhHant('旁鏈修剪')
    .ar("""
        السايدشين
        مُوازَنةٌ""")
    .he('סייד-צ׳יין טרים')
)

ts.append(T(tag="ParamLabel/text",
    text='Sidechain Source')
    .es('Fuente de Sidechain')
    .pt('Sidechain – Fonte')
    .fr('Source de Couplage')
    .ja('サイドチェインソース')
    .ko('사이드체인 소스 선택')
    .zhHans('旁链声源')
    .zhHant('旁鏈聲源')
    .ar('منبع السايدشين')
    .he('סייד-צ׳יין חיצוני')
)

ts.append(T(tag="ParamLabel/text",
    text='Warmth')
    .es('Calidez')
    .pt('Calor')
    .fr('Chaleur')
    .ja('ウォーム')
    .ko('따스함')
    .zhHans('暖度')
    .zhHant('暖度')
    .ar('الدفء')
    .he('חום')
)

ts.append(T(tag="Parameter/option",
    context="LinkMode",
    text='Left/Right')
    .es('Izquierda/Derecha')
    .pt('Esquerda/Direita')
    .fr('Gauche/Droite')
    .ja('左/右')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('يمين/يسار')
    .he('ימין/שמאל')
)

ts.append(T(tag="Parameter/option",
    context="LinkMode",
    text='Mid/Side')
    .es(1)
    .pt('Meio/Lados')
    .fr(1)
    .ja('ミッド/サイド')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('ميد/سايد')
    .he('אמצע/צדדים')
)

ts.append(T(tag="Parameter/option",
    context="SidechainSource",
    text='External')
    .es('Externa')
    .pt('Externa')
    .fr('Externe')
    .ja('外部')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('خارجي')
    .he('חיצוני')
)

ts.append(T(tag="Parameter/option",
    context="SidechainSource",
    text='Internal')
    .es('Interna')
    .pt('Interna')
    .fr('Interne')
    .ja('内部')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('داخلي')
    .he('פנימי')
)

ts.append(T(tag="Tagline",
    text='Peak limiter w/ a big magnetic field.')
    .es('Limitador de picos con un gran campo magnético.')
    .pt('Limitador de picos com um campo magnético gigante.')
    .fr('Limiteur de crête avec un grand champ magnétique.')
    .ja('マルチカラーのバイブス\u3000音楽の為のピークリミッター')
    .ko('거대한 자기장 같은 피크 리미터')
    .zhHans('带有强大磁场的峰值限制器')
    .zhHant('帶有強大磁場的峰值限制器')
    .ar('محدِّد قِمم مع حقل مغناطيسي كبير')
    .he('פיק לימיטר עם שדה מגנטי ענק')
)

