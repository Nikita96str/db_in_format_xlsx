import pandas as pd

test_file = 'test.xlsx'
xl = pd.ExcelFile(test_file)
df = xl.parse()

# Укажите регион, с наибольшим средним чеком покупок, совершенных за январь:
# Получение уникального списка стран
global set_country
set_country = set()

def func_set_country(country):
    set_country.add(country)
df['country_name'].apply(func_set_country)
list_country = list(set_country)
list_country.sort()
# print(list_country)

# Создаем новый столбец mounth 
def func_create_mounth(date):
    date = str(date)
    if date[5:7] == '01':
        return 'January'
    elif date[5:7] == '02':
        return 'February'
    elif date[5:7] == '03':
        return 'March'
    elif date[5:7] == '04':
        return 'April'
    elif date[5:7] == '05':
        return 'May'
    elif date[5:7] == '06':
        return 'June'
    elif date[5:7] == '07':
        return 'June'
    elif date[5:7] == '08':
        return 'August'
    elif date[5:7] == '09':
        return 'September'
    elif date[5:7] == '10':
        return 'October'
    elif date[5:7] == '11':
        return 'November'
    elif date[5:7] == '12':
        return 'December'
    else:
        return 0

df['mounth'] = df['date'].apply(func_create_mounth)

# Получаем средний чек по городу за январь
dict_mean_cheque = dict()
for country in list_country:
    jan_mean_cheque = df[(df['status'] == 1)&(df['mounth']=='January')&(df['country_name']==country)]['cheque'].mean()
    if str(jan_mean_cheque) == 'nan':
        jan_mean_cheque = 0
    dict_mean_cheque[country] = jan_mean_cheque
# print('Средний чек за январь по всем странам', dict_mean_cheque)

country_best_cheque = ''
value_best_cheque = 0 
for country in dict_mean_cheque:
    if dict_mean_cheque[country] > value_best_cheque:
        value_best_cheque = dict_mean_cheque[country]
        country_best_cheque = country
print('Страна с наибольшим средним чеком за январь: ', country_best_cheque, value_best_cheque)

# Найдите регион с самым высоким числом успешных покупок за весь заданный период и в ответе укажите число этих покупок.
# Получаем количество покупок в каждой стране 
dict_purchases = dict()
for country in list_country:
    value = len(df[(df['status'] == 1)&(df['country_name']==country)])
    if str(value) == 'nan':
        value = 0
    dict_purchases[country] = value
# print('Среднее количество покупок по всем странам за указанный период', dict_purchases)

#  Находим регион с самым высоким числом успешных покупок за весь заданный период
country_max_purchases = ''
value_max_purchases = 0 
for country in dict_purchases:
    if dict_purchases[country] > value_max_purchases:
        value_max_purchases = dict_purchases[country]
        country_max_purchases = country
print('Страна с наибольшим количеством покупок: ', country_max_purchases, value_max_purchases)
