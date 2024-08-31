import pytest

from helpers.arguments import get_arguments
from unittest.mock import patch

@patch("argparse.ArgumentParser")
def test_get_arguments(self):
    # Arrange - set up input and expected output
    expected_type = dict

    # Act
    args = get_arguments()

    # Assert
    assert type(args) == expected_type
    assert len(args) == 5
    assert 'metrics' in args
    assert 'dimensions' in args
    assert 'start_date' in args
    assert 'end_date' in args
    assert 'avoid_aggregate' in args