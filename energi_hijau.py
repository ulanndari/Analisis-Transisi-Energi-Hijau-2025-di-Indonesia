# impor pandas untuk mengelola data CSV
import pandas as pd

# Baca file CSV untuk emisi perusahaan.csv dari folder proyek
df = pd.read_csv('c:/energihijau2025/emisi_perusahaan.csv')

# Definisikan dulu batas pajak karbon (50ton Co2, sesuai dengan regulasi pemerintah)
batas = 50

# iterasi setiap baris di dataframe untuk melakukan cek emisi
for index, row in df.iterrows():
    # ambil nilai emisi dari kolom emisi_2024
    emisi = row['Emisi_2024']
    # ambil nama perusahaan untuk output
    perusahaan = row['Nama_Perusahaan']
    # cek apakah emisi itu melebihi batas penggunaan, dengan menggunakan if-else
    if emisi > batas:
        # cetak status kena pajak emisi jika > 50 ton
        print(f"{perusahaan} KENA pajak karbon dengan emisi {emisi} ton!")
    else:
        # cetak status bebas pajak jika emisi <= 50 ton
        print(f"{perusahaan} BEBAS pajak karbon dengan emisi {emisi} ton!")

# import pandas untuk mengelola data CSV
import pandas as pd

# Baca file CSV untuk emisi perusahaan.csv dari folder proyek
df = pd.read_csv('C:/energihijau2025/emisi_perusahaan.csv')

# Definisikan dulu batas pajak karbon (50ton Co2, sesuai dengan regulasi pemerintah)
batas = 50
tarif = 20000

# iterasi setiap baris di dataframe untuk melakukan cek emisi
for index, row in df.iterrows():
    # ambil nilai emisi dari kolom emisi_2024
    emisi = row['Emisi_2024']
    # ambil nama perusahaan untuk output
    perusahaan = row['Nama_Perusahaan']
    # cek apakah emisi itu melebihi batas penggunaan, dengan menggunakan if-else
    if emisi > batas:
        # hitung pajak: (emisi - batas) * tarif
        pajak = (emisi - batas) * tarif
        # cetak status kena pajak emisi jika > 50 ton
        print(f"{perusahaan} KENA pajak karbon Rp {pajak}")
    else:
        # cetak status bebas pajak jika emisi <= 50 ton
        print(f"{perusahaan} BEBAS pajak karbon")

# import pandas untuk mengelola data CSV
import pandas as pd

# Baca file CSV untuk emisi perusahaan.csv dari folder proyek
df = pd.read_csv('c:/energihijau2025/emisi_perusahaan.csv')

# INISIASI LIST KOSONG UNTUK MENYIMPAN EMISI
emisi_list = []

# iterasi setiap baris di dataframe untuk melakukan cek emisi
for index, row in df.iterrows():
    # ambil nilai emisi dari kolom emisi_2024
    emisi = row['Emisi_2024']
    # tambahkan emisi kedalam list menggunakan "APPEND"
    emisi_list.append(emisi)
# cetak list emisi untuk verifikasi
print("Data emisi perusahaan:",emisi_list)

# import pandas untuk mengelola data CSV
import pandas as pd

# Baca file CSV untuk emisi perusahaan.csv dari folder proyek
df = pd.read_csv('c:/energihijau2025/emisi_perusahaan.csv')

# INISIASI LIST KOSONG UNTUK MENYIMPAN EMISI
emisi_list = []

# iterasi setiap baris di dataframe untuk melakukan cek emisi
for index, row in df.iterrows():
    # ambil nilai emisi dari kolom emisi_2024
    emisi = row['Emisi_2024']
    # tambahkan emisi kedalam list menggunakan "APPEND"
    emisi_list.append(emisi)

# Definisikan dulu batas pajak karbon (50ton Co2, sesuai dengan regulasi pemerintah)
batas = 50

# iterasi list emisi untuk cek kepatuhan

