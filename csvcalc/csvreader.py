""" This is the csvcalc reader class"""
import pandas as pd
# the csvcalc class just contains the methods to obtain data

class CSVreader:
    # pylint: disable=too-few-public-methods
    """ This is the Csv reader class"""

    @staticmethod
    def csv_to_json():
        """ returns just the dataframe """
        data_frame = pd.read_csv("./results/log.csv")
        data_dict = data_frame.to_dict()
        return data_dict
