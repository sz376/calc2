""" This is the csvcalc reader class"""
import pandas as pd

# the csvcalc class just contains the methods to obtain data


class CSVreader:
    """ This is the Csv reader class"""

    @staticmethod
    def get_list_of_tuples(filename):
        """reads in csv and returns a list of tuples"""
        data_frame = pd.read_csv("./input/"+filename)
        records = data_frame.to_records(index=False)
        list_of_tuples = list(records)
        return list_of_tuples

    @staticmethod
    def get_dataframe(filename):
        """ returns just the dataframe """
        data_frame = pd.read_csv("./input/" + filename)
        return data_frame
