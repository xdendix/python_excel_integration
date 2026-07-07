# Python Excel Integration

A small Django web tool to merge multiple Excel (.xlsx/.xls) files into a single master Excel file.

## Overview

This project provides a simple web interface where users can drag-and-drop or select multiple Excel files. The server (Django + pandas + openpyxl) reads the uploaded files, concatenates them into a single DataFrame, and returns a downloadable Master Excel file named `Master_Rekap_Data.xlsx`.

Key characteristics:
- Lightweight Django app (single app: `tools`).
- Uses `pandas` and `openpyxl` to read, merge, and write Excel files in memory.
- Records each merge attempt in a `MergeHistory` model (audit trail).

## Features

- Drag & drop multiple `.xlsx`/`.xls` files via the web UI.
- Client-side feedback and automatic download of the merged file.
- Basic error handling and an audit trail saved to the database.

## Project structure (important files)

- `manage.py` — Django CLI entry point.
- `core/settings.py` — Django settings used for development.
- `tools/views.py` — Main view handling file uploads and merging logic.
- `tools/models.py` — `MergeHistory` model for recording merge runs.
- `tools/templates/merge_tool.html` — Frontend UI (drag & drop form + JS).
- `excel_dummy.py` — Small helper script to generate example Excel files.
- `requirements.txt` — Python dependencies.

## Requirements

- Python 3.10+ recommended
- See `requirements.txt` for exact packages and versions. Install with:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Setup & Run (development)

1. Create and activate virtual environment (see above).
2. Install dependencies: `pip install -r requirements.txt`.
3. Apply migrations:

```bash
python manage.py migrate
```

4. (Optional) Create superuser to inspect `MergeHistory` in admin:

```bash
python manage.py createsuperuser
```

5. Run the development server:

```bash
python manage.py runserver
```

6. Open your browser at `http://127.0.0.1:8000/` and use the web interface to upload and merge files.

## Usage

1. Click the drag & drop area or drop multiple `.xlsx` / `.xls` files.
2. The UI shows selected files; click `Process & Merge Files`.
3. The browser will automatically download the merged file named `Master_Rekap_Data.xlsx` when the merge completes.

If any file fails to be read, an error banner will show the message and the merge will continue for readable files; the `MergeHistory` entry will include an `error_message` when appropriate.

## Example screenshot

Place a screenshot image (for example the provided UI) in the repository and reference it here. Example Markdown to include an image placed at `docs/screenshot.png`:

```md
![Merge UI example](docs/screenshot.png)
```

The image shown in the repository preview should look like the app's main UI (drag & drop card and a large `Process & Merge Files` button).

## Notes

- The merge operation runs in memory and writes the final file to a Bytes buffer before sending it to the client. For large uploads you may need to consider stream-based processing or increased server resources.
- This project is configured for development (`DEBUG = True`). Do not run with `DEBUG = True` in production.

## Quick tip — generate example Excel files

You can run the included `excel_dummy.py` to create three example `.xlsx` files in the project folder:

```bash
python excel_dummy.py
```

## Contributing

Feel free to open issues or PRs. For major changes, please open an issue first to discuss the proposed change.

## License

This project does not include a license file. Add a license if you intend to publish or distribute the project.
