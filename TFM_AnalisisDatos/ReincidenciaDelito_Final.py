import pandas as pd
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pickle
Classificacion=pd.read_csv(r'D:/Maestria/TFM/Datos/OUTPUT/CSV_Visualizacion10.csv')
Classificacion.info()
x_train,x_test, y_train,y_test = train_test_split( 
    Classificacion[['delito','niv_consu','ocupacion']],
    Classificacion['rein_delito'],
    test_size=0.20,
    random_state=0
 )
modelo= RandomForestClassifier(n_estimators=50,n_jobs=-1)
prediccion =modelo.fit(x_train,y_train)
filename = 'D:\Maestria\TFM\Datos\OUTPUT\salidas_modelos\modeloRandomForest.pkl'
pickle.dump(prediccion, open(filename, 'wb'))