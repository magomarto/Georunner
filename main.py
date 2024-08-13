from core.georunner_core import GeorunnerCore
from core.georunner_panel import GeorunnerPanel
    
GeorunnerPanel.print_banner()
print("-"*70)
print("Welcome to Georunner!")
print("-"*70)
    
while True:

    print("1 - Locate an IP address")
    print("2 - Query info")
    print("3 - Quit")
    print("-"*70)
    question = int(input("Choose an option :"))
    print("-"*70)
    
    if question == 1 :
        question_ip = input("Enter a valid Ipv4/Ipv6 adress :")
        ip_info = GeorunnerCore.get_ip_info(question_ip)
        GeorunnerCore.display_ip_info(ip_info)
        break
    
    if question == 2:
        GeorunnerPanel.query_description()
    
    elif question == 3:
        break
    
    else:
        print("Error, Try again")
