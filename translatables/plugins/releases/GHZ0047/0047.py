from pbt.translations import *


ts = TranslationSet()

ts.append(T(tag="ClumpLabel/text",
    text='Bias')
    .es(1)
    .pt(1)
    .fr('Tension')
    .it(0)
    .ja('バイアス')
    .ko('바이어스')
    .zhHans('磁带偏差')
    .zhHant('磁帶偏差')
    .ar(0)
    .he(0)
)

ts.append(T(tag="ClumpLabel/text",
    text="""
        CAL
        TRIM""")
    # as in Calibration
    .es("""
        AJUSTE 
        DE CAL""")
    .pt("""
        GANHO DE
        CALIBRAGEM""")
    .fr("""
        VOLUME DE
        CALIBR.""")
    .it(0)
    .ja('校正トリム')
    .ko('보정 트림')
    .zhHans('校准修剪')
    .zhHant('校準修剪')
    .ar(0)
    .he(0)
)

ts.append(T(tag="ClumpLabel/text",
    text='EMPHASIS')
    .es('ÉNFASIS')
    .pt('ÊNFASE')
    .fr('ACCENTUATION')
    .it(0)
    .ja('エンファシス')
    .ko('엠퍼시스')
    .zhHans('加重')
    .zhHant('加重')
    .ar(0)
    .he(0)
)

ts.append(T(tag="ClumpLabel/text",
    text='FILTER')
    .es('FILTRO')
    .pt('FILTRO')
    .fr('FILTRE')
    .it(0)
    .ja('フィルター')
    .ko('필터')
    .zhHans('滤波')
    .zhHant('濾波')
    .ar(0)
    .he(0)
)

ts.append(T(tag="ClumpLabel/text",
    text='Noise')
    .es('Ruido')
    .pt('Ruído')
    .fr('Bruit')
    .it(0)
    .ja('ノイズ')
    .ko('노이즈')
    .zhHans('噪声')
    .zhHant('噪聲')
    .ar(0)
    .he(0)
)

ts.append(T(tag="ParamLabel/text",
    text='DRY')
    .es(1)
    .pt(1)
    .fr(1)
    .it(0)
    .ja('原音')
    .ko('원음')
    .zhHans('干声')
    .zhHant('乾聲')
    .ar(0)
    .he(0)
)

ts.append(T(tag="ParamLabel/text",
    text='Drive')
    .es(1)
    .pt(1)
    .fr(1)
    .it(0)
    .ja('ドライブ')
    .ko('드라이브')
    .zhHans('输入')
    .zhHant('輸入')
    .ar(0)
    .he(0)
)

ts.append(T(tag="ParamLabel/text",
    text='Output')
    .es('Salida')
    .pt('Saída')
    .fr('Sortie')
    .it(0)
    .ja('アウトプット')
    .ko('아웃풋')
    .zhHans('輸出')
    .zhHant('输出')
    .ar(0)
    .he(0)
)

ts.append(T(tag="ParamLabel/text",
    text='Tilt')
    .es('Incl.')
    .pt('Incl.')
    .fr('Incl.')
    .it(0)
    .ja('チルト')
    .ko('틸트')
    .zhHans('倾斜')
    .zhHant('傾斜')
    .ar(0)
    .he(0)
)

ts.append(T(tag="ParamLabel/text",
    text='Trim')
    .es('Ajuste')
    .pt('Volume')
    .fr('Volume')
    .it(0)
    .ja('トリム')
    .ko('트림')
    .zhHans('调整')
    .zhHant('調整')
    .ar(0)
    .he(0)
)

ts.append(T(tag="Parameter/option",
    text='EMPHASIS')
    .es('ÉNFASIS')
    .pt('ÊNFASE')
    .fr('ACCENT.')
    .it(0)
    .ja('エンファシス')
    .ko('엠퍼시스')
    .zhHans('加重')
    .zhHant('加重')
    .ar(0)
    .he(0)
)

ts.append(T(tag="Parameter/option",
    text='FILTER')
    .es('FILTRO')
    .pt('FILTRO')
    .fr('FILTRE')
    .it(0)
    .ja('フィルター')
    .ko('필터')
    .zhHans('滤波')
    .zhHant('濾波')
    .ar(0)
    .he(0)
)

ts.append(T(tag="Parameter/option",
    context="AdvPage",
    text='EMPHASIS')
    .es('ÉNFASIS')
    .pt('ÊNFASE')
    .fr('ACCENT.')
    .it(0)
    .ja('エンファシス')
    .ko('엠퍼시스')
    .zhHans('加重')
    .zhHant('加重')
    .ar(0)
    .he(0)
)

