from dateutil.parser import *

MAC1 = """
reboot    ~                         Wed Apr 10 22:39
reboot    ~                         Wed Mar 27 16:24
reboot    ~                         Wed Mar 27 15:01
reboot    ~                         Sun Mar  3 14:51
reboot    ~                         Sun Feb 17 11:36
reboot    ~                         Thu Jan 17 21:54
reboot    ~                         Mon Jan 14 09:25
"""
MAC2 = """
reboot ~ Tue Sep 22 12:52
reboot ~ Sun Aug 30 23:17
reboot ~ Sat Aug 29 01:12
reboot ~ Fri Aug 28 22:07
"""
MAC3 = """
reboot    ~                         Fri Dec 18 23:58
reboot    ~                         Mon Dec 14 09:54
reboot    ~                         Wed Dec 11 23:21
reboot    ~                         Tue Nov 17 21:52
reboot    ~                         Tue Nov 17 06:01
reboot    ~                         Wed Nov 11 12:14
reboot    ~                         Sat Oct 31 13:40
reboot    ~                         Wed Oct 28 15:56
reboot    ~                         Wed Oct 28 11:35
reboot    ~                         Tue Oct 27 00:00
reboot    ~                         Sun Oct 18 17:28
reboot    ~                         Sun Oct 18 17:11
reboot    ~                         Mon Oct  5 09:35
reboot    ~                         Sat Oct  3 18:57
"""


def calc_max_uptime(reboots):
    """Parse the passed in reboots output,
       extracting the datetimes.

       Calculate the highest uptime between reboots =
       highest diff between extracted reboot datetimes.

       Return a tuple of this max uptime in days (int) and the
       date (str) this record was hit.

       For the output above it would be (30, '2019-02-17'),
       but we use different outputs in the tests as well ...
    """
    reboot_list = reboots.split('\n')
    reboot_times = []
    for r in reboot_list:
        try:
            reboot_times.append(parse(r.split('~')[1].lstrip()))
        except IndexError:
            pass
    reboot_final = []

    for i in range(len(reboot_times)):
        try:
            display_date = reboot_times[i].date().strftime('%Y-%m-%d')
            reboot_final.append(((reboot_times[i] - reboot_times[i + 1]).days, display_date))
        except IndexError:
            pass

    return sorted(reboot_final, key=lambda x: x[0], reverse=True)[0]

c = calc_max_uptime(MAC1)
print(c)