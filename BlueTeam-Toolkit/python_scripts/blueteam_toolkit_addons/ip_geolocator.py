import geoip2.database

def locate_ip(ip):
    reader = geoip2.database.Reader('GeoLite2-City.mmdb')
    response = reader.city(ip)
    return {
        "ip": ip,
        "country": response.country.name,
        "city": response.city.name
    }
