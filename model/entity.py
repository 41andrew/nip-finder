

class Entity:

    def __init__(self, name):
        self.name = name
        self.nip_list = []

    def __str__(self):
        return "[{0.name}][{0.nip_list}]".format(self)

    def print_assigned_entities(self):
        print("Nazwa spółki: ", self.name)
        for entity in self.nip_list:
            print(entity)