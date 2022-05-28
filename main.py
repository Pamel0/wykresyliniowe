import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# sns.set (rc={'figure.figsize': (8, 8)})
# sns.lineplot(x=[1,2,3,4], y=[1,4,9,16],
#              label='linia nr1', color='red', marker='o',linestyle=':')
# sns.lineplot(x=[1,2,3,4], y=[2,5,10,17],
#              label='linia nr2', color='green', marker='^',linestyle=':')
# plt.xlabel('oś x')
# plt.ylabel('oś y')
# plt.title('Wykres liniowy')
# plt.show()

#wczytanie pliku, ramka danych do ramki danych + na wykres (pandas)
#wczytanie pliku do ramki danych, grupa i wykres

# x = [1, 20] - krok 0,75
# f(x) = 1/x - 75 - wartości z przedziału

# x = np.linspace(1, 20, 75)
# x1 = np.arange(1, 20.75, 1)
# y = (1/x)
# plt.plot(x, y, 'mo-', label='f(x) = 1/x')
# plt.legend()
# plt.xlabel('oś x')
# plt.ylabel('oś y')
# plt.title('Ciekawy wykres')
# plt.show()
# print(x)
# print(x1)

#######################################################################################################
#Zad1.
# etykiety = np.arange(0, 5)
#
# wartosciDuze = [101, 70, 75, 25, 50]
# wartosciMale = [20, 10, 30, 10, 0]
#
# linia = np.arange(0, 6)
# wartosc = np.full(6, 120)
#
# plt.title('Tytul')
# plt.bar(x=etykiety, height=wartosciDuze, color=['teal', 'darkgreen', 'greenyellow', 'pink', 'lawngreen'])
# plt.bar(x=etykiety, height=wartosciMale, color=['indigo', 'cyan', 'lime', 'blue', 'blue'])
# plt.plot(linia, wartosc, 'g')
# plt.axis([-0.60, 5.25, 0, 150])
# plt.savefig('1.pdf', format='pdf')
# plt.show()

#Zad2.
# xlsx = pd.ExcelFile('mieszkania1.xlsx')
# df = pd.read_excel(xlsx, header = 0)
#
# ind = df[df['Formy budownictwa'] == 'indywidualne']
# spo = df[df['Formy budownictwa'] == 'spółdzielcze']
# kom = df[df['Formy budownictwa'] == 'komunalne']
#
# lata = df.groupby('Rok').groups.keys()
#
# plt.axis([2014, 2019, 0, 90000])
# plt.bar(x = lata, height = ind['Wartość'], color = 'blue', label = 'indywidualne')
# plt.bar(x = lata, height = spo['Wartość'], color = 'gray', label = 'spółdzielcze')
# plt.bar(x = lata, height = kom['Wartość'], color = 'green', label = 'komunalne')
# plt.title('Wykres wartości mieszkań w latach w zależności od formy budownictwa')
# plt.ylabel('Wartość')
# plt.xlabel('Lata')
# plt.text(2014.1, 85000, '990624')
# plt.legend()
# plt.savefig('mieszkania.pdf', format='pdf')
# plt.show()

# #Zad3.
# xlsx = pd.ExcelFile('turystyka1.xlsx')
# df = pd.read_excel(xlsx, header=0)
#
# nowydf = df.transpose()
#
# nowydf = nowydf.reset_index()
#
#
# nowydf.columns = ['Kategoria', 'Rok', 'Ilość']
#
#
# print(nowydf.groupby('Kategoria').mean())
#
#
# # seria = nowydf.groupby('Kategoria')['Ilość'].sum()
# #
# # plt.pie(x = seria)
# # plt.show()
# # print(seria)
#
# # print(nowydf)

# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx)

#######################################################################################################

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)

roczniki = df['Rok'].unique()
grupa = df.groupby(['Rok']).agg({'Liczba':['sum']})
wykres = grupa.plot()
wykres.set_ylabel('Liczba urodzonych dzieci')
wykres.set_xticks(roczniki)
wykres.tick_params(axis='x', labelrotation=80)
wykres.legend()
plt.subplots_adjust(left=0.15, right=0.9, bottom=0.15, top=0.9)
plt.title("Liczba urodzonych dzieci dla każdego roku")
plt.show()
































#
# m = (df[df.Plec == 'M'])
# k = (df[df.Plec == 'K'])
#
# wykres = m.plot.bar()
# wykres.set_ylabel('Ilość osób')
# wykres.set_xlabel('Płeć')
# wykres.tick_params(axis='x', labelrotation=0)
# wykres.legend()
# wykres.set_title('Płcie')
# plt.show()





























