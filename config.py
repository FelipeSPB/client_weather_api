from pathlib import Path
import requests



def creating_folder():
    folder = Path("config/")
    folder.mkdir(parents=True, exist_ok=True)

def creating_command_install_requirements():
    Path('config/install.bat').touch()
    write = Path('./config/install.bat')
    write.write_text('cd..\npip install -r requirements.txt')

def config_token():
    Path('./api/models/token.py').touch()
    token = input('digite seu token da API Climatempo em aspas duplas (ex: "seu_id"): ')
    write = Path('./api/models/token.py')
    write.write_text('token = {}\ntoken=str(token)'.format(token))

def config_run_server():
    Path('config/run_server.bat').touch()
    write = Path('./config/run_server.bat')
    write.write_text('cd../api/\npython app.py')

if __name__ == '__main__':
    creating_folder()
    creating_command_install_requirements()
    config_token()
    config_run_server()
