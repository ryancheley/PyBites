'''Extract datetimes from log entries and calculate the time
   between the first and last shutdown events'''
from datetime import datetime
import os
import urllib.request
import re

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def convert_to_datetime(line):
    '''
       Given a log line extract its timestamp and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)'''
    regex = re.compile('\d{4}(-\d{2}){2}T[0-9]{2}(:[0-9]{2}){2}')
    date_time_format = '%Y-%m-%dT%H:%M:%S'
    line_date_time = datetime.strptime(re.search(regex, line).group(), date_time_format)
    return line_date_time



def time_between_shutdowns(loglines):
    '''TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and calculate the
       timedelta between the first and last one.
       Return this datetime.timedelta object.'''
    shutdown_initated = []
    for i in loglines:
        if re.search('Shutdown', i):
            shutdown_initated.append(i)

    diff = convert_to_datetime(shutdown_initated[-1]) - convert_to_datetime(shutdown_initated[0])

    return diff

t = time_between_shutdowns(loglines)
print(t)

