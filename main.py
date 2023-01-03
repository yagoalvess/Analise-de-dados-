## Importação das bilbliotecas
import os
import pandas as pd

## Pegar os nomes dos arquivos
nome_arquivo = os.listdir("D:\Documents\python\Vendas")

# Pega os dados das tabelas e colocar em uma tabela só
tabela_total = pd.DataFrame()
for nome in nome_arquivo:
    if "Vendas" in nome:
        tabela = pd.read_csv(f"D:\Documents\python\Vendas\{nome}")
        tabela_total = tabela_total.append(tabela)



#Manipulação da tabela para se conseguir insights na tabela
tabela_produtos = tabela_total.groupby('Produto').sum()
print(tabela_produtos)




