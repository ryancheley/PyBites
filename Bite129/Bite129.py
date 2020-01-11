import requests
from collections import defaultdict

STOCK_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/stocks.json'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(STOCK_DATA).json()


# your turn:

def _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off and multiple by 1,000 and return
         value as float"""
    result = 0
    if cap == 'n/a':
        return result
    else:
        if cap[-1] == 'M':
            result = float(cap[1:-1])
        else:
            result = float(cap[1:-1]) * 1000
            result = int(result)
        return result


def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""
    cap_value_list = []
    for d in data:
        if d.get('industry') == industry:
            cap_value_list.append(_cap_str_to_mln_float(d.get('cap')))
    total_cap = sum(cap_value_list)
    return float("%.2f" % total_cap)


def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""
    cap_list = []
    for d in data:
        cap_list.append((_cap_str_to_mln_float(d.get('cap')), d.get('symbol')))
    result = sorted(cap_list)[-1][1]
    return result


def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    d = defaultdict(int)
    sector_list = []
    for item in data:
        if item.get('sector') != 'n/a':
            sector_list.append(item.get('sector'))

    for k in sector_list:
        d[k] +=1

    return max(d, key=d.get), min(d, key=d.get)


g = get_sectors_with_max_and_min_stocks()
print(g)