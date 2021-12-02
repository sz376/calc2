""" This is the csvcalc writer class"""
import pandas as pd

# the csvcalc class just contains the methods to obtain data


class CSVwriter:
    """This is the Csv writer class"""

    @staticmethod
    def write_log(timestamps, filenames, record_num, operations, results):
        """writes to csv"""
        data_frame = pd.DataFrame(
            {
                "time stamp": timestamps,
                "file name": filenames,
                "record_num": record_num,
                "operation": operations,
                "results": results,
            }
        )
        data_frame.to_csv("./results/log.csv", index=False, mode="a", header=False)

    @staticmethod
    def write_error(timestamp, filename, record_num, operation, error):
        """writes to error log"""
        data_frame = pd.DataFrame(
            {
                "time stamp": [timestamp],
                "file name": [filename],
                "record_num": [record_num],
                "operation": [operation],
                "error": [error],
            }
        )
        data_frame.to_csv(
            "./results/error_log.csv", index=False, mode="a", header=False
        )
