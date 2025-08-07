import requests

def fetch_data_from_api():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response=requests.get(url)
    data=response.json()
    if data["success"] and data["data"]:
        user_data=data["data"]
        username=user_data["login"]["username"]
        country=user_data["location"]["country"]
        return username ,country
    else:
        raise Exception("Failed to fetch data from api")



def main():
    try:
        username,country=fetch_data_from_api()
        print(f" \n username:{username} \n country:{country}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__=="__main__":
    main()
