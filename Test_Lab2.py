import Lab2
def test_find_min_max():
    numbers = [1,2,3,4,5,6,7]
    result = Lab2.find_min_max(numbers)
    assert (result == 1,7


            )

def test_calc_average():
    numbers =[1, 2, 3, 4, 5]
    average = Lab2.calc_average(numbers)
    assert (average == 3)
def test_calc_median_temperature():
    numbers =[1, 2, 3, 4, 5]
    median = Lab2.calc_median(numbers)
    assert (median == 3)