import pandas as pd
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pickle
import hashlib
import base64
Reincidencias =pd.read_csv('D:/Maestria/TFM/Datos/OUTPUT/CSV_Visualizacion10.csv')
feature_cols =['delito','niv_consu','ocupacion']
x = Reincidencias[feature_cols]
y=Reincidencias.rein_delito    
x_train, x_test, y_train, y_test =train_test_split(
    x,y,test_size=0.20,random_state=0
)
modelo = LogisticRegression()
prediccion=modelo.fit(x_train,y_train)                   
filename = 'D:\Maestria\TFM\Datos\OUTPUT\salidas_modelos\modeloRegresionLogistica.pkl'
pickle.dump(prediccion, open(filename, 'wb'))  