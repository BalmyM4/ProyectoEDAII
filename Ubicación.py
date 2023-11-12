'''
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="Proyecto_EDAII")
ubicacion = geolocator.reverse("22.1577057,-102.2731303")

print(ubicacion.address)
print(ubicacion.latitude, ubicacion.longitude)
'''

from geopy.geocoders import GoogleV3

punto = '22.1577057,-102.2731303'
geolocalizador = GoogleV3()
direccion = geolocalizador.reverse(punto)

print(direccion[0])