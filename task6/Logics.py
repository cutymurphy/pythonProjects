with open('DEF-9xx.csv', 'r', encoding='UTF-8') as File:
    array = [row.split(';') for row in File]
array = array[1:]


def find_information(telephone):
    code = telephone[1:4]
    main_digits = telephone[4:]

    for row in array:
        if row[0] == code and row[1] <= main_digits <= row[2]:
            return row[4], row[5], row[6], row[7]
    return 0
