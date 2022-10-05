from Bace_of_Motherboards import Bace_of_Motherboards


class INTEL(Bace_of_Motherboards):
    def __init__(self, cpu, price, brand, model, generation, chip_set):
        super().__init__(cpu, price)
        self.cpu = cpu
        self.brand = brand
        self.model = model
        self.generation = generation
        self.chip_set = chip_set

    def out_data(self):
        return f'cpu - {self.cpu} \nprice - {self.price} \nbrand - {self.brand} \n' \
               f'model - {self.model} \ngeneration - {self.generation} \nchip_set - {self.chip_set} \n'

    def return_data(self):
        return self.cpu, self.price, self.brand, self.model, self.generation, self.chip_set