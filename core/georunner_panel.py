class GeorunnerPanel:

    def display_banner(): # Banner created in: https://www.asciiart.eu/text-to-ascii-art
        banner = '''

    _________          ________                                  
    __  ____/_____________  __ \___  ____________________________
    _  / __ _  _ \  __ \_  /_/ /  / / /_  __ \_  __ \  _ \_  ___/
    / /_/ / /  __/ /_/ /  _, _// /_/ /_  / / /  / / /  __/  /    
    \____/  \___/\____//_/ |_| \__,_/ /_/ /_//_/ /_/\___//_/     

        '''
        print(banner)
        print("   | API provided by: http://ip-api.com/ | Author : MagoMarto |")
        print("-"*70)
        print("Welcome to Georunner!")
        print("-"*70)

    def main_panel():
        print("1 - Locate an IP address")
        print("2 - Query info")
        print("3 - Quit")
        print("-"*70)
        question = int(input("Choose an option :"))

        return question
    