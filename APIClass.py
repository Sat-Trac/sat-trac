import requests

# Let's get a method to return the time as the key and value of a tuple containing alt and az
# Perhaps allow the method call to specify the amount of data retrieved.


class APIClass:
    def __init__(self, sat_id):
        if(not sat_id.isnumeric()):
            print("Invalid Satellite Tracking ID")
            return
        length = 3600*2
        link = f'https://api.n2yo.com/rest/v1/satellite/positions/{sat_id}/41.4591/-84.306728/223/{length}/&apiKey=84KF72-KBE76V-3TF4JS-585A'
        response = requests.get(link)
        if response:
            self.r_dict = response.json()
            self.elaz_dict = {}
            self.satellite_name = self.r_dict["info"]["satname"]
            for i in range(0, length):
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
            return None
        
    def get_satellite_name(self):
        return self.satellite_name;
