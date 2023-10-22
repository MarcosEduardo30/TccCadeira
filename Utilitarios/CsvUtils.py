import csv
import pandas as pd


def exportarCSV(nm_arquivo, lst_conteudo, novo_arquivo, lst_cabecalho=None):
    try:
        if novo_arquivo:
            with open(nm_arquivo, 'w', newline='') as arquivoCSV:
                escritorCVS = csv.writer(arquivoCSV)
                escritorCVS.writerow(lst_cabecalho)
                escritorCVS.writerows(lst_conteudo)
        else:
            with open(nm_arquivo, 'a', newline='') as arquivoCSV:
                escritorCVS = csv.writer(arquivoCSV)
                escritorCVS.writerows(lst_conteudo)
    except FileNotFoundError:
        print("Arquivo não encontrado")


def importarCSV(nm_arquivo):
    try:
        return pd.read_csv(nm_arquivo)
    except FileNotFoundError:
        print("Arquivo não encontrado")
