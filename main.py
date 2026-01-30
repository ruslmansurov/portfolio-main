# from animals.cat import Cat

# cat_1 = Cat("Abc", 32)
# cat_1.say_age()



ph_list = []
n_list = []
k_list = []

with open("data.txt", encoding="utf-8") as file:
    for line in file:
        line = line.strip()

        # Игнорируем пустые строки и маркер конца данных
        if not line or line == "#КОНЕЦ_ДАННЫХ":
            continue

        parts = line.split()

        try:
            ph = float(parts[0])
        except:
            continue

        # Проверка диапазона pH
        if ph < 3.5 or ph > 9.0:
            continue

        # Азот (N)
        if len(parts) > 1:
            n = float(parts[1])
        else:
            n = -99.0

        # Калий (K)
        if len(parts) > 2:
            k = float(parts[2])
        else:
            k = -99.0

        ph_list.append(ph)
        n_list.append(n)
        k_list.append(k)

print(f"pH:{ph_list}")
print(f"N:{n_list}")
print(f"K:{k_list}")