for i,emisi in enumerate(emisi_list):
    perusahaan = df.iloc[i]['Nama_Perusahaan']

    # cek apakah emisi itu melebihi batas penggunaan, dengan menggunakan if-else
    if emisi > batas:
        # hitung pajak: (emisi - batas) * tarif
        pajak = (emisi - batas) * tarif
        # cetak status kena pajak jika emisi > 50 ton
        print(f"{perusahaan} KENA pajak dengan emisi {emisi} ton")
    else:
        # cetak status bebas pajak jika emisi <= 50 ton
        print(f"{perusahaan} BEBAS pajak dengan emisi {emisi} ton!")

        # import pandas untuk mengelola data CSV
import pandas as pd

# Baca file CSV untuk emisi perusahaan.csv dari folder proyek
df = pd.read_csv('c:/energihijau2025/emisi_perusahaan.csv')

# INISIASI DICT KOSONG UNTUK MENYIMPAN EMISI
emisi_dict = {}

# iterasi setiap baris di dataframe untuk simpan ke dictionary
for index, row in df.iterrows():
    # ambil nama perusahaa  sebagai key dictionary
    perusahaan = row['Nama_Perusahaan']
    # tambahkan nilai emisi dari kolom emisi_2024 sebagai nilainya
    emisi = row['Emisi_2024']
    # tambahkan pasangan perusahaan sama emisi kedalam dictionary
    emisi_dict[perusahaan] = emisi

# cetak dictionary emisi untuk verifikasi
print("data emisi perusahaan: ",emisi_dict)

# impor pandas untuk mengelola data CSV 
import pandas as pd

# baca file CSV emisi_perusahaan.csv dari folder proyek
df = pd.read_csv('C:/energihijau2025/emisi_perusahaan.csv')

emisi_dict = {}  # Inisialisasi dictionary kosong

for index, row in df.iterrows():
    perusahaan = row['Nama_Perusahaan']
    # simpan emisi dan klaim hijau dalam dictionary bersarang
    emisi_dict[perusahaan] = {
        'emisi': row['Emisi_2024'],
        'klaim': row['Klaim_Hijau']
    }

# iterasi dictionary untuk cek greenwashing
for perusahaan, data in emisi_dict.items():
    # cek apakah perusahaan mengklaim hijau dan emisi > 50 ton
    if data['klaim'] == 'Ya' and data['emisi'] > 50:
        print(f"{perusahaan} berpotensi melakukan greenwashing.")


# iterasi dictionary untuk cek greenwashing
for perusahaan, data in emisi_dict.items():
    # cek apakah perusahaan mengklaim hijau dan emisi >50 ton
    if data['klaim']=='ya'and data['emisi']>50:
        # cetak status greenwashing jika kondisi terpenuhi
        print(f"{perusahaan} TERDETEKSI greenwashing dengan emisi {data['emisi']} ton!")
    else:
        # cetak status tidak greenwashing jika kondisi tidak terpenuhi
        print(f"{perusahaan} TIDAK TERDETEKSI greenwashing!")

        # Impor Pandas untuk mengelola data CSV
import pandas as pd

# Definisikan fungsi untuk menghitung pajak karbon
def hitung_pajak(emisi, batas=50, tarif=20000):
    # Cek apakah emisi melebihi batas
    if emisi > batas:
        # Hitung pajak: (emisi - batas) * tarif
        pajak = (emisi - batas) * tarif
        # Kembalikan nilai pajak
        return pajak
    # Kembalikan 0 jika emisi <= batas
    return 0

# Baca file CSV emisi_perusahaan.csv dari folder proyek
df = pd.read_csv('C:/energihijau2025/emisi_perusahaan.csv')

# Iterasi setiap baris di dataframe untuk hitung pajak
for index, row in df.iterrows():
    # Ambil nama perusahaan untuk output
    perusahaan = row['Nama_Perusahaan']
    # Ambil nilai emisi dari kolom Emisi_2024
    emisi = row['Emisi_2024']
    # Panggil fungsi hitung_pajak untuk dapatkan pajak
    pajak = hitung_pajak(emisi)
    # Cetak hasil pajak atau status bebas
    if pajak > 0:
        print(f"{perusahaan} kena pajak karbon Rp {pajak}")
    else:
        print(f"{perusahaan} bebas pajak karbon")

# Impor Pandas untuk mengelola data CSV
import pandas as pd

