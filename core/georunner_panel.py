class GeorunnerPanel:
    
    def print_banner(): # Banner created in: https://www.asciiart.eu/text-to-ascii-art
        banner = '''

    _________          ________                                  
    __  ____/_____________  __ \___  ____________________________
    _  / __ _  _ \  __ \_  /_/ /  / / /_  __ \_  __ \  _ \_  ___/
    / /_/ / /  __/ /_/ /  _, _// /_/ /_  / / /  / / /  __/  /    
    \____/  \___/\____//_/ |_| \__,_/ /_/ /_//_/ /_/\___//_/     

        '''
        print(banner)
    
    def query_description():
        
        print(f"| NAME         | DESCRIPTION                       |")
        print("|--------------|-----------------------------------| ")
        print(f"| IP:          | IP used for the query             |")
        print(f"| Status:      | Success or fail                   |")
        print(f"| Continent:   | Continent name                    |")
        print(f"| Country:     | Country name                      |")
        print(f"| Region name  | Region/state                      |")
        print(f"| City:        | City name                         |")
        print(f"| Zip code:    | Zip code                          |")
        print(f"| Latitude:    | Latitude                          |")
        print(f"| Longitude:   | Longitude                         |")
        print(f"| Timezone:    | Timezone                          |")
        print(f"| ISP:         | ISP name                          |")
        print(f"| Organization | Organization name                 |")
        print(f"| AS:          | AS number and organization        |")
        print(f"| Mobile:      | Mobile connection                 |")
        print(f"| Proxy:       | Proxy, VPN or Tor exit address    |")
        print(f"| Hosting:     | Hosting, colocated or data center |")
        print("|--------------|-----------------------------------| ")