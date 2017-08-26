from googleplaces import GooglePlaces, types, lang
import subprocess
import pygeoip
from tts import tts 
def location():
    YOUR_API_KEY = 'AIzaSyDYR6I8sEYHyY4-pZsEnzlmB8zb3SdlgEA'
    google_places = GooglePlaces(YOUR_API_KEY)


    #ip_add = subprocess.check_output(['hostname', '-I'])
    #ip_add = ip_add.strip()
    ip_add = "103.229.19.21"

    path = './GeoLiteCity.dat'
    gic = pygeoip.GeoIP(path)
    abc = gic.record_by_addr(ip_add)
    lat = abc['latitude']
    lng = abc['longitude']

    lt_lng = {'lat':lat,'lng':lng}
    i = 0
    #query_result = google_places.nearby_search(keyword='gas_station',lat_lng=lt_lng,radius=2000, types=[types.TYPE_FOOD])
    query_result = google_places.nearby_search(lat_lng=lt_lng, keyword='Petrol',radius=2000,rankby='distance')
    for place in query_result.places:
        print place.name
        place.get_details()
        d=place.details
        vic = d['vicinity']
        print vic
        print place.local_phone_number
        print ""
        if i == 0:
            dic = {'name':place.name,'vicinity':vic,'phone':place.local_phone_number}
	i=i+1
	if i==5:
	    break
    tts("Nearest petrol pump is "+dic['name'])
    tts(" at "+dic['vicinity'])
    tts(" and phone number is "+dic['phone'])
    
        
    
