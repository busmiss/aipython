# 실습
import pandas as pd

box = pd.read_excel('BoxOffice.xlsx')
info = box.info()
print(info)

nation = box['대표국적'].value_counts()
print(nation)

UK = box[box['대표국적']=='영국']
print(UK)

box.groupby('대표국적').min(['순위'])