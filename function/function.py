from math import sqrt, fabs
from function.constant import student_fisher

def AverageValue(data_list):
    average_value = sum(data_list)/len(data_list)

    return average_value

def StandardDeviation(cfg_student_fisher, data_list, average_value):
    sum = 0
    for value in data_list:
        sum = sum + (average_value - value)**2
    
    standard_deviation = sqrt(sum)/sqrt(len(data_list))
    if student_fisher == 0:
        pass
    if student_fisher == 1:
        standard_deviation = standard_deviation * student_fisher[len(data_list) - 1]
    
    return standard_deviation 

def TotalUncertainty(uncertainty_type_a, uncertainty_type_b):
    total_uncertainty = sqrt(uncertainty_type_a**2 + uncertainty_type_b**2)

    return total_uncertainty

def UncertaintyTypeBDigital(value, resolution, gauge_class, coefficient):
    uncertainty_type_b = (gauge_class*0.01*value + coefficient*resolution)/sqrt(3)

    return uncertainty_type_b

def UncertaintyTypeBAnalog(gauge_class, range):
    uncertainty_type_b = (gauge_class*range)/sqrt(3)

    return uncertainty_type_b

def CompatibilityTest(average_value, pchysical_table_value, check_multiplier, uncertainty):
    substraction = fabs(average_value - pchysical_table_value)
    if substraction <= uncertainty*check_multiplier:
        return True
    else:
        return False
