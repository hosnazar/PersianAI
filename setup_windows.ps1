$ErrorActionPreference = "Stop"

Write-Host "Creating virtual environment..."
python -m venv .venv

Write-Host "Activating virtual environment..."
. .\.venv\Scripts\Activate.ps1

Write-Host "Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

Write-Host "Setup complete. Install Ollama manually if not installed: https://ollama.com"
Write-Host "Then run: ollama pull llama3.1:8b"
Write-Host "Then run: .\run_local.ps1"
