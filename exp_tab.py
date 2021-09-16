import requests
# import exp_tab

def region_ua(reg_ua):

    https = "https://www.ukrposhta.ua/address-classifier-ws/"
    https_get = "get_regions_by_region_ua"
    headers = {'Accept': 'application/json', 'Authorization': 'Bearer 371e26f3-7f69-3972-9b3d-9236d45ad98b'}
    params_vi = (
        ('region_name', reg_ua),
        # ('region_name_en', 'Vol'),
    )
    resp = requests.get(https + https_get, headers=headers, params=params_vi)
    print(resp.status_code)
    print(resp.json())
    zm = resp.json()
    print(resp.url)
    for a,b in zm.items():
        for c,d in b.items():
            for i in d:
                for e,f in i.items():
                    if e == 'REGION_ID':
                        region_id = f
    return (region_id)


def region_id_code(reg_id,reg_district_ua):
    https = "https://www.ukrposhta.ua/address-classifier-ws/"
    https_get = "get_districts_by_region_id_and_district_ua"
    headers = {'Accept': 'application/json', 'Authorization': 'Bearer 371e26f3-7f69-3972-9b3d-9236d45ad98b'}
    params_vi = (
        ('region_id', reg_id),
        ('district_ua', reg_district_ua),
    )
    resp = requests.get(https + https_get, headers=headers, params=params_vi)
    print(resp.status_code)
    print(resp.json())
    zm = resp.json()
    print(resp.url)
    for a,b in zm.items():
        for c,d in b.items():
            for i in d:
                for e,f in i.items():
                    if e == 'DISTRICT_ID':
                        district_id = f
    return (district_id)



#
def city_ua(reg_id_cod,reg_city_ua):
    https = "https://www.ukrposhta.ua/address-classifier-ws/"
    https_get = "get_city_by_region_id_and_district_id_and_city_ua"
    headers = {'Accept': 'application/json', 'Authorization': 'Bearer 371e26f3-7f69-3972-9b3d-9236d45ad98b'}
    params_vi = (
        ('district_id', reg_id_cod),
        ('city_ua', reg_city_ua),
    )
    resp = requests.get(https + https_get, headers=headers, params=params_vi)
    print(resp.status_code)
    print(resp.json())
    zm = resp.json()
    print(resp.url)
    for a,b in zm.items():
        for c,d in b.items():
            for i in d:
                for e,f in i.items():
                    if e == 'CITY_ID':
                        city_id = f
    return (city_id)

def address(region_id,city_id,district_id,street_ua,shortstreettype_ua):
    https = "https://www.ukrposhta.ua/address-classifier-ws/"
    https_get = "get_street_by_region_id_and_district_id_and_city_id_and_street_ua"
    headers = {'Accept': 'application/json', 'Authorization': 'Bearer 371e26f3-7f69-3972-9b3d-9236d45ad98b'}
    params_vi = (
        ('district_id', district_id),
        ('region_id', region_id),
        ('city_id', str(city_id)),
        ('street_ua', street_ua),
    )
    resp = requests.get(https + https_get, headers=headers, params=params_vi)
    print(resp.status_code)
    print(resp.json())
    zm = resp.json()
    print(resp.url)
    print(zm)
    for a,b in zm.items():
        for c,d in b.items():
            for i in d:
                for e,f in i.items():
                    if e == 'SHORTSTREETTYPE_UA' and f == shortstreettype_ua :
                        print(i)
                        for g, h in i.items():
                            if g == 'STREET_ID':
                                print(h)
                                street_id = h
    return (street_id)


def postcode(street_id, housenumber):
    https = "https://www.ukrposhta.ua/address-classifier-ws/"
    https_get = "get_addr_house_by_street_id"
    headers = {'Accept': 'application/json', 'Authorization': 'Bearer 371e26f3-7f69-3972-9b3d-9236d45ad98b'}
    params_vi = (
        ('street_id', str(street_id)),
        ('housenumber', housenumber)
    )
    resp = requests.get(https + https_get, headers=headers, params=params_vi)
    print(resp.status_code)
    print(resp.json())
    zm = resp.json()
    print(resp.url)
    print(zm)
    for a,b in zm.items():
        for c,d in b.items():
            for i in d:
                for e,f in i.items():
                    if e == 'POSTCODE':
                        print(f)
                        post_code = f
    return (post_code)



def main():
# 'DISTRICT_UA': "Кам'янець-Подільський", 'DISTRICT_ID': '894',
# 'DISTRICT_UA': 'Хмельницький', 'DISTRICT_ID': '1009',
# 'DISTRICT_UA': 'Шепетівський', 'DISTRICT_ID': '1010',
    reg_ua = 'хм'
    reg_district_ua = "Хмельницький"
    # reg_district_ua = "Кам'янець-Подільський"
    # reg_district_ua = "Шепетівський"
    reg_city_ua = 'хмель'
    street_ua = 'іпод'
    # shortstreettype_ua = 'вул.'
    shortstreettype_ua = 'пров.'
    housenumber = 2

    region_id=region_ua(reg_ua)
    print(region_id)

    district_id=region_id_code(region_id,reg_district_ua)
    print(district_id)

    city_id = city_ua(district_id,reg_city_ua)
    print(city_id)

    street_id = address(region_id, city_id, district_id, street_ua, shortstreettype_ua)
    print(street_id)

    post_code = postcode(street_id, housenumber)
    print(post_code)

if __name__ == "__main__":
    main()

