from enum import Enum
from datetime import datetime
from collections import Counter


class DateFormat(Enum):
    DDMMYY = 0  # dd/mm/yy
    MMDDYY = 1  # mm/dd/yy
    YYMMDD = 2  # yy/mm/dd
    NONPARSABLE = -999

    @classmethod
    def get_d_parse_formats(cls, val=None):
        """ Arg:
        val(int | None) enum member value
        Returns:
        1. for val=None a list of explicit format strings
            for all supported date formats in this enum
        2. for val=n an explicit format string for a given enum member value
        """
        d_parse_formats = ["%d/%m/%y", "%m/%d/%y", "%y/%m/%d"]
        if val is None:
            return d_parse_formats
        if 0 <= val <= len(d_parse_formats):
            return d_parse_formats[val]
        raise ValueError


class InfDateFmtError(Exception):
    """custom exception when it is not possible to infer a date format
    e.g. too many NONPARSABLE or a tie """
    pass


def _maybe_DateFormats(date_str):
    """ Args:
    date_str (str) string representing a date in unknown format
    Returns:
    a list of enum members, where each member represents
    a possible date format for the input date_str
    """
    d_parse_formats = DateFormat.get_d_parse_formats()
    maybe_formats = []
    for idx, d_parse_fmt in enumerate(d_parse_formats):
        try:
            _parsed_date = datetime.strptime(date_str, d_parse_fmt) # pylint: disable=W0612
            maybe_formats.append(DateFormat(idx))
        except ValueError:
            pass
    if len(maybe_formats) == 0:
        maybe_formats.append(DateFormat.NONPARSABLE)
    return maybe_formats


def get_dates(dates):
    """ Args:
    dates (list) list of date strings
    where each list item represents a date in unknown format
    Returns:
    list of date strings, where each list item represents
    a date in yyyy-mm-dd format. Date format of input date strings is
    inferred based on the most prevalent format in the dates list.
    Alowed/supported date formats are defined in a DF enum class.
    """
    # complete this method
    date_format = []
    result = []
    for d in dates:
        for i in _maybe_DateFormats(d):
            date_format.append(i)

    c = Counter(date_format)
    if c.most_common()[0][1] == c.most_common()[1][1] or c.most_common()[0][0].name == 'NONPARSABLE':
        raise InfDateFmtError

    date_format_str = c.most_common()[0][0].get_d_parse_formats(c.most_common()[0][0].value)


    for d2 in dates:
        if c.most_common()[0][0].name != 'NONPARSABLE':
            try:
                result.append(
                    datetime.strptime(d2, date_format_str).strftime('%Y-%m-%d')
                )
            except ValueError:
                result.append('Invalid')

    return result


dates = [
    "11/11/07",
    "01/05/07",
    "05/12/04",
    "06/11/01",
    "10/03/09",
    "10/08/09",
    "04/11/11",
    "02/05/10",
    "05/10/08",
    "12/03/01",
    "10/10/12",
    "03/10/02",
]
g = get_dates(dates)
print(g)