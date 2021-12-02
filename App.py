""" the main driver program for the csv reader """
from csvcalc.parser import Parser

CSV_PATH= './input'
Parser.parse_folder(CSV_PATH)
