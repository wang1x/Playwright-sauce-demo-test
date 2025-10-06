
# ===============================
# Playwright + Python Setup Script
# ===============================

# 1. Check if Python is installed
$pythonVersion = python --version 2>$null
if (!$pythonVersion) {
Write-Host "Python is not installed. Please install Python first from https://www.python.org/downloads/" -ForegroundColor Red
exit
} else {
Write-Host "Python detected: $pythonVersion" -ForegroundColor Green
}

# 2. Create virtual environment (venv)
if (Test-Path "venv") {
Write-Host "Virtual environment 'venv' already exists. Skipping creation..." -ForegroundColor Yellow
} else {
Write-Host "Creating virtual environment 'venv'..."
python -m venv venv
}

# 3. Activate virtual environment
Write-Host "Activating virtual environment..."
. .\venv\Scripts\Activate

# 4. Upgrade pip
Write-Host "Upgrading pip..."
python -m pip install --upgrade pip

# 5. Install required packages
Write-Host "Installing pytest and pytest-playwright..."
pip install pytest pytest-playwright

# 6. Install Playwright browsers
Write-Host "Installing Playwright browsers..."
playwright install

Write-Host "Setup complete! Virtual environment 'venv' is ready and Playwright is installed." -ForegroundColor Green
Write-Host "To activate venv in the future, run: .\venv\Scripts\Activate" -ForegroundColor Cyan