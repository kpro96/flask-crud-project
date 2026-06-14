import pandas as pd 

data = {'Name':['raj','amit','vijay','suresh'], 'Score' :[44.45,38,48,42]}
df= pd.DataFrame(data)
df['Status']=df['Score'].apply(lambda x:'pass' if x >= 45 else 'fail')
print(df)