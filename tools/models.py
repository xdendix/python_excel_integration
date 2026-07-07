from django.db import models


# Create your models here.
class MergeHistory(models.Model):
    # Pilihan status untuk membatasi input di database
    STATUS_CHOICES = [
        ("SUCCESS", "Success"),
        ("FAILED", "Failed"),
    ]

    # Mencatat waktu secara otomatis
    processed_at = models.DateTimeField(auto_now_add=True)

    # Menyimpan jumlah file dan total baris data yang dihasilkan
    file_count = models.IntegerField(default=0)
    total_rows = models.IntegerField(default=0)

    # Status proses penggabungan
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="SUCCESS")

    # Menyimpan pesan error jika proses gagal
    error_message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"[{self.processed_at.strftime('%Y-%m-%d %H:%M')}] {self.status} - {self.file_count} files"
