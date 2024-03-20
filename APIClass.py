import requests


class APIClass:
    def __init__(self):
        link = str(
            "https://api.n2yo.com/rest/v1/satellite/positions/25544/41.5291/-84.306728/223/300/&apiKey=84KF72-KBE76V-3TF"
            + "4JS-585A")
        response = requests.get(link)
        if response:
            self.retString = "Azimuth & Elevation Info"
            self.azArray = []
            self.elArray = []
            r_dict = response.json()
            for i in range(0, 300):
                self.retString = self.retString + "\n" + "Azimuth: " + str(
                    r_dict["positions"][i]["azimuth"]) + "; Elevation: " + str(
                    r_dict["positions"][i]["elevation"]) + ";"
                self.azArray.append(r_dict["positions"][i]["azimuth"])
                self.elArray.append(r_dict["positions"][i]["elevation"])
        else:
            print("Error: Something went wrong, try again.")
            exit()

    def __str__(self):
        return self.retString

    def getAzimuthArray(self):
        return self.azArray

    def getElevationArray(self):
        return self.elArray


api = APIClass()
print(api.getAzimuthArray())
print(api.getElevationArray())
