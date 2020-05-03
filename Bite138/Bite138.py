class Animal:
    zoo_list = []

    def __init__(self, name):
        self.name = name.capitalize()
        self.zoo_list.append(f'{len(self.zoo_list)+10001}. {self.name}')

    def __str__(self):
        display = f'{len(self.zoo_list)+10000}. {self.name}'
        return display

    @classmethod
    def zoo(cls):
        return cls.zoo_list
