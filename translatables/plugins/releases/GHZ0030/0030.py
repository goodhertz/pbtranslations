from pbtranslations.translations import *


ts = TranslationSet()

ts.append(T(tag="Parameter/option",
    context="TempoSync",
    text='Manual')
    .es(1)
    .pt(1)
    .fr('Manuel')
    .it('Manuale')
    .ja('マニュアル')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('يدوي')
    .he('ידני')
)

ts.append(T(tag="Parameter/option",
    context="TempoSync",
    text='Synced')
    .es('Sincronizado')
    .pt('Sincronizado')
    .fr('Synchronisé')
    .it('Sincronizzato')
    .ja('シンクロ')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('متزامِنٌ')
    .he('סינק')
)

ts.append(T(tag="Parameter/option",
    context="AnalogMode",
    text='Cassette')
    .es('Casete')
    .pt('K7')
    .fr(1)
    .it('Audiocassetta')
    .ja('カセット')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('كاسيت')
    .he('טייפ קסטה')
)

ts.append(T(tag="Parameter/option",
    context="RandomMode",
    text='Speed')
    .es('Velocidad')
    .pt('Velocidade')
    .fr('Vitesse')
    .it('Frequenza')
    .ja('スピード')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('السرعة')
    .he('מהירות')
)

ts.append(T(tag="Parameter/option",
    context="RandomMode",
    text='Amount')
    .es('Intensidad')
    .pt('Intensidade')
    .fr('Intensité')
    .it('Intensità')
    .ja('量')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('الكمية')
    .he('מיקס')
)

ts.append(T(tag="Parameter/option",
    context="RandomMode",
    text='Shape')
    .es('Forma')
    .pt('Formato')
    .fr('Forme')
    .it('Forma')
    .ja('波形')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('الشكل')
    .he('צורה')
)

ts.append(T(tag="Parameter/option",
    context="RandomMode",
    text='Stereo Phase')
    .es('Fase estéreo')
    .pt('Fase Estéreo')
    .fr('Phase Stéréo')
    .it('Sfasamento Stereo')
    .ja('ステレオフェーズ')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('طور إستريو')
    .he('פאזה סטריאו')
)

ts.append(T(tag="Parameter/option",
    context="RandomMode",
    text='Phase Offset')
    .es('Desfase')
    .pt('Deslocamento de Fase')
    .fr('Déphasage')
    .it('Sfasamento')
    .ja('フェーズオフセット')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('فرق الطور')
    .he('אוף-סט פאזה')
)

ts.append(T(tag="Parameter/option",
    context="RandomMode",
    text='Amount + Speed')
    .es('Intensidad + Velocidad')
    .pt('Quantidade + Velocidade')
    .fr('Intensité + Vitesse')
    .it('Intensità + Frequenza')
    .ja('量＋スピード')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('الكمية+السرعة')
    .he('מיקס+מהירות')
)

ts.append(T(tag="Parameter/option",
    context="RandomMode",
    text='Wet Delay')
    .es('Retraso Wet')
    .pt('Atraso – Wet')
    .fr('Delay Wet')
    .it('Ritardo Effetto')
    .ja('ウェットディレイ')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('التأخير الزمني الرطب')
    .he('מיקס דיליי')
)

ts.append(T(tag="Tagline",
    text='Wow, flutter, tape')
    .es('Wow, flutter y sonido de cinta')
    .pt('Modulação, vibração e som de fita')
    .fr('Wow, flutter, bande magnétique')
    .it('Wow, flutter, nastro')
    .ja('ワウ・フラッター・レコード・テープ・サチュレーション')
    .ko('완벽한 테이프 시뮬레이터')
    .zhHans('哇声、抖晃、与类比盘带模拟')
    .zhHant('哇聲、抖晃、與類比盤帶模擬')
    .ar('تفاوت,خفقان,تشبع شريط كاسيت')
    .he('ואוו, פלאטר, טייפ')
)

ts.append(T(tag="ClumpLabel/text",
    text='RATE')
    .es('FRECUENCIA')
    .pt('FREQUÊNCIA')
    .fr('FRÉQUENCE')
    .it('CICLICITÀ')
    .ja('レート')
    .ko('비율')
    .zhHans('比率')
    .zhHant('比率')
    .ar('المعدل')
    .he('תדר')
)

