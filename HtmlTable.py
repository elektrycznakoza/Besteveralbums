import pandas as pd

url = "https://www.officialcharts.com/chart-news/the-best-selling-albums-of-all-time-on-the-official-uk-chart__15551/"
tables = pd.read_html(url)
df = tables[0].iloc[1:]

df = df.iloc[:, 1:]
df.columns = ['TYTUŁ', 'ARTYSTA', 'ROK', 'MAX POZ']

liczba_artystow = df['ARTYSTA'].nunique()
print(f"Ilość pojedynczych artystów na liście: {liczba_artystow}")

najczestsze_zespoly = df['ARTYSTA'].value_counts().index.tolist()
print(f"Najczęściej pojawiające się zespoły na liście: {', '.join(najczestsze_zespoly)}")

df.columns = df.columns.str.capitalize()
print(f"Nagłówki kolumn: {', '.join(df.columns)}")

df = df.drop(columns=['Max poz'])
print(f"Nagłówki kolumn bez Max Poz: {', '.join(df.columns)}")

najwiecej_albumow_rok = df['Rok'].value_counts().idxmax()
print(f"Najwięcej albumów wyszło w roku: {najwiecej_albumow_rok}")

df['Rok'] = df['Rok'].astype(int)  # Konwersja kolumny 'Rok' na liczby całkowite
ilosc_albumow_1960_1990 = df[(df['Rok'] >= 1960) & (df['Rok'] <= 1990)].shape[0]
print(f"Ilość albumów wydanych między 1960 a 1990 rokiem: {ilosc_albumow_1960_1990}")

indeks_najmlodszego_albumu = df['Rok'].idxmin()
najmlodszy_album_rok = df.loc[indeks_najmlodszego_albumu, 'Rok']
print(f"Najmłodszy album na liście wyszedł w roku: {najmlodszy_album_rok}")

najwczesniejsze_albumy = df.groupby('Artysta', as_index=False).agg({'Rok': 'min', 'Tytuł': 'first'})
najwczesniejsze_albumy.columns = ['Artysta', 'Najwcześniejszy album', 'Rok najwcześniejszego albumu']

print("Najwcześniej wydane albumy każdego artysty:")
print(najwczesniejsze_albumy)

najwczesniejsze_albumy.to_csv(r'C:\Users\leszek.stanislawski\Downloads\Kodilla\Python\Pandas\najwczesniejsze_albumy.csv', index=False)
