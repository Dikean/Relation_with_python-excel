import pandas as pd

df1= pd.read_excel('./Database/Empleados.xlsx', sheet_name="Empleados")
df2= pd.read_excel('./Database/Salarios.xlsx')

df_resulante= pd.merge(df1, df2, on="Cedula")

df_resulante.to_excel("./Resulante.xlsx", index=False)


#test