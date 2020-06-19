import pandas as pd
import requests
import ast
import sqlite3

veritabani = sqlite3.connect("gizemsenoldb.db")
cursor = veritabani.cursor()

#data = pd.read_csv('./paytm_com-ecommerce_sample.csv')
#df = pd.DataFrame(data)
#df = df.drop_duplicates(subset='image')
#df = df.head(20)
#df.to_csv('e-commersedata.csv')

data = pd.read_csv('e-commersedata.csv')

df = pd.DataFrame(data)

dictionary = {}
counter = 0
datas = df.to_dict(orient="records")
cursor.execute("delete from products;")
for data in datas:
    # print(data)
    isim = data['name']
    genel = data['breadcrumbs']
    aciklama = data['desc']
    fiyat = data['list_price']
    marka = data['brand']
    image = data["image"]

    tur = genel.split(" | ")[2]
    
    cursor.execute('''INSERT INTO products(isim,genel,aciklama,fiyat,marka,tur,image) VALUES(?,?,?,?,?,?,?)''',
                    (isim ,genel ,aciklama ,int(fiyat ),marka ,tur, image))
    veritabani.commit()
cursor.close()



    