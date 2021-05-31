import sys
from function.open_file import *
from function.constant import *
from function.function import *

def RunFunction(agrument):
    try:   
        print(f"Liczba argumentów: {len(sys.argv)}")

        for i, arg in enumerate(sys.argv):
            print(f"argument {i:>6}: {arg}")

            if arg == "-h" or arg == "--help":
                print(how_to_run_info)
                exit()

            if arg == "-r" or arg == "--run":
                try:
                    config_path = sys.argv[i+1]
                except(IndexError):
                    print(cfg_path_error)
                    exit()
            
                try:
                    data_path = sys.argv[i+2]
                except(IndexError):
                    print(data_path_error)
                    exit()

                return OpenConfig(config_path), OpenData(data_path)
    
    except(NameError, TypeError):
        print(how_to_run_info)
        exit()

def MainAverageValue(data_list, dic_config):
    if average in dic_config:
        if dic_config[average] == 1:
            return AverageValue(data_list)
        else: return 0
    else: return 0

def MainUnceraintyA(dic_config, data_list, dic_results):
    if uncertainty in dic_config and uncertainty_type_a_dic in dic_config:      
        if dic_config[uncertainty_type_a_dic] == 1 and average_result in dic_results and student_fisher_dic in dic_config:           
            return StandardDeviation(dic_config[student_fisher_dic], data_list, dic_results[average_result])
        
        if dic_config[uncertainty_type_a_dic] != 1:
            return 0

        else:
            print(cfg_not_enough_data + uncertainty_type_a_argument)
            exit()

    else: return 0
            
def MainUncertaintyB(dic_config, data_list, dic_results):
    if uncertainty in dic_config and uncertainty_type_b_dic in dic_config:
        if dic_config[uncertainty_type_b_dic] == 1 and (uncertainty_analog in dic_config or uncertainty_digital in dic_config):
            if dic_config[uncertainty_digital] == 1 and gauge_class in dic_config and gauge_coefficienty in dic_config and gauge_resolution in dic_config and average_result in dic_results:
                return UncertaintyTypeBDigital(dic_results[average_result], dic_config[gauge_resolution], dic_config[gauge_class], dic_config[gauge_coefficienty])
            
            if dic_config[uncertainty_digital] == 1 and (gauge_class not in dic_config or gauge_coefficienty not in dic_config or gauge_resolution not in dic_config or average_result not in dic_results):
                print(cfg_not_enough_data + uncertainty_b_argument_digital)
                exit()
            
            if dic_config[uncertainty_analog] == 1 and gauge_class in dic_config and gauge_range in dic_config:
                return UncertaintyTypeBAnalog(dic_config[gauge_class], dic_config[gauge_range])
            
            if dic_config[uncertainty_analog] == 1 and (gauge_class not in dic_config or gauge_range not in dic_config):
                print(cfg_not_enough_data + uncertainty_b_argument_analog)
                exit()
            
            else: return 0

        else:
            print(uncertainty_type_b_argument)
            exit()

    else: return 0

def MainTotalUncertainty(dic_config, dic_results):
    if uncertainty in dic_config:
        if dic_config[uncertainty] == 1:
            return TotalUncertainty(dic_results[uncertainty_type_a_result], dic_results[uncertainty_type_b_result])
        else:
            return 0
    else: return 0



def MainCompatiblityTest(dic_config, dic_results):
    if compatibility_test in dic_config:
        if dic_config[compatibility_test] == 1 and dic_results[average_result] != 0 and dic_results[uncertainty_result] != 0 and physical_tabel_value in dic_config and check_multiplier in dic_config:
            if CompatibilityTest(dic_results[average_result], dic_config[physical_tabel_value], dic_config[check_multiplier], dic_results[uncertainty_result]) == True: return test_result_positive
            if CompatibilityTest(dic_results[average_result], dic_config[physical_tabel_value], dic_config[check_multiplier], dic_results[uncertainty_result]) == False: return test_result_negative
        if dic_config[compatibility_test] != 1: return 0

        if dic_config[compatibility_test] == 1 and (dic_results[average_result] == 0 or dic_results[uncertainty_result] == 0 or physical_tabel_value not in dic_config or check_multiplier not in dic_config):
            print(compatibility_error_info)
            exit()
    else: return 0

def Show(dic_results):
    items = dic_results.items()
    for data in items:
        if data[1] != 0:
            print("{}: {}".format(data[0], data[1]))

