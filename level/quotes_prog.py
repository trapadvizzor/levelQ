#напиши здесь свою программу
filename = 'quotes.txt'

with open(filename, 'r', encoding='utf-8') as file:
    content = file.read()

print("Содержимое файла", filename)
print(content)

authors = []
authors.append(input('Кто написал эти строки?'))

with open(filename, 'a', encoding='utf-8') as file:
        file.write(f"\n автор - {authors[-1]}\n")

something_else = input('Хотите добавить ещё одну цитату?')
something_else = something_else.replace(" ", "")

while something_else.lower() != 'нет':
    content = input('Введите цитату:')
    authors.append(input('Введите автора цитаты:'))

    with open(filename, 'a', encoding='utf-8') as file:
        file.write(f"\n{content}\n")
        file.write(f"\nавтор - {authors[-1]}\n")
    something_else = input('Хотите добавить ещё одну цитату?')
    something_else = something_else.replace(" ", "")

print('Авторы цитат в файле:')
for author in authors:
    print(f"\n{author}\n")
