import json
import unicodedata
from aplicatie2.spider.spider import titles, years, ratings

encoding = "utf-8"


def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    return only_ascii


def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)


path = './'
fileName = 'movies'

number_of_dictionaries = len(titles)

list_of_dictionaries = [dict() for number in range(number_of_dictionaries)]

for dictionary in list_of_dictionaries:
    dictionary['model'] ='aplicatie2.Movies'
    dictionary['fields'] = {}
    index = list_of_dictionaries.index(dictionary)
    title = remove_accents(titles[index])
    dictionary['fields']['title'] = title.decode(encoding)
    dictionary['fields']['year'] = years[index][1:-1]
    dictionary['fields']['rating'] = ratings[index]

writeToJSONFile(path, fileName, list_of_dictionaries)
