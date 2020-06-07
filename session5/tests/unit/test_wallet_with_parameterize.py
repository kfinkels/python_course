import pytest


@pytest.mark.parametrize("earned,spent,expected", [
    (30, 10, 20),
    (20, 2, 18),
])
def test_transactions(empty_wallet, earned, spent, expected):
    empty_wallet.add_cash(earned)
    empty_wallet.spend_cash(spent)
    assert expected == empty_wallet.balance


@pytest.mark.parametrize("earned", (30, 20))
@pytest.mark.parametrize("spent", (10, 15))
def test_allowed_transactions(empty_wallet, earned, spent):
    empty_wallet.add_cash(earned)
    empty_wallet.spend_cash(spent)
    assert empty_wallet.balance >= 0
