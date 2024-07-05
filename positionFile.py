import io
from pprint import pprint

file_name = 'SpicokPosFile.txt'
strings = ['Text for tell.', 'Используйте кодировку utf-8.', 'Because there are 2 languages!', 'Спасибо!']
strings_positions = {}
count = 0
def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='UTF-8')
    for i in strings:
        global count
        count += 1
        strings_positions[(count, file.tell())] = i
        file.write(i + '\n')
    file.closed
    return


result = custom_write('SpicokPosFile.txt', strings)
for elem in strings_positions.items():
    print(elem)



