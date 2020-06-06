import pytest

from wallet import Wallet, InsufficientAmount


@pytest.fixture
def local_empty_wallet():
    '''Returns a Wallet instance with a zero balance'''
    return Wallet()


@pytest.fixture
def local_wallet():
    '''Returns a Wallet instance with a balance of 20'''
    return Wallet(20)


def test_default_initial_amount(local_empty_wallet):
    assert local_empty_wallet.balance == 0


def test_setting_initial_amount(local_wallet):
    assert local_wallet.balance == 20


def test_wallet_add_cash(local_wallet):
    local_wallet.add_cash(80)
    assert local_wallet.balance == 100


def test_wallet_spend_cash(local_wallet):
    local_wallet.spend_cash(10)
    assert local_wallet.balance == 10


def test_wallet_spend_cash_raises_exception_on_insufficient_amount(local_empty_wallet):
    with pytest.raises(InsufficientAmount):
        local_empty_wallet.spend_cash(100)