ts.append(T(tag="ParamLabel/text",
    text='Speed')
    .es('Velocidad')
    .pt('Velocidade')
    .fr('Vitesse')
    .it('Frequenza')
    .ja('スピード')
    .ko('속도')
    .zhHans('速度')
    .zhHant('速度')
    .ar('السرعة')
    .he('מהירות')
)

ts.append(T(tag="ParamLabel/text",
    text='BPM')
    .es(1)
    .pt(1)
    .fr(1)
    .it(1)
    .ja(1)
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar(1)
    .he(1)
)

ts.append(T(tag="ParamLabel/text",
    text='BPM Sync')
    .es('Sincronizar BPM')
    .pt('Sincronizar BPM')
    .fr('Synchronisation BPM')
    .it('Sinc BPM')
    .ja('BPMシンク')
    .ko('BPM 싱크')
    .zhHans('BPM同步')
    .zhHant('BPM同步')
    .ar('BPMتزامن ال')
    .he('BPM סינק')
)

ts.append(T(tag="ClumpLabel/text",
    text='SHAPE')
    .es('FORMA')
    .pt('FORMATO')
    .fr('FORME')
    .it('FORMA')
    .ja('シェイプ')
    .ko('모양')
    .zhHans('形状')
    .zhHant('形狀')
    .ar('الشكل')
    .he('צורה')
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
    text='Multiplier')
    .es('Multiplicador')
    .pt('Multiplicar')
    .fr('Multiplicateur')
    .it('Moltiplicatore')
    .ja('倍率')
    .ko('배수')
    .zhHans('乘数')
    .zhHant('乘數')
    .ar('معامل الضرب')
    .he('מכפיל')
)

ts.append(T(tag="ParamLabel/text",
    text='Shape')
    .es('Forma')
    .pt('Formato')
    .fr('Forme')
    .it('Forma')
    .ja('波形')
    .ko('형태')
    .zhHans('形状')
    .zhHant('形狀')
    .ar('الشكل')
    .he('צורה')
)

ts.append(T(tag="ParamLabel/text",
    text='Dry / Wet')
    .es(1)
    .pt(1)
    .fr(1)
    .it('Orig / Effetto')
    .ja('ドライ / ウェット')
    .ko('원음 / 적용 후')
    .zhHans('干/湿声')
    .zhHant('乾/濕聲')
    .ar('جاف / رطب')
    .he('יבש/רטוב')
)

ts.append(T(tag="ClumpLabel/text",
    text='ANALOG')
    .es('ANÁLOGO')
    .pt('ANALÓGICO')
    .fr('ANALOGIQUE')
    .it('ANALOGICO')
    .ja('アナログ')
    .ko('아날로그')
    .zhHans('模拟')
    .zhHant('類比')
    .ar('أنالوج')
    .he('אנלוג')
)

ts.append(T(tag="ParamLabel/text",
    text='Color')
    .es('Coloración')
    .pt('Colorir')
    .fr('Coloration')
    .it('Colore')
    .ja('カラー')
    .ko('컬러')
    .zhHans('色彩')
    .zhHant('色彩')
    .ar('اللون')
    .he('צבע')
)

ts.append(T(tag="ParamLabel/text",
    text='Saturate')
    .es('Saturación')
    .pt('Saturar')
    .fr('Saturation')
    .it('Saturazione')
    .ja('サチュレート')
    .ko('세츄레이트')
    .zhHans('飽和')
    .zhHant('飽和')
    .ar('التشبع')
    .he('סאטורציה')
)

ts.append(T(tag="ParamLabel/text",
    text='Mode')
    .es('Modo')
    .pt('Modo')
    .fr(1)
    .it('Modalità')
    .ja('モード')
    .ko('모드')
    .zhHans('模式')
    .zhHant('模式')
    .ar('الوضع')
    .he('מצב')
)

ts.append(T(tag="ClumpLabel/text",
    text='TRIM')
    .es('AJUSTE')
    .pt('VOLUME')
    .fr('VOLUME')
    .it('VOL')
    .ja('トリム')
    .ko('트림')
    .zhHans('调整')
    .zhHant('調整')
    .ar('مُوازَنةٌ')
    .he('טרים')
)

