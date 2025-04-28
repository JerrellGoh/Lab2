import bmi as bmi

def test_bmi_normal_weight():
    result = []
    input_height = 1.8
    input_weight = 70
    result = bmi.calculate_bmi(input_height, input_weight)
    result = bmi.classify_bmi(result)
    
    assert (result == 0)

def test_bmi_over_weight():
    result = []
    input_height = 1.8 
    input_weight = 90
    result = bmi.calculate_bmi(input_height, input_weight)
    result = bmi.classify_bmi(result)

    assert (result == 1)




def test_bmi_under_weight():
    result = []
    input_height = 1.8 
    input_weight = 50
    result = bmi.calculate_bmi(input_height, input_weight)
    result = bmi.classify_bmi(result)

    assert (result == -1)

