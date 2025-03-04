from pbtranslations.translations import *


ts = TranslationSet()

ts.append(T(tag="Parameter/option",
    context="ProcessingMode",
    text='Stereo')
    .es('Estéreo')
    .pt('Estéreo')
    .fr('Stéréo')
    .it('Stereo')
    .ja('ステレオ')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('إستريو')
    .he('סטריאו')
)

ts.append(T(tag="Parameter/option",
    context="ProcessingMode",
    text='Left Only')
    .es('Solo Izquierda')
    .pt('Solo: Esquerda')
    .fr('Gauche Seulement')
    .it('Solo Sx')
    .ja('左のみ')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('اليسار فقط')
    .he('רק שמאל')
)

ts.append(T(tag="Parameter/option",
    context="ProcessingMode",
    text='Right Only')
    .es('Solo Derecha')
    .pt('Solo: Direita')
    .fr('Droite Seulement')
    .it('Solo Dx')
    .ja('右のみ')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('اليمين فقط')
    .he('רק ימין')
)

ts.append(T(tag="Parameter/option",
    context="ProcessingMode",
    text='Mid Only')
    .es('Solo Mid')
    .pt('Solo: Meio')
    .fr('Mid Seulement')
    .it('Solo Centro')
    .ja('ミッドのみ')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('الميد فقط')
    .he('רק אמצע')
)

ts.append(T(tag="Parameter/option",
    context="ProcessingMode",
    text='Side Only')
    .es('Solo Side')
    .pt('Solo: Lados')
    .fr('Side Seulement')
    .it('Solo Lati')
    .ja('サイドのみ')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('السايد فقط')
    .he('רק צד')
)

ts.append(T(tag="Tagline",
    text='Timeless EQ, taken back to the future')
    .es('Ecualización clásica, de vuelta al futuro')
    .pt('Equalização clássica, trazida de volta ao futuro')
    .fr('Égaliseur classique, de retour vers le futur')
    .it('Equalizzazione senza tempo, riportata al futuro')
    .ja('音の輪郭、枠線を微細にコントロール\u3000Mix and Mastering Equalizer')
    .ko('사운드의 윤곽을 만들어내는 직관적인 EQ')
    .zhHans('绝美永恒的音色，带你穿越未来')
    .zhHant('絕美永恆的音色，帶你穿越未來')
    .ar('موازن ترددات خالد، مبعوث إلَى المستقبل من جديد')
    .he('איקולייזר על-זמני שהגיע חזרה אל העתיד')
)

ts.append(T(tag="HUD/state",
    text='Stereo')
    .es('Estéreo')
    .pt('Estéreo')
    .fr('Stéréo')
    .it('Stereo')
    .ja('ステレオ')
    .ko('스테레오')
    .zhHans('立体声')
    .zhHant('立體聲')
    .ar('إستريو')
    .he('צדדים')
)

ts.append(T(tag="HUD/state",
    text='Left')
    .es('Izquierda')
    .pt('Esquerda')
    .fr('Gauche')
    .it('Sinistra')
    .ja('左のみ')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('اليسار')
    .he('שמאל')
)

ts.append(T(tag="HUD/state",
    text='Right')
    .es('Derecha')
    .pt('Direita')
    .fr('Droite')
    .it('Destra')
    .ja('右のみ')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('اليمين')
    .he('ימין')
)

ts.append(T(tag="HUD/state",
    text='Mid')
    .es(1)
    .pt('Meio')
    .fr(1)
    .it('Centro')
    .ja('ミッド')
    .ko('미드')
    .zhHans('中')
    .zhHant('中')
    .ar('الميد')
    .he('אמצע')
)

ts.append(T(tag="HUD/state",
    text='Side')
    .es(1)
    .pt('Lados')
    .fr(1)
    .it('Lati')
    .ja('サイド')
    .ko('사이드')
    .zhHans('侧')
    .zhHant('側')
    .ar('السايد')
    .he('צד')
)

