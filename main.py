import sys
from function.open_file import *
from function.constant import *
from function.function import *

try:   
    print(f"Liczba argumentów: {len(sys.argv)}")

    for i, arg in enumerate(sys.argv):
        print(f"argument {i:>6}: {arg}")

        if arg == "-help":
            print(how_to_run_info)

        if arg == "-run":
            try:
                config_path = sys.argv[i+1]
            except(IndexError):
                print(cfg_path_error)
        
            try:
                data_path = sys.argv[i+2]
            except(IndexError):
                print(data_path_error)
                break

    dic_config = OpenConfig(config_path)
    data_list = OpenData(data_path)
    list_results = []
    dic_results = {}
except(NameError):
    print(how_to_run_info)

if dic_config['AVERAGE'] == 1:
        average_value = AverageValue(data_list)
        list_results.append(average_value)
        

if dic_config['UNCERTAINTY'] == 1:
        if dic_config['UNCERTAINTYTYPEA'] == 1:
            uncertainty_type_a = StandardDeviation(dic_config['STUDENTFISHER'], data_list, average_value)
            list_results.append(uncertainty_type_a)

        if dic_config['UNCERTAINTYTYPEB'] == 1:
            if  dic_config['UNCERTAINTYDIGITAL'] == 1:
                uncertainty_type_b = UncertaintyTypeBDigital(average_value, dic_config['GAUGERESOLUTION'], dic_config['GAUGECLASS'], dic_config['GAUGECOEFFICIENTY'])
            if  dic_config['UNCERTAINTYANALOG'] == 1:
                uncertainty_type_b = UncertaintyTypeBAnalog(dic_config['GAUGECLASS'], dic_config['GAUGERANGE'])
            list_results.append(uncertainty_type_b)
try:
    uncertainty = TotalUncertainty(uncertainty_type_a, uncertainty_type_b)  
    list_results.append(uncertainty)  
except(NameError):
    try:
        uncertainty = TotalUncertainty(0, uncertainty_type_b)  
    except(NameError):
        uncertainty = TotalUncertainty(uncertainty_type_a, 0)
        
    list_results.append(uncertainty) 

if dic_config['COMPATIBILITYTEST'] == 1:

    try:
        if CompatibilityTest(average_value, dic_config['PHYSICALTABELVALUE'], dic_config['CHECKMULTIPLIER'], uncertainty) == True: print(test_result_positive)
        if CompatibilityTest(average_value, dic_config['PHYSICALTABELVALUE'], dic_config['CHECKMULTIPLIER'], uncertainty) == False: print(test_result_negative)
    except(KeyError):
        print(compatibility_error_info)
        exit()
    
print(list_results)



