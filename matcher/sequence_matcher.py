from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from data_loader.data_loader import CsvDataLoader
from data_loader.crm_data_loader import CrmDataLoader
from data_loader.emis_data_loader import EmisLoader


class FuzzyMatcher:

    def similarity_checker(self, a, b):
        return fuzz.ratio(a.lower(), b.lower())

    def assign_objects_from_crm(self):

        for entity in CsvDataLoader.input_entities:
            for entity_to_match in CrmDataLoader.all_crm_entities:
                ratio = self.similarity_checker(entity, entity_to_match)
                print ("Porównuję spółkę ", entity, " ze spółką: ", entity_to_match, ". Podobieństwo to: ", ratio, "%")
                if (ratio > 90):
                    CsvDataLoader.input_entities[entity].nip_list.append(CrmDataLoader.all_crm_entities[entity_to_match])
                    print ("Do listy spółki ", entity, " dodaję obiekt: ", CrmDataLoader.all_crm_entities[entity_to_match])

    def assign_objects_from_emis(self):

        for entity in CsvDataLoader.input_entities:
            for entity_to_match in EmisLoader.all_emis_entities:
                ratio = self.similarity_checker(entity, entity_to_match)
                #print ("Porównuję spółkę ", entity, " ze spółką: ", entity_to_match, ". Podobieństwo to: ", ratio, "%")
                if (ratio > 90):
                    CsvDataLoader.input_entities[entity].nip_list.append(EmisLoader.all_emis_entities[entity_to_match])
                    print ("Do listy spółki ", entity, " dodaję obiekt: ", EmisLoader.all_emis_entities[entity_to_match])




