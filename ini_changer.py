import configparser
import re
import json

# test_path = {
#     "czech": "\\\\192.168.0.100\\upload\\_AKTUALIZACJE\\instalki\\CAD 3w1\\AKTUALNA\\CZ\\Setup.ini",
#     "deutsch": "\\\\192.168.0.100\\upload\\_AKTUALIZACJE\\instalki\\CAD 3w1\\AKTUALNA\\DE\\Setup.ini",
#     "eng": "\\\\192.168.0.100\\upload\\_AKTUALIZACJE\\instalki\\CAD 3w1\\AKTUALNA\\EN\\Setup.ini",
#     "spain": "\\\\192.168.0.100\\upload\\_AKTUALIZACJE\\instalki\\CAD 3w1\\AKTUALNA\\ES\\Setup.ini",
#     "hun": "\\\\192.168.0.100\\upload\\_AKTUALIZACJE\\instalki\\CAD 3w1\\AKTUALNA\\HU\\Setup.ini",
#     "pol": "\\\\192.168.0.100\\upload\\_AKTUALIZACJE\\instalki\\CAD 3w1\\AKTUALNA\\PL\\Setup.ini",
#     "rus": "\\\\192.168.0.100\\upload\\_AKTUALIZACJE\\instalki\\CAD 3w1\\AKTUALNA\\RU\\Setup.ini",
#     "slov": "\\\\192.168.0.100\\upload\\_AKTUALIZACJE\\instalki\\CAD 3w1\\AKTUALNA\\SK\\Setup.ini",
#     "ukr": "\\\\192.168.0.100\\upload\\_AKTUALIZACJE\\instalki\\CAD 3w1\\AKTUALNA\\UK\\Setup.ini",
# }


def data_check():
    data_file = "./paths_data.json"
    test_path = {
        "test": "\\\\192.168.5.666\\katalog\\katalog\\Setup.ini",
        "test2": "\\\\192.168.5.666\\katalog\\katalog\\Setup.ini",
    }
    try:
        with open(data_file, "r") as f:
            paths = json.load(f)
    except FileNotFoundError:
        with open(data_file, "w") as f:
            json.dump(test_path, f)
        print(
            "Został dodany plik 'paths_data.json' w katalogu programu - proszę uzupełnić ścieżki"
        )
        input()
        exit()
    return paths


def parser_function(file, version, choice, parser):
    parser.optionxform = str
    parser.read(file)
    if choice == "1":
        parser["ICADVERDEF"] = {"DOT4VER": version}
        save_file(file, parser)
    elif choice == "2":
        parser["NAME"] = {"v. " + version: None}
        save_file(file, parser)
    elif choice == "3":
        parser_show(file, parser)


def save_file(file, parser):
    with open(file, "w") as saved_file:
        parser.write(saved_file, space_around_delimiters=False)


def parser_show(file, config):
    var_1 = config.items("NAME")[0][0]
    var_2 = config.items("ICADVERDEF")[0][1]
    print(f"ścieżka: {file}")
    print(f"wersja programu: {var_1}")
    print(f"wersja dot4CADa: {var_2}")
    print()


def validation_checker(par_name, choice, input_v):
    if choice == "1":
        while True:
            x = re.search(r"([0-9.]){14}", input_v)
            if x == None or len(input_v) != 14:
                print("Wpisz prawidłową wartość.")
                input_v = input(f"{par_name} version: ").replace(" ", "")
            else:
                return input_v
    elif choice == "2":
        while True:
            x = re.search(r"([0-9.]){5}", input_v)
            if x == None or len(input_v) != 5:
                print("Wpisz prawidłową wartość.")
                input_v = input(f"{par_name} version: ").replace(" ", "")
            else:
                return input_v


def getting_input(parameter_name, rest_text, choiced_option):
    print(f"Wpisz wersję{parameter_name}, {rest_text}")
    x = input(f"{parameter_name} version: ").replace(" ", "")
    return validation_checker(parameter_name, choiced_option, x)


def executive_function(input, choosen_o):
    for key in paths.keys():
        parser_function(
            paths[key], input, choosen_o, configparser.ConfigParser(allow_no_value=True)
        )
        if choosen_o == "1":
            print(paths[key] + " - plik zaktualizowany, wersja dot4Cada: " + input)
        elif choosen_o == "2":
            print(paths[key] + " - plik zaktualizowany, wersja programu: " + input)


paths = data_check()
while True:
    print("Wybierz parametr do zmiany:")
    print("[1] dot4CAD")
    print("[2] wersja")
    print("[3] pokaż obecne wartości w Setup.ini")
    print("[4] zakończ")
    print()
    choice = input()

    if choice == "1":
        executive_function(
            getting_input(" dot4CADa", "odpowiedni format to: xx.x.xxxx.xxxx", choice),
            choice,
        )
        print()
        continue

    elif choice == "2":
        executive_function(
            getting_input("", "odpowiedni format to: x.x.x", choice), choice
        )
        print()
        continue

    elif choice == "3":
        executive_function("", choice)
        continue

    elif choice == "4":
        break

    else:
        continue
