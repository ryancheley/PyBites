from datetime import timedelta, datetime
from typing import List
import string

text1 = """
1
00:00:00,498 --> 00:00:02,827
Beautiful is better than ugly. #25

2
00:00:02,827 --> 00:00:06,383
Explicit is better than implicit. #28

3
00:00:06,383 --> 00:00:09,427
Simple is better than complex. #25
"""
text2 = """
18
00:01:12,100 --> 00:01:17,230
If you want a bit more minimalistic view, you can actually hide the sidebar.

19
00:01:18,200 --> 00:01:19,500
If you go to Settings

20
00:01:23,000 --> 00:01:26,150
scroll down to 'Focus Mode'.

21
00:01:28,200 --> 00:01:35,180
You can actually hide the sidebar and have only the description and the code editor.
"""  # noqa E501

text4 = '\n'.join(text2.splitlines()[5:])


def get_srt_section_ids(text: str) -> List[int]:
    result_list = []
    list_item = text.split('\n')
    for i, item in enumerate(list_item):
        if i > 0 and '-->' in item:
            speech_length = (datetime.strptime(item.split('-->')[1].strip(), '%H:%M:%S,%f') -
              datetime.strptime(item.split('-->')[0].strip(), '%H:%M:%S,%f'))
            result_list.append((
                sum(c in string.ascii_letters for c in list_item[i+1]) / speech_length.total_seconds(),
                int(list_item[i-1])
            ))
    result_list = sorted(result_list, key=lambda result_list: result_list[0], reverse=True)
    return [i[1] for i in result_list]


print(get_srt_section_ids(text1))
