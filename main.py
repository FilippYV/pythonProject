from Motherboards import Motherboards
from Bace_of_Motherboards import Bace_of_Motherboards
from INTEL import INTEL

if __name__ == '__main__':
    i1 = INTEL('INTEL', 25000, 'ASUS', 'ROG STRIX', '1700', 'Z')
    print(i1.out_data())


    #__init__(self, cpu, price, brand, model, generation, chip_set):