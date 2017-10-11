from model.entity import Entity
from data_loader.data_loader import CsvDataLoader
from data_loader.crm_data_loader import CrmDataLoader
from data_loader.emis_data_loader import EmisLoader
from matcher.sequence_matcher import FuzzyMatcher

if __name__ == "__main__":

    data_loader = CsvDataLoader()
    data_loader.load_data()
    data_loader.print_objects()

    crm_data_loader = CrmDataLoader()
    crm_data_loader.connect_to_crm()
    crm_data_loader.load_data_from_crm()
    crm_data_loader.create_dict_from_crm_entities()
    crm_data_loader.print_all_crm_entities()

    emis_data_loader = EmisLoader()
    emis_data_loader.load_data()
    emis_data_loader.print_emis_entities()

    fuzzy = FuzzyMatcher(data_loader.get_input_enities_dict(), crm_data_loader.get_crm_entities_dict(),
                         emis_data_loader.get_all_emis_entities())

    fuzzy.assign_objects_from_crm()