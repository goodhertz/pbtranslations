from pbtranslations.translations import *


ts = TranslationSet()

ts.append(T(tag="Parameter/option",
    text='D\nO\nT')
    # Referring to note length; set vertically in a very tight spot
    .es('P\nU\nN\nT\nO')
    .pt('P\nO\nN\nT\nO')
    .fr('P\nO\nI\nN\nT\nÉ')
    .it('P\nU\nN\nT\nO')
    .ja('付\n点')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('نقطة')
    )

ts.append(T(tag="Parameter/option",
    text='DOT')
    # Referring to note length
    .es('PUNTO')
    .pt('PONTO')
    .fr('POINTÉ')
    .it('PUNTO')
    .ja('付点')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('نقطة')
    )

ts.append(T(tag="Parameter/option",
    text='Ext.')
    # Short for `External`
    .es(1)
    .pt(1)
    .fr(1)
    .it('Est.')
    .ja('外部')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar(1)
    )

ts.append(T(tag="Parameter/option",
    text='Int.')
    # Short for `Internal`
    .es(1)
    .pt(1)
    .fr(1)
    .it(1)
    .ja('内部')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar(1)
    )

ts.append(T(tag="Parameter/option",
    text='N\nO\nT\nE')
    # Referring to note length; set vertically in a very tight spot
    .es('N\nO\nT\nA')
    .pt('N\nO\nT\nA')
    .fr(1)
    .it('N\nO\nT\nA')
    .ja('音\n符')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('النوتة')
    )

ts.append(T(tag="Parameter/option",
    text='NOTE')
    # Referring to note length
    .es('NOTA')
    .pt('NOTA')
    .fr(1)
    .it('NOTA')
    .ja('音符')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('النوتة')
    )

ts.append(T(tag="Parameter/option",
    text='Off')
    # Default for booleans
    .es(1)
    .pt('Des.')
    .fr(1)
    .it(1)
    .ja('オフ')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar(1)
    )

ts.append(T(tag="Parameter/option",
    text='On')
    # Default for booleans
    .es(1)
    .pt('Lig.')
    .fr(1)
    .it(1)
    .ja('オン')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar(1)
    )

ts.append(T(tag="Parameter/option",
    text='T\nI\nM\nE')
    # Referring to note length; set vertically in a very tight spot
    .es('T\nI\nE\nM\nP\nO')
    .pt('T\nE\nM\nP\nO')
    .fr('T\nE\nM\nP\nS')
    .it('T\nE\nM\nP\nO')
    .ja('時\n間')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('الوقت')
    )

ts.append(T(tag="Parameter/option",
    text='T\nR\nI\nP')
    # Referring to note length; set vertically in a very tight spot
    .es('T\nR\nS\nI\nL\nL\nO')
    .pt('T\nE\nR\nC\nI\nN\nA')
    .fr('T\nR\nI\nO\nL\nE\nT')
    .it('T\nE\nR\nZ')
    .ja('三\n連\n符')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('المسيرة')
    )

ts.append(T(tag="Parameter/option",
    text='TIME')
    # Referring to note length
    .es('TIEMPO')
    .pt('TEMPO')
    .fr('TEMPS')
    .it('TEMPO')
    .ja('時間')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('الوقت')
    )

ts.append(T(tag="Parameter/option",
    text='TRIP')
    # Referring to note length
    .es('TRSILLO')
    .pt('TERCINA')
    .fr('TRIOLET')
    .it('TERZINA')
    .ja('三連符')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('المسيرة')
    )

