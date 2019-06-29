import time
import pandas as pd

# Set some pandas options controlling output format
pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 99)
pd.set_option('display.max_rows', 99999)
pd.set_option('display.width', 9999)

def sentiment(x):
    dfm['positivo'] = dfm['verbatim'].str.contains(positivo)
    dfm['negativo'] = dfm['verbatim'].str.contains(negativo)
    dfm1 = dfm[['negativo','positivo','verbatim']]


def sentiment_analysis(x):
    positivo_sum = dfm.groupby(['empresa', 'prod'])['positivo'].sum().rename("count")
    positivo_porc = positivo_sum / positivo_sum.groupby(level=0).sum()
    print("__________________________________") 
    print("Cantidad de Respuestas Positivas")
    print("__________________________________")
    print(positivo_sum)
    print("__________________________________") 
    print("Porcentaje de Respuestas Positivas")
    print("__________________________________")    
    print(positivo_porc)
        
def motive(x):
    dfm['servicio'] = dfm['verbatim'].str.contains(servicio)
    dfm['conveniencia'] = dfm['verbatim'].str.contains(conveniencia)
    dfm['relacionamiento'] = dfm['verbatim'].str.contains(relacionamiento)        
    dfm2 = dfm[['servicio','conveniencia','relacionamiento','verbatim']]


def motive_analysis(x):  
    dfm['servicio'] = dfm['verbatim'].str.contains(servicio)    
    servicio_sum = dfm.groupby(['empresa', 'prod'])['servicio'].sum().rename("count")
    servicio_porc = servicio_sum / servicio_sum.groupby(level=0).sum()
    print("__________________________________") 
    print("Cantidad de Respuestas sobre Servicio")
    print("__________________________________")
    print(servicio_sum)
    print("__________________________________") 
    print("Porcentaje de Respuestas sobre Servicio")
    print("__________________________________")    
    print(servicio_porc)
                       
dfm = pd.read_csv("2018NPS-Stor.csv", index_col='id', encoding='utf-8', sep=';')
dfm['verbatim'] = dfm['verbatim'].str.lower()
verbatim = dfm['verbatim']
print(dfm.columns)

positivo = ('bueno|genial|barbaro|buenas|bien|perfecto|satisfecho|recomiendo|buenisimo|lujo|encantado|maravilla|increible')
negativo = ('malo|pesimo|malisimo|peor|caro|problema|problemas|fallas|corta|mal|mejorar|pierde|cortes')
servicio = ('cobertura|señal|llamo|llama|llamadas|llamados|mensajes|internet|navegar|navegacion|navego|cortes|corta|corto|velocidad|lento|rapido|rápido')
relacionamiento = ('atencion|atención|oficina|representante|atienden|resuelven|solucion|resolucion|esperar|espera|asesor|asesoran')
conveniencia = ('precio|precios|coto|costoso|caro|barato|carisimo|baratisimo|aumento|aumenta|aumentos|tarifa|factura|recarga|recargo|abono|plan|planes|promo|promocion|promoción|promociones')

start = time.time()

sentiment(verbatim)
sentiment_analysis(verbatim)
motive(verbatim)
motive_analysis(verbatim)

end = time.time()
print('Tiempo en segundos (W/Processes) -', end - start)