from collections import defaultdict

# fake data from https://www.mockaroo.com
data = """last_name,first_name,country_code
Watsham,Husain,ID
Harrold,Alphonso,BR
Apdell,Margo,CN
Tomblings,Deerdre,RU
Wasielewski,Sula,ID
Jeffry,Rudolph,TD
Brenston,Luke,SE
Parrett,Ines,CN
Braunle,Kermit,PL
Halbard,Davie,CN"""


# cities_by_state = defaultdict(list)
# for state, city in city_list:
#   cities_by_state[state].append(city)

def group_names_by_country(data: str = data) -> defaultdict:
    countries = defaultdict(list)
    items = data.split()
    for i in items:
        if i.split(',')[2] != 'country_code':
            countries[i.split(',')[2]].append(i.split(',')[1]+' '+i.split(',')[0])
    return countries


c = group_names_by_country(data)
print(c)