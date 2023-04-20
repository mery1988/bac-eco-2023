import pandas as pd
com=pd.read_csv("commandes.csv",sep=";",encoding="utf-8")

print(com.shape)
com["PrixTotal"]=com["PrixPlat"]*com["NbrePlats"]
print(com.info())
print("----------sum prix total-----------")
print(com["PrixTotal"].sum())
com_tri=com.sort_values(by=["NumTable","NomPlat"],ascending=[True,False])
print("------data frame trié-------------")
print(com_tri[["NumTable","NomPlat"]])