import sys
from function.open_file import *
from function.constant import *
from function.function import *

def RunFunction(agrument):
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

                return dic_config, data_list
    
    except(NameError):
        print(how_to_run_info)
        exit()