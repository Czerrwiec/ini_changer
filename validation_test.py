import re


print("Wpisz wersję dot4CADA, odpowiedni format to xx.x.xxxx.xxxx")
icad_version = input("dot4CAD version: ").replace(" ", "")


while True:
    x = re.search(r"([0-9.]){14}", icad_version)
    if x == None or len(icad_version) != 14:
        print("Wpisz prawidłową wartość.")
        icad_version = input("dot4CAD version: ").replace(" ", "")
    else:
        break
