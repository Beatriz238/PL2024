# Proibido usar o módulo CSV;
#Ler o dataset, processá-lo e criar os seguintes resultados:
    #Lista ordenada alfabeticamente das modalidades desportivas;
    #Percentagens de atletas aptos e inaptos para a prática desportiva;
    #Distribuição de atletas por escalão etário (escalão = intervalo de 5 anos): ... [30-34], [35-39], ...

def ler_csv(csv):
    data = []
    modalidades = set()
    aptos = 0
    inaptos = 0
    distribuicao_escalao = {}

    with open(csv, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        header = lines[0].strip().split(',')  #ignora o cabeçalho
        lines = lines[1:]

        for line in lines:
            values = line.strip().split(',')  #faz o parsing

            record = {}
            for i in range(len(header)):
                record[header[i]] = values[i]
            data.append(record)

            modalidades.add(record['modalidade'])  #adiciona a modalidade ao conjunto

            if record['resultado'] == 'true':  #verifica se o atleta está apto ou inapto
                aptos += 1
            else:
                inaptos += 1

            # calcula o escalão etário do atleta e adiciona ao dicionário de distribuição
            idade = int(record['idade'])
            escalao = f"[{idade // 5 * 5} - {idade // 5 * 5 + 4}]"
            if escalao not in distribuicao_escalao:
                distribuicao_escalao[escalao] = 1
            else:
                distribuicao_escalao[escalao] += 1

    
    distribuicao_percentagens = {escalao: (quantidade, (quantidade / (aptos +inaptos)) * 100) for escalao, quantidade in distribuicao_escalao.items()}
                
    return sorted(list(modalidades)), (aptos / (aptos + inaptos)) * 100, (inaptos / (aptos + inaptos)) * 100, {k: distribuicao_percentagens[k] for k in sorted(distribuicao_percentagens)}

csv = 'emd.csv'
modalidades, percentagem_aptos, percentagem_inaptos, distribuicao_escalao = ler_csv(csv)
print("\nModalidades desportivas:", modalidades)
print("\nPercentagem de atletas aptos:", percentagem_aptos, '%')
print("Percentagem de atletas inaptos:", percentagem_inaptos, '%')
print("\nDistribuição de atletas por escalão etário:")
for escalao, (quantidade, percentagem) in distribuicao_escalao.items():
    print(f"{escalao} -> {quantidade} atletas ({percentagem:.2f}%)")
print('\n')