ts.append(T(tag="Parameter/option",
    context="AdvPage",
    text='FILTER+CAL')
    .es('FILTRO+CAL')
    .pt('FILTRO+CAL.')
    .fr('FILTRE+CAL.')
    .it(0)
    .ja('フィルター・校正')
    .ko('필터+보정')
    .zhHans('滤波+校准')
    .zhHant('濾波+校準')
    .ar(0)
    .he(0)
)

ts.append(T(tag="Parameter/option",
    context="FilterPosition",
    text='BTW')
    .es('ENTRE')
    .pt('ENTRE')
    .fr('ENTRE')
    .it(0)
    .ja('ビトウィーン')
    .ko('비트윈')
    .zhHans('中间')
    .zhHant('中間')
    .ar(0)
    .he(0)
)

ts.append(T(tag="Parameter/option",
    context="FilterPosition",
    text='POST')
    .es(1)
    .pt('PÓS')
    .fr(1)
    .it(0)
    .ja('ポスト')
    .ko('포스트')
    .zhHans('后')
    .zhHant('後')
    .ar(0)
    .he(0)
)

ts.append(T(tag="Parameter/option",
    context="FilterPosition",
    text='PRE')
    .es(1)
    .pt('PRÉ')
    .fr('PRÉ')
    .it(0)
    .ja('プリ')
    .ko('프리')
    .zhHans('前')
    .zhHant('前')
    .ar(0)
    .he(0)
)

ts.append(T(tag="Parameter/option",
    context="OptoMode",
    text='COMP')
    .es(1)
    .pt(1)
    .fr(1)
    .it(0)
    .ja('コンプ')
    .ko('컴프')
    .zhHans('压缩')
    .zhHant('壓縮')
    .ar(0)
    .he(0)
)

ts.append(T(tag="Parameter/option",
    context="OptoMode",
    text='LIMIT')
    .es('LÍMITE')
    .pt(1)
    .fr(1)
    .it(0)
    .ja('リミット')
    .ko('리미트')
    .zhHans('限幅')
    .zhHant('限幅')
    .ar(0)
    .he(0)
)

ts.append(T(tag="Parameter/option",
    context="OptoPosition",
    text='BTW')
    .es('ENTRE')
    .pt('ENTRE')
    .fr('ENTRE')
    .it(0)
    .ja('ビトウィーン')
    .ko('비트윈')
    .zhHans('中间')
    .zhHant('中間')
    .ar(0)
    .he(0)
)

ts.append(T(tag="Parameter/option",
    context="OptoPosition",
    text='POST')
    .es(1)
    .pt('PÓS')
    .fr(1)
    .it(0)
    .ja('ポスト')
    .ko('포스트')
    .zhHans('后')
    .zhHant('後')
    .ar(0)
    .he(0)
)

ts.append(T(tag="Parameter/option",
    context="OptoPosition",
    text='PRE')
    .es(1)
    .pt('PRÉ')
    .fr('PRÉ')
    .it(0)
    .ja('プリ')
    .ko('프리')
    .zhHans('前')
    .zhHant('前')
    .ar(0)
    .he(0)
)

ts.append(T(tag="Parameter/option",
    context="OptoPosition",
    text='SAT')
    .es(1)
    .pt(1)
    .fr(1)
    .it(0)
    .ja('サチュレーション')
    .ko('세츄레이션')
    .zhHans('饱和')
    .zhHant('飽和')
    .ar(0)
    .he(0)
)

ts.append(T(tag="Parameter/option",
    context="TubeTapeOrder",
    text='Tape -> Tube')
    .es('Cinta -> Bulbo')
    .pt(1)
    .fr(1)
    .it(0)
    .ja('テープ -> チューブ')
    .ko('테이프 -> 진공관')
    .zhHans('磁帶 -> 真空管')
    .zhHant('磁帶 -> 真空管')
    .ar(0)
    .he(0)
)

ts.append(T(tag="Parameter/option",
    context="TubeTapeOrder",
    text='Tube -> Tape')
    .es('Bulbo -> Cinta')
    .pt(1)
    .fr(1)
    .it(0)
    .ja('チューブ -> テープ')
    .ko('진공관 -> 테이프')
    .zhHans('真空管 -> 磁带')
    .zhHant('真空管 -> 磁帶')
    .ar(0)
    .he(0)
)

ts.append(T(tag="Tagline",
    text='Tube + Tape = Tupe')
    .es(1)
    .pt(1)
    .fr(1)
    .it(0)
    .ja('チューブ + テープ = チュープ')
    .ko('진공관 + 테이프 = 튜프')
    .zhHans('真空管 + 磁带 = 磁管')
    .zhHant('真空管 + 磁帶 = 磁管')
    .ar(0)
    .he(0)
)

