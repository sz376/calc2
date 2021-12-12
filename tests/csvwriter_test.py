"""Testing the Writing"""
from csvcalc.csvwriter import CSVwriter

def test_write_log():
    """testing that pandas writer is working"""
    my_time = "123"
    my_operation = "addition"
    my_value1 = 1
    my_value2 = 2
    my_result = 3
    CSVwriter.write_log(my_time, my_operation, my_value1, my_value2, my_result)
    with open('./results/log.csv',encoding="utf8") as file:
        lines = file.readlines()
    test = '123,addition,1,2,3\n'
    assert lines[1] == test
