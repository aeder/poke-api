import requests
import json

from ..config.config import Config


class BerryAPI():
    def get_berry_data(self, berry_data_url):
        try:
            print(f"Fetching {berry_data_url}")
            raw_berry_data = json.loads(requests.get(berry_data_url).text)
            return {"name": raw_berry_data["name"], "growth_time": raw_berry_data["growth_time"]}
        except Exception as e:
            print(e)

    def get_berry_url_list(self, limit: int, offset: int):
        try:
            print(f"Fetching list with offset: {offset}")
            response = requests.get(f'{Config.POKE_API_URL}/berry/',
                                    params={"offset": offset, "limit": limit})
            json_response = json.loads(response.text)
            berry_url_list = json_response["results"]
            total_count = int(json_response["count"])
            return {"list": berry_url_list, "total_count": total_count}
        except Exception as e:
            print(e)
