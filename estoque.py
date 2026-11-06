import json

def carregar_produtos():
    arquivo = open("produtos.json", "r", encoding="utf-8")
    produtos = json.load(arquivo)
    arquivo.close()
    return produtos 
def salvar_produtos(produtos):
    arquivo = open("produtos.json", "w", enconding="utf-8")
    json.dump(produtos, arquivo, indent=4, ensure_ascii=False)
    arquivo.close()


def v_item():
    user = input("Digite o usúario que deseja pesquisar: ")
    for produto in produtos:
        if produto["usuario"] == user:
            print(produto)


def prioridade():
    pri = input("Digite a prioridade(Baixa,Média,Alta,Crítica): ")
    for chamado in chamados:
        if chamado["prioridade"] == pri:
            print(chamado)   

def status():
    sta = input("Digite o status que deseja(Aberto, Em progresso, Fechado): ")
    for chamado in chamados:
        if chamado["status"] == sta:
            print(chamado)   


def urgentes():
    for chamado in chamados:
        if chamado["prioridade"] == "Crítica" and chamado["status"] == "Aberto":
            print(chamado)       

def criar():
    id = chamados[-1]["id"]          
    titulo = input("Digite o titulo do seu problema: ")
    prioridade = input("Digite a prioridade do seu projeto(Baixa,Média,Alta,Crítica): ") 
    status = input("Digite o status(Aberto, Em progresso, Fechado): ") 
    usuario = input("Digite o nome do usuario: ")
    id += 1 

    novo_chamado = {
        "id": id,
        "titulo": titulo,
        "prioridade": prioridade,
        "status": status,
        "usuario": usuario
    }   

    chamados.append(novo_chamado)  
    print(novo_chamado) 



def resolver():
    resolve = input("Digite o usuario do chamado que deseja resolver: ")
    for chamado in chamados:
        if chamado["usuario"] == resolve:
            chamado["status"] = "Em progresso"
            print(chamado)


def fechar():
    fecha = input("Digite o usuario do chamado que deseja fechar: ")
    for chamado in chamados:
        if chamado["usuario"] == fecha:
            chamados.remove(chamado)
            break
    print(chamados)                   








while True: 
   print("Estoque")
   print("1 - Pesquisa por item")
   print("2 - Pesquisa por categoria")
   print("3 - Pesquisa por data de entrada")
   print("4 - Pesquisa por validade")
   print("5 - Adicionar item")
   print("6 - Registrar saída ")
   print("7 - Substituir item")
   print("8 - Mostrar estoque")
   print("0 - sair")

   opcao = input("Escolha uma opção: ")

   if opcao == "1":
      usuario()

   elif opcao == "2":
       prioridade()

   elif opcao == "3":
       status()

   elif opcao == "4":
       urgentes()

   elif opcao == "5":
       criar()

   elif opcao == "6":
       resolver()   

   elif opcao == "7":
       fechar()

   elif opcao == "0":
    print("Saindo do sistema...")
    break
  
   else:
       print("Opção inválida, tente novamente!!!")    