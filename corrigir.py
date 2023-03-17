import pandas as pd
import re
import sys

if len(sys.argv) < 2:
    print("Por favor, forneça o caminho para o arquivo como argumento.")
    sys.exit()

filename = sys.argv[1]

df = pd.read_excel(filename, dtype={'NR_CPF': str})


def corrigir_FONE(DDD, FONE):
    if pd.isna(DDD) or pd.isna(FONE):
        return None

    FONE = re.sub(r'\D', '', str(FONE))

    if len(FONE) != 8 and len(FONE) != 9:
        return None

    return '{} {}'.format(str(DDD), FONE)


df['FONE1'] = df.apply(lambda x: corrigir_FONE(
    x['DDD1'], x['FONE1']), axis=1)

df['FONE2'] = df.apply(lambda x: corrigir_FONE(
    x['DDD2'], x['FONE2']), axis=1)

df['DDD2'] = df.apply(lambda x: corrigir_FONE(
    x['DDD2'], ''), axis=1)

df_nulos = df[df['NR_CPF'].isna()]

df_nulos_fones = df[(df['NR_CPF'].isna()) & (
    df['FONE1'].isna()) & (df['FONE2'].isna())]

df = df.dropna(subset=['NR_CPF'])

df_nulos.to_excel('CPFsnulos.xlsx', index=False)
df_nulos_fones.to_excel('CPFs_e_fones_nulos.xlsx', index=False)

df.iloc[0, df.columns.get_loc('DS_ENDERECO')] = pd.NA

df['DS_ENDERECO'] = df['DS_ENDERECO'].str.upper()
df['DS_BAIRRO'] = df['DS_BAIRRO'].str.upper()
df['DS_COMPLEMENTO'] = df['DS_COMPLEMENTO'].str.upper()

df.to_excel('COMCPF.xlsx', index=False)

print(f"Tabela original tem {df.shape[0]} linhas")
print(f"Tabela com registros de CPF´s nulos tem {df_nulos.shape[0]} linhas")
print(f"Tabela com registros nulos de telefone e CPF tem {df_nulos_fones.shape[0]} linhas")
