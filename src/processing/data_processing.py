import collections
import statistics
from typing import Any, List
from ..services.pokeapi import PokeAPI


class BerryGenerator():
    _counter: int = 1
    _offset_multiplier: int = 0
    _collection: List[Any] = None

    def __init__(self, api, limit: int = 20, offset: int = 20) -> None:
        print(limit, offset)
        self._counter = 0
        self._offset = offset
        self._limit = limit
        self._api = api
        self._collection = api.get_berry_url_list(self._limit, self._offset * self._offset_multiplier)

    def get(self):
        try:
            while self._counter < self._collection["total_count"]:
                for berry in self._collection["list"]:
                    value = self._api.get_berry_data(berry["url"])
                    print(f"Iterator value: {value}")
                    self._counter += 1
                    print(
                        f"{self._counter}/{self._collection['total_count']} Berries")
                    yield value
                if self._offset * self._offset_multiplier < self._collection["total_count"]:
                    print("Fetching next page...")
                    self._offset_multiplier += 1
                    self._collection = self._api.get_berry_url_list(
                        self._limit, self._offset * self._offset_multiplier)
        except Exception as e:
            print(e)


def get_all_berry_data(berry_api=PokeAPI()):
    berry_iterator = BerryGenerator(berry_api)
    berry_data_list = [berry for berry in berry_iterator.get()]
    return berry_data_list


def process_berry_data(berry_data_list):
    frequency_data = collections.Counter(
        berry['growth_time'] for berry in berry_data_list)
    payload = {
        "berries_names": [berry['name'] for berry in berry_data_list],
        # time, int
        "min_growth_time": min(berry['growth_time'] for berry in berry_data_list),
        # time, float
        "median_growth_time": statistics.median((berry['growth_time'] for berry in berry_data_list)),
        # time, int
        "max_growth_time": max(berry['growth_time'] for berry in berry_data_list),
        # time, float
        "variance_growth_time": statistics.variance(berry['growth_time'] for berry in berry_data_list),
        # time, float
        "mean_growth_time": float(statistics.mean(berry['growth_time'] for berry in berry_data_list)),
        # time, {growth_time: frequency, ...}
        "frequency_growth_time": [{'growth_time': key, 'frequency': value} for key, value in frequency_data.items()],
    }
    return payload
