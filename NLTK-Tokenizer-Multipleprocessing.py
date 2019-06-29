from multiprocessing import Pool
import time
import nltk
import pandas as pd
import numpy as np

# Set some pandas options controlling output format
pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 99)
pd.set_option('display.max_rows', 99999)
pd.set_option('display.width', 9999)


def naturalang1():  
    for sent in (verbatim1):
        nltk.word_tokenize(sent, language='spanish')    

def naturalang2():  
    for sent in (verbatim2):
        nltk.word_tokenize(sent, language='spanish')
        
def naturalang3():  
    for sent in (verbatim3):
        nltk.word_tokenize(sent, language='spanish')      

def naturalang4():  
    for sent in (verbatim4):
        nltk.word_tokenize(sent, language='spanish')
        

dfm = pd.read_csv("2018NPS-Stor.csv", index_col='id', encoding='utf-8', sep=';')
verbatim = dfm['verbatim']


ndivisiones = 4
print("PARTICIONES EN BLOQUES: ", ndivisiones)
verbatim1 = (np.array_split(dfm['verbatim'],ndivisiones)[0])
verbatim2 = (np.array_split(dfm['verbatim'],ndivisiones)[1])
verbatim3 = (np.array_split(dfm['verbatim'],ndivisiones)[2])
verbatim4 = (np.array_split(dfm['verbatim'],ndivisiones)[3])


if __name__ == '__main__':
    processes = 4
    pool = Pool(processes)

    start2 = time.time()
         
    r1 = pool.apply_async(naturalang1)
    
    r2 = pool.apply_async(naturalang2)

    r3 = pool.apply_async(naturalang3)

    r4 = pool.apply_async(naturalang4)

    
    pool.close()
    pool.join()
    end2 = time.time()
    
    print('Tiempo en segundos (4 Processes) -', end2 - start2)

#