PowerShell or command prompt

Run PowerShell:

&nbsp;  Win + R, type powershell

Create a virtual env:

&nbsp; C:\\Users\\You\\Projects\\demo-test

&nbsp; python -m venv myenv -> make a sandbox called myenv

&nbsp; myenv\\Scripts\\activate -> step inside that sandbox and use its Python+pip

&nbsp; deactivate -> take you back to your system Python

&nbsp; 

&nbsp; C:\\Users\\You\\Projects\\demo-test\\

&nbsp; |--myenv\\

&nbsp; |   |--Include\\

&nbsp; |   |--Lib\\

&nbsp; |   |--Scripts\\

&nbsp; |   |--pyvenv.cfg

&nbsp; |--tests\\

&nbsp; |--requitements.txt

* Scripts\\ -> contains activate, deactivate, and the local python.exe, pip.exe
* Lib\\site-package\\ -> where all package you install with pip will go (e.g. pytest, playwright)
* pyvenv.cfg -> config file that points to your base Python installation



Before deleting an old venv, save your installed packages:

&nbsp;  pip freeze > requirements.txt

After recreating venv:

&nbsp;  pip install -r requirements.txt (This way you get the same dependencies back)

Temporarily bypass PowerShell restrictions:

&nbsp;  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

Update PATH to use venv version of python or pip:
&nbsp;  myenv\Scripts\activate
  

Setting up Playwright on Windows:
  1. Install Python (if not already installed)
     (1) Download latest Python: python.org/downloads
     (2) During installation, check "Add Python to PATH"
     (3) Verify installation: python --version, pip --version
  2. Create a Virtual Environment(recommended)
     python -m venv myenv
     myenv\scripts\activate
  3. Install Playwright
     pip install pytest pytest-playwright
  4. Install Browsers
     playwright install
     playwright install --with-deps(not usually needed on Windows, more for Linux)
  5. Verify Playwright
     pytest --collect-only
     pytest --headed
  6. Generate Reports (optional)
     For HTML reports:
     pip install pytest-html
     pytest --html=report.html --self-contained-html

Add dependencies manually
  write this inside requirements.txt
      pytest
      pytest-playwright
      requests
  or let pip generate it for you
      pip install pytest pytest-playwright requests
      pip freeze > requirements.txt

Run with pytest
  pytest tests\test_cart.py -v
Install pytest--html
  pip install pytest-html
Initialize Git in Your Project
  git init
Add Your Files to Git
  git add .
Make Your First Commit
  git commit -m "Initial commit"