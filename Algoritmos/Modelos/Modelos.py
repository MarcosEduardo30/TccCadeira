import joblib


def ExportarModelo(modelo, nome_arquivo):
    joblib.dump(modelo, nome_arquivo)


def ImportarModelo(nome_arquivo):
    return joblib.load(nome_arquivo)
