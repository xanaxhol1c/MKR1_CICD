import pytest
from unittest.mock import mock_open, patch
from io import StringIO
from mkr1task import sort_by_area, sort_by_population, read_population_data

@pytest.fixture
def temp_data():
    return [
        ("Ukraine", 603500, 41400000),
        ("Poland", 312696, 38386000),
        ("Germany", 357022, 83149300),
        ("France", 551695, 67081000),
        ("Spain", 505990, 47351567)
    ]

@pytest.fixture
def mock_file():
    file_content = """Ukraine, 603500, 41400000
    Poland, 312696, 38386000
    Germany, 357022, 83149300
    France, 551695, 67081000
    Spain, 505990, 47351567"""
    return StringIO(file_content)


def test_sort_by_area(temp_data):
    sorted_data = sort_by_area(temp_data)
    assert sorted_data[0][0] == "Ukraine"  
    assert sorted_data[-1][0] == "Poland"  


def test_sort_by_population(temp_data):
    sorted_data = sort_by_population(temp_data)
    assert sorted_data[0][0] == "Germany"  
    assert sorted_data[-1][0] == "Poland"  

def test_read_population_data():
    mock_file_content = "Country1, 100000, 1000000\nCountry2, 200000, 2000000\n"
    
    with patch("builtins.open", mock_open(read_data=mock_file_content)) as mock_file:
        data = read_population_data("mockfile.txt")
        
        assert len(data) == 2
        assert data[0] == ('Country1', 100000.0, 1000000)
        assert data[1] == ('Country2', 200000.0, 2000000)
        
        mock_file.assert_called_with("mockfile.txt", 'r', encoding='utf-8')


@pytest.mark.parametrize("sort_function, expected_first_country", [
    (sort_by_area, "Ukraine"),
    (sort_by_population, "Germany")
])
def test_sorting_functions(temp_data, sort_function, expected_first_country):
    sorted_data = sort_function(temp_data)
    assert sorted_data[0][0] == expected_first_country
