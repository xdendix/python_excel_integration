#!/bin/sh

# Keluar jika ada error
set -e

# 1. Jalankan migrasi database otomatis
echo "Running database migrations..."
python manage.py migrate --noinput

# 2. Opsional: Buat superuser otomatis (jika environment variable ada)
# Ini menjaga klien lo tetap bisa masuk admin panel tanpa harus manual create
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ]; then
    echo "Creating superuser..."
    python manage.py createsuperuser --noinput || echo "Superuser already exists."
fi

# 3. Jalankan perintah utama (Gunicorn)
echo "Starting Gunicorn server..."
exec "$@"