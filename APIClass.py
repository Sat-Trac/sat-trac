import requests
import json


class APIClass:
    def __init__(self, sat_id):

        if(not sat_id.isnumeric()):
            print("Invalid Satellite Tracking ID")
            return

        with open("apikeys.json", "r") as jsonsettings:
            settings = json.load(jsonsettings)

        API_KEY = settings['api_Key']
        TRACKING_SECONDS = settings['api_tracking_seconds']

        link = f'https://api.n2yo.com/rest/v1/satellite/positions/{sat_id}/41.4591/-84.306728/223/{TRACKING_SECONDS}/&apiKey={API_KEY}'

        response = requests.get(link)
        if response:
            self.r_dict = response.json()
            self.elaz_dict = {}
            self.satellite_name = self.r_dict["info"]["satname"]
            for i in range(0, TRACKING_SECONDS):
                self.elaz_dict[self.r_dict["positions"][i]["timestamp"]] = {
                    "azimuth" : self.r_dict["positions"][i]["azimuth"],
                    "elevation" : self.r_dict["positions"][i]["elevation"]
                }
        else:
            print("Error: Something went wrong, try again.")

    def get_data_at_time(self, time_second):
        try:
            return self.elaz_dict[time_second]
        except KeyError:
            print(f"Error: No data found for: {time_second}")
        
    def get_satellite_name(self):
        return self.satellite_name;
