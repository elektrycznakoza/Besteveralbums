import pandas as pd

# Krok 1: Wczytaj dane
url = "https://www.officialcharts.com/chart-news/the-best-selling-albums-of-all-time-on-the-official-uk-chart__15551/"
tables = pd.read_html(url)

# Wybierz odpowiednią tabelę i pomij pierwszy wiersz
df = tables[0].iloc[1:]

# Usuń zbędną kolumnę
df = df.iloc[:, 1:]

# Krok 2: Zmień nagłówki kolumn na polskie odpowiedniki
df.columns = ['TYTUŁ', 'ARTYSTA', 'ROK', 'MAX POZ']

# Krok 3: Ilość pojedynczych artystów
liczba_artystow = df['ARTYSTA'].nunique()
print(f"Ilość pojedynczych artystów na liście: {liczba_artystow}")

# Krok 4: Zespoły pojawiające się najczęściej
najczestsze_zespoly = df['ARTYSTA'].value_counts().index.tolist()
print(f"Najczęściej pojawiające się zespoły na liście: {', '.join(najczestsze_zespoly)}")

# Krok 5: Zmień nagłówki kolumn
df.columns = df.columns.str.capitalize()
print(f"Nagłówki kolumn: {', '.join(df.columns)}")

# Krok 6: Wyrzuć kolumnę ‘Max Poz’
df = df.drop(columns=['Max poz'])
print(f"Nagłówki kolumn bez Max Poz: {', '.join(df.columns)}")

# Krok 7: W którym roku wyszło najwięcej albumów
najwiecej_albumow_rok = df['Rok'].value_counts().idxmax()
print(f"Najwięcej albumów wyszło w roku: {najwiecej_albumow_rok}")

# Krok 8: Ile albumów między 1960 a 1990
df['Rok'] = df['Rok'].astype(int)  # Konwersja kolumny 'Rok' na liczby całkowite
ilosc_albumow_1960_1990 = df[(df['Rok'] >= 1960) & (df['Rok'] <= 1990)].shape[0]
print(f"Ilość albumów wydanych między 1960 a 1990 rokiem: {ilosc_albumow_1960_1990}")

# Krok 9: Najmłodszy album na liście
indeks_najmlodszego_albumu = df['Rok'].idxmin()
najmlodszy_album_rok = df.loc[indeks_najmlodszego_albumu, 'Rok']
print(f"Najmłodszy album na liście wyszedł w roku: {najmlodszy_album_rok}")

# Krok 10: Lista najwcześniej wydanych albumów każdego artysty
najwczesniejsze_albumy = df.groupby('Artysta')['Rok'].min().reset_index()
print("Najwcześniej wydane albumy każdego artysty:")
print(najwczesniejsze_albumy)

# Krok 11: Zapisz listę do pliku CSV
najwczesniejsze_albumy.to_csv("najwczesniejsze_albumy.csv", index=False)
