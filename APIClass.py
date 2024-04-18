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
            
            self.retString = "Azimuth & Elevation Info"

            self.r_dict = response.json()
            self.azList = []
            self.elList = []
            self.time_stamp = []
            self.satellite_name = self.r_dict["info"]["satname"]
            for i in range(0, length):
                self.retString = self.retString + "\n" + "Azimuth: " + str(
                    self.r_dict["positions"][i]["azimuth"]) + "; Elevation: " + str(
                    self.r_dict["positions"][i]["elevation"]) + ";"
                self.azList.append(self.r_dict["positions"][i]["azimuth"])
                self.elList.append(self.r_dict["positions"][i]["elevation"])
                self.time_stamp.append(self.r_dict["positions"][i]["timestamp"])
        else:
            print("Error: Something went wrong, try again.")
            
        print(len(response.json()["positions"]))

    def __str__(self):
        return self.retString
    
    def getNextInfo(self):
        if(len(self.azList) > 0):
            return (self.azList.pop(0), self.elList.pop(0), self.time_stamp.pop(0))
        else:
            return (None, None, None)
    def getAzimuthArray(self):
        return self.azArray

    def getElevationArray(self):
        return self.elArray
        
    def get_satellite_name(self):
        return self.satellite_name;



#api = APIClass()
#print(api.getNextInfo())
#print(api.getNextInfo())
#print(api.__str__())
