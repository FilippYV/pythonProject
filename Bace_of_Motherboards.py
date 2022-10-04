from Motherboards import Motherboards

class Bace_of_Motherboards(Motherboards):
    def __init__(self, cpu, price):
        self.cpu = cpu
        self.price = price

    def print_b_of_m(self):
        print(f'cpu={self.cpu}, price={self.price}')


