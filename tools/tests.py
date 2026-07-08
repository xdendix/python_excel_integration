import io
from unittest.mock import patch

import pandas as pd
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from .models import MergeHistory


class MergeExcelViewTests(TestCase):
    def _create_excel_bytes(self, rows):
        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
            pd.DataFrame(rows).to_excel(writer, index=False)
        buffer.seek(0)
        return buffer.getvalue()

    def test_upload_merges_excel_and_creates_history(self):
        file_bytes = self._create_excel_bytes([{"name": "Alice", "value": 1}])
        uploaded_file = SimpleUploadedFile(
            "sample.xlsx",
            file_bytes,
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )

        response = self.client.post(
            reverse("merge_excel"),
            {"excel_files": [uploaded_file]},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response["Content-Disposition"],
            'attachment; filename="Master_Rekap_Data.xlsx"',
        )
        self.assertTrue(MergeHistory.objects.filter(status="SUCCESS").exists())

    @patch("tools.views.pd.concat", side_effect=ValueError("boom"))
    def test_merge_failure_logs_readable_error_message(self, mocked_concat):
        file_bytes = self._create_excel_bytes([{"name": "Alice", "value": 1}])
        uploaded_file = SimpleUploadedFile(
            "sample.xlsx",
            file_bytes,
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )

        response = self.client.post(
            reverse("merge_excel"),
            {"excel_files": [uploaded_file]},
        )

        self.assertEqual(response.status_code, 200)
        history = MergeHistory.objects.latest("processed_at")
        self.assertEqual(history.status, "FAILED")
        self.assertEqual(history.error_message, "Failed to merge files: boom")
