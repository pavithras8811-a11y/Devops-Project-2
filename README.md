# Smart Server Health Monitoring System

A beginner-friendly DevOps project that displays CPU, memory, and disk usage in a Streamlit dashboard and warns when usage crosses defined limits.

## Features
- CPU usage monitoring
- Memory usage monitoring
- Disk usage monitoring
- Threshold-based warning messages
- Recent resource-usage chart
- Docker support

## Requirements
- Python 3.10 or newer
- VS Code (recommended)
- Docker Desktop (optional, for container deployment)

## Run locally on Windows

1. Extract the ZIP file.
2. Open the extracted folder in VS Code.
3. Open the VS Code terminal.
4. Create a virtual environment:

   ```powershell
   python -m venv .venv
   ```

5. Activate it:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

6. Install the packages:

   ```powershell
   python -m pip install -r requirements.txt
   ```

7. Start the dashboard:

   ```powershell
   python -m streamlit run app.py
   ```

8. Open the local URL shown in the terminal, usually http://localhost:8501.

## Run using Docker

Make sure Docker Desktop is running, then run:

```bash
docker compose up --build
```

Open http://localhost:8501. To stop the container, press `Ctrl+C` and run `docker compose down` in the terminal.

## Customize alert limits

Open `app.py` and change `CPU_LIMIT`, `MEMORY_LIMIT`, and `DISK_LIMIT` near the top of the file.

## Important notes
- The dashboard measures the machine/environment where the Python app is running.
- When running inside Docker, resource readings may reflect the container or host depending on the operating system and Docker configuration.
- This starter project displays live readings when refreshed; it is not yet a 24/7 monitoring or notification service.
- Add screenshots, test results, and your own improvements before presenting it as completed work.
