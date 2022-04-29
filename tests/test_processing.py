import pytest

from src.processing.data_processing import process_berry_data


@pytest.fixture
def berry_data():
    berry_list = [
        {"name": "berry1", "growth_time": 1},
        {"name": "berry2", "growth_time": 2},
        {"name": "berry3", "growth_time": 3},
        {"name": "berry4", "growth_time": 4},
        {"name": "berry5", "growth_time": 5}
    ]
    return berry_list

class TestGrowthTimeProcessing():

    def test_process_berry_data_min(self, berry_data):
        assert process_berry_data(berry_data)["min_growth_time"] == 1

    def test_process_berry_data_min_type(self, berry_data):
        assert type(process_berry_data(berry_data)["min_growth_time"]) is int
        
    def test_process_berry_data_max(self, berry_data):
        assert process_berry_data(berry_data)["max_growth_time"] == 5

    def test_process_berry_data_max_type(self, berry_data):
        assert type(process_berry_data(berry_data)["max_growth_time"]) is int

    def test_process_berry_data_median(self, berry_data):
        assert process_berry_data(berry_data)["median_growth_time"] == 3

    def test_process_berry_data_median_type(self, berry_data):
        assert type(process_berry_data(berry_data)["median_growth_time"]) is int

    def test_process_berry_data_variance(self, berry_data):
        assert process_berry_data(berry_data)["variance_growth_time"] == 2.5

    def test_process_berry_data_variance_type(self, berry_data):
        assert type(process_berry_data(berry_data)["variance_growth_time"]) is float
    
    def test_process_berry_data_mean(self, berry_data):
        assert process_berry_data(berry_data)["mean_growth_time"] == 3

    def test_process_berry_data_mean_type(self, berry_data):
        assert type(process_berry_data(berry_data)["mean_growth_time"]) is float