# Definisikan fungsi untuk cek greenwashing
def cek_greenwashing(emisi_dict):
    # Iterasi dictionary untuk cek greenwashing
    for perusahaan, data in emisi_dict.items():
        # Cek apakah klaim hijau dan emisi > 50 ton
        if data['klaim'] == 'ya' and data['emisi'] > 50:
            # Cetak status greenwashing
            print(f"{perusahaan} TERDETEKSI greenwashing dengan emisi {data['emisi']} ton!")
        else:
            # Cetak status tidak greenwashing
            print(f"{perusahaan} TIDAK TERDETEKSI greenwashing.")

# Baca file CSV emisi_perusahaan.csv dari folder proyek
df = pd.read_csv('C:/energihijau2025/emisi_perusahaan.csv')

# Inisiasi dictionary kosong untuk menyimpan emisi dan klaim
emisi_dict = {}

# Iterasi setiap baris di dataframe untuk simpan ke dictionary
for index, row in df.iterrows():
    # Ambil nama perusahaan sebagai kunci
    perusahaan = row['Nama_Perusahaan']
    # Simpan emisi dan klaim dalam dictionary bersarang
    emisi_dict[perusahaan] = {
        'emisi': row['Emisi_2024'],
        'klaim': row['Klaim_Hijau']
    } 
    
import pandas as pd  

# Definisikan fungsi untuk cek risiko konflik lahan
def cek_konflik(lahan_dict):
    for proyek, data in lahan_dict.items():
        if data['luas'] > 500 or str(data['konflik']).lower() == 'ya':
            print(f"Proyek {proyek} BERISIKO konflik lahan!")
        else:
            print(f"Proyek {proyek} AMAN dari konflik.")

#  Baca file CSV konflik_lahan.csv dari folder proyek
df = pd.read_csv('C:/energihijau2025/konflik_lahan.csv')

# Inisiasi dictionary untuk menyimpan data lahan
lahan_dict = {}

# Isi dictionary dengan data dari DataFrame
for index, row in df.iterrows():
    proyek = row['Nama_Proyek']
    lahan_dict[proyek] = {
        'luas': row['Luas_Lahan'],
        'konflik': row['Status_Konflik']
    }

# Panggil fungsi cek_konflik
cek_konflik(lahan_dict)

# Panggil fungsi untuk cek greenwashing
cek_greenwashing(emisi_dict)

# Impor Pandas untuk mengelola data CSV
import pandas as pd
# Impor Matplotlib untuk membuat grafik
import matplotlib.pyplot as plt

# Definisikan fungsi untuk membuat bar chart emisi
def plot_emisi(emisi_dict):
    # Ambil nama perusahaan sebagai sumbu x
    perusahaan = list(emisi_dict.keys())
    # Ambil emisi sebagai sumbu y
    emisi = [data['emisi'] for data in emisi_dict.values()]
    # Buat bar chart dengan warna hijau (simbol energi hijau)
    plt.bar(perusahaan, emisi, color='green')
    # Tambahkan label sumbu x
    plt.xlabel('Perusahaan')
    # Tambahkan label sumbu y
    plt.ylabel('Emisi (ton CO2)')
    # Tambahkan judul grafik
    plt.title('Emisi Karbon Perusahaan 2024')
    # Tambahkan garis batas pajak (50 ton, merah, putus-putus)
    plt.axhline(y=50, color='red', linestyle='--', label='Batas Pajak (50 ton)')
    # Tambahkan legenda untuk garis batas
    plt.legend()
    # Rotasi label sumbu x agar tidak bertumpuk
    plt.xticks(rotation=90)
    # Atur layout agar grafik rapi
    plt.tight_layout()
    # Tampilkan grafik
    plt.show()

# Baca file CSV emisi_perusahaan.csv dari folder proyek
df = pd.read_csv('C:/energihijau2025/emisi_perusahaan.csv')

# Inisiasi dictionary kosong untuk menyimpan emisi
emisi_dict = {}

