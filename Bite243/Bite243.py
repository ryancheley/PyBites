import os
from pathlib import Path
from ipaddress import IPv4Network, IPv4Address
from urllib.request import urlretrieve

import pytest

from Bite243.tests import (ServiceIPRange, parse_ipv4_service_ranges,
                 get_aws_service_range)

URL = "https://bites-data.s3.us-east-2.amazonaws.com/ip-ranges.json"
TMP = os.getenv("TMP", "/tmp")
PATH = Path(TMP, "ip-ranges.json")
IP = IPv4Network('192.0.2.8/29')


@pytest.fixture(scope='module')
def json_file():
    """Import data into tmp folder"""
    urlretrieve(URL, PATH)
    return PATH


def test_parse_ipv4_service_ranges(json_file):
    actual = parse_ipv4_service_ranges(json_file)
    assert len(actual) == 1886


def test_service_ip_range_string():
    service = 'AMAZON'
    region = 'ap-east-1'
    cidr = '54.240.17.0/24'
    actual_my_service_ip_range = str(ServiceIPRange(service, region, cidr))
    expected_my_service_ip_range = '54.240.17.0/24 is allocated to the AMAZON service in the ap-east-1 region'
    assert actual_my_service_ip_range == expected_my_service_ip_range


def test_get_aws_service_range_no_error():
    service = 'AMAZON'
    region = 'ap-east-1'
    cidr = IPv4Network('54.240.17.0/24')
    ip_range = [ServiceIPRange(service, region, cidr), ]
    actual = get_aws_service_range('54.240.17.5', ip_range)
    expected = '54.240.17.5'
    print(actual)
    print(expected)
    assert actual == ip_range


def test_get_aws_service_range_error():
    with pytest.raises(ValueError, match="Address must be a valid IPv4 address"):
        get_aws_service_range('a.b.c.d', ['a'])

