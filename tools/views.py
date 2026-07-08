import pandas as pd
import io
from django.shortcuts import render
from django.http import HttpResponse
from .models import MergeHistory


# Create your views here.
def merge_excel_view(request):
    error_msg = ""

    # Jika user menekan tombol submit (post request)
    if request.method == "POST" and request.FILES.getlist("excel_files"):
        uploaded_files = request.FILES.getlist("excel_files")
        data_frames = []
        error_msg = ""

        # Looping membaca semua file yg diupload
        for file in uploaded_files:

            if not file.name.endswith((".xlsx", ".xls")):
                error_msg += f"{file.name} is not a valid Excel file. | "
                continue

            try:
                # Pandas membaca file excel langsung dari memori
                df = pd.read_excel(file)

                # tambahkan kolom penanda sumber file
                df["Source_File"] = file.name

                # Hapus duplikat, baris kosong dan reset index
                df = df.drop_duplicates()
                df = df.dropna(how="all")
                df = df.reset_index(drop=True)

                # vectorize kolom yang memiliki tipe data object (string)
                str_cols = df.select_dtypes(include=["object", "string"]).columns
                for col in str_cols:
                    df[col] = df[col].astype(str).str.strip()

                data_frames.append(df)
            except Exception as e:
                error_msg += f"Failed to read {file.name}: {str(e)} | "

        # Jika ada data yg berhasil dibaca, gabungkan!
        if data_frames:
            try:
                master_df = pd.concat(data_frames, ignore_index=True)
                total_rows = len(master_df)

                # Siapkan ruang di memori untuk menulis file Excel baru
                buffer = io.BytesIO()
                with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
                    master_df.to_excel(writer, index=False)

                buffer.seek(0)  # Kembalikan kursor ke awal sebelum dikirim

                # Catat ke database (audit trail)
                MergeHistory.objects.create(
                    file_count=len(uploaded_files),
                    total_rows=total_rows,
                    status="SUCCESS",
                    error_message=error_msg if error_msg else None,
                )

                # Kirim file sebagai response untuk didownload
                response = HttpResponse(
                    buffer.getvalue(),
                    content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                )
                response["Content-Disposition"] = (
                    'attachment; filename="Master_Rekap_Data.xlsx"'
                )
                return response

            except Exception as e:
                error_msg = f"Failed to merge files: {str(e)}"
                MergeHistory.objects.create(
                    file_count=len(uploaded_files),
                    total_rows=0,
                    status="FAILED",
                    error_message=error_msg,
                )

                return render(
                    request,
                    "merge_tool.html",
                    {"error_msg": error_msg},
                )

        # Jika user hanya membuka halaman biasa (Get Request)
    return render(request, "merge_tool.html", {"error_msg": error_msg})
