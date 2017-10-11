import os
from model.entity_to_assign import EntityToMatch
import tkinter as tk
from tkinter import filedialog

class EmisLoader():

    def __init__(self):
        self.all_emis_entities = {}
        self.data_path_input = "source_files/all_entities.csv"

    def get_all_emis_entities(self):
        return self.all_emis_entities

    def load_data(self):

        self._add_input_rows_to_dict()

    def _add_input_rows_to_dict(self):

        for line in self._read_lines_from_file(self.data_path_input):
            emis_entity = self._parse_object_from_csv_line(line)
            self.all_emis_entities[emis_entity.name] = emis_entity

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
            emis_entity = EntityToMatch(name=line[0], nip=line[1])

            return emis_entity

        except IndexError as e:
            print(e)

    def print_emis_entities(self):

        for entity in self.all_emis_entities:
            print (entity, " : ", self.all_emis_entities[entity])