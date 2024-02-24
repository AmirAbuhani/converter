# Amir Abu Hani
def conversions():
    conversion_choice = input("Please choose the conversion type:\n temp(F->C) or temp(C->F)\n speed(MPH->KPH)"
                              " or speed(KPH->MPH)\n weight(kg->stone) or weight(stone->kg) or weight(stone->Ibs)"
                              " or weight(Ibs->stone) or weight(kg->Ibs) or weight(Ibs->kg): \n")
    if conversion_choice == "temp(F->C)":
        f_value = int(input("Enter your F value:"))
        c_value = round(9/5 * (f_value - 32), 2)
        print(c_value)
    elif conversion_choice == "temp(C->F)":
        c_input = float(input("Enter your C value:"))
        f_value = ((9 / 5) * c_input) + 32
        print(f_value)
    elif conversion_choice == "speed(MPH->KPH)":
        mph_input = float(input("Enter your MPH speed:"))
        kph_value = mph * 1.60934
        print(kph_value)
    elif conversion_choice == "speed(KPH->MPH)":
        kph_value = float(input("Enter your KPH speed:"))
        mph_value = kph_value / 1.60934
        print(mph_value)
    elif conversion_choice == "weight(kg->stone)":
        kg_value = float(input("Enter your kg weight:"))
        stone_value = kg_value / 6.35029
        print(stone_value)
    elif conversion_choice == "weight(stone->kg)":
        stone_value = float(input("Enter your stone weight:"))
        kg_value = stone_value * 6.35029318
        print(kg_value)
    elif conversion_choice == "weight(stone->Ibs)":
        stone_value = float(input("Enter your stone weight:"))
        Ibs_valuse = stone_value * 14
        print(Ibs_valuse)
    elif conversion_choice == "weight(Ibs->stone)":
        Ibs_value = float(input("Enter your Ibs weight:"))
        stone_value = Ibs_value / 14
        print(stone_value)
    elif conversion_choice == "weight(kg->Ibs)":
        kg_value = float(input("Enter your kg weight:"))
        Ibs_valuse = kg_value * 2.240462
        print(Ibs_valuse)
    else:
        Ibs_value = float(input("Enter your Ibs weight:"))
        kg_value = Ibs_value / 2.240462
        print(kg_value)


conversions()


