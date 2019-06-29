import time
import nltk
import pandas as pd


# Set some pandas options controlling output format
pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 99)
pd.set_option('display.max_rows', 99999)
pd.set_option('display.width', 9999)


def naturalang():  
    for sent in (verbatim):
        nltk.word_tokenize(sent, language='spanish')


dfm = pd.read_csv("2018NPS-Stor.csv", index_col='id', encoding='utf-8', sep=';')
verbatim = dfm['verbatim']

dfm['verbatim'] = dfm['verbatim'].str.lower()

print(dfm.columns)


start = time.time()
naturalang()
end = time.time()
print('Tiempo en segundos (W/Processes) -', end - start)

