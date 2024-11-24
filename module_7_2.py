def custom_write(file_name, strings):
    file = open(file_name, 'w+', encoding='utf-8')
    dict_ = dict()
    for i in range((len(strings))):
        dict_[(i + 1, file.tell())] = strings[i]
        file.write(strings[i] + '\n')
    file.close()
    return dict_

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]
result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)