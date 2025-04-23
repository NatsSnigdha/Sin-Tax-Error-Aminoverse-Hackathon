import requests

# Example UniProt accession
accession = "P69905"  # Hemoglobin subunit alpha

url = f"https://rest.uniprot.org/uniprotkb/{accession}"
response = requests.get(url, headers={"Accept": "application/json"})

if response.ok:
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code)