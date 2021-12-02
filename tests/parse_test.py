"""Testing the Parser"""
from csvcalc.parser import Parser

def test_parse():
    """testing that parsing is working"""
    Parser.parse_folder("./testcsvs")
    with open('./results/log.csv',encoding="utf8") as file:
        lines = file.readlines()
    assert lines[3][-2:] == '0\n'
