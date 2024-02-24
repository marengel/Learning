user = -1
table = []

def calculate_fosfor():
    result_fosfor = int(input("Podaj wynik badania fosforu [g/m2]: "))
    fosfor = 60.0
    if result_fosfor != fosfor:
        print("Odchylenie od zasobności optymalnej P g/m2: ", result_fosfor - fosfor)
    diferencesP = (result_fosfor - fosfor)
    if diferencesP < 0:
        
        dose = ((diferencesP * (-0.2)) * 2.3)
        fosfor_dose = ("Konieczne jest dodatkowe nawożenie Fosforem P2O5 w ilości (g/m2) ", str(dose))
        table.append(fosfor_dose)
        print(table)
        print("Konieczne jest dodatkowe nawożenie w dawce: ", dose, "g/m2 P2O5")
    elif diferencesP < 31:
        print("Nawożenie jest zbędne: ")
    else:
        print("Zasobność jest zbyt wysoka - konieczne jest dodanie torfu niskiego lub kompostu: ")

def calculate_azot():
    result_azot = int(input("Podaj wynik badania azotu: "))
    azot = 90.0
    diferenceN = result_azot - azot
    if diferenceN < 0:
        doseN = (diferenceN * (-0.2))
        nitrogen_dose = ("Azot w g/m2 ", str(doseN))
        table.append(nitrogen_dose)
      #  print(table)
        print("Konieczne jest dodatkowe nawożenie azotowe w ilości: ", doseN, "g/m2")
    else:
        print("Nawożenie nie jest konieczne: ")

def show_results_table():
    print(table)
    #index_recomendation = 1
    for index, doses in enumerate(table, start=1):
        print(f'[{index}] {doses}')
        #print(fosfor_dose + Nitrogen_dose + "["+ str(index_recomendation) + "]")
        #index_recomendation += 1

def delete_recomendation():
    index_to_delete = int(input("Wpisz indeks zalecenia do usunięcia: ")) - 1
    
    if index_to_delete < 0 or index_to_delete > len(table) -1:
        print("nie ma takiego zalecenia: ")
    else:
        table.pop(index_to_delete)
        print("zalecenie usunięto: ")
        
def save_recomendation_to_file():
    with open("table.txt", "w") as file:
        for f, a in table:
            file.write(f"{f}{a}\n")

def load_recomendation_from_file():
    file = open("table.txt")
    for line in file.readlines():
        print(line)
    file.close()

while user != 7:
    print("1. Policz potrzeby nawozowe dla fosforu")
    print("2. Policz potrzeby nawozowe dla azotu: ")
    print("3. Pokaż tabelę z dawkami: ")
    print("4. zapisz do pliku: ")
    print("5. Pokaż zapisane dawki")
    print("6. Usuń zalecenie: ")
    print("7. Wyjdź: ")
    if user == 1:
        calculate_fosfor()
    if user == 2:
        calculate_azot()
    if user == 3:
        show_results_table()
    if user == 4:
        save_recomendation_to_file()
    if user == 5:
        load_recomendation_from_file()
    if user == 6:
        delete_recomendation()
    
    user = int(input("Wpisz liczbę: "))
