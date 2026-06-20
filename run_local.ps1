$ErrorActionPreference = "Stop"

if (!(Test-Path ".\.venv\Scripts\Activate.ps1")) {
    Write-Host "Virtual environment not found. Run setup_windows.ps1 first."
    exit 1
}

. .\.venv\Scripts\Activate.ps1

Write-Host "Starting FastAPI backend on http://localhost:8000"
Start-Process powershell -ArgumentList "-NoExit", "-Command", ". .\.venv\Scripts\Activate.ps1; uvicorn app.main:app --reload --port 8000"

Start-Sleep -Seconds 3

Write-Host "Starting Streamlit UI..."
streamlit run app/ui.py
