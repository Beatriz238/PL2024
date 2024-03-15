import csv
import re

def carregar_produtos():
    produtos = {}
    with open('produtos.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            produto_id = int(row['Id'])
            produto_nome = row['Produto'].strip()  # Remove espaços em branco
            produto_preco = row['Preço'].strip()  # Remove espaços em branco
            produtos[produto_id] = {'produto': produto_nome, 'preco': produto_preco}
    return produtos

# Função para listar os produtos disponíveis
def listar_produtos(produtos):
    for id, info in produtos.items():
        print(f"{id}: {info['produto']} ({info['preco']})")

# Função para processar moedas
def processar_moeda(saldo_atual, moedas):
    saldo_euros = 0
    saldo_centavos = 0
    moedas_validas = {'5c': 5, '10c': 10, '20c': 20, '50c': 50, '1e': 1, '2e': 2}
    for moeda in moedas:
        moeda_lower = moeda.lower()  # Converter para minúsculas
        if moeda_lower in moedas_validas:
            valor = moedas_validas[moeda_lower]
            if moeda_lower.endswith('e'):
                saldo_euros += valor
            elif moeda_lower.endswith('c'):
                saldo_centavos += valor
        else:
            print(f"Moeda inválida: {moeda}")
    saldo_atual += saldo_euros * 100 + saldo_centavos
    return saldo_atual

def selecionar_produto(produtos, saldo_atual, id_produto):
    if id_produto in produtos:
        produto = produtos[id_produto]
        preco_produto_str = produto['preco']
        
        # Verificar se o preço é em euros ou em centavos
        if 'e' in preco_produto_str:
            # Extrair valores separadamente para euros e centavos
            match = re.match(r'(\d+)e (\d+)c', preco_produto_str)
            
            if match:
                preco_euros = int(match.group(1))
                preco_centimos = int(match.group(2))
                preco_total = preco_euros * 100 + preco_centimos
                
                print(f"Produto {id_produto} selecionado: {produto['produto']} ({preco_euros}e {preco_centimos}c)")
                
                if saldo_atual >= preco_total:
                    saldo_atual -= preco_total
                    return saldo_atual
                else:
                    print("Erro: Saldo insuficiente.")
                    return saldo_atual
            else:
                print("Erro: Formato de preço inválido.")
                return saldo_atual
        else:
            preco_centavos = int(re.findall(r'\d+', preco_produto_str)[0])
            
            print(f"Produto {id_produto} selecionado: {produto['produto']} ({preco_produto_str})")
            
            if saldo_atual >= preco_centavos:
                saldo_atual -= preco_centavos
                return saldo_atual
            else:
                print("Erro: Saldo insuficiente.")
                return saldo_atual
    else:
        print("Produto não encontrado.")
        return saldo_atual

# Função principal
def main():
    produtos = carregar_produtos()
    saldo_atual = 0

    print("Escolha dos seguintes comandos:\n")
    print("1. LISTAR (lista todos os produtos da máquina)")
    print("2. MOEDA (Ex.: MOEDA 1e 2c- colocar dinheiro na máquina)")
    print("3. SELECIONAR (Ex.: SELECIONAR 1- seleciona o produto que quer comprar)")
    print("4. SAIR (devolve-lhe o troco)")


    while True:
        comando = input("\n>> ").upper()

        if comando.startswith("LISTAR"):
            listar_produtos(produtos)

        elif comando.startswith("MOEDA"):
            moedas = comando.split()[1:]
            if len(moedas) == 1:
                saldo_atual = processar_moeda(saldo_atual, [moedas[0]])
            else:
                saldo_atual = processar_moeda(saldo_atual, moedas)
            print("Dinheiro inserido com sucesso!")
            print(f"Saldo = {saldo_atual // 100}e {saldo_atual % 100}c")

        elif comando.startswith("SELECIONAR"):
            id_produto = int(comando.split()[1])
            saldo_atual = selecionar_produto(produtos, saldo_atual, id_produto)
            print(f"Saldo = {saldo_atual // 100}e {saldo_atual % 100}c")

        elif comando == "SAIR":
            print(f"Troco: {saldo_atual // 100}e {saldo_atual % 100}c")
            print("Obrigado por comprar conosco!")
            break

        else:
            print("Comando inválido.")

if __name__ == "__main__":
    main()