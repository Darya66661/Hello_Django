#Найти самое длинное слово в строке.
a = "Найти самое длинное слово в строке"
print(max(a.split(), key = len))

#Преобразовать текст в список слов с удалением знаков препинания.
b = "Преобразовать текст в список слов с удалением знаков препинания"
c = list(b)
print(b.split())
