"""Testing the Reader"""
from csvcalc.csvreader import CSVreader

def test_csv_to_json():
    """testing the csv to json method"""
    # pylint: disable=line-too-long
    my_dict = {'time': {0: 123}, 'operation': {0: 'addition'}, 'value1': {0: 1}, 'value2': {0: 2}, 'result': {0: 3}}
    data_frame = CSVreader.csv_to_json()
    assert data_frame == my_dict
