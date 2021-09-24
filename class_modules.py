import requests
class Region_city:
    https = "https://www.ukrposhta.ua/address-classifier-ws/"
    __headers = {'Accept': 'application/json', 'Authorization': 'Bearer 371e26f3-7f69-3972-9b3d-9236d45ad98b'}
    street_lane = 'SHORTSTREETTYPE_UA'
    api_params_search = [0,1,2,3,4]
    https_get_api = [
        "get_regions_by_region_ua",
        "get_districts_by_region_id_and_district_ua",
        "get_city_by_region_id_and_district_id_and_city_ua",
        "get_street_by_region_id_and_district_id_and_city_id_and_street_ua",
        "get_addr_house_by_street_id",
    ]

    def __init__(self, region_name, district_ua, city_ua, street_ua, shortstreettype_ua, housenumber):
        self.region_name = region_name
        self.district_ua = district_ua
        self.city_ua = city_ua
        self.street_ua = street_ua
        self.shortstreettype_ua = shortstreettype_ua
        self.housenumber = housenumber

    def ukr_pochta_api(self):
        for i in range(len(self.https_get_api)):
            respomse_api = requests.get(self.https + self.https_get_api[i], headers=self.__headers, params=self.params_def(i))
            # print(respomse_api.json())
            zm = respomse_api.json()
            self.api_params_search[i] = self.dvizok(zm,self.search_api(i))
            # print('xxxxx' , self.api_params_search)


    def search_api(self, numb):
        search_api_text = [
        'REGION_ID',
        'DISTRICT_ID',
        'CITY_ID',
        'STREET_ID',
        'POSTCODE',
        ]
        return search_api_text[numb]

    def params_def(self,numb):
        params_def_tup = [
            (('region_name', self.region_name),),
            (('region_id', self.api_params_search[0]), ('district_ua', self.district_ua),),
            (('district_id', self.api_params_search[1]), ('city_ua', self.city_ua),),
            (('district_id', self.api_params_search[1]), ('region_id', self.api_params_search[0]), ('city_id', str(self.api_params_search[2])),('street_ua', self.street_ua),),
            (('street_id', self.api_params_search[3]), ('housenumber', self.housenumber))
        ]
        return params_def_tup[numb]


    def dvizok(self, zm1, zm2):
        for a, b in zm1.items():
            for c, d in b.items():
                for i in d:
                    for e, f in i.items():
                        if e == self.street_lane and f == self.shortstreettype_ua:
                            for g, h in i.items():
                                if g == zm2:
                                    # print(zm2)
                                    z = h
                            return (z)
                        if e == zm2:
                            z = f
                            print(z)
        return (z)
