from decimal import *
def check_split(item_total, tax_rate, tip, people):
    """Calculate check value and evenly split.

       :param item_total: str (e.g. '$8.68')
       :param tax_rate: str (e.g. '4.75%)
       :param tip: str (e.g. '10%')
       :param people: int (e.g. 3)

       :return: tuple of (grand_total: str, splits: list)
                e.g. ('$10.00', [3.34, 3.33, 3.33])
    """
    item_total_float = Decimal(item_total[1:]).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)
    tax_rate_float = Decimal(tax_rate[:-1]).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)
    tip_float = Decimal(tip[:-1]).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)
    total_with_tax = Decimal(item_total_float * (1 + tax_rate_float / 100)).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)
    total_with_tip_post_tax = Decimal(total_with_tax * (1 + tip_float/100)).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)
    per_person = Decimal(total_with_tip_post_tax / people).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)
    extra = total_with_tip_post_tax - per_person * people
    per_person_list = [round(per_person, 2)] * people
    per_person_list[0] = per_person_list[0] + extra
    total = round(sum(per_person_list), 2)

    # return item_total_float, tax_rate_float, tip_float, total_with_tax, total_with_tip_post_tax\
    #     , per_person, extra, per_person_list, total

    return '${:,.2f}'.format(total), per_person_list

