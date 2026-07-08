# Python Excel Integration (Production-Ready)

Turn 2 hours of manual data entry into 2 seconds. A lightweight, modern Django web application designed to instantly merge multiple Excel files (`.xlsx`/`.xls`) into a single, clean, and downloadable master workbook.

Perfect for HR, Finance, or Admin teams dealing with scattered attendance records, financial reports, or survey data.

## Key Features

- **Blazing Fast Merging:** Powered by `pandas`, processing happens entirely in-memory for maximum speed.
- **Modern UI/UX:** Built with Tailwind CSS for a sleek, responsive, drag-and-drop interface.
- **Enterprise-Grade Deployment:** Fully containerized with Docker, Gunicorn, and WhiteNoise. Ready to be deployed on any VPS or local intranet server.
- **Audit Trail:** Built-in SQLite database tracks all merge histories (file count, row count, status, and error logs) for administrative review.
- **Bulletproof Architecture:** Uses Docker Volumes to ensure database persistence even when the server restarts or updates.
- **Zero-Touch Setup:** Automatic database migrations upon container startup via custom `entrypoint.sh`.

## Technology Stack

- **Backend:** Django 6.0.2, Python 3.14
- **Data Engine:** pandas, openpyxl
- **Frontend:** HTML5, Tailwind CSS
- **Server/DevOps:** Docker Compose, Gunicorn, WhiteNoise, SQLite

---

## One-Click Deployment (Recommended)

You don't need to install Python or any dependencies on your machine. Just use Docker.

1. Clone this repository:
   ```bash
   git clone https://github.com/[username-github-lo]/python_excel_integration.git
   cd python_excel_integration
   ```

2. Create a `.env` file based on the example:
   ```bash
   cp .env.example .env
   ```

3. Spin up the production server:
   ```bash
   docker compose up -d --build
   ```

That's it! The application is now running securely at `http://localhost:8000/`. 
*(Note: Database migrations are handled automatically during startup).*

---

## Local Development Setup

If you wish to modify the code locally without Docker:

1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run migrations and start the server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

## Project Structure Highlights

- `core/` — Django project configuration & WSGI/ASGI entry points.
- `tools/` — Main application containing upload, merge logic (`views.py`), and history tracking (`models.py`).
- `docker-compose.yml` & `Dockerfile` — Enterprise standard containerization blueprint.
- `entrypoint.sh` — Automation script for seamless database migrations on deployment.
- `excel_dummy.py` — Helper script to quickly generate dummy Excel files for testing.

## Screenshot

![Merge UI example](docs/screenshot.png)

## Looking for Customization? (Freelance Services)

While this core engine is open-source, every business has unique data structures. I offer freelance services to adapt this tool to your company's specific needs, including:
- **Custom Column Mapping:** Automatically clean, format, or map specific columns during the merge.
- **White-labeling:** Redesign the UI to match your company's branding and logo.
- **Automated Delivery:** Send the merged file directly to a specified Email or Telegram bot.
- **Server Installation:** Securely deploy this application on your company's internal server/VPS.

**Contact me:** workemaildendi@gmail.com

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details. You are free to use, modify, and distribute this software.