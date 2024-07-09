
import pandas as pd
import csv 
import seaborn as sns
import matplotlib.pyplot as plt

    
data = pd.read_csv('gasolina.csv', delimiter=',', decimal='.')
gasolina = data

plt.figure(figsize=(8, 5))

sns.set_style("ticks")
graph = sns.lineplot(x="dia", y="venda", data=gasolina, marker='o')

plt.title('Preço da Gasolina', fontsize=15)
plt.xlabel('Data', fontsize=13)
plt.ylabel('Valor', fontsize=12)

plt.savefig("gasolina.png")
plt.show()
