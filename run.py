from pathlib import Path
import os
import sys
import requests as require

class Menu:
    def __init__(self):
        self.choices = {
                "1": self.config_environment,
                "2": self.discovering_id_city,
                "3": self.quit
                }

    def display_menu(self):
        print("""
API CONFIG MENU\n
1. Configure Environment
3. Discovering Id City
3. Quit
""")

    def run(self):
        '''Display the menu and respond to choices.'''
        while True:
            self.display_menu()
            choice = str(input("Enter an option: "))
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def config_environment(self):
        os.system("config.py")
        print("System configured with success")
        
        
    def discovering_id_city(self):
        token = input('Type your token of API Climatempo without the double quotes (ex: ID): ')
        cityName = str(input("Type the city that you want to have the id "))
        url_request = "http://apiadvisor.climatempo.com.br/api/v1/locale/city?name="+cityName+"&token="+str(token)
        response = require.api.get(url_request).json()
        print("id: ",response[0]['id'],"\n")
        id_save_folder = Path("ids_saved/")
        id_save_folder.mkdir(parents=True, exist_ok=True)
        Path('ids_saved/id.txt').touch()
        write = Path('./ids_saved/id.txt')
        write.write_text('{}: {}'.format(cityName, response[0]['id']))
        print("Id saved with sucess\n")   
    def quit(self):
        print("\nThank you for running this code!")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()
