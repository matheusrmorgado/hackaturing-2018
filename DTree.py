import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
import matplotlib as plt
from sklearn.metrics import classification_report
import graphviz 

data = pd.read_csv("export_dataframe.csv")
X = data.drop(['base_hackaturing.pago_ou_nao', 'base_hackaturing.servico' ,'base_hackaturing.carater_atendimento_URGENCIA','base_hackaturing.carater_atendimento_-','base_hackaturing.tipo_item_OPME','base_hackaturing.tipo_item_PROCEDIMENTO','base_hackaturing.valor_item','base_hackaturing.quantidade', 'base_hackaturing.valor_pago','base_hackaturing.tipo_item_TAXAS DIVERSAS','base_hackaturing.tipo_item_GASES MEDICINAIS','base_hackaturing.tipo_item_DIARIAS','base_hackaturing.tipo_item_MEDICAMENTOS','base_hackaturing.tipo_guia_Honorario'], axis=1)
Y = data['base_hackaturing.pago_ou_nao']
X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.5, random_state = 100)

# Creating the Decision Tree using Gini
clf_gini = tree.DecisionTreeClassifier(criterion = "gini", random_state = 100)
clf_gini.fit(X_train, y_train)


# Create a Prediction version of the Tree using the test portion of the dataset
y_pred = clf_gini.predict(X_test)
y_pred

target_names = [ 'Não pago', 'Pago']
print(classification_report(y_test, y_pred, target_names=target_names))

dot_data = tree.export_graphviz(clf_gini, out_file=None) 
graph = graphviz.Source(dot_data) 
graph.render("DecisionTree")