from sklearn.naive_bayes import GaussianNB
import pandas as pd
import joblib
from Utilitarios.CsvUtils import importarCSV
from Modelos.Modelos import ExportarModelo


class NaiveBayes:
    def __init__(self):
        pass

    @staticmethod
    def treinar(nome_arquivo_csv, nome_arquivo_modeloknn):
        nb = GaussianNB()
        dtfr_DadosSensores = importarCSV(nome_arquivo_csv)

        dtfr_DadosSensores.drop('postura', axis='columns')
        dtfr_Posturas = dtfr_DadosSensores['postura']

        nb.fit(dtfr_DadosSensores, dtfr_Posturas)
        ExportarModelo(nb, nome_arquivo_modeloknn)

    @staticmethod
    def reconhecer(lst_sensores, modelo):
        lst_colunas = ["sensor0", "sensor1", "sensor2", "sensor3",
                       "sensor4", "sensor5", "sensor6", "sensor7"]
        dtfr_sensores = pd.DataFrame(lst_sensores, columns=lst_colunas)
        classificacao = modelo.Predict(dtfr_sensores)
        return classificacao

