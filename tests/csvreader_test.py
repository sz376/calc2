"""Testing the Reader"""
import pandas as pd
from pandas._testing import assert_frame_equal
from csvcalc.csvreader import CSVreader

def test_return_tuples():
    """testing that pandas reader is working"""
    in_csv = "testcsv.csv"
    res = CSVreader.get_list_of_tuples(in_csv)
    res = tuple(res[0])
    assert res == (0, 2, 3)

def test_get_dataframe():
    """testing the getting dataframe method"""
    in_csv = "testcsv.csv"
    res = CSVreader.get_dataframe(in_csv)
    data_frame = pd.DataFrame({'value1': [0,1], 'value2': [2,1], 'value3': [3,1]})
    assert_frame_equal(res, data_frame)
