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
            exit()

        if arg == "-run":
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

            dic_config = OpenConfig(config_path)
            data_list = OpenData(data_path)

            list_results = []
            dic_results = {}
except(NameError):
    print(how_to_run_info)
    exit()

try:
    if dic_config[average] == 1:
        average_value = AverageValue(data_list)
        list_results.append(average_value)
except(NameError):
    pass    

        
try:
    if dic_config[uncertainty] == 1:
        try:
            if dic_config[uncertainty_type_a_dic] == 1:
                uncertainty_type_a = StandardDeviation(dic_config[student_fisher_dic], data_list, average_value)
                list_results.append(uncertainty_type_a)

            if dic_config[uncertainty_type_b_dic] == 1:
                try:
                    try:
                        if  dic_config[uncertainty_digital] == 1:
                            uncertainty_type_b = UncertaintyTypeBDigital(average_value, dic_config[gauge_resolution], dic_config[gauge_class], dic_config[gauge_coefficienty])
                    except(KeyError):    
                        if  dic_config[uncertainty] == 1:
                            uncertainty_type_b = UncertaintyTypeBAnalog(dic_config[gauge_class], dic_config[gauge_range])
                    list_results.append(uncertainty_type_b)
                except(KeyError):
                    print(cfg_not_enough_data + "\n" + uncertainty_b_argument_digital + "\n" + uncertainty_b_argument_analog)
                    exit()

        except(NameError):
            average_value = AverageValue(data_list)
            if dic_config[uncertainty_type_a_dic] == 1:
                uncertainty_type_a = StandardDeviation(dic_config[student_fisher_dic], data_list, average_value)
                list_results.append(uncertainty_type_a)

            if dic_config[uncertainty_type_b_dic] == 1:
                try:
                    try:
                        if  dic_config[uncertainty_digital] == 1:
                            uncertainty_type_b = UncertaintyTypeBDigital(average_value, dic_config[gauge_resolution], dic_config[gauge_class], dic_config[gauge_coefficienty])
                    except(KeyError):    
                        if  dic_config[uncertainty] == 1:
                            uncertainty_type_b = UncertaintyTypeBAnalog(dic_config[gauge_class], dic_config[gauge_range])
                    list_results.append(uncertainty_type_b)
                except(KeyError):
                    print(cfg_not_enough_data + "\n" + uncertainty_b_argument_digital + "\n" + uncertainty_b_argument_analog)
                    exit()
        try:
            total_uncertainty = TotalUncertainty(uncertainty_type_a, uncertainty_type_b) 
            list_results.append(total_uncertainty)   
        except(NameError):
            try:
                total_uncertainty = TotalUncertainty(0, uncertainty_type_b) 
            except(NameError):
                total_uncertainty = TotalUncertainty(uncertainty_type_a, 0)
            list_results.append(total_uncertainty)
except(NameError):
    pass    

try:
    if dic_config[compatibility_test] == 1:
        try:
            if CompatibilityTest(average_value, dic_config[physical_tabel_value], dic_config[check_multiplier], total_uncertainty) == True: print(test_result_positive)
            if CompatibilityTest(average_value, dic_config[physical_tabel_value], dic_config[check_multiplier], total_uncertainty) == False: print(test_result_negative)
        except(KeyError):
            print(compatibility_error_info)
            exit()
        except(NameError):
            average_value = AverageValue(data_list)
            if CompatibilityTest(average_value, dic_config[physical_tabel_value], dic_config[check_multiplier], total_uncertainty) == True: print(test_result_positive)
            if CompatibilityTest(average_value, dic_config[physical_tabel_value], dic_config[check_multiplier], total_uncertainty) == False: print(test_result_negative)
except(NameError):
    pass
    
print(list_results)



