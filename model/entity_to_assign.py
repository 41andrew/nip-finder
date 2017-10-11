

class EntityToMatch:

    def __init__(self, name, nip):
        self.name = name
        self.nip = nip

    def __str__(self):
        return "[{0.name}][{0.nip}]".format(self)