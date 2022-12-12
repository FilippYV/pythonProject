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


def transformations(data):
    if data == 'z_chipset':
        data = ["chip", 'Z']
    elif data == 'h_chipset':
        data = ["chip", 'H']
    elif data == 'x_chipset':
        data = ["chip", 'Z']
    elif data == 'b_chipset':
        data = ["chip", 'B']
    elif data == 'intel':
        data = ["cpu", 'INTEL']
    elif data == 'amd':
        data = ["cpu", 'AMD']
    return data


# print(read_json())H
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
    if slot == "value":
        print(">= | = | <=")
        sign = input("Знак - ")
    else:
        sign = '='
    meaning = input("Значение - ")
    if level == "chipset_of_motherboard" or level == "bace_of_motherboard":
        serpch_in_main_class(level, slot, sign, meaning)
    else:
        serpch_in_inherited_class(level, slot, sign, meaning)


def serpch_in_main_class(level, slot, sign, meaning):
    database = read_json(file_bace)
    if sign == '=':
        for i in database:
            if slot == 'value':
                if i[slot] == int(meaning):
                    where(i, level, slot, meaning)
            elif i[slot] == meaning:
                where(i, level, slot, meaning)
    elif sign == '>=' and slot == 'value':
        for i in database:
            if i[slot] >= int(meaning):
                where(i, level, slot, meaning)
    elif sign == '<=' and slot == 'value':
        for i in database:
            if i[slot] <= int(meaning):
                where(i, level, slot, meaning)


def serpch_in_inherited_class(level, slot, sign, meaning):
    level = transformations(level)
    database = read_json(file_bace)
    if sign == '=':
        for i in database:
            if slot == 'value':
                if i[level[0]] == level[1] and i[slot] == int(meaning):
                    where(i, level, slot, meaning)
            elif i[level[0]] == level[1] and i[slot] == meaning:
                where(i, level, slot, meaning)
    elif sign == '>=' and slot == 'value':
        for i in database:
            if i[level[0]] == level[1] and i[slot] >= int(meaning):
                where(i, level, slot, meaning)
    elif sign == '<=' and slot == 'value':
        for i in database:
            if i[level[0]] == level[1] and i[slot] <= int(meaning):
                where(i, level, slot, meaning)


def where(data, level, slot, meaning):
    print()
    for i in data:
        print(i, ' - ', data[i], end=' | ')
    print()
    base = []
    if data["cpu"] == 'INTEL':
        base.append("База плат -> INTEL")
    if data["cpu"] == 'AMD':
        base.append("База плат -> AMD")
    if data["chip"] == 'X':
        base.append("Типы плат -> X чипсет")
    if data["chip"] == 'B':
        base.append("Типы плат -> B чипсет")
    if data["chip"] == 'Z':
        base.append("Типы плат -> Z чипсет")
    if data["chip"] == 'H':
        base.append("Типы плат -> H чипсет")
    for i in base:
        print(i, end=' | ')
    print()
    print("=" * 50)
    # for i in data_json:
    #     if data_json[i] != "False":
    #         print(data_json[i])


if __name__ == '__main__':
    out()
