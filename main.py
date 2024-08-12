from core.ip_geolocation import Georunner

while True:
    
    print("Welcome to Georunner!")
    
    print("1 - Locate an IP address")
    print("2 - Quit")
    
    question = input("Choose an option :")
    
    if question == '1' :
        question_ip = input("Enter a valid Ipv4/Ipv6 adress :")
        ip_info = Georunner.get_ip_info(question_ip)
        Georunner.display_ip_info(ip_info)
        break
    
    elif question == '2':
        break
    
    else:
        print("Error, Try again")
        # 177.34.189.63

