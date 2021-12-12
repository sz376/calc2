"""Testing the Reader"""
import pandas as pd

def test_csv_to_json():
    """testing the csv to json method"""
    # pylint: disable=line-too-long
    my_dict = {'time': {0: 123}, 'operation': {0: 'addition'}, 'value1': {0: 1}, 'value2': {0: 2}, 'result': {0: 3}}
    data_frame = pd.read_csv("./results/log.csv")
    data_dict = data_frame.to_dict()
    print(data_dict)
    assert data_dict == my_dict
