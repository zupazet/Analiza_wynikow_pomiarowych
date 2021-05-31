student_fisher = [0, 1.837, 1.321, 1.197, 1.141, 1.110, 1.090, 1.077, 1.066, 1.059, 1.052, 1.047, 1.043, 1.040, 1.037, 1.034, 1.032, 1.030, 1.028, 1.027]
percent = 0.01

cfg_path_error = "Brak nazwy pliku config"
data_path_error = "Brak nazwy pliku z danymi"
how_to_run_info = "Aby uruchumić wpisz w terminalu: python main.py -run <nazwa pliku config> <nazwa pliku z danymi>"
value_error = "Zły format danych"
cfg_value_error = "Zła wartość w pliku config, dla {configname}"
cfg_not_enough_data = "W pliku config podano za mało danych"
uncertainty_b_argument_analog = """Do obliczenia niepewności typu b miernika analogowego uzupełnij plik config o poniższe wartości:
Gauge Class, Gauge Range"""
uncertainty_b_argument_digital = """Do obliczenia niepewności typu b miernika cyfrowego uzupełnij plik config o poniższe wartości:
Gauge Class, Gauge coefficienty, Gauge resolution, Average Value = 1"""
uncertainty_type_a_argument = """Do obliczenia niepweności typu a uzupełnij plik config o poniższe wartości:
Average Value = 1, Student Fisher = 0 lub 1"""
uncertainty_type_b_argument = """Do obliczenia niepewności typu b podaj w pliku config jedną z poniższych wartości:
Uncertainty type B analog = 1 lub Uncertainty type B digital = 1"""
test_result_positive = "Wyznaczona wartość jest zgodna z wartością tablicową"
test_result_negative = "Wyznaczona wartość nie jest zgodna z wartością tablicową"
compatibility_error_info = """Podano za mało danych w pliku konfiguracyjnym
Do sprawdzenia zgodności uzupełnij plik konfiguracyjny o poniższe wartości:
Check Multiplier, Physical Tabel Value, Average Value = 1, Uncertaint = 1"""
average = 'AVERAGEVALUE'
uncertainty = 'UNCERTAINTY'
uncertainty_type_a_dic = 'UNCERTAINTYTYPEA'
uncertainty_type_b_dic = 'UNCERTAINTYTYPEB'
student_fisher_dic = 'STUDENTFISHER'
uncertainty_digital = 'UNCERTAINTYDIGITAL'
uncertainty_analog = 'UNCERTAINTYANALOG'
gauge_resolution = 'GAUGERESOLUTION'
gauge_class = 'GAUGECLASS'
gauge_range = 'GAUGERANGE'
gauge_coefficienty = 'GAUGECOEFFICIENTY'
compatibility_test = 'COMPATIBILITYTEST'
physical_tabel_value = 'PHYSICALTABELVALUE'
check_multiplier = 'CHECKMULTIPLIER'
uncertainty_result = 'Niepewność'
average_result = 'Wartość średnia'
uncertainty_type_a_result = 'Niepewność typu a'
uncertainty_type_b_result = 'Niepewność typu b'
compatibility_test_result = 'Test zgodności'