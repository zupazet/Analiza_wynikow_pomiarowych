def OpenConfig(config_path):
    file = open(config_path)
    lines = file.readlines()
    dic = {}
    for line in lines:
        data = line.strip().replace(" ", "").split("=")
        if (len(data) == 2 and data[1]):
            try:
                dic[data[0].upper()] = int(data[1])
            except:
                try: 
                    dic[data[0].upper()] = float(data[1])
                except:
                    dic[data[0].upper()] = data[1]
    return dic    