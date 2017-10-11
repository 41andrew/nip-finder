import pypyodbc
from model.entity import Entity
from model.entity_to_assign import EntityToMatch

class CrmDataLoader:

    all_crm_entities = {}

    def __init__(self):
        self.conn = None

    def get_crm_entities_dict(self):
        return CrmDataLoader.all_crm_entities

    def connect_to_crm(self):

        try:
            self.conn = pypyodbc.connect(r'DRIVER={SQL Server};SERVER=plwawdb20,1113;DATABASE=MARS4_API;Trusted_Connection=yes;')
            print("Connected to CRM")
        except Exception as e:
            print("Unable to connect to the database")
            print("Error msg : {}".format(e))

    def load_data_from_crm(self):

        cursor = self.conn.cursor()

        sql = """SELECT en.EntityName, en.TaxNumber
                 FROM ems.v_Entity en"""

        cursor.execute(sql)

        return cursor.fetchall()

    def create_dict_from_crm_entities(self):

        crm_entities = self.load_data_from_crm()

        for entity_row in crm_entities:
            entity = EntityToMatch(name=entity_row[0], nip=entity_row[1])
            CrmDataLoader.all_crm_entities.update({entity_row[0]:entity})

    def print_all_crm_entities(self):

        for k, v in self.all_crm_entities.items():
            print (k, v)