ts.append(T(tag="ParamLabel/text",
    text='Input')
    .es('Entrada')
    .pt('Entrada')
    .fr('Entrée')
    .it('Ingresso')
    .ja('インプット')
    .ko('인풋')
    .zhHans('输入')
    .zhHant('輸入')
    .ar('إشارة الإدخال')
    .he('כניסה')
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

ts.append(T(tag="ClumpLabel/text",
    text='MISC')
    .es(1)
    .pt('OUTROS')
    .fr('AUTRES')
    .it('CONTR. MISTI')
    .ja('その他')
    .ko('기타')
    .zhHans('杂项')
    .zhHant('雜項')
    .ar('متنوعات')
    .he('שונות')
)

ts.append(T(tag="ParamLabel/text",
    text='Stereo Phase')
    .es('Fase estéreo')
    .pt('Fase – Estéreo')
    .fr('Phase Stéréo')
    .it('Sfasamento Stereo')
    .ja('ステレオフェーズ')
    .ko('스테레오 페이즈')
    .zhHans('立体声相位')
    .zhHant('立體聲相位')
    .ar('طور إستريو')
    .he('פאזה סטריאו')
)

ts.append(T(tag="ParamLabel/text",
    text='Phase Offset')
    .es('Desfase')
    .pt('Deslocamento de Fase')
    .fr('Déphasage')
    .it('Sfasamento')
    .ja('フェーズオフセット')
    .ko('페이즈 오프셋')
    .zhHans('相位偏移')
    .zhHant('相位偏移')
    .ar('فرق الطور')
    .he('אוף-סט פאזה')
)

ts.append(T(tag="ParamLabel/text",
    text='Wet Delay')
    .es('Retraso Wet')
    .pt('Atraso – Wet')
    .fr('Delay Wet')
    .it('Ritardo Effetto')
    .ja('ウェットディレイ')
    .ko('추가 딜레이')
    .zhHans('效果延迟')
    .zhHant('效果延遲')
    .ar('التأخير الزمني الرطب')
    .he('מיקס דיליי')
)

ts.append(T(tag="ParamLabel/text",
    text='Flutter Amount')
    .es('Intensidad de Flutter')
    .pt('Quantidade de Vibração')
    .fr('Intensité du Flutter')
    .it('Vibrazioni ad alta frequenza')
    .ja('フラッター量')
    .ko('플러터 정도')
    .zhHans('抖晃量')
    .zhHant('抖晃量')
    .ar('كمية  الخفقان')
    .he('מיקס פלאטר')
)

ts.append(T(tag="ParamLabel/text",
    text='Analog Noise Gain')
    .es('Ganancia de Ruido Análogo')
    .pt('Ganho do Ruído Analógico')
    .fr('Gain de Bruit Analogique')
    .it('Livello Rumore Analogico')
    .ja('アナログノイズゲイン')
    .ko('아날로그 노이즈 게인')
    .zhHans('模拟噪声增益')
    .zhHant('類比噪聲增益')
    .ar('ربح الضجيج')
    .he('רעש אנלוגי')
)

ts.append(T(tag="ClumpLabel/text",
    text='RANDOM')
    .es('ALEATORIO')
    .pt('ALEATÓRIO')
    .fr('ALÉATOIRE')
    .it('CASUALITÀ')
    .ja('ランダム')
    .ko('랜덤')
    .zhHans('随机')
    .zhHant('隨機')
    .ar('عشوائي')
    .he('אקראי')
)

ts.append(T(tag="ParamLabel/text",
    text='Mode')
    .es('Modo')
    .pt('Modo')
    .fr(1)
    .it('Modalità')
    .ja('モード')
    .ko('모드')
    .zhHans('模式')
    .zhHant('模式')
    .ar('الوضع')
    .he('מצב')
)

ts.append(T(tag="ParamLabel/text",
    text='Speed')
    .es('Velocidad')
    .pt('Velocidade')
    .fr('Vitesse')
    .it('Frequenza')
    .ja('スピード')
    .ko('속도')
    .zhHans('速度')
    .zhHant('速度')
    .ar('السرعة')
    .he('מהירות')
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
    text='Smoothing')
    .es('Alisado')
    .pt('Suavizar')
    .fr('Polissage')
    .it('Gradualità')
    .ja('スムージング')
    .ko('스무딩')
    .zhHans('平滑')
    .zhHant('平滑')
    .ar('الصقل')
    .he('החלקה')
)

ts.append(T(tag="ParamLabel/text",
    text='Seed')
    .es('Semilla aleatoria')
    .pt('Semente')
    .fr('Graine Aléatoire')
    .it('Seme Casualità')
    .ja('ランダムシード')
    .ko('랜덤 시드')
    .zhHans('随机种子')
    .zhHant('隨機種子')
    .ar('القيمة الإبتدائية')
    .he('סיד')
)

