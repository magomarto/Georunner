from core.georunner_core import GeorunnerCore
from core.georunner_panel import GeorunnerPanel
    
GeorunnerPanel.display_banner()
    
while True:

    option = GeorunnerPanel.main_panel()

    if option == 1 :
        question_ip = input("Enter a valid Ipv4/Ipv6 adress :")
        ip_info = GeorunnerCore.get_ip_info(question_ip)
        GeorunnerCore.display_ip_info(ip_info)
    
    elif option == 2:
        GeorunnerCore.query_description()
    
    elif option == 3:
        print("Quitting...")
        break
    
    else:
        print("Error, Try again")
