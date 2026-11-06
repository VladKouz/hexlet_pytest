from hexlet_pytest.example import reverse
from pathlib import Path

def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


def test_reverse_using_files():
    expected = read_file("reverse_output.txt")
    actual = reverse(read_file("reverse_input.txt"))

    assert actual == expected
