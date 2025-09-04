from pbtranslations.translations import *


ts = TranslationSet()

ts.append(T(tag="Tagline",
    text='Easy Mid/Side Conversion')
    .es('Conversión sencilla a Mid/Side')
    .pt('Conversão simples Mid/Side')
    .fr('Conversion Mid/Side simplifiée')
    .it('Conversione Centro/Lati semplificata')
    .ja('Mid/Side イージーコンヴァージョン')
    .ko('심플한 미드/사이드 컨트롤')
    .zhHans('超简易中侧处理转换器')
    .zhHant('超簡易中側處理轉換器')
    .ar('تحويل ميد/سايد بسُهُولة')
    )

ts.append(T(tag="ClumpLabel/text",
    text='INPUT')
    .es('ENTRADA')
    .pt('ENTRADA')
    .fr('ENTRÉE')
    .it('INGRESSO')
    .ja('インプット')
    .ko('인풋')
    .zhHans('输入')
    .zhHant('輸入')
    .ar('إشارة الإدخال')
    )

ts.append(T(tag="ClumpLabel/text",
    text='OUTPUT')
    .es('SALIDA')
    .pt('SAÍDA')
    .fr('SORTIE')
    .it('USCITA')
    .ja('アウトプット')
    .ko('아웃풋')
    .zhHans('输出')
    .zhHant('輸出')
    .ar('إشارة الإخراج')
    )

ts.append(T(tag="ClumpLabel/text",
    text='FLIP')
    .es('INVERTIR')
    .pt('INVERTER')
    .fr('INVERSER')
    .it('INVERSIONE')
    .ja('入れ替え')
    .ko('뒤집기')
    .zhHans('翻转')
    .zhHant('翻轉')
    .ar('عَكّس')
    )

ts.append(T(tag="ClumpLabel/text",
    text='MID')
    .es(1)
    .pt(1)
    .fr(1)
    .it('CENTRO')
    .ja('ミッド')
    .ko('미드')
    .zhHans('中')
    .zhHant('中')
    .ar('ميد')
    )

ts.append(T(tag="ClumpLabel/text",
    text='SIDE')
    .es(1)
    .pt(1)
    .fr(1)
    .it('LATI')
    .ja('サイド')
    .ko('사이드')
    .zhHans('侧')
    .zhHant('側')
    .ar('سايد')
    )

