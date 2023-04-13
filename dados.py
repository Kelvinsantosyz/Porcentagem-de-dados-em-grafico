import datetime
import pandas as pd
import json


class Validador:
    def __init__(self, id, nome, idade, cpf, cidade):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.cidade = cidade
        
    

    def verificar(self, id, nome, idade, cpf, cidade):
        if nome == '' and idade is None and cpf is None:
            return 'Vazio'
        if self.id == '':
            return "Id vazio"

        if nome == '':
            return "Nome vazio"

        if nome.isdigit():
            return 'Nome inválido, digite apenas letras'

        if idade == '':
            return "Idade vazia"

        if not idade.isdigit():
            return 'Idade inválida, digite apenas números'

        if not cpf and cidade == '':
            return "Campos cidade e CPF vazios"

        if not cpf:
            return 'CPF vazio'

        if cidade == '':
            return 'Cidade vazia'

        return 'Preenchido'


def dados_main():
   
    with open('Dados.txt', 'r', encoding='utf8') as arquivo:
        linhas = arquivo.readlines()
        dados = [linha.strip().split(',') for linha in linhas]
        colunas = ['ID', 'Nome Completo', 'Idade', 'CPF', 'Cidade']

        df = pd.DataFrame(dados, columns=colunas)

        # Verifica se os campos ID, Nome, Idade e CPF estão preenchidos e adiciona uma nova coluna para mostrar mensagem
        df['Verificação Dados'] = df.apply(
            lambda row: Validador(row['ID'], row['Nome Completo'], row['Idade'], row['CPF'], row['Cidade']).verificar(
                row['ID'], row['Nome Completo'], row['Idade'], row['CPF'], row['Cidade']), axis=1)

        # Cria uma nova coluna 'Data' e preenche com a data atual
        data_atual = datetime.date.today()
        df['Data'] = data_atual.strftime("%d/%m/%Y")

        # Calcula a quantidade de campos preenchidos corretamente
        campos_preenchidos = df['Verificação Dados'][df['Verificação Dados'] == 'Preenchido'].count()

        # Calcula a quantidade de campos não preenchidos corretamente
        campos_nao_preenchidos = df['Verificação Dados'][df['Verificação Dados'] != 'Preenchido'].count()
        

        # Exibe as quantidades
        print(f"Campos preenchidos corretamente: {campos_preenchidos}")
        print(f"Campos não preenchidos corretamente: {campos_nao_preenchidos}")

        # Salva o DataFrame em um arquivo Excel com a data atual no nome
        nome_arquivo = data_atual.strftime("dados_%Y-%m-%d.xlsx")
        df.to_excel(nome_arquivo, index=False)

        return campos_preenchidos, campos_nao_preenchidos



if __name__ == '__main__':
    dados_main()
