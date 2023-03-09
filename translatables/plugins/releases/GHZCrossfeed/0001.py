from pbt.translations import *


ts = TranslationSet()

ts.append(T(tag="ClumpLabel/text",
    text='CROSSFEED')
    .es(1)
    .pt(1)
    .fr(1)
    .it('DIAFONIA')
    .ja('クロスフィード')
    .ko('크로스피드')
    .zhHans('互馈效果')
    .zhHant('互饋效果')
    .ar('الكروسفِيد')
    .he('קרוס-פיד')
)

ts.append(T(tag="ClumpLabel/text",
    text='EQUALIZATION')
    .es('ECUALIZACIÓN')
    .pt('EQUALIZAÇÃO')
    .fr('ÉGALISATION')
    .it('EQUALIZZAZIONE')
    .ja('イコライゼーション')
    .ko('EQ')
    .zhHans('频率均衡器')
    .zhHant('頻率均衡器')
    .ar('موازنة الترددات')
    .he('איקווליזציה')
)

ts.append(T(tag="HUD/state",
    text='Safe')
    .es('Seguro')
    .pt('Segurança')
    .fr('Précaution')
    .it('Protezione')
    .ja('セーフ')
    .ko('세이프')
    .zhHans('安全')
    .zhHant('安全')
    .ar('الحذَرِ')
    .he('סייף')
)

ts.append(T(tag="ParamLabel/text",
    text='Amount')
    .es('Intensidad')
    .pt('Quantidade')
    .fr('Intensité')
    .it('Quantità')
    .ja('量')
    .ko('정도')
    .zhHans('量')
    .zhHant('量')
    .ar('الكمية')
    .he('מיקס')
)

ts.append(T(tag="ParamLabel/text",
    text='Angle')
    .es('Ángulo')
    .pt('Ângulo')
    .fr(1)
    .it('Larghezza')
    .ja('角度')
    .ko('각도')
    .zhHans('角度')
    .zhHant('角度')
    .ar('الزاوية')
    .he('זווית')
)

ts.append(T(tag="ParamLabel/text",
    text='Bass')
    .es('Graves')
    .pt('Grave')
    .fr('Graves')
    .it('Basse')
    .ja('低域')
    .ko('저역대')
    .zhHans('低频')
    .zhHant('低頻')
    .ar('الباس')
    .he('בס')
)

ts.append(T(tag="ParamLabel/text",
    text='Bass Frequency')
    .es('Frecuencia de Graves')
    .pt('Frequência – Grave')
    .fr('Basses Fréquences')
    .it('Crossover Basse Frequenze')
    .ja('低域周波数')
    .ko('저역대 필터 기준')
    .zhHans('低频')
    .zhHant('低頻')
    .ar('تردد الباس')
    .he('תדר בס')
)

ts.append(T(tag="ParamLabel/text",
    text='Compensation')
    .es('Compensación')
    .pt('Compensação')
    .fr(1)
    .it('Loudness')
    .ja('補償')
    .ko('보상')
    .zhHans('补偿')
    .zhHant('補償')
    .ar('التعويض')
    .he('פיצוי')
)

ts.append(T(tag="ParamLabel/text",
    text='Crossfeed Realism')
    .es('Realismo de Crossfeed')
    .pt('Realismo do Crossfeed')
    .fr('Qualité du Crossfeed')
    .it('Realismo Diafonia')
    .ja('クロスフィードリアリズム')
    .ko('크로스피드 리얼리즘')
    .zhHans('互馈真实度')
    .zhHant('互饋真實度')
    .ar('واقِعيةُ الكروسفِيد')
    .he('קרוס-פיד ריאליזם')
)

ts.append(T(tag="ParamLabel/text",
    text='Dim Level')
    .es('Nivel de Atenuación')
    .pt('Nível de Atenuação')
    .fr("Niveau d'Atténuation")
    .it('Livello Attenuato')
    .ja('ディムレベル')
    .ko('딤 레벨')
    .zhHans('衰减程度')
    .zhHant('衰減程度')
    .ar('مستوَى التخفيف')
    .he('דים')
)

ts.append(T(tag="ParamLabel/text",
    text='Dither')
    .es('Tramado')
    .pt(1)
    .fr(1)
    .it(1)
    .ja('ディザー')
    .ko('디더')
    .zhHans('抖动')
    .zhHant('抖動')
    .ar('الديثر')
    .he('דיט׳ר')
)

ts.append(T(tag="ParamLabel/text",
    text='L/R Balance')
    .es('Balance L/R')
    .pt('Equilíbrio L/R')
    .fr('Équilibre L/R')
    .it('Equilibrio S/D')
    .ja('左/右バランス')
    .ko('좌/우 밸런스')
    .zhHans('左/右平衡')
    .zhHant('左/右平衡')
    .ar('L/R توازن')
    .he('בלאנס ימין/שמאל')
)

ts.append(T(tag="ParamLabel/text",
    text='Output')
    .es('Salida')
    .pt('Saída')
    .fr('Sortie')
    .it('Uscita')
    .ja('アウトプット')
    .ko('아웃풋')
    .zhHans('输出')
    .zhHant('輸出')
    .ar('إشارة الإخراج')
    .he('יציאה')
)

