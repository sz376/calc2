""" This is the csvcalc reader class"""
import time
import os
from csvcalc.csvreader import CSVreader
from csvcalc.csvwriter import CSVwriter
import calc.calculator

# the csvcalc class just contains the methods to obtain data


class Parser:
    """This is the Csv reader class"""

    @staticmethod
    def parse_folder(path):
        """parses the folder where csvs are held"""
        for file in os.listdir(path):
            if file.endswith(".csv"):
                Parser.parse(file)
                os.rename(path + "/" + file, "./done/" + file)

    @staticmethod
    def parse(filename):
        """reads in csv in does operations on the rows"""
        tuples = CSVreader.get_list_of_tuples(filename)
        timestamps = []
        filenames = []
        record_num = []
        operations = []
        results = []
        for i, tup in enumerate(tuples):
            calc.calculator.Calculator.division(tup)
            if (
                calc.calculator.Calculator.get_last_result_value() == "You can't divide by zero!"

            ):
                print("Divide by zero error!")
                CSVwriter.write_error(
                    time.time(), filename, i, "division", "Divide by zero"
                )
            else:
                timestamps.append(time.time())
                filenames.append(filename)
                record_num.append(i)
                operations.append("division")
                results.append(calc.calculator.Calculator.get_last_result_value())
            timestamps.append(time.time())
            filenames.append(filename)
            record_num.append(i)
            operations.append("addition")
            calc.calculator.Calculator.addition(tup)
            results.append(calc.calculator.Calculator.get_last_result_value())
            timestamps.append(time.time())
            filenames.append(filename)
            record_num.append(i)
            operations.append("subtraction")
            calc.calculator.Calculator.subtraction(tup)
            results.append(calc.calculator.Calculator.get_last_result_value())
            timestamps.append(time.time())
            filenames.append(filename)
            record_num.append(i)
            operations.append("multiplication")
            calc.calculator.Calculator.multiplication(tup)
            results.append(calc.calculator.Calculator.get_last_result_value())
        CSVwriter.write_log(timestamps, filenames, record_num, operations, results)
