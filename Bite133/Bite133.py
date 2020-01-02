import re

original_links = [
    ('https://www.amazon.com/War-Art-Through-Creative-Battles/dp/1936891026/'
     '?keywords=war+of+art'),
    ('https://amazon.com/War-Art-Through-Creative-Battles/dp/1936891026/'
     'ref=sr_1_1'),
    ('https://www.amazon.es/War-Art-Through-Creative-Battles/dp/1936891026/'
     '?qid=1537226234'),
     'https://www.amazon.co.uk/Pragmatic-Programmer-Andrew-Hunt/dp/020161622X',
    ('https://www.amazon.com.au/Python-Cookbook-3e-David-Beazley/dp/'
     '1449340377/'),
    ('https://www.amazon.com/fake-book-with-longer-asin/dp/'
     '1449340377000/'),
]  # noqa E501
result_links = [
    'http://www.amazon.com/dp/1936891026/?tag=pyb0f-20',
    'http://www.amazon.com/dp/1936891026/?tag=pyb0f-20',
    'http://www.amazon.com/dp/1936891026/?tag=pyb0f-20',
    'http://www.amazon.com/dp/020161622X/?tag=pyb0f-20',
    'http://www.amazon.com/dp/1449340377/?tag=pyb0f-20',
    'http://www.amazon.com/dp/1449340377000/?tag=pyb0f-20',
]


def generate_affiliation_link(url):
    start_of_id = re.search('\/\d+[A-Z]?\/?', url).span()[0]
    end_of_id = re.search('\/\d+[A-Z]?\/?', url).span()[1]
    id = url[start_of_id:end_of_id].replace('/', '')
    sufix = '?tag=pyb0f-20'
    afiliate_link = 'http://www.amazon.com/dp/'+id+'/'+sufix
    return afiliate_link


i = 0

t = generate_affiliation_link(original_links[i])

print(t)
print(result_links[i])

print(result_links[i] == t)