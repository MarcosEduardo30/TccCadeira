from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import joblib
from Utilitarios.CsvUtils import importarCSV
from Modelos.Modelos import ExportarModelo


class KNN:
    def __init__(self):
        pass

    @staticmethod
    def treinar(nome_arquivo_csv, nome_arquivo_modeloknn):
        knn5 = KNeighborsClassifier(n_neighbors=5)
        dtfr_DadosSensores = importarCSV(nome_arquivo_csv)

        dtfr_DadosSensores.drop('postura', axis='columns')
        dtfr_Posturas = dtfr_DadosSensores['postura']

        knn5.fit(dtfr_DadosSensores, dtfr_Posturas)
        ExportarModelo(knn5, nome_arquivo_modeloknn)

    @staticmethod
    def reconhecer(lst_sensores, modelo):
        lst_colunas = ["sensor0", "sensor1", "sensor2", "sensor3",
                       "sensor4", "sensor5", "sensor6", "sensor7"]
        dtfr_sensores = pd.DataFrame(lst_sensores, columns=lst_colunas)
        classificacao = modelo.Predict(dtfr_sensores)
        return classificacao

