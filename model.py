import pandas as pd
import pickle



dataset = pd.read_csv("health care diabetes.csv")

dataset['Outcome'].value_counts()

dataset['Glucose'].isin([0]).sum()
mean_data_glucose = dataset['Glucose'].mean(skipna = True)
dataset['Glucose']=dataset.replace(0,mean_data_glucose)
dataset['Glucose'].isin([0]).sum()

dataset.head()


dataset['BloodPressure'].isin([0]).sum()
median_data_bloodpressure = dataset["BloodPressure"].median(skipna= True)
median_data_bloodpressure


dataset['BloodPressure']=dataset['BloodPressure'].replace(0,median_data_bloodpressure)
dataset['BloodPressure'].isin([0]).sum()

def median_replace(dataset_1):
    median_data = dataset_1.median(skipna=True)
    dataset_1_upd = dataset_1.replace(0,median_data)
    return dataset_1_upd

dataset['SkinThickness']=median_replace(dataset['SkinThickness'])

dataset['SkinThickness'].isin([0]).sum()

dataset['Insulin'].isin([0]).sum()
dataset['Insulin']=median_replace(dataset["Insulin"])

dataset['BMI'].isin([0]).sum()
dataset['BMI'] = median_replace(dataset["BMI"])

dataset['BMI'].isin([0]).sum()




X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)


from sklearn.ensemble import RandomForestClassifier
classifier =RandomForestClassifier(n_estimators=20)
classifier.fit(X_train,y_train)

filename = 'diabetes-prediction-rfc-model.pkl'
pickle.dump(classifier, open(filename, 'wb'))




