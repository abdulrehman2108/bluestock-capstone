import requests
import pandas as pd 

apis = {
    "SBI_Bluechip":" https://api.mfapi.in/mf/119551",
    "ICICI_Bluechip":" https://api.mfapi.in/mf/120503",
    "HDFC":" https://api.mfapi.in/mf/125497",
    "Axis_Bluechip":" https://api.mfapi.in/mf/119092",
    "Kotak_Bluechip":" https://api.mfapi.in/mf/120841",
    "Nippon_Large_Cap":" https://api.mfapi.in/mf/118632",
    "Fund_Master":"https://api.mfapi.in/mf",
    "Fund_Master_latest":"https://api.mfapi.in/mf/latest" 
}

for name, url in apis.items():
    try:
        print("fetching data from {name} API...")

        response=requests.get(url)
        response.raise_for_status()

        data = response.json()
        if isinstance(data, list):
            df = pd.DataFrame(data)

        elif isinstance(data, dict):

        
            if "data" in data and isinstance(data["data"], list):
                df = pd.DataFrame(data["data"])

            else:
            
                df = pd.DataFrame([data])

        else:
            print(f"Unsupported format from {name}")
            continue


        file_name = f"{name}.csv"
        df.to_csv(file_name,index=False)
        print(f"File saved as {file_name}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching{name} API", e)

print("All API data fetched and stored seperately")

         
