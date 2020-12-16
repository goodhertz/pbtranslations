(DATPenSet()
    .append(DATPen()
        .tag("parameter-edges")
        .moveTo((0.0, 768.0))
        .lineTo((384.0, 768.0))
        .endPath()
        .moveTo((192.0, 396.0))
        .lineTo((192.0, 768.0))
        .endPath()
        .moveTo((192.0, 548.0))
        .lineTo((384.0, 548.0))
        .endPath()
        .moveTo((192.0, 396.0))
        .lineTo((192.0, 768.0))
        .endPath()
        .moveTo((192.0, 472.0))
        .lineTo((384.0, 472.0))
        .endPath()
        .moveTo((192.0, 396.0))
        .lineTo((192.0, 768.0))
        .endPath()
        .moveTo((384.0, 768.0))
        .lineTo((768.0, 768.0))
        .endPath()
        .moveTo((384.0, 548.0))
        .lineTo((576.0, 548.0))
        .endPath()
        .moveTo((576.0, 548.0))
        .lineTo((576.0, 768.0))
        .endPath()
        .moveTo((384.0, 472.0))
        .lineTo((576.0, 472.0))
        .endPath()
        .moveTo((576.0, 472.0))
        .lineTo((576.0, 548.0))
        .endPath()
        .moveTo((576.0, 396.0))
        .lineTo((576.0, 472.0))
        .endPath()
        .moveTo((484.0, 260.0))
        .lineTo((484.0, 396.0))
        .endPath()
        .moveTo((200.0, 60.0))
        .lineTo((568.0, 60.0))
        .endPath()
        .moveTo((568.0, 60.0))
        .lineTo((568.0, 188.0))
        .endPath()
        .moveTo((568.0, 60.0))
        .lineTo((568.0, 188.0))
        .endPath()
        .moveTo((0.0, 188.0))
        .lineTo((768.0, 188.0))
        .endPath()
        .moveTo((200.0, 60.0))
        .lineTo((200.0, 188.0))
        .endPath()
        .moveTo((568.0, 60.0))
        .lineTo((568.0, 188.0))
        .endPath()
        .moveTo((1340.0, 688.0))
        .lineTo((1340.0, 840.0))
        .endPath()
        .moveTo((1340.0, 688.0))
        .lineTo((1340.0, 840.0))
        .endPath()
        .moveTo((1116.0, 688.0))
        .lineTo((1116.0, 840.0))
        .endPath()
        .moveTo((1340.0, 688.0))
        .lineTo((1340.0, 840.0))
        .endPath()
        .moveTo((892.0, 616.0))
        .lineTo((1228.0, 616.0))
        .endPath()
        .moveTo((1228.0, 616.0))
        .lineTo((1564.0, 616.0))
        .endPath()
        .moveTo((892.0, 396.0))
        .lineTo((1228.0, 396.0))
        .endPath()
        .moveTo((892.0, 236.0))
        .lineTo((1228.0, 236.0))
        .endPath()
        .moveTo((1120.0, 60.0))
        .lineTo((1120.0, 236.0))
        .endPath()
        .moveTo((1228.0, 396.0))
        .lineTo((1564.0, 396.0))
        .endPath()
        .moveTo((1228.0, 236.0))
        .lineTo((1564.0, 236.0))
        .endPath()
        .moveTo((1456.0, 60.0))
        .lineTo((1456.0, 236.0))
        .endPath()
        .moveTo((892.0, 468.0))
        .lineTo((1564.0, 468.0))
        .endPath()
        .f(bw(0.0, 0.0))
        .s(bw(0.5))
        .sw(3))
    .append(DATPen()
        .tag("clump-edges")
        .moveTo((0, 60))
        .lineTo((768, 60))
        .endPath()
        .moveTo((384.0, 396.0))
        .lineTo((384.0, 840.0))
        .endPath()
        .moveTo((0.0, 396.0))
        .lineTo((768.0, 396.0))
        .endPath()
        .moveTo((0.0, 260.0))
        .lineTo((768.0, 260.0))
        .endPath()
        .moveTo((892.0, 688.0))
        .lineTo((1564.0, 688.0))
        .endPath()
        .moveTo((1228.0, 468.0))
        .lineTo((1228.0, 688.0))
        .endPath()
        .moveTo((1228.0, 60.0))
        .lineTo((1228.0, 468.0))
        .endPath()
        .f(bw(0.0, 0.0))
        .s(bw(0.25))
        .sw(5))
    .append(DATPen()
        .tag("sidebar")
        .moveTo((768, 0))
        .lineTo((892, 0))
        .lineTo((892, 840))
        .lineTo((768, 840))
        .closePath()
        .f(bw(0.5)))
    .append(DATPen()
        .tag("advbar")
        .moveTo((892, 0))
        .lineTo((1564, 0))
        .lineTo((1564, 60))
        .lineTo((892, 60))
        .closePath()
        .f(bw(0.75)))
    .append(DATPenSet()
        .tag("labels")
        .append(DATPen()
            .add_data({'ts': ['ParamLabel/text', 'Stereo Width', None]})
            .moveTo((6.0, 272.0))
            .lineTo((478.0, 272.0))
            .lineTo((478.0, 336.0))
            .lineTo((6.0, 336.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ParamLabel/text', 'Width Mode', None]})
            .moveTo((490.0, 272.0))
            .lineTo((762.0, 272.0))
            .lineTo((762.0, 336.0))
            .lineTo((490.0, 336.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ParamLabel/text', 'Strength', None]})
            .moveTo((6, 72))
            .lineTo((194.0, 72.0))
            .lineTo((194.0, 136.0))
            .lineTo((6, 136))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ParamLabel/text', 'Frequency', None]})
            .moveTo((206.0, 72.0))
            .lineTo((562.0, 72.0))
            .lineTo((562.0, 136.0))
            .lineTo((206.0, 136.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ParamLabel/text', 'Bass Makeup', None]})
            .moveTo((574.0, 72.0))
            .lineTo((762.0, 72.0))
            .lineTo((762.0, 136.0))
            .lineTo((574.0, 136.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ParamLabel/text', 'Input Mode', None]})
            .moveTo((898.0, 716.0))
            .lineTo((1110.0, 716.0))
            .lineTo((1110.0, 780.0))
            .lineTo((898.0, 780.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ParamLabel/text', 'Output Mode', None]})
            .moveTo((1122.0, 716.0))
            .lineTo((1334.0, 716.0))
            .lineTo((1334.0, 780.0))
            .lineTo((1122.0, 780.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ParamLabel/text', 'Flip L/R', None]})
            .moveTo((1346.0, 716.0))
            .lineTo((1558.0, 716.0))
            .lineTo((1558.0, 780.0))
            .lineTo((1346.0, 780.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ParamLabel/text', 'Range', None]})
            .moveTo((898.0, 248.0))
            .lineTo((1222.0, 248.0))
            .lineTo((1222.0, 312.0))
            .lineTo((898.0, 312.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ParamLabel/text', 'Loudness\nMode', None]})
            .moveTo((898, 72))
            .lineTo((1114.0, 72.0))
            .lineTo((1114.0, 136.0))
            .lineTo((898, 136))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ParamLabel/text', 'Range', None]})
            .moveTo((1234.0, 248.0))
            .lineTo((1558.0, 248.0))
            .lineTo((1558.0, 312.0))
            .lineTo((1234.0, 312.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ParamLabel/text', 'Loudness\nMode', None]})
            .moveTo((1234.0, 72.0))
            .lineTo((1450.0, 72.0))
            .lineTo((1450.0, 136.0))
            .lineTo((1234.0, 136.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'us': 'IN'})
            .moveTo((790.0, 550.0))
            .lineTo((822.0, 550.0))
            .lineTo((822.0, 586.0))
            .lineTo((790.0, 586.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'us': 'OUT'})
            .moveTo((790, 514))
            .lineTo((822.0, 514.0))
            .lineTo((822.0, 550.0))
            .lineTo((790.0, 550.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ClumpLabel/text', 'MID', None]})
            .moveTo((14.0, 768.0))
            .lineTo((370.0, 768.0))
            .lineTo((370.0, 840.0))
            .lineTo((14.0, 840.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ClumpLabel/text', 'SIDE', None]})
            .moveTo((398.0, 768.0))
            .lineTo((754.0, 768.0))
            .lineTo((754.0, 840.0))
            .lineTo((398.0, 840.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ClumpLabel/text', 'MONO BELOW', None]})
            .moveTo((14.0, 188.0))
            .lineTo((754.0, 188.0))
            .lineTo((754.0, 260.0))
            .lineTo((14.0, 260.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ClumpLabel/text', 'MID PAN', None]})
            .moveTo((906.0, 616.0))
            .lineTo((1154.0, 616.0))
            .lineTo((1154.0, 688.0))
            .lineTo((906.0, 688.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ClumpLabel/text', 'SIDE PAN', None]})
            .moveTo((1302.0, 616.0))
            .lineTo((1550.0, 616.0))
            .lineTo((1550.0, 688.0))
            .lineTo((1302.0, 688.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ClumpLabel/text', 'MID TILT', None]})
            .moveTo((906.0, 396.0))
            .lineTo((1166.0, 396.0))
            .lineTo((1166.0, 468.0))
            .lineTo((906.0, 468.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ClumpLabel/text', 'SIDE TILT', None]})
            .moveTo((1290.0, 396.0))
            .lineTo((1550.0, 396.0))
            .lineTo((1550.0, 468.0))
            .lineTo((1290.0, 468.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPenSet()
            .add_data({'initialValue': 0, 'shows_all_strings': False})
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', 'SOLO', None], 'value': 0})
                .moveTo((198.0, 478.0))
                .lineTo((378.0, 478.0))
                .lineTo((378.0, 542.0))
                .lineTo((198.0, 542.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', 'SOLO', None], 'value': 1})
                .moveTo((198.0, 478.0))
                .lineTo((378.0, 478.0))
                .lineTo((378.0, 542.0))
                .lineTo((198.0, 542.0))
                .closePath()
                .f(bw(0.0, 0.05))))
        .append(DATPenSet()
            .add_data({'initialValue': 0, 'shows_all_strings': False})
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', 'MUTE', None], 'value': 0})
                .moveTo((198.0, 402.0))
                .lineTo((378.0, 402.0))
                .lineTo((378.0, 466.0))
                .lineTo((198.0, 466.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', 'MUTE', None], 'value': 1})
                .moveTo((198.0, 402.0))
                .lineTo((378.0, 402.0))
                .lineTo((378.0, 466.0))
                .lineTo((198.0, 466.0))
                .closePath()
                .f(bw(0.0, 0.05))))
        .append(DATPenSet()
            .add_data({'initialValue': 0, 'shows_all_strings': False})
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', 'SOLO', None], 'value': 0})
                .moveTo((390.0, 478.0))
                .lineTo((570.0, 478.0))
                .lineTo((570.0, 542.0))
                .lineTo((390.0, 542.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', 'SOLO', None], 'value': 1})
                .moveTo((390.0, 478.0))
                .lineTo((570.0, 478.0))
                .lineTo((570.0, 542.0))
                .lineTo((390.0, 542.0))
                .closePath()
                .f(bw(0.0, 0.05))))
        .append(DATPenSet()
            .add_data({'initialValue': 0, 'shows_all_strings': False})
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', 'MUTE', None], 'value': 0})
                .moveTo((390.0, 402.0))
                .lineTo((570.0, 402.0))
                .lineTo((570.0, 466.0))
                .lineTo((390.0, 466.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', 'MUTE', None], 'value': 1})
                .moveTo((390.0, 402.0))
                .lineTo((570.0, 402.0))
                .lineTo((570.0, 466.0))
                .lineTo((390.0, 466.0))
                .closePath()
                .f(bw(0.0, 0.05))))
        .append(DATPenSet()
            .add_data({'initialValue': 0, 'shows_all_strings': False})
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', 'Standard', 'StereoWidthMode'], 'value': 0})
                .moveTo((518.0, 314.0))
                .lineTo((734.0, 314.0))
                .lineTo((734.0, 366.0))
                .lineTo((518.0, 366.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', 'Natural', 'StereoWidthMode'], 'value': 1})
                .moveTo((518.0, 314.0))
                .lineTo((734.0, 314.0))
                .lineTo((734.0, 366.0))
                .lineTo((518.0, 366.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', 'Shuffler A', 'StereoWidthMode'], 'value': 2})
                .moveTo((518.0, 314.0))
                .lineTo((734.0, 314.0))
                .lineTo((734.0, 366.0))
                .lineTo((518.0, 366.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', 'Shuffler B', 'StereoWidthMode'], 'value': 3})
                .moveTo((518.0, 314.0))
                .lineTo((734.0, 314.0))
                .lineTo((734.0, 366.0))
                .lineTo((518.0, 366.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', 'Shuffler C', 'StereoWidthMode'], 'value': 4})
                .moveTo((518.0, 314.0))
                .lineTo((734.0, 314.0))
                .lineTo((734.0, 366.0))
                .lineTo((518.0, 366.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', 'M/S Blend', 'StereoWidthMode'], 'value': 5})
                .moveTo((518.0, 314.0))
                .lineTo((734.0, 314.0))
                .lineTo((734.0, 366.0))
                .lineTo((518.0, 366.0))
                .closePath()
                .f(bw(0.0, 0.05))))
        .append(DATPenSet()
            .add_data({'initialValue': 0, 'shows_all_strings': False})
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', 'Left | Right', 'InputMode'], 'value': 0})
                .moveTo((912.0, 754.0))
                .lineTo((1096.0, 754.0))
                .lineTo((1096.0, 806.0))
                .lineTo((912.0, 806.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', 'Mid | Side', 'InputMode'], 'value': 1})
                .moveTo((912.0, 754.0))
                .lineTo((1096.0, 754.0))
                .lineTo((1096.0, 806.0))
                .lineTo((912.0, 806.0))
                .closePath()
                .f(bw(0.0, 0.05))))
        .append(DATPenSet()
            .add_data({'initialValue': 0, 'shows_all_strings': False})
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', 'Left | Right', 'InputMode'], 'value': 0})
                .moveTo((1136.0, 754.0))
                .lineTo((1320.0, 754.0))
                .lineTo((1320.0, 806.0))
                .lineTo((1136.0, 806.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', 'Mid | Side', 'InputMode'], 'value': 1})
                .moveTo((1136.0, 754.0))
                .lineTo((1320.0, 754.0))
                .lineTo((1320.0, 806.0))
                .lineTo((1136.0, 806.0))
                .closePath()
                .f(bw(0.0, 0.05))))
        .append(DATPenSet()
            .add_data({'initialValue': 0, 'shows_all_strings': False})
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', 'Left | Right', 'FlipLR'], 'value': 0})
                .moveTo((1360.0, 754.0))
                .lineTo((1544.0, 754.0))
                .lineTo((1544.0, 806.0))
                .lineTo((1360.0, 806.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', 'Right | Left', 'FlipLR'], 'value': 1})
                .moveTo((1360.0, 754.0))
                .lineTo((1544.0, 754.0))
                .lineTo((1544.0, 806.0))
                .lineTo((1360.0, 806.0))
                .closePath()
                .f(bw(0.0, 0.05))))
        .append(DATPenSet()
            .add_data({'initialValue': 2, 'shows_all_strings': False})
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', 'Auto', 'MidTiltLoudnessMode'], 'value': 0})
                .moveTo((926.0, 146.0))
                .lineTo((1086.0, 146.0))
                .lineTo((1086.0, 198.0))
                .lineTo((926.0, 198.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', 'Standard', 'MidTiltLoudnessMode'], 'value': 1})
                .moveTo((926.0, 146.0))
                .lineTo((1086.0, 146.0))
                .lineTo((1086.0, 198.0))
                .lineTo((926.0, 198.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', 'Treble', 'MidTiltLoudnessMode'], 'value': 2})
                .moveTo((926.0, 146.0))
                .lineTo((1086.0, 146.0))
                .lineTo((1086.0, 198.0))
                .lineTo((926.0, 198.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', 'Bass', 'MidTiltLoudnessMode'], 'value': 3})
                .moveTo((926.0, 146.0))
                .lineTo((1086.0, 146.0))
                .lineTo((1086.0, 198.0))
                .lineTo((926.0, 198.0))
                .closePath()
                .f(bw(0.0, 0.05))))
        .append(DATPenSet()
            .add_data({'initialValue': 2, 'shows_all_strings': False})
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', 'Auto', 'MidTiltLoudnessMode'], 'value': 0})
                .moveTo((1262.0, 146.0))
                .lineTo((1422.0, 146.0))
                .lineTo((1422.0, 198.0))
                .lineTo((1262.0, 198.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', 'Standard', 'MidTiltLoudnessMode'], 'value': 1})
                .moveTo((1262.0, 146.0))
                .lineTo((1422.0, 146.0))
                .lineTo((1422.0, 198.0))
                .lineTo((1262.0, 198.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', 'Treble', 'MidTiltLoudnessMode'], 'value': 2})
                .moveTo((1262.0, 146.0))
                .lineTo((1422.0, 146.0))
                .lineTo((1422.0, 198.0))
                .lineTo((1262.0, 198.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', 'Bass', 'MidTiltLoudnessMode'], 'value': 3})
                .moveTo((1262.0, 146.0))
                .lineTo((1422.0, 146.0))
                .lineTo((1422.0, 198.0))
                .lineTo((1262.0, 198.0))
                .closePath()
                .f(bw(0.0, 0.05))))))