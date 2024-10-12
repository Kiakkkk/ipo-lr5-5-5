s = input("Введите строку: ") #ввод строки
s = s.split()
k = 0
for i in s:
    k += 1 if i == "Python" else 0
print(f"Слово 'Python' встречается в строке {s.count("Python")} раз")