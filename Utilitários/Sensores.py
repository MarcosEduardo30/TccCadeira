import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
from time import sleep
from CsvUtils import exportarCSV


def lerSensores():
    spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
    cs = digitalio.DigitalInOut(board.D5)
    mcp = MCP.MCP3008(spi, cs)

    sensor0 = AnalogIn(mcp, MCP.P0)
    sensor1 = AnalogIn(mcp, MCP.P1)
    sensor2 = AnalogIn(mcp, MCP.P2)
    sensor3 = AnalogIn(mcp, MCP.P3)
    sensor4 = AnalogIn(mcp, MCP.P4)
    sensor5 = AnalogIn(mcp, MCP.P5)
    sensor6 = AnalogIn(mcp, MCP.P6)
    sensor7 = AnalogIn(mcp, MCP.P7)
    lstLeituras = [sensor0.value, sensor1.value, sensor2.value, sensor3.value,
                   sensor4.value, sensor5.value, sensor6.value, sensor7.value]
    return lstLeituras


def criaDataSetCSV(nm_arquivo_csv, novo_arquivo, postura):
    input("Aperte qualquer tecla para começar a rotina: ")
    lst_leituras = []
    for leituras in range(50):
        lst_sensores = [lerSensores(), postura]
        lst_leituras.append(lst_sensores)
        sleep(0.5)
    lst_colunas = ["sensor0", "sensor1", "sensor2", "sensor3",
                   "sensor4", "sensor5", "sensor6", "sensor7", "postura"]
    exportarCSV(nm_arquivo_csv, lst_leituras, novo_arquivo, lst_colunas)
    print("Dados importados para o arquivo " + nm_arquivo_csv)

def isSensoresPressionados(leitura_sensores):
    for leitura in leitura_sensores:
        if leitura != 0:
            return True
    return False