ts.append(T(tag="ClumpLabel/text",
    text='BASS')
    .es('GRAVE')
    .pt('GRAVE')
    .fr('GRAVES')
    .it('BASSE')
    .ja('低域')
    .ko('저역 컨트롤')
    .zhHans('低频')
    .zhHant('低頻')
    .ar('باَس')
    .he('בס')
)

ts.append(T(tag="ParamLabel/text",
    text='Frequency')
    .es('Frecuencia')
    .pt('Frequência')
    .fr('Fréquence')
    .it('Frequenza')
    .ja('基準周波数')
    .ko('기준 프리퀀시')
    .zhHans('频率')
    .zhHant('頻率')
    .ar('التردد')
    .he('תדר')
)

ts.append(T(tag="ParamLabel/text",
    text='Slope')
    .es('Pendiente')
    .pt('Declive')
    .fr('Ordre')
    .it('Pendenza')
    .ja('スロープ')
    .ko('기울기')
    .zhHans('坡度')
    .zhHant('坡度')
    .ar('الميل')
    .he('מדרון')
)

ts.append(T(tag="ParamLabel/text",
    text='Gain')
    .es('Ganancia')
    .pt('Ganho')
    .fr(1)
    .it('Guadagno')
    .ja('ゲイン')
    .ko('게인')
    .zhHans('增益')
    .zhHant('增益')
    .ar('الربح')
    .he('גיין')
)

ts.append(T(tag="ClumpLabel/text",
    text='TREBLE')
    .es('AGUDO')
    .pt('AGUDO')
    .fr('AIGUS')
    .it('ALTE')
    .ja('高域')
    .ko('고역 컨트롤')
    .zhHans('高频')
    .zhHant('高頻')
    .ar('الصوت العالي')
    .he('טרבל')
)

ts.append(T(tag="ParamLabel/text",
    text='Gain')
    .es('Ganancia')
    .pt('Ganho')
    .fr(1)
    .it('Guadagno')
    .ja('ゲイン')
    .ko('게인')
    .zhHans('增益')
    .zhHant('增益')
    .ar('الربح')
    .he('גיין')
)

ts.append(T(tag="ParamLabel/text",
    text='Frequency')
    .es('Frecuencia')
    .pt('Frequência')
    .fr('Fréquence')
    .it('Frequenza')
    .ja('基準周波数')
    .ko('기준 프리퀀시')
    .zhHans('频率')
    .zhHant('頻率')
    .ar('التردد')
    .he('תדר')
)

ts.append(T(tag="ParamLabel/text",
    text='Slope')
    .es('Pendiente')
    .pt('Declive')
    .fr('Ordre')
    .it('Pendenza')
    .ja('スロープ')
    .ko('기울기')
    .zhHans('坡度')
    .zhHant('坡度')
    .ar('الميل')
    .he('מדרון')
)

ts.append(T(tag="ClumpLabel/text",
    text='LOW CUT')
    .es('PASO ALTOS')
    .pt('CORTE GRAVE')
    .fr('COUPE-BAS')
    .it('PASSA ALTE')
    .ja('ローカット')
    .ko('로우컷 필터')
    .zhHans('低切')
    .zhHant('低切')
    .ar('تمرير عال')
    .he('לו-קאט')
)

ts.append(T(tag="ParamLabel/text",
    text='Frequency')
    .es('Frecuencia')
    .pt('Frequência')
    .fr('Fréquence')
    .it('Frequenza')
    .ja('基準周波数')
    .ko('기준 프리퀀시')
    .zhHans('频率')
    .zhHant('頻率')
    .ar('التردد')
    .he('תדר')
)

ts.append(T(tag="ParamLabel/text",
    text='Slope')
    .es('Pendiente')
    .pt('Declive')
    .fr('Ordre')
    .it('Pendenza')
    .ja('スロープ')
    .ko('기울기')
    .zhHans('坡度')
    .zhHant('坡度')
    .ar('الميل')
    .he('מדרון')
)

