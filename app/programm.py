import json

file_data = "../static/data.json"
file_bace = "../static/data_bace_of_motherboard.json"


def save_json(new_data: dict, file_name):
    """
    записываем пользователей в json
    """
    with open(file_name, 'w', encoding='utf-8') as file:
        data = json.dumps(new_data)
        file.write(data)


def read_json(file_name):
    """
    читам json файл с пользователями
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        return json.load(file)


def main():
    database = read_json(file_bace)
    bace_of_motherboard = []
    chipset_of_motherboard = []
    z_chipset = []
    h_chipset = []
    x_chipset = []
    b_chipset = []
    intel = []
    amd = []
    for i in database:
        if i["cpu"] == "INTEL":
            bace_of_motherboard.append(i)
            chipset_of_motherboard.append(i)
            intel.append(i)
        if i["cpu"] == "AMD":
            bace_of_motherboard.append(i)
            chipset_of_motherboard.append(i)
            amd.append(i)
        if i["chip"] == "X":
            bace_of_motherboard.append(i)
            chipset_of_motherboard.append(i)
            x_chipset.append(i)
        if i["chip"] == "B":
            bace_of_motherboard.append(i)
            chipset_of_motherboard.append(i)
            b_chipset.append(i)
        if i["chip"] == "H":
            bace_of_motherboard.append(i)
            chipset_of_motherboard.append(i)
            h_chipset.append(i)
        if i["chip"] == "Z":
            bace_of_motherboard.append(i)
            chipset_of_motherboard.append(i)
            z_chipset.append(i)


# print(read_json())
def out():
    print("| bace_of_motherboard | chipset_of_motherboard "
          "|\n| z_chipset | h_chipset | x_chipset | b_chipset |\n| intel | amd |")
    level = input("Выберете уровень: ")
    print("\nСлоты:")
    data = read_json(file_data)[level][0]
    for i in data:
        if data[i] != "False":
            print(data[i])
    slot = input("Выберете слот: ")
    print()
    print(">= | = | <=")
    sign = input("Знак - ")
    meaning = input("Значение - ")
    print()
    database = read_json(file_bace)
    if sign == '=':
        for i in database:
            if i[slot] == meaning:
                where(i, slot, meaning)
    elif sign == '>=' and slot == 'value':
        for i in database:
            if i[slot] >= int(meaning):
                where(i, slot, meaning)
    elif sign == '<=' and slot == 'value':
        for i in database:
            if i[slot] <= int(meaning):
                where(i, slot, meaning)


def where(data, slot, meaning):
    print()
    for i in data:
        print(i, ' - ', data[i], end=' | ')
    print()
    base = ["chipset_of_motherboard", "chipset_of_motherboard"]
    if data["cpu"] == 'INTEL':
        base.append("intel")
    if data["cpu"] == 'AMD':
        base.append("amd")
    if data["chip"] == 'X':
        base.append("x_chipset")
    if data["chip"] == 'B':
        base.append("b_chipset")
    if data["chip"] == 'Z':
        base.append("z_chipset")
    if data["chip"] == 'H':
        base.append("h_chipset")
    for i in base:
        print(i, end=' | ')
    print()
    print("=" * 50)
    # for i in data_json:
    #     if data_json[i] != "False":
    #         print(data_json[i])


if __name__ == '__main__':
    out()
