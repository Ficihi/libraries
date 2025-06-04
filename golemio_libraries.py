import requests
import json

GOLEMIO_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MzY3MCwiaWF0IjoxNzQ5MDM2MjE5LCJleHAiOjExNzQ5MDM2MjE5LCJpc3MiOiJnb2xlbWlvIiwianRpIjoiODNiNTg4MjctY2NhNy00MjE3LWFjNDctYjIyMzMwMWI4MjhlIn0.0oWOfUhjNwdSKknmeJHGvBiTVltiCQFGnLYamGZtSow"
url = "https://api.golemio.cz/v2/municipallibraries"


headers = {"x-access-token": GOLEMIO_API_KEY}
response = requests.get(url, headers=headers)
response.raise_for_status()

data = response.json()

extracted = []
for item in data.get("features", []):
    props = item.get("properties", {})
    coords = item.get("geometry", {}).get("coordinates", [None, None])
    address = props.get("address", {})

    extracted.append({
        "id": props.get("id"),
        "name": props.get("name"),
        "street": address.get("street_address"),
        "zipcode": address.get("postal_code"),
        "city": address.get("address_locality"),
        "region": "",  # nie je v dátach, môže sa neskôr doplniť z geolokácie
        "country": address.get("address_country"),
        "latitude": coords[1],  # GeoJSON má [longitude, latitude]
        "longitude": coords[0],
        "opening_hours": props.get("opening_hours", [])
    })

# Uloženie do JSON súboru
with open("libraries_data.json", "w", encoding="utf-8") as f:
    json.dump(extracted, f, ensure_ascii=False, indent=2)

print(f"Uložených knižníc: {len(extracted)}")
