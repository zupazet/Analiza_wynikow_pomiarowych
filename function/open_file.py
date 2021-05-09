from function.constant import *

def OpenConfig(config_path):
    file = open(config_path)
    lines = file.readlines()
    dic_config = {}
    for line in lines:
        data = line.strip().replace(" ", "").split("=")
        if (len(data) == 2 and data[1]):
            try:
                dic_config[data[0].upper()] = int(data[1])
            except:
                try: 
                    dic_config[data[0].upper()] = float(data[1])
                except:
                    print(cfg_value_error.format(data))
    return dic_config    

def OpenData(data_path):
    file = open(data_path)
    lines = file.readlines()
    data_list = []
    for line in lines:
        data = line.strip().replace(" ", "")
        try:
            data = int(data)
            data_list.append(data)
        except:
            try:
                data = float(data)
                data_list.append(data)
            except:
                print(value_error)
    
    return data_list
