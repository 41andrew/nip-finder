import pyodbc
from model.entity import Entity
from model.entity_to_assign import EntityToMatch

class CrmDataLoader:

    all_entities = {}

    def __init__(self):
        self.conn = None

    def connect_to_crm(self):

        try:
            self.conn = pyodbc.connect(r'DRIVER={SQL Server};SERVER=plwawdb20,1113;DATABASE=MARS4_API;Trusted_Connection=yes;')
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
            self.all_entities[entity_row[0]].append(entity)
