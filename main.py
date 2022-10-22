from INTEL import INTEL

if __name__ == '__main__':
    Motherboard0 = INTEL(cpu='INTEL', price=16000, brand='MSI', model='PRO', generation='1700', chip_set='H')
    Motherboard1 = INTEL(cpu='INTEL', price=16000, brand='MSI', model='PRO', generation='1700', chip_set='H')


    # def save_json(new_data: dict):
    #     '''
    #     записываем пользователей в json
    #     '''
    #     with open(filename, 'w', encoding='utf-8') as file:
    #         data = json.dumps(new_data)
    #         file.write(data)

    def sravnenie():
        print(Motherboard0.return_data())
        print(Motherboard1.return_data())
        if Motherboard0.return_data() == Motherboard1.return_data():
            Motherboard0.out_data()
            Motherboard1.out_data()
            print("Sucsefull")


    sravnenie()
