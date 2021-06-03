from pbt.translations import *


ts = TranslationSet()

ts.append(T(tag="ClumpLabel/text",
    text='Bias')
    .es(1)
    .pt(0)
    .fr('Tension')
    .ja('バイアス')
    .ko('바이어스')
    .zhHans('交流偏磁')
    .zhHant('交流偏磁')
    .ar(0)
    .he(0)
)

ts.append(T(tag="ClumpLabel/text",
    text="""
        CAL
        TRIM""")
    # as in Calibration
    .es(0)
    .pt(0)
    .fr("""
        Volume de
        Calibration""")
    .ja('校正トリム')
    .ko('보정 트림')
    .zhHans('校准修剪')
    .zhHant('校準修剪')
    .ar(0)
    .he(0)
)

ts.append(T(tag="ClumpLabel/text",
    text='EMPHASIS')
    .es(0)
    .pt(0)
    .fr('Accentuation')
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
    .pt(0)
    .fr('FILTRE')
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
    .pt(0)
    .fr('Bruit')
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
    .pt(0)
    .fr(1)
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
    .pt(0)
    .fr(1)
    .ja('ドライブ')
    .ko('드라이브')
    .zhHans('激励')
    .zhHant('激勵')
    .ar(0)
    .he(0)
)

ts.append(T(tag="ParamLabel/text",
    text='Output')
    .es('Salida')
    .pt(0)
    .fr('Sortie')
    .ja('アウトプット')
    .ko('아웃풋')
    .zhHans('輸出')
    .zhHant('输出')
    .ar(0)
    .he(0)
)

ts.append(T(tag="ParamLabel/text",
    text='Tilt')
    .es('Incl')
    .pt(0)
    .fr('Incl')
    .ja('チルト')
    .ko('틸트')
    .zhHans('倾斜')
    .zhHant('傾斜')
    .ar(0)
    .he(0)
)

ts.append(T(tag="ParamLabel/text",
    text='Trim')
    .es(0)
    .pt(0)
    .fr('Volume')
    .ja('トリム')
    .ko('트림')
    .zhHans('修剪')
    .zhHant('修剪')
    .ar(0)
    .he(0)
)

ts.append(T(tag="Parameter/option",
    context="AdvPage",
    text='EMPHASIS')
    .es(0)
    .pt(0)
    .fr('Accentuation')
    .ja('エンファシス')
    .ko('엠퍼시스')
    .zhHans('加重')
    .zhHant('加重')
    .ar(0)
    .he(0)
)

ts.append(T(tag="Parameter/option",
    context="AdvPage",
    text='FILTERING')
    .es(0)
    .pt(0)
    .fr('Filtration')
    .ja('フィルタリング')
    .ko('필터링')
    .zhHans('过滤')
    .zhHant('過濾')
    .ar(0)
    .he(0)
)

ts.append(T(tag="Parameter/option",
    context="FilterPosition",
    text='BTW')
    .es(0)
    .pt(0)
    .fr('ENTRE')
    .ja(0)
    .ko(0)
    .zhHans(0)
    .zhHant(0)
    .ar(0)
    .he(0)
)

ts.append(T(tag="Parameter/option",
    context="FilterPosition",
    text='POST')
    .es(1)
    .pt(0)
    .fr(1)
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
    .pt(0)
    .fr('PRÉ')
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
    .es(0)
    .pt(0)
    .fr(1)
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
    .es(0)
    .pt(0)
    .fr(1)
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
    .es(0)
    .pt(0)
    .fr('ENTRE')
    .ja(0)
    .ko(0)
    .zhHans(0)
    .zhHant(0)
    .ar(0)
    .he(0)
)

ts.append(T(tag="Parameter/option",
    context="OptoPosition",
    text='POST')
    .es(1)
    .pt(0)
    .fr(1)
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
    .pt(0)
    .fr('PRÉ')
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
    .es(0)
    .pt(0)
    .fr(1)
    .ja(0)
    .ko(0)
    .zhHans(0)
    .zhHant(0)
    .ar(0)
    .he(0)
)

ts.append(T(tag="Parameter/option",
    context="TubeTapeOrder",
    text='Tape -> Tube')
    .es('Cinta -> Bulbo')
    .pt(0)
    .fr(1)
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
    .pt(0)
    .fr(1)
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
    .pt(0)
    .fr(1)
    .ja('チューブ + テープ = チュープ')
    .ko('진공관 + 테이프 = 튜프')
    .zhHans('真空管 + 磁带 = 磁管')
    .zhHant('真空管 + 磁帶 = 磁管')
    .ar(0)
    .he(0)
)

