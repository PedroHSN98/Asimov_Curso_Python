import json
import sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')

data_json = '''
{
  "assinantes" : [
    {
         "nome": "Adriano Soares",
        "telefone": "51 99999999",
        "email": "adriano@email.com",
        "em_dia": true
    },
    {
        "nome": "Maria Silva",
        "telefone": "51 99999999",
        "email": "maria_silva@email.com",
        "em_dia": false
    }
    ],
    "data_extração": "2024-06-17"
}
'''

#Convertendo json para dicionário
dado_convertido = json.loads(data_json)

#print(type(data_json))
#print(type(dado_convertido))
#print(dado_convertido)


###convertendo novamente para json
#dado_desconvertido = json.dumps(dado_convertido, ensure_ascii=False, indent=2)
#print(type(dado_convertido))
#print(type(dado_desconvertido))
#print(dado_desconvertido)

###lendo arquivos json
pasta_atual = Path(__file__).parent
with open(pasta_atual / 'json' / 'assinantes.json') as f:
    dado_carregado = (json.load(f))
print(type(dado_carregado))
print(dado_carregado)
print(dado_carregado['assinantes'])


#escrevendo arquivos json

with open(pasta_atual / 'json' / 'assinantes_copia.json', 'w', encoding='utf-8') as f:
    json.dump(dado_carregado, f, indent=2, ensure_ascii=False)