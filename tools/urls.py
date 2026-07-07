from django.urls import path
from . import views

# Daftar rute khusus untuk apps 'tools'
urlpatterns = [
    # Jika user mengakses rute kosong string (''), maka jalankan fungsi merge_excel_view
    path("", views.merge_excel_view, name="merge_excel"),
]
