from script.data_creation import create_data


class Master_Data:

    def __init__(self):
        self.order_entities = ['inventoryonhand']

    def create_data(self):
        create_data(self.order_entities, '1000', 1)


x = Master_Data()
x.create_data()
