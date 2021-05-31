import base64
import csv
from typing import List  # will remove with 3.9

csv1 = b"""
Zmlyc3RfbmFtZSxsYXN0X25hbWUsY3JlZGl0X2NhcmQKS2VlbGJ5LE1hY0NhZmZlcmt5LD
YzOTM3MTk0MzMzMjk5MjQKTGlubmVsbCxDbGVtbWV0dCwzNTU1NTg0OTI0MDkzOTU0CkVs
eXNoYSxNZWlnaGFuLDYzODU3OTU3OTM4OTcxMDYKS2F0YWxpbixFdGhlcnRvbiwzNTg0Mj
MwMDExNjgwNzAwCkZpbmEsUGFzZWssNTEwMDEzNjYzMTY2NDY4NwpBcmRlbGxhLEJyYXpp
ZXIsMjAxNzEyNjEzNjUzMzc0CkRvcnRoZWEsS2FycGluc2tpLDMwNTAyNjYxMjUxMTcyCl
Jhbm5hLER1ZmYsMzU3NjM5MzA1NjQ5MzMxMgpDaW5uYW1vbixLYWFzbWFuLDU0NDIwMjgx
NTA4MDg1NzAKSmFjbGluLFRvbmdlLDM1NDk4NTIxMDQ3MjQ1MjcK
"""

def get_credit_cards(data: bytes) -> List[str]:
    """Decode the base64 encoded data which gives you a csv
    of "first_name,last_name,credit_card", from which you have
    to extract the credit card numbers.
    """
    returned_data = []
    decoded_data = base64.b64decode(data).decode('utf8').split('\n')
    for cc in decoded_data[1:]:
        if cc:
            returned_data.append(cc.split(',')[-1])
    return returned_data


print(get_credit_cards(csv1))