import requests


class APIClass:
    def __init__(self):
        link = str(
            "https://api.n2yo.com/rest/v1/satellite/positions/25544/41.5291/-84.306728/223/300/&apiKey=84KF72-KBE76V-3TF"
            + "4JS-585A")
        response = requests.get(link)
        if response:
            self.retString = "Azimuth & Elevation Info"
            r_dict = response.json()
            for i in range(0, 300):
                self.retString = self.retString + "\n" + "Azimuth: " + str(
                    r_dict["positions"][i]["azimuth"]) + "; Elevation: " + str(
                    r_dict["positions"][i]["elevation"]) + ";"
        else:
            print("Error: Something went wrong, try again.")
            exit()

    def __str__(self):
        return self.retString


api = APIClass()
print(api.__str__())
