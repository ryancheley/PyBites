# nice snippet: https://gist.github.com/tonybruess/9405134
from collections import namedtuple
import re

social_platforms = """Twitter
  Min: 1
  Max: 15
  Can contain: a-z A-Z 0-9 _

Facebook
  Min: 5
  Max: 50
  Can contain: a-z A-Z 0-9 .

Reddit
  Min: 3
  Max: 20
  Can contain: a-z A-Z 0-9 _ -
"""

# note range is of type range and regex is a re.compile object
Validator = namedtuple('Validator', 'range regex')


def parse_social_platforms_string():
    """Convert the social_platforms string above into a dict where
       keys = social platformsname and values = validator namedtuples"""

    # Get the Social Platform Names into a list

    social_platform_names = re.findall(r'[A-Z][a-z]*\n', social_platforms)
    social_platform_names_final = []
    for s in social_platform_names:
        social_platform_names_final.append(s.replace('\n', ''))

    # Get the Social Platform Character Ranges into a list

    range_min = re.findall('\d+', ';'.join(re.findall(r'Min: \d+', social_platforms)))
    range_max = re.findall('\d+', ';'.join(re.findall(r'Max: \d+', social_platforms)))
    social_platform_range = []
    for i in range(len(range_min)):
        social_platform_range.append(range(int((range_min[i])), int(range_max[i])))

    # Get the Social Platform valid chars into a list

    social_platform_valid_chars = []
    social_platform_valid = re.findall(r'Can contain: .*', social_platforms)
    for s in social_platform_valid:
        social_platform_valid_chars.append(re.compile('['+s.replace('Can contain: ', '').replace(' ', '')+']*'))

    # create the dictionary
    social_platform_dict = {}
    for i in range(len(social_platform_names_final)):
        social_platform_dict[social_platform_names_final[i]] = Validator(social_platform_range[i],
                                                                         social_platform_valid_chars[i])

    return social_platform_dict


def validate_username(platform, username):
    """Receives platforms(Twitter, Facebook or Reddit) and username string,
       raise a ValueError if the wrong platform is passed in,
       return True/False if username is valid for entered platform"""
    all_validators = parse_social_platforms_string()
    result = False
    if platform not in all_validators:
        raise ValueError

    if len(username) in all_validators[platform].range \
            and re.search(all_validators[platform].regex, username).group() == username:
        result = True

    return result