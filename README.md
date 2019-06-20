# client_weather_api

Um webservice com apenas um endpoint que possui três parâmetros de entrada (id da cidade, datas inicial e data final) sendo que as não podem ser mais de 7 dias.
O endpoint envia os seguintes dados em json: temperatura mais alta e a respectiva data; temperatura mais baixa e a respectiva data; o dia de maior probabilidade 
de chuva, a precipitação e a respectiva data.

Para conseguir adequar a api na sua máquina abra 'run.py'

Selecione a primeira opção, lembrando que neste passo o seu token deverá estar com as aspas inclusas.
Após executar a primeira opção, vai ser criada a pasta config e alguns scripts bat que automatizam a API

'install.bat' > é o script que instalará os requeriment.txt para a aplicação desempenhar na máquina.

'run_server.bat' > é o script que rodará a api.

Lembrando que caso precise descobrir o id da cidade, abra run.py novamente. Selecione a segunda opção, coloque seu token novamente sem aspas dessa vez. Depois digite
o nome da cidade solicitada, depois que aparecer na tela o id... não se preocupe, você verá a pasta ids_saved e o arquivo id.txt com o nome da cidade da última vez.

Tendo o id e as datas desejadas, digite 'localhost:3000/<id_cidade>/<data_inicial>/<data_final>








