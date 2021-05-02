from math import sqrt

def AverageValue():
    average_value = sum(data)/len(data)

def StandardDeviation(student_fisher):
    if student_fisher == 0:
        sum = 0
        for value in data:
            sum = sum + (average_value - value)^2
    
        standard_deviation = sqrt(sum)/sqrt(len(data))
    if student_fisher == 1:
        pass
    
    return standard_deviation 

def TotalUncertainty(uncertainty_type_a, uncertainty_type_b):
    total_uncertainty = sqrt(uncertainty_type_a^2 + uncertainty_type_b^2)

    return total_uncertainty

def UncertaintyTypeBDigital(value, resolution, class, coefficient):
    uncertainty_type_b = (class*0.01*value + coefficient*resolution)/sqrt(3)

    return uncertainty_type_b

def UncertaintyTypeBAnalog(class, range):
    uncertainty_type_b = (class*range)/sqrt(3)

    return uncertainty_type_b