ts.append(T(tag="ClumpLabel/text",
    text='MASTER')
    .es('MÁSTER')
    .pt(1)
    .fr(1)
    .it(1)
    .ja('マスター')
    .ko('마스터')
    .zhHans('主控')
    .zhHant('主控')
    .ar('الماستر')
    .he('מאסטר')
)

ts.append(T(tag="ParamLabel/text",
    text='Air')
    .es('Aire')
    .pt('Ar')
    .fr(1)
    .it('Aria')
    .ja('エア')
    .ko('에어')
    .zhHans('空气感')
    .zhHant('空氣感')
    .ar('هواء')
    .he('אוויר')
)

ts.append(T(tag="ParamLabel/text",
    text='Mix')
    .es('Mezcla')
    .pt(1)
    .fr(1)
    .it('Miscela')
    .ja('ミックス')
    .ko('믹스')
    .zhHans('混合')
    .zhHant('混合')
    .ar('الميكس')
    .he('מיקס')
)

ts.append(T(tag="ParamLabel/text",
    text='Gain')
    .es('Ganancia')
    .pt('Ganho')
    .fr(1)
    .it('Guadagno')
    .ja('ゲイン')
    .ko('게인')
    .zhHans('增益')
    .zhHant('增益')
    .ar('الربح')
    .he('גיין')
)

ts.append(T(tag="ClumpLabel/text",
    text='HIGH CUT')
    .es('PASO BAJOS')
    .pt('CORTE AGUDO')
    .fr('COUPE-HAUT')
    .it('PASSA BASSE')
    .ja('ハイカット')
    .ko('하이컷 필터')
    .zhHans('高切')
    .zhHant('高切')
    .ar('تمرير منخفض')
    .he('היי-קאט')
)

ts.append(T(tag="ParamLabel/text",
    text='Frequency')
    .es('Frecuencia')
    .pt('Frequência')
    .fr('Fréquence')
    .it('Frequenza')
    .ja('基準周波数')
    .ko('기준 프리퀀시')
    .zhHans('频率')
    .zhHant('頻率')
    .ar('التردد')
    .he('תדר')
)

ts.append(T(tag="ParamLabel/text",
    text='Slope')
    .es('Pendiente')
    .pt('Declive')
    .fr('Ordre')
    .it('Pendenza')
    .ja('スロープ')
    .ko('기울기')
    .zhHans('坡度')
    .zhHant('坡度')
    .ar('الميل')
    .he('מדרון')
)

ts.append(T(tag="ClumpLabel/text",
    text='MODE')
    .es('MODO')
    .pt('MODO')
    .fr(1)
    .it('TIPO')
    .ja('モード')
    .ko('세부 조절')
    .zhHans('高级模式')
    .zhHant('進階模式')
    .ar('الوضع')
    .he('מצב')
)

ts.append(T(tag="ParamLabel/text",
    text='Processing Mode')
    .es('Modo de Procesamiento')
    .pt('Modo de Processamento')
    .fr('Mode de Traitement')
    .it('Configurazione Ingressi')
    .ja('動作モード')
    .ko('프로세스 모드')
    .zhHans('处理模式')
    .zhHant('處理模式')
    .ar('وضع المعالجة')
    .he('מצב')
)

ts.append(T(tag="ClumpLabel/text",
    text='EQ STYLE')
    .es('ESTILO DE EQ')
    .pt('ESTILO DE EQ')
    .fr('STYLE DE EQ')
    .it('STILE EQ')
    .ja('EQスタイル')
    .ko('EQ 스타일')
    .zhHans('EQ样式')
    .zhHant('EQ類型')
    .ar('EQ اسلوب ال')
    .he('אי-קיו סטייל')
)

ts.append(T(tag="ParamLabel/text",
    text='Linear Phase')
    .es('Fase Linear')
    .pt('Fase Linear')
    .fr('Phase Linéaire')
    .it('Fase Lineare')
    .ja('リニアフェーズ')
    .ko('리니어 페이즈')
    .zhHans('线性相位')
    .zhHant('線性相位')
    .ar('طورُخطي')
    .he('פאזה לינארית')
)

