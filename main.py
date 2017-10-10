from model.entity import Entity
from data_loader.data_loader import CsvDataLoader

if __name__ == "__main__":

    data_loader = CsvDataLoader()
    data_loader.load_data()
    data_loader.print_objects()