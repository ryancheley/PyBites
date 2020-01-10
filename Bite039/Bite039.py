from datetime import datetime, timedelta
import os
import re
import urllib.request

# getting the data
COURSE_TIMES = os.path.join(
    os.getenv("TMP", "/tmp"),
    'course_timings'
)
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/course_timings',
    COURSE_TIMES
)


def get_all_timestamps():
    """Read in the COURSE_TIMES and extract all MM:SS timestamps.
       Here is a snippet of the input file:

       Start  What is Practical JavaScript? (3:47)
       Start  The voice in your ear (4:41)
       Start  Is this course right for you? (1:21)
       ...

        Return a list of MM:SS timestamps
    """
    course_list = []
    result = []
    with open(COURSE_TIMES, 'r') as f:
        for line in f:
            course_list.append(line)

    for c in course_list:
        if re.search('\d{1,}\:\d{2}', c):
            time_str = re.search('\d{1,}\:\d{2}', c).group()
            result.append(time_str)

    return result


def calc_total_course_duration(timestamps):
    """Takes timestamps list as returned by get_all_timestamps
       and calculates the total duration as HH:MM:SS"""
    total_seconds = 0
    total_minutes = 0
    for t in timestamps:
        time_object = datetime.strptime(t, '%M:%S').time()
        total_seconds = total_seconds + time_object.second
        total_minutes = total_minutes + time_object.minute
    return str(timedelta(minutes=total_minutes, seconds=total_seconds))
    # return total_minutes, total_seconds


d = calc_total_course_duration(get_all_timestamps())
print(d)
