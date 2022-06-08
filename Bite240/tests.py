from Bite240.Bite240 import Account

import pytest


def test_account():
    my_account = Account('Ryan', 100)
    expected_account_amount = 100
    expected_account_owner = 'Ryan'
    assert repr(my_account) == "Account('Ryan', 100)"
    assert my_account.amount == expected_account_amount
    assert my_account.owner == expected_account_owner
    assert str(my_account) == 'Account of Ryan with starting amount: 100'
    assert len(my_account) == 0


def test_account_start_with_zero():
    my_account = Account('Ryan')
    expected_account_amount = 0
    expected_account_owner = 'Ryan'
    assert repr(my_account) == "Account('Ryan', 0)"
    assert my_account.amount == expected_account_amount
    assert my_account.owner == expected_account_owner
    assert str(my_account) == 'Account of Ryan with starting amount: 0'
    assert len(my_account) == 0


def test_add_transaction_wrong_type():
    my_account = Account('Ryan', 100)
    with pytest.raises(ValueError) as e:
        my_account.add_transaction('A')
        raise ValueError('please use int for amount')
    assert str(e.value) =='please use int for amount'


def test_add_transaction_wrong_type_zero_starting():
    my_account = Account('Ryan')
    with pytest.raises(ValueError) as e:
        my_account.add_transaction('A')
        raise ValueError('please use int for amount')
    assert str(e.value) =='please use int for amount'


def test_add_transaction():
    my_account = Account('Ryan', 100)
    my_account.add_transaction(10)
    assert my_account.balance == 110
    assert my_account.__getitem__(0) == 10


def test_equality_comparison():
    my_account = Account('Ryan', 100)
    assert Account('Other', 100) == my_account


def test_lt_comparison():
    my_account = Account('Ryan', 100)
    other_account = Account('Other', 100)
    another_account = Account('Another', 90)
    assert another_account < my_account
    assert not other_account < my_account


def test_add_operator():
    owner_1 = 'Ryan'
    owner_2 = 'Other'
    owner = '{}&{}'.format(owner_1, owner_2)
    my_account = Account(owner_1, 50)
    my_account.add_transaction(50)
    other_account = Account(owner_2, 50)
    other_account.add_transaction(50)
    total_account = my_account + other_account
    assert list(my_account) + list(other_account) == ([50] + [50])
    assert total_account.owner == owner
    assert total_account.balance == 200

