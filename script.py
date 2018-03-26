import chardet


def get_data(filename):
    with open(filename, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        s = data.decode(result['encoding'])
        s = s.replace('\n', '')
    return s


def print_top_ten(filename):
    data = get_data(filename)
    word_list = data.split(' ')

    short_list = [word.lower() for word in word_list if len(word) >= 6]
    frequency_of_words = dict()
    for word in short_list:
        if word not in frequency_of_words:
            frequency_of_words[word] = 1
        else:
            frequency_of_words[word] += 1
    items = [(v, k) for k, v in frequency_of_words.items()]
    sorted_items = sorted(items, key=lambda x: x[1], reverse=True)
    top_ten = sorted_items[:10]
    print('топ 10 самых часто встречающихся в новостях слов длиннее 6 символов в файле {}:'.format(filename))
    for k, v in top_ten:
        print('\t{0} - {1} раз'.format(v, k))


print_top_ten('newsafr.txt')
print('\n')
print_top_ten('newscy.txt')
print('\n')
print_top_ten('newsfr.txt')
print('\n')
print_top_ten('newsit.txt')
