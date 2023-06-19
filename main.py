import re

#Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print("----------\n")
    expression = re.compile('data')
    chaine = "Bonjour tout le monde !! "
    req = re.search(r"tout", chaine, re.I)

    print(req.group())

    # position de départ en commençant par 0
    print("début: ",req.start())

    # position de fin en commençant par 0
    print("fin: ", req.end())

    # l'interval en commençant par 0
    print(req.span())

    text = """Vous êtes le numéro 123
                le suivant est le 124
                et on terminera à 62222"""
    regex = '\d{3,4}'
    res = re.findall(regex, text)
    print(res)
    print("---------substitute-------")


    res = re.sub(r'\d', "", text)
    print(res)

    res = re.sub(r'\d+', "", text, count=1)
    print(res)

    numero = "0033-6-07-41-47-08"
    print("tel: ", numero)

    regex = "(0|\\+33|0033)( |\\.|-)[1-9]( |\\.|-)([0-9][0-9][ |.|-]?){4}$"

    if re.match(regex, numero) is not None :
        print("Numéro Valide")
    else:
        print("Numéro invalide")
