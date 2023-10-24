from sklearn.ensemble import GradientBoostingClassifier
import pandas as pd
import joblib
from Utilitarios.CsvUtils import importarCSV
from Modelos.Modelos import ExportarModelo


class DecisionTree:
    def __init__(self):
        pass

    @staticmethod
    def treinar(nome_arquivo_csv, nome_arquivo_modeloknn):
        GBC = GradientBoostingClassifier()
        dtfr_DadosSensores = importarCSV(nome_arquivo_csv)

        dtfr_DadosSensores.drop('postura', axis='columns')
        dtfr_Posturas = dtfr_DadosSensores['postura']

        GBC.fit(dtfr_DadosSensores, dtfr_Posturas)
        ExportarModelo(GBC, nome_arquivo_modeloknn)

    @staticmethod
    def reconhecer(lst_sensores, modelo):
        lst_colunas = ["sensor0", "sensor1", "sensor2", "sensor3",
                       "sensor4", "sensor5", "sensor6", "sensor7"]
        dtfr_sensores = pd.DataFrame(lst_sensores, columns=lst_colunas)
        classificacao = modelo.Predict(dtfr_sensores)
        return classificacao

