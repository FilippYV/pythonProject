from Motherboards import Motherboards

class Bace_of_Motherboards(Motherboards):
    def __init__(self, chip_set):
        self.chip_set = chip_set

    def print_bace(self):
        print(f'cpu={self.chip_set}, price={self.chip_set}')

    def return_data(self):
        return self.chip_set


