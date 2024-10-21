import os
import subprocess

# Change to the app directory
os.chdir(r'C:\Users\Asus\HeartDiseaseApp')  # Make sure this is the correct path

# Activate the virtual environment and run the Streamlit app
subprocess.run([r'venv\Scripts\activate.bat', '&&', 'streamlit', 'run', 'app.py'], shell=True)