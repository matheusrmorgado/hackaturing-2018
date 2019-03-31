from sklearn.neural_network import MLPClassifier
import pandas as pd
from sklearn.model_selection import train_test_split



data = pd.read_csv("final_dataframe.csv")
dataOut = data['base_hackaturing.pago_ou_nao']
dataIn = data.drop(['base_hackaturing.pago_ou_nao','base_hackaturing.carater_atendimento_URGENCIA','base_hackaturing.tipo_item_OPME','base_hackaturing.tipo_item_PROCEDIMENTO','base_hackaturing.valor_item','base_hackaturing.tipo_item_TAXAS DIVERSAS','base_hackaturing.tipo_item_GASES MEDICINAIS','base_hackaturing.tipo_item_MEDICAMENTOS',], axis=1)

redeNeural = MLPClassifier(verbose = True,
                           max_iter = 1000)
# X_train, X_test, y_train, y_test = train_test_split( dataIn, dataOut, test_size = 0.3, random_state = 100)


rede = redeNeural.fit(dataIn,dataOut)
print(redeNeural)



rede.predict([[20103069,12,1,0,0]])