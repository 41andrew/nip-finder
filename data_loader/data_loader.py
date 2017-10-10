import os
from model.entity import Entity
import tkinter as tk
from tkinter import filedialog

class CsvDataLoader:

    def __init__(self):
        root = tk.Tk()
        root.withdraw()
        self.data_path_input = "matcher/entities_to_match.csv"
        #filedialog.askopenfilename(title='Wybierz plik ze spółkami', filetypes=(('csv files', '*.csv'),))
        self.input_entities = {}

    def load_data(self):
        """
        Method responsible for loading data from input csv file

        :return:
        """
        self._add_input_rows_to_dict()

    def _add_input_rows_to_dict(self):

        for line in self._read_lines_from_file(self.data_path_input):
            input_entity = self._parse_object_from_csv_line(line)
            self.input_entities[input_entity.name] = input_entity

    def _read_lines_from_file(self, file_path):

        print("Reading file: {}".format(os.path.abspath(self.data_path_input)))

        try:
            with open(self.data_path_input, 'r', encoding='utf-8', errors='ignore') as source_file:
                return source_file.readlines()
        except FileNotFoundError as e:
            print(e)

    def _parse_object_from_csv_line(self, line):

        try:
            line = line.strip('\n').split(sep=';')
            input_entity = Entity(line[0])

            return input_entity

        except IndexError as e:
            print(e)

    def print_objects(self):

        for x in self.input_entities:
            print(self.input_entities[x].nip_list)

