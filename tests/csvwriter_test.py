"""Testing the Reader"""
import pytest
import pandas as pd
import time
import os
from pandas._testing import assert_frame_equal
from csvcalc.csvwriter import CSVwriter

def test_write_log():
    """testing that pandas reader is working"""
    my_time = ["123"]
    my_filename = ["file"]
    my_rec = [1]
    my_op = ["addition"]
    my_results = [0]
    CSVwriter.write_log(my_time, my_filename, my_rec, my_op, my_results)
    with open('./results/log.csv') as f:
        lines = f.readlines()
    test = ['123,file,1,addition,0\n']
    assert lines == test

def test_write_error_log():
    """testing that pandas reader is working"""
    my_time = "123"
    my_filename = "file"
    my_rec = 1
    my_op = "addition"
    my_results = "error"
    CSVwriter.write_error(my_time, my_filename, my_rec, my_op, my_results)
    with open('./results/error_log.csv') as f:
        lines = f.readlines()
    test = ['123,file,1,addition,error\n']
    assert lines == test
