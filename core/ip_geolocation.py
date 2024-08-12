import requests

def get_ip_info(ip=None):
    try:
        url = f'http://ip-api.com/json/{ip}' if ip else 'http://ip-api.com/json/'
        response = requests.get(url)
        response.raise_for_status()  # Levanta um erro para códigos de status HTTP 4xx/5xx
        data = response.json()
        
        if data['status'] == 'fail':
            print(f"Erro: {data['message']}")
        else:
            return data

    except requests.RequestException as e:
        print(f"Erro na requisição: {e}")

def display_ip_info(data):
        
        if not data:
            return
    
        print(f"IP: {data.get('query', 'N/A')}")
        print(f"Status: {data.get('status', 'N/A')}")
        print(f"País: {data.get('country', 'N/A')}")
        print(f"Região: {data.get('regionName', 'N/A')}")
        print(f"Cidade: {data.get('city', 'N/A')}")
        print(f"Código Postal: {data.get('zip', 'N/A')}")
        print(f"Latitude: {data.get('lat', 'N/A')}")
        print(f"Longitude: {data.get('lon', 'N/A')}")
        print(f"Fuso Horário: {data.get('timezone', 'N/A')}")
        print(f"ISP: {data.get('isp', 'N/A')}")
        print(f"Organização: {data.get('org', 'N/A')}")
        print(f"AS: {data.get('as', 'N/A')}")

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Consulta geolocalização de IP usando IP-API.')
    parser.add_argument('ip', nargs='?', default=None, help='Endereço IP para consulta. Se não fornecido, será usado o IP da requisição.')

    args = parser.parse_args()
    ip_info = get_ip_info(args.ip)
    display_ip_info(ip_info)
