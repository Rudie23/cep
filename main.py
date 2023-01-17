import pprint
import requests


def cep_place():
    cep = input('Informe o cep: ')
    cep = cep.replace("-", "").replace(".", "").replace(" ", "")
    if len(cep) == 8:
        link = f'https://viacep.com.br/ws/{cep}/json/'
        request = requests.get(link)
        print()
        print(request, "\n")

        dic_request = request.json()
        uf = dic_request['uf']
        cidade = dic_request['localidade']
        bairro = dic_request['bairro']
     

        print(uf, cidade, bairro)
        print()
        print(dic_request)
    else:
        print("CEP inválido")

    option = int(input("Deseja realizar uma consulta? \n1. Sim\n2. Sair\n"))
    if option == 1:
        cep_place()
    else:
        print("Bye...")


def search_cep():
    uf = "RJ"
    cidade = "Rio de Janeiro"
    endereco = "Rio Branco"

    link = f'https://viacep.com.br/ws/{uf}/{cidade}/{endereco}/json'
    request = requests.get(link)
    print(request)

    dic_request = request.json()
    pprint.pprint(dic_request)


if __name__ == '__main__':
    cep_place()
    search_cep()
    