# Iterasi setiap baris di dataframe untuk simpan ke dictionary
for index, row in df.iterrows():
    # Ambil nama perusahaan sebagai kunci
    perusahaan = row['Nama_Perusahaan']
    # Simpan emisi dalam dictionary
    emisi_dict[perusahaan] = {'emisi': row['Emisi_2024']}

# Panggil fungsi untuk membuat bar chart
plot_emisi(emisi_dict)

# Impor Pandas untuk mengelola data CSV
import pandas as pd
# Impor Matplotlib untuk membuat grafik
import matplotlib.pyplot as plt

# Definisikan fungsi untuk membuat pie chart konflik lahan
def plot_konflik(lahan_dict):
    # Hitung jumlah proyek berisiko (luas > 500 ha atau konflik 'ya')
    risiko = sum(1 for data in lahan_dict.values() if data['luas'] > 500 or data['konflik'] == 'ya')
    # Hitung jumlah proyek aman
    aman = len(lahan_dict) - risiko
    # Definisikan label untuk pie chart
    labels = ['Berisiko', 'Aman']
    # Definisikan ukuran untuk pie chart
    sizes = [risiko, aman]
    # Definisikan warna (merah untuk risiko, hijau untuk aman)
    colors = ['red', 'green']
    # Buat pie chart dengan persentase
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
    # Tambahkan judul grafik
    plt.title('Distribusi Risiko Konflik Lahan Proyek PLTS')
    # Tampilkan grafik
    plt.show()

# Baca file CSV konflik_lahan.csv dari folder proyek
df = pd.read_csv('C:/EnergiHijau2025/konflik_lahan.csv')

# Inisiasi dictionary kosong untuk menyimpan data lahan
lahan_dict = {}

# Iterasi setiap baris di dataframe untuk simpan ke dictionary
for index, row in df.iterrows():
    # Ambil nama proyek sebagai kunci
    proyek = row['Nama_Proyek']
    # Simpan luas lahan dan status konflik dalam dictionary
    lahan_dict[proyek] = {
        'luas': row['Luas_Lahan'],
        'konflik': row['Status_Konflik']
    }

# Panggil fungsi untuk membuat pie chart
plot_konflik(lahan_dict)

# Impor Pandas untuk mengelola data CSV
import pandas as pd
# Impor Matplotlib untuk membuat grafik
import matplotlib.pyplot as plt

# Definisikan fungsi untuk membuat line chart tren emisi
def plot_tren_emisi(emisi_dict):
    # Definisikan tahun untuk sumbu x
    tahun = [2020, 2021, 2022, 2023]
    # Iterasi dictionary untuk plot setiap perusahaan
    for perusahaan, emisi_list in emisi_dict.items():
        # Buat garis untuk setiap perusahaan dengan marker titik
        plt.plot(tahun, emisi_list, marker='o', label=perusahaan)
    # Tambahkan label sumbu x
    plt.xlabel('Tahun')
    # Tambahkan label sumbu y
    plt.ylabel('Emisi (ton CO2)')
    # Tambahkan judul grafik
    plt.title('Tren Emisi Karbon Perusahaan 2020-2023')
    # Tambahkan garis batas pajak (50 ton, merah, putus-putus)
    plt.axhline(y=50, color='red', linestyle='--', label='Batas Pajak (50 ton)')
    # Tambahkan legenda untuk perusahaan dan garis batas
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    # Atur layout agar grafik rapi
    plt.tight_layout()
    # Tampilkan grafik
    plt.show()

# Baca file CSV tren_emisi.csv dari folder proyek
df = pd.read_csv('C:/energihijau2025/tren_emisi.csv')

# Inisiasi dictionary kosong untuk menyimpan tren emisi
emisi_dict = {}

# Iterasi setiap baris di dataframe untuk simpan ke dictionary
for index, row in df.iterrows():
    # Ambil nama perusahaan sebagai kunci
    perusahaan = row['Nama_Perusahaan']
    # Simpan emisi tahunan dalam list
    emisi_list = [row['Emisi_2020'], row['Emisi_2021'], row['Emisi_2022'], row['Emisi_2023']]
    # Simpan ke dictionary
    emisi_dict[perusahaan] = emisi_list

# Panggil fungsi untuk membuat line chart
plot_tren_emisi(emisi_dict)