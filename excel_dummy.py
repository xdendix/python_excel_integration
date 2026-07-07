import pandas as pd

print("Membuat file Excel dummy...")

# 1. Data Cabang Jakarta
df1 = pd.DataFrame(
    {
        "ID_Karyawan": ["JKT-001", "JKT-002", "JKT-003"],
        "Nama": ["Andi", "Budi", "Citra"],
        "Divisi": ["IT", "Finance", "HR"],
        "Gaji": [10000000, 8500000, 7500000],
    }
)

# 2. Data Cabang Bandung
df2 = pd.DataFrame(
    {
        "ID_Karyawan": ["BDO-001", "BDO-002"],
        "Nama": ["Dewi", "Eko"],
        "Divisi": ["Marketing", "IT"],
        "Gaji": [6500000, 9500000],
    }
)

# 3. Data Cabang Surabaya
df3 = pd.DataFrame(
    {
        "ID_Karyawan": ["SBY-001", "SBY-002", "SBY-003"],
        "Nama": ["Fajar", "Gita", "Hadi"],
        "Divisi": ["Finance", "HR", "Marketing"],
        "Gaji": [8000000, 7000000, 6000000],
    }
)

# Menyimpan ke dalam bentuk .xlsx
df1.to_excel("data_cabang_jakarta.xlsx", index=False)
df2.to_excel("data_cabang_bandung.xlsx", index=False)
df3.to_excel("data_cabang_surabaya.xlsx", index=False)

print("Selesai! 3 File berhasil dibuat di folder proyek lo.")
