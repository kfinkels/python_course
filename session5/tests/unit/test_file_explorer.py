from mock import patch, MagicMock

from file_explorer import create_dir, MyError


def test_create_dir_with_failed():
    with(patch('file_explorer.os.path.isdir', return_value=True)):
        assert create_dir('some dir') == 'exists'


@patch('file_explorer.os.path.isdir')
def test_create_dir_failed(isdir_mock):
    isdir_mock.return_value = True
    assert create_dir('some dir') == 'exists'


@patch('file_explorer.os.mkdir')
@patch('file_explorer.os.path.isdir')
def test_create_dir_success(isdir_mock, mkdir_mock):
    isdir_mock.return_value = False
    assert create_dir('some dir') == 'created'


@patch('file_explorer.os.mkdir', side_effect=MyError)
@patch('file_explorer.os.path.isdir')
def test_create_dir_raise_error(isdir_mock, mkdir_mock):
    isdir_mock.return_value = False
    assert create_dir('some dir') == 'failed'


@patch('file_explorer.os.path.isdir')
def test_create_dir_failed_extra_asserts(isdir_mock):
    isdir_mock.return_value = True
    assert create_dir('some dir') == 'exists'
    isdir_mock.assert_called()
    isdir_mock.assert_called_once()
    isdir_mock.assert_called_with('some dir')
    isdir_mock.assert_called_once_with('some dir')
