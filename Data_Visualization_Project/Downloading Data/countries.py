from pygal.maps.world import COUNTRIES

"""Pygal’s country codes are stored in the module pygal.maps.world. 
   The dictionary COUNTRIES contains the two-letter country
   codes as keys and the country names as values"""
for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])