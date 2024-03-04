import requests


API_KEY="4b9adb86c0a0ea0035d18455132e768e"
def get_data(place,forecast_days,kind):
    url=f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response=requests.get(url)
    data=response.json()
    filtered_data=data["list"]
    nr_values=forecast_days*8
    filtered_data=filtered_data[:nr_values]
    if kind=="Temperature":
        filtered_data=[dict["main"]["temp"]for dict in filtered_data]
    if kind=="Sky":
        filtered_data=[dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data

if __name__ == "__main__":
    print(get_data(place="Tokyo",forecast_days=2,kind="Sky"))

