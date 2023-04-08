s = input("введите строку :")
array = []
vowels = set("ауоыэяюёие")  # набор гласных
for word in s.split():
    array.append(sum(1 for c in word if c in vowels))

if len(set(array)) == 1:
    print("Парам пам-пам")
else:
    print("Пам парам")
    
