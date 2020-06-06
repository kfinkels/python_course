from mock import Mock


def test_mock_capabilities():

    # import pdb;pdb.set_trace()
    json = Mock()
    json.loads('{"key": "value"}')

    json.loads.assert_called()
    json.loads.assert_called_once()
    json.loads.assert_called_with('{"key": "value"}')
    json.loads.assert_called_once_with('{"key": "value"}')
