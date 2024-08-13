from core.ip_geolocation import Georunner

def print_banner(): # Banner created in: https://www.asciiart.eu/text-to-ascii-art
    banner = '''

    _________          ________                                  
    __  ____/_____________  __ \___  ____________________________
    _  / __ _  _ \  __ \_  /_/ /  / / /_  __ \_  __ \  _ \_  ___/
    / /_/ / /  __/ /_/ /  _, _// /_/ /_  / / /  / / /  __/  /    
    \____/  \___/\____//_/ |_| \__,_/ /_/ /_//_/ /_/\___//_/     

    '''
    print(banner)
    
while True:
    
    print_banner()
    print("-"*70)
    print("Welcome to Georunner!")
    print("-"*70)
    print("1 - Locate an IP address")
    print("2 - Query info")
    print("3 - Quit")
    print("-"*70)
    question = input("Choose an option :")
    print("-"*70)
    
    if question == '1' :
        question_ip = input("Enter a valid Ipv4/Ipv6 adress :")
        ip_info = Georunner.get_ip_info(question_ip)
        Georunner.display_ip_info(ip_info)
        break
    
    if question == '2':
        Georunner.query_description()
        break
    
    elif question == '3':
        break
    
    else:
        print("Error, Try again")
