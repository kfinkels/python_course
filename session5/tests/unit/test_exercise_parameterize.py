import pytest


def get_match_items(dict1, dict2):
    if dict1 is None or dict2 is None:
        return {}
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        return {}
    return {key: value for (key, value) in set(dict1.items()) & set(dict2.items())}


@pytest.mark.parametrize('dict1,dict2,result', [
    ({'a': 1, 'b': 2}, {'c': 3, 'b': 1}, {}),
    ({'a': 1, 'b': 2}, {'a': 1, 'b': 2}, {'a': 1, 'b': 2}),
    ({'a': 1, 'b': 2}, {'a': 1, 'b': 1}, {'a': 1}),
    (None, {'a': 1, 'b': 2}, {}),
    ({'a': 1, 'b': 2}, None, {}),
    ([1, 2], {'a': 1, 'b': 2}, {}),
    ({'a': 1, 'b': 2}, [1, 2], {})
])
def test_get_match_items(dict1, dict2, result):
    assert result == get_match_items(dict1, dict2)
