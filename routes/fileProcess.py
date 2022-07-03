import pandas as pd
from flask import Blueprint, Response, render_template
processFile=Blueprint("processFile", __name__)
def procesoDeExcel():
    data=pd.read_csv("./static/excel/matriz.csv", delimiter=";")
    contenidoCabezera=[]
    contenidoBody=[]
    
    datos=data.iloc[0:, 0:]
    for c in datos:
        contenidoCabezera.append(c)
    for d in datos.values:
        contenidoBody.append(d)
    primerContenido=[contenidoCabezera, contenidoBody]
    return primerContenido

def procesoExcelRender(numeroDeFilas="s",
                       numeroDeColumnas="s", 
                       desdeLaFila="s", 
                       hastaLaFila="s",
                       desdeLaColumna="",
                       hastaLaColumna="s", 
                       nPrimerasFilas="s", 
                       nUltimasFilas="s",
                       soloLaFila="s",
                       soloLaColumna="s",
                       lasFilas="s",
                       lasColumnas="s"
                       ):
    
    data=pd.read_csv("./static/excel/matriz.csv", delimiter=";")
    lenCol=len(data.columns)
    lenR=data.describe().values
    lenRow=int(lenR[0][0])
    cabezeraPorDefecto=[]
    cabezerasNuevos=[]
    datosPorDefecto=[]
    datosNuevos=[]
    if numeroDeFilas.isdigit() or numeroDeColumnas.isdigit():
        if numeroDeFilas.isdigit() and numeroDeColumnas.isdigit():
            dataPandas=data.iloc[0:int(numeroDeFilas), 0:int(numeroDeColumnas)]
        elif  numeroDeFilas.isdigit():
            dataPandas=data.iloc[0:int(numeroDeFilas), 0:lenCol]
        elif numeroDeColumnas.isdigit():
            dataPandas=data.iloc[0:lenRow, 0:int(numeroDeColumnas)]
    else:
        dataPandas=data.iloc[0:lenRow, 0:lenCol]
            
    if desdeLaFila.isdigit() and hastaLaFila.isdigit() or desdeLaColumna.isdigit() and hastaLaColumna.isdigit():    
        if desdeLaFila.isdigit() and hastaLaFila.isdigit():
            dataPandas=data.iloc[int(desdeLaFila)-1:int(hastaLaFila), 0:lenCol]
            if desdeLaColumna.isdigit() and hastaLaColumna.isdigit():
                dataPandas=data.iloc[int(desdeLaFila)-1:int(hastaLaFila), int(desdeLaColumna)-1:int(hastaLaColumna)] 
    
        elif desdeLaColumna.isdigit() and hastaLaColumna.isdigit():
            dataPandas=data.iloc[0:lenRow, int(desdeLaColumna)-1:int(hastaLaColumna)]
            # if desdeLaFila.isdigit() and hastaLaFila.isdigit():          
            #     dataPandas=data.iloc[int(desdeLaFila)-1:int(hastaLaFila), int(desdeLaColumna):int(hastaLaColumna)] 
    
    if nPrimerasFilas is not None and nPrimerasFilas.isdigit():
        dataPandas=data.head(int(nPrimerasFilas))   
    if nUltimasFilas is not None and nUltimasFilas.isdigit():
        dataPandas=data.tail(int(nUltimasFilas))    
    # parte fuerte
    
    if soloLaFila !=None and soloLaFila.isdigit():
        dataPandas=data.iloc[int(soloLaFila)-1:int(soloLaFila), 0:lenCol]
    if soloLaColumna != None and soloLaColumna.isdigit():
        dataPandas=data.iloc[0:lenRow, int(soloLaColumna)-1:int(soloLaColumna)]
    
    if lasFilas!=None and len(lasFilas)>1 or lasColumnas != None and len(lasColumnas)>1:
        if lasFilas!=None and len(lasFilas)>1:
            try:
                listaLetraFil=lasFilas.split(" ")
                listaNumeroFil=[]
                for num in listaLetraFil:
                    listaNumeroFil.append((int(num))-1)
                dataPandas=data.iloc[listaNumeroFil,0:lenCol]
                if lasColumnas != None and len(lasColumnas)>1:
                    try:
                        listaLetraCol=lasColumnas.split(" ")
                    except Exception as error:
                        pass
                    listaNumeroCol=[]
                    for num in listaLetraCol:
                        listaNumeroCol.append((int(num))-1)
                    dataPandas=data.iloc[ listaNumeroFil, listaNumeroCol]
            except Exception as error:
                pass
        elif lasColumnas != None and len(lasColumnas)>1:
            try:
                listaLetraCol=lasColumnas.split(" ")
                listaNumeroCol=[]
                for num in listaLetraCol:
                    listaNumeroCol.append((int(num))-1)
                dataPandas=data.iloc[ 0:lenRow, listaNumeroCol]
            except Exception as error:
                pass
            
    for i in dataPandas:
        cabezerasNuevos.append(i)
    for i in dataPandas.values:
            datosNuevos.append(i)
    
    dataFinal=[cabezerasNuevos,datosNuevos]
    return dataFinal
@processFile.route("/excel-file")
def excelFile():
    p="Hola mundo con responde"
    return p