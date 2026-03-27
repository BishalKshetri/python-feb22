
from tabulate import tabulate
# table = [["name","bishal"],["id",5]]
# print(tabulate(table))

import requests
import json
from tabulate import tabulate

province = []
district = []
mapping_province = {}

# example = [["Sun",696000,1989100000],["Earth",6371,5973.6],
#           ["Moon",1737,73.5],["Mars",3390,641.85]]
url = "https://electionadmin.psbnepal.gov.np/api/v1/home_api/"
r = requests.get(url)
if r.status_code == 200:
    for i in r.json():
        if i['type']=="provinces":

            for j in i['data']:
                mapping_province.update({j['province_number']:j['province_en']})
                province_data = []
                province_data.append(j.get("province_number"))
                province_data.append(j.get("province_en"))
                province_data.append(0)
                province.append(province_data)

        if i['type']=="district":
            for k in i['data']:
                district_data = []
                district_data.append(k.get("disrict_number"))
                district_data.append(k.get("disrict_name"))
                district_data.append(mapping_province.get(k.get('province_number')))
                district.append(district_data)

final_province =tabulate(province, headers=["Province No", "Province English","Total District"], tablefmt="grid")
final_district =tabulate(district, headers=["District No", "District English","Province no"], tablefmt="grid")
print(mapping_province)
print(final_province)
print('--------------'*10)
print(final_district)