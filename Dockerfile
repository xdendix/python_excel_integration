# 1. Gunakan sistem operasi Linux mini yang sudah ada Python 3.10
FROM python:3.14-slim

# 2. Atur environment agar Python berjalan lebih cepat dan efisien di server
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Buat folder bernama /app di dalam docker sebagai ruang kerja
WORKDIR /app

# 4. Salin list library (requirements.txt) dari laptop ke dalam docker
COPY requirements.txt /app/

# 5. Minta docker untuk meng-install Pandas, Django, Gunicorn, dll
RUN pip install --no-cache-dir -r requirements.txt

# 6. Salin semua kodingan web lo ke dalam docker
COPY . /app/
RUN chmod +x /app/entrypoint.sh

# 7. Tetapkan entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]

# 8. Nyalakan mesin Gunicorn saat docker dibuka
# Di Docker WAJIB pakai 0.0.0.0 agar bisa diakses dari luar docker
CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]