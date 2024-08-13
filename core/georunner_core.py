import requests

class GeorunnerCore:

    def get_ip_info(ip=None):
        try:
            if ip:  
                url = f'http://ip-api.com/json/{ip}?fields=18083839' 
                
            else:
                'http://ip-api.com/json/'
                
            response = requests.get(url)
            response.raise_for_status() 
            data = response.json()
            
            if data['status'] == 'fail':
                print(f"Error: {data['message']}")
            else:
                return data

        except requests.RequestException as e:
            print(f"Request error: {e}")

    def display_ip_info(data):
            
            if not data:
                return
        
            print(f"IP: {data.get('query', 'N/A')}")
            print(f"Status: {data.get('status', 'N/A')}")
            print(f"Continent: {data.get('continent', 'N/A')}")
            print(f"Country: {data.get('country', 'N/A')}")
            print(f"Region name: {data.get('regionName', 'N/A')}")
            print(f"City: {data.get('city', 'N/A')}")
            print(f"Zip code: {data.get('zip', 'N/A')}")
            print(f"Latitude: {data.get('lat', 'N/A')}")
            print(f"Longitude: {data.get('lon', 'N/A')}")
            print(f"Timezone: {data.get('timezone', 'N/A')}")
            print(f"ISP: {data.get('isp', 'N/A')}")
            print(f"Organization: {data.get('org', 'N/A')}")
            print(f"AS: {data.get('as', 'N/A')}")
            print(f"Mobile: {data.get('mobile', 'N/A')}")
            print(f"Proxy: {data.get('proxy', 'N/A')}")
            print(f"Hosting: {data.get('hosting', 'N/A')}")
            

        
        


