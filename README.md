# Algoritmo de Limpeza de Dados em Python para as Planilhas 

Este é um algoritmo desenvolvido em Python 3 para limpar dados de uma tabela em formato Excel, com o objetivo de padronizar e corrigir valores, além de separar registros com valores nulos para posterior tratamento.

## Dependências

O algoritmo requer as seguintes bibliotecas Python:

- pandas
- re
- sys

Certifique-se de ter o Python 3 instalado em seu computador. Você pode baixar o Python em [python.org](https://www.python.org/).

Instale as dependências usando o pip. Abra o terminal ou prompt de comando e digite o seguinte comando:

```shell
pip install pandas re sys
```

## Como Usar

1. Faça o download do script de limpeza de dados em formato .py e do arquivo Excel que deseja limpar.

2. No terminal ou prompt de comando, navegue até a pasta em que o script e o arquivo Excel estão localizados.

3. Execute o script com o seguinte comando, substituindo "nome_do_arquivo.xlsx" pelo nome do arquivo que você deseja limpar:

```shell
python corrigir.py nome_do_arquivo.xlsx
```

4. O script criará três novos arquivos Excel na mesma pasta em que o arquivo original está localizado:
   - COMCPF.xlsx: tabela limpa com valores padronizados e sem registros nulos de CPF.
   - CPFsnulos.xlsx: tabela com registros nulos de CPF.
   - CPFs_e_fones_nulos.xlsx: tabela com registros nulos de CPF e telefone.

O script também imprimirá no terminal ou prompt de comando as seguintes informações:

- Número total de linhas na tabela original.
- Número total de linhas na tabela com registros nulos de CPF.
- Número total de linhas na tabela com registros nulos de CPF e telefone.

Pronto! Agora você pode usar os arquivos Excel gerados para análise e tratamento posterior dos registros nulos.
