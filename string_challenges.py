# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])
print(20 * '-')

# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))
print(20 * '-')

# Вывести количество гласных букв в слове
word = 'Архангельск'
print(sum(1 for letter in word.lower() if letter in ['е', 'ы', 'а', 'о', 'я', 'и', 'ю']))
print(20 * '-')


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))
print(20 * '-')


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
print(*(word[0][0] for word in sentence.split()), sep='\n')
print(20 * '-')


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
summy = 0
for word in sentence.split():
    summy += len(word)
print(summy / len(sentence.split()))