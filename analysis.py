import sys
from function.constant import *
from function.function import *
from function.main_function import *

dic_config, data_list = RunFunction(sys.argv)
dic_results = {}

dic_results[average_result] = MainAverageValue(data_list, dic_config)    
dic_results[uncertainty_type_a_result] = MainUnceraintyA(dic_config, data_list, dic_results)
dic_results[uncertainty_type_b_result] = MainUncertaintyB(dic_config, data_list, dic_results)
dic_results[uncertainty_result] = MainTotalUncertainty(dic_config, dic_results)
dic_results[compatibility_test_result] = MainCompatiblityTest(dic_config, dic_results)
Show(dic_results)