ts.append(T(tag="ParamLabel/text",
    text='Safe Gain')
    .es('Ganancia Anticlipping')
    .pt('Ganho de Segurança')
    .fr('Gain de Précaution')
    .it('Volume di Protezione')
    .ja('セーフゲイン')
    .ko('세이프 게인')
    .zhHans('安全增益')
    .zhHant('安全增益')
    .ar('ربحُ الحذَرِ')
    .he('גיין סייף')
)

ts.append(T(tag="ParamLabel/text",
    text='Soft Start Time')
    .es('Fundido de Entrada')
    .pt('Tempo de Fade In')
    .fr('Temps de Fondu')
    .it('Fade In Interferenza')
    .ja('ソフトスタート時間')
    .ko('페이드인 타임')
    .zhHans('淡入时间')
    .zhHant('淡入時間')
    .ar('وَقتُ التضاؤُل')
    .he('פייד-אין')
)

ts.append(T(tag="ParamLabel/text",
    text='Treble')
    .es('Agudos')
    .pt('Agudo')
    .fr('Aigus')
    .it('Alte')
    .ja('高域')
    .ko('고역대')
    .zhHans('高频')
    .zhHant('高頻')
    .ar('الصوتُ العالي')
    .he('טרבל')
)

ts.append(T(tag="ParamLabel/text",
    text='Treble Frequency')
    .es('Frecuencia de Agudos')
    .pt('Frequência – Agudo')
    .fr('Hautes Fréquences')
    .it('Crossover Alte Frequenze')
    .ja('高域周波数')
    .ko('고역대 필터 기준')
    .zhHans('高频')
    .zhHant('高頻')
    .ar('تردد الصوتُ العالي')
    .he('תדר טרבל')
)

ts.append(T(tag="Parameter/option",
    text='Dim')
    .es('Atenuación')
    .pt('Atenuar')
    .fr('Atténuation')
    .it('Attenuazione')
    .ja('ディム')
    .ko('딤')
    .zhHans('衰减')
    .zhHant('衰減')
    .ar('التخفيف')
    .he('דים')
)

ts.append(T(tag="Parameter/option",
    text='Flip L/R')
    .es('Invertir L/R')
    .pt('Inverter L/R')
    .fr('Inverser L/R')
    .it('Inversione D/S')
    .ja('左/右入れ替え')
    .ko('좌/우 뒤집기')
    .zhHans('左/右翻转')
    .zhHant('左/右翻轉')
    .ar('L/R عَكّس')
    .he('היפוך ימין/שמאל')
)

ts.append(T(tag="Parameter/option",
    text='Mono')
    .es(1)
    .pt(1)
    .fr(1)
    .it(1)
    .ja('モノ')
    .ko('모노')
    .zhHans('单声道')
    .zhHant('单声道')
    .ar('مونو')
    .he('מונו')
)

ts.append(T(tag="Parameter/option",
    text='Polarity')
    .es('Polaridad')
    .pt('Polaridade')
    .fr('Polarité')
    .it('Polarità')
    .ja('極')
    .ko('극성')
    .zhHans('极性')
    .zhHant('極性')
    .ar('القطبية')
    .he('קוטביות')
)

ts.append(T(tag="Parameter/option",
    context="CrossfeedRealism",
    text='Hyperrealistic')
    .es('Hyperrealista')
    .pt('Mais Realista')
    .fr('Très Réaliste')
    .it('Iperrealistico')
    .ja('超リアル')
    .ko('하이퍼리얼')
    .zhHans('超现实')
    .zhHant('超現實')
    .ar('اكثرُ واقعيةٌ')
    .he('הייפר-ריאליסטי')
)

ts.append(T(tag="Parameter/option",
    context="CrossfeedRealism",
    text='Realistic')
    .es('Realista')
    .pt('Realista')
    .fr('Réaliste')
    .it('Realistico')
    .ja('リアル')
    .ko('리얼')
    .zhHans('真实')
    .zhHant('真實')
    .ar('واقعي')
    .he('ריאליסטי')
)

ts.append(T(tag="Parameter/option",
    context="CrossfeedRealism",
    text='Standard')
    .es('Estándar')
    .pt('Padrão')
    .fr('Normale')
    .it(1)
    .ja('普通')
    .ko('스탠다드')
    .zhHans('标准')
    .zhHant('標準')
    .ar('عادي')
    .he('סטנדרט')
)

ts.append(T(tag="Tagline",
    text='Conjure speakers from your headphones')
    .es('Conjura altavoces desde tus audífonos')
    .pt('Transforme seu fone em um par de caixas')
    .fr('Transformez votre casque en enceintes de monitoring')
    .it('Fa apparire altoparlanti dalle tue cuffie')
    .ja('ヘッドフォンにスピーカーをインストール')
    .ko('헤드폰에 스피커를 가져오는 마술')
    .zhHans('用耳机营造出音箱般的音响效果')
    .zhHant('用耳機營造出喇叭般的音響效果')
    .ar('حول سماعات الرأس إلى مكبرات صوت')
    .he(1)
)
