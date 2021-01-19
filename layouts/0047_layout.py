(DATPens()
    .append(DATPen()
        .tag("parameter-edges")
        .moveTo((0.0, 676.0))
        .lineTo((126.0, 676.0))
        .endPath()
        .moveTo((634.0, 676.0))
        .lineTo((760.0, 676.0))
        .endPath()
        .moveTo((176.0, 188.0))
        .lineTo((380.0, 188.0))
        .endPath()
        .moveTo((380.0, 188.0))
        .lineTo((582.0, 188.0))
        .endPath()
        .moveTo((532.0, 60.0))
        .lineTo((532.0, 128.0))
        .endPath()
        .moveTo((608.0, 60.0))
        .lineTo((608.0, 128.0))
        .endPath()
        .moveTo((684.0, 60.0))
        .lineTo((684.0, 128.0))
        .endPath()
        .moveTo((126.0, 128.0))
        .lineTo((126.0, 676.0))
        .endPath()
        .moveTo((634.0, 246.0))
        .lineTo((634.0, 676.0))
        .endPath()
        .moveTo((380.0, 128.0))
        .lineTo((380.0, 246.0))
        .endPath()
        .moveTo((634.0, 128.0))
        .lineTo((634.0, 246.0))
        .endPath()
        .moveTo((1004.0, 608.0))
        .lineTo((1004.0, 676.0))
        .endPath()
        .moveTo((1384.0, 608.0))
        .lineTo((1384.0, 676.0))
        .endPath()
        .moveTo((884.0, 608.0))
        .lineTo((1524.0, 608.0))
        .endPath()
        .moveTo((884.0, 556.0))
        .lineTo((1524.0, 556.0))
        .endPath()
        .f(bw(0.0, 0.0))
        .s(bw(0.5))
        .sw(3))
    .append(DATPen()
        .tag("clump-edges")
        .moveTo((0, 60))
        .lineTo((760, 60))
        .endPath()
        .moveTo((0.0, 128.0))
        .lineTo((760.0, 128.0))
        .endPath()
        .f(bw(0.0, 0.0))
        .s(bw(0.25))
        .sw(5))
    .append(DATPen()
        .tag("sidebar")
        .moveTo((760, 0))
        .lineTo((884, 0))
        .lineTo((884, 676))
        .lineTo((760, 676))
        .closePath()
        .f(bw(0.5)))
    .append(DATPen()
        .tag("advbar")
        .moveTo((884, 0))
        .lineTo((1524, 0))
        .lineTo((1524, 60))
        .lineTo((884, 60))
        .closePath()
        .f(bw(0.75)))
    .append(DATPens()
        .tag("labels")
        .append(DATPen()
            .tag("param")
            .add_data({'align': [6, 3], 'ts': ['ParamLabel/text', 'Drive', None]})
            .moveTo((6.0, 154.0))
            .lineTo((120.0, 154.0))
            .lineTo((120.0, 218.0))
            .lineTo((6.0, 218.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .tag("param")
            .add_data({'align': [6, 3], 'ts': ['ParamLabel/text', 'Output', None]})
            .moveTo((640.0, 154.0))
            .lineTo((754.0, 154.0))
            .lineTo((754.0, 218.0))
            .lineTo((640.0, 218.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .tag("param")
            .add_data({'align': [4, 5], 'ts': ['ParamLabel/text', 'Bias', None]})
            .moveTo((186.0, 192.0))
            .lineTo((246.0, 192.0))
            .lineTo((246.0, 250.0))
            .lineTo((186.0, 250.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .tag("param")
            .add_data({'align': [4, 5], 'ts': ['ParamLabel/text', 'Noise', None]})
            .moveTo((306.0, 132.0))
            .lineTo((374.0, 132.0))
            .lineTo((374.0, 192.0))
            .lineTo((306.0, 192.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .tag("param")
            .add_data({'align': [4, 5], 'ts': ['ParamLabel/text', 'Bias', None]})
            .moveTo((390.0, 192.0))
            .lineTo((450.0, 192.0))
            .lineTo((450.0, 250.0))
            .lineTo((390.0, 250.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .tag("param")
            .add_data({'align': [4, 5], 'ts': ['ParamLabel/text', 'Noise', None]})
            .moveTo((508.0, 132.0))
            .lineTo((576.0, 132.0))
            .lineTo((576.0, 192.0))
            .lineTo((508.0, 192.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .tag("param")
            .add_data({'align': [6, 5], 'ts': ['ParamLabel/text', 'DRY', None]})
            .moveTo((6, 60))
            .lineTo((134.0, 60.0))
            .lineTo((134.0, 128.0))
            .lineTo((6.0, 128.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .tag("clump")
            .add_data({'align': [6, 5], 'ts': ['ClumpLabel/text', 'FILTER', None]})
            .moveTo((1018.0, 608.0))
            .lineTo((1370.0, 608.0))
            .lineTo((1370.0, 676.0))
            .lineTo((1018.0, 676.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .tag("clump")
            .add_data({'align': [6, 5], 'ts': ['ClumpLabel/text', 'TILT', None]})
            .moveTo((898.0, 556.0))
            .lineTo((970.0, 556.0))
            .lineTo((970.0, 608.0))
            .lineTo((898.0, 608.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPens()
            .tag("options")
            .add_data({'initialValue': 0, 'string_count': 16, 'shows_all_strings': False})
            .append(DATPen()
                .tag("value")
                .add_data({'align': [6, 5], 'us': '5751 Lo', 'value': 0})
                .moveTo((158.0, 258.0))
                .lineTo((348.0, 258.0))
                .lineTo((348.0, 302.0))
                .lineTo((158.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'align': [6, 5], 'us': '5751 Med', 'value': 1})
                .moveTo((158.0, 258.0))
                .lineTo((348.0, 258.0))
                .lineTo((348.0, 302.0))
                .lineTo((158.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'align': [6, 5], 'us': '5751 Hi', 'value': 2})
                .moveTo((158.0, 258.0))
                .lineTo((348.0, 258.0))
                .lineTo((348.0, 302.0))
                .lineTo((158.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'align': [6, 5], 'us': '6L6 Lo', 'value': 3})
                .moveTo((158.0, 258.0))
                .lineTo((348.0, 258.0))
                .lineTo((348.0, 302.0))
                .lineTo((158.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'align': [6, 5], 'us': '6L6 Med', 'value': 4})
                .moveTo((158.0, 258.0))
                .lineTo((348.0, 258.0))
                .lineTo((348.0, 302.0))
                .lineTo((158.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'align': [6, 5], 'us': '6L6 Hi', 'value': 5})
                .moveTo((158.0, 258.0))
                .lineTo((348.0, 258.0))
                .lineTo((348.0, 302.0))
                .lineTo((158.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'align': [6, 5], 'us': 'EL34 Lo', 'value': 6})
                .moveTo((158.0, 258.0))
                .lineTo((348.0, 258.0))
                .lineTo((348.0, 302.0))
                .lineTo((158.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'align': [6, 5], 'us': 'EL34 Hi', 'value': 7})
                .moveTo((158.0, 258.0))
                .lineTo((348.0, 258.0))
                .lineTo((348.0, 302.0))
                .lineTo((158.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'align': [6, 5], 'us': '12AX7', 'value': 8})
                .moveTo((158.0, 258.0))
                .lineTo((348.0, 258.0))
                .lineTo((348.0, 302.0))
                .lineTo((158.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'align': [6, 5], 'us': 'Reserved 1', 'value': 9})
                .moveTo((158.0, 258.0))
                .lineTo((348.0, 258.0))
                .lineTo((348.0, 302.0))
                .lineTo((158.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'align': [6, 5], 'us': 'Reserved 2', 'value': 10})
                .moveTo((158.0, 258.0))
                .lineTo((348.0, 258.0))
                .lineTo((348.0, 302.0))
                .lineTo((158.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'align': [6, 5], 'us': 'Reserved 3', 'value': 11})
                .moveTo((158.0, 258.0))
                .lineTo((348.0, 258.0))
                .lineTo((348.0, 302.0))
                .lineTo((158.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'align': [6, 5], 'us': 'Reserved 4', 'value': 12})
                .moveTo((158.0, 258.0))
                .lineTo((348.0, 258.0))
                .lineTo((348.0, 302.0))
                .lineTo((158.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'align': [6, 5], 'us': 'Reserved 5', 'value': 13})
                .moveTo((158.0, 258.0))
                .lineTo((348.0, 258.0))
                .lineTo((348.0, 302.0))
                .lineTo((158.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'align': [6, 5], 'us': 'Reserved 6', 'value': 14})
                .moveTo((158.0, 258.0))
                .lineTo((348.0, 258.0))
                .lineTo((348.0, 302.0))
                .lineTo((158.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'align': [6, 5], 'us': 'Reserved 7', 'value': 15})
                .moveTo((158.0, 258.0))
                .lineTo((348.0, 258.0))
                .lineTo((348.0, 302.0))
                .lineTo((158.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05))))
        .append(DATPens()
            .tag("options")
            .add_data({'initialValue': 0, 'string_count': 16, 'shows_all_strings': False})
            .append(DATPen()
                .tag("value")
                .add_data({'align': [6, 5], 'us': '2 Track Hi', 'value': 0})
                .moveTo((412.0, 258.0))
                .lineTo((602.0, 258.0))
                .lineTo((602.0, 302.0))
                .lineTo((412.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'align': [6, 5], 'us': '2 Track Lo', 'value': 1})
                .moveTo((412.0, 258.0))
                .lineTo((602.0, 258.0))
                .lineTo((602.0, 302.0))
                .lineTo((412.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'align': [6, 5], 'us': 'C90 Hi', 'value': 2})
                .moveTo((412.0, 258.0))
                .lineTo((602.0, 258.0))
                .lineTo((602.0, 302.0))
                .lineTo((412.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'align': [6, 5], 'us': 'C90 Lo', 'value': 3})
                .moveTo((412.0, 258.0))
                .lineTo((602.0, 258.0))
                .lineTo((602.0, 302.0))
                .lineTo((412.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'align': [6, 5], 'us': 'Opto Limiter', 'value': 4})
                .moveTo((412.0, 258.0))
                .lineTo((602.0, 258.0))
                .lineTo((602.0, 302.0))
                .lineTo((412.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'align': [6, 5], 'us': 'Reserved 1', 'value': 5})
                .moveTo((412.0, 258.0))
                .lineTo((602.0, 258.0))
                .lineTo((602.0, 302.0))
                .lineTo((412.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'align': [6, 5], 'us': 'Reserved 2', 'value': 6})
                .moveTo((412.0, 258.0))
                .lineTo((602.0, 258.0))
                .lineTo((602.0, 302.0))
                .lineTo((412.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'align': [6, 5], 'us': 'Reserved 3', 'value': 7})
                .moveTo((412.0, 258.0))
                .lineTo((602.0, 258.0))
                .lineTo((602.0, 302.0))
                .lineTo((412.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'align': [6, 5], 'us': 'Reserved 4', 'value': 8})
                .moveTo((412.0, 258.0))
                .lineTo((602.0, 258.0))
                .lineTo((602.0, 302.0))
                .lineTo((412.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'align': [6, 5], 'us': 'Reserved 5', 'value': 9})
                .moveTo((412.0, 258.0))
                .lineTo((602.0, 258.0))
                .lineTo((602.0, 302.0))
                .lineTo((412.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'align': [6, 5], 'us': 'Reserved 6', 'value': 10})
                .moveTo((412.0, 258.0))
                .lineTo((602.0, 258.0))
                .lineTo((602.0, 302.0))
                .lineTo((412.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'align': [6, 5], 'us': 'Reserved 7', 'value': 11})
                .moveTo((412.0, 258.0))
                .lineTo((602.0, 258.0))
                .lineTo((602.0, 302.0))
                .lineTo((412.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'align': [6, 5], 'us': 'Reserved 8', 'value': 12})
                .moveTo((412.0, 258.0))
                .lineTo((602.0, 258.0))
                .lineTo((602.0, 302.0))
                .lineTo((412.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'align': [6, 5], 'us': 'Reserved 9', 'value': 13})
                .moveTo((412.0, 258.0))
                .lineTo((602.0, 258.0))
                .lineTo((602.0, 302.0))
                .lineTo((412.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'align': [6, 5], 'us': 'Reserved 10', 'value': 14})
                .moveTo((412.0, 258.0))
                .lineTo((602.0, 258.0))
                .lineTo((602.0, 302.0))
                .lineTo((412.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'align': [6, 5], 'us': 'Reserved 11', 'value': 15})
                .moveTo((412.0, 258.0))
                .lineTo((602.0, 258.0))
                .lineTo((602.0, 302.0))
                .lineTo((412.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05))))
        .append(DATPens()
            .tag("options")
            .add_data({'initialValue': 1, 'string_count': 1, 'shows_all_strings': False})
            .append(DATPen()
                .tag("value")
                .add_data({'align': [6, 5], 'us': 'TU', 'value': 0})
                .moveTo((538.0, 66.0))
                .lineTo((602.0, 66.0))
                .lineTo((602.0, 122.0))
                .lineTo((538.0, 122.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'align': [6, 5], 'us': 'TU', 'value': 1})
                .moveTo((538.0, 66.0))
                .lineTo((602.0, 66.0))
                .lineTo((602.0, 122.0))
                .lineTo((538.0, 122.0))
                .closePath()
                .f(bw(0.0, 0.05))))
        .append(DATPens()
            .tag("options")
            .add_data({'initialValue': 1, 'string_count': 1, 'shows_all_strings': False})
            .append(DATPen()
                .tag("value")
                .add_data({'align': [6, 5], 'us': 'PE', 'value': 0})
                .moveTo((614.0, 66.0))
                .lineTo((678.0, 66.0))
                .lineTo((678.0, 122.0))
                .lineTo((614.0, 122.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'align': [6, 5], 'us': 'PE', 'value': 1})
                .moveTo((614.0, 66.0))
                .lineTo((678.0, 66.0))
                .lineTo((678.0, 122.0))
                .lineTo((614.0, 122.0))
                .closePath()
                .f(bw(0.0, 0.05))))
        .append(DATPens()
            .tag("options")
            .add_data({'initialValue': 1, 'string_count': 1, 'shows_all_strings': False})
            .append(DATPen()
                .tag("value")
                .add_data({'align': [6, 5], 'us': 'FLT', 'value': 0})
                .moveTo((690.0, 66.0))
                .lineTo((754.0, 66.0))
                .lineTo((754.0, 122.0))
                .lineTo((690.0, 122.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'align': [6, 5], 'us': 'FLT', 'value': 1})
                .moveTo((690.0, 66.0))
                .lineTo((754.0, 66.0))
                .lineTo((754.0, 122.0))
                .lineTo((690.0, 122.0))
                .closePath()
                .f(bw(0.0, 0.05))))
        .append(DATPens()
            .tag("options")
            .add_data({'initialValue': 0, 'string_count': 2, 'shows_all_strings': False})
            .append(DATPen()
                .tag("value")
                .add_data({'align': [6, 5], 'ts': ['Parameter/option', 'Pre', 'FilterPosition'], 'value': 0})
                .moveTo((896.0, 620.0))
                .lineTo((992.0, 620.0))
                .lineTo((992.0, 664.0))
                .lineTo((896.0, 664.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'align': [6, 5], 'ts': ['Parameter/option', 'Post', 'FilterPosition'], 'value': 1})
                .moveTo((896.0, 620.0))
                .lineTo((992.0, 620.0))
                .lineTo((992.0, 664.0))
                .lineTo((896.0, 664.0))
                .closePath()
                .f(bw(0.0, 0.05))))
        .append(DATPens()
            .tag("options")
            .add_data({'initialValue': 0, 'string_count': 2, 'shows_all_strings': False})
            .append(DATPen()
                .tag("value")
                .add_data({'align': [6, 5], 'us': '+-30 dB', 'value': 0})
                .moveTo((1396.0, 620.0))
                .lineTo((1512.0, 620.0))
                .lineTo((1512.0, 664.0))
                .lineTo((1396.0, 664.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'align': [6, 5], 'us': '+-15 dB', 'value': 1})
                .moveTo((1396.0, 620.0))
                .lineTo((1512.0, 620.0))
                .lineTo((1512.0, 664.0))
                .lineTo((1396.0, 664.0))
                .closePath()
                .f(bw(0.0, 0.05))))))