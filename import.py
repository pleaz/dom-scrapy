from pymongo import MongoClient
import csv

client = MongoClient('localhost', 27017)
db = client.parsing
collection = db.villa
with open('export.csv', mode='w') as csv_file:
    fieldnames = ['_id', 'name', 'id', 'images', 'first_image', 'second_image', 'Количество спален', 'Веранда',
                  'Тренажерный зал', 'Общая площадь', 'Эркер', '3 спальни', 'Терраса', 'Мансардный этаж',
                  'Количество комнат', 'Балкон', 'Цоколь', 'Бассейн', 'Балконы', 'На 2 семьи (Дуплекс)', 'Гарабитры',
                  'Камин', 'Чердак', 'Гараж', 'Навес для авто', 'Кухня - гостиная', 'Этажность', 'Количество с/у',
                  'Особенности', 'Котельная', 'Второй свет', 'Сауна', 'Чердачное помещение', 'Терраса-солярий',
                  'Гараж-навес', 'Габариты', 'Особенность', 'Цокольный этаж', 'Мансарда', 'Зимний сад', 'Дюрисол',
                  'Кирпич', 'Велокс', 'Газобетон', 'Каркас']
    writer = csv.DictWriter(csv_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL, fieldnames=fieldnames)
    writer.writeheader()
    # props = set()
    for doc in collection.find():
        # new = []
        # for fields in fieldnames:
            # new.append('')
        all_props = {}

        for prop in doc['props'].items():
            for item in prop:
                if type(item) is dict:
                    prop_name = item['name'].replace(':', '').strip()
                    if 'value' in item:
                        prop_value = item['value'].strip()
                        all_props[prop_name] = prop_value
                    else:
                        all_props[prop_name] = ''
                    # prop_index = fieldnames.index(prop_name)
                    # new.insert(prop_index, item['value'].replace(':', '').strip())

        for price in doc['price'].items():
            for item in price:
                if type(item) is dict:
                    price_name = item['name'].replace(':', '').strip()
                    if 'value' in item:
                        price_value = item['value'].strip()
                        all_props[price_name] = price_value
                    else:
                        all_props[price_name] = ''

        all_props['_id'] = doc['_id']
        all_props['name'] = doc['name']
        all_props['id'] = doc['id']
        all_props['first_image'] = doc['images'][0]
        all_props['second_image'] = doc['images'][1]

        for image in doc['images']:
            all_props['images'] = image
            writer.writerow(all_props)

    # block for getting unique props
        # for prop in doc['props'].items():
        # for item in prop:
        # if type(item) is dict:
        # props.add(item['name'].replace(':', '').strip())
