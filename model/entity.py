

class Entity:

    def __init__(self, name):
        self.name = name
        self.nip_list = []

    def __str__(self):
        return "[{0.name}]".format(self)