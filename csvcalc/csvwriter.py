""" This is the csvcalc writer class"""
import pandas as pd
# the csvcalc class just contains the methods to obtain data


class CSVwriter:
    # pylint: disable=too-few-public-methods
    """This is the Csv writer class"""

    @staticmethod
    def write_log(time, operation, value1, value2, result):
        """writes to csv"""
        data_frame = pd.DataFrame(
            {
                "time stamp": [time],
                "operation": [operation],
                "value1": [value1],
                "value2": [value2],
                "results": [result],
            }
        )
        data_frame.to_csv("./results/log.csv", index=False, mode="a", header=False)
