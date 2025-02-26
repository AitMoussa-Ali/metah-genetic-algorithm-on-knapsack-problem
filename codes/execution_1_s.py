import subprocess

from anyio import sleep

for i in range(5):
    print(f"Exécution {i+1}...")
    subprocess.run(["python", "C:\\Users\\sofia\\OneDrive\\Bureau\\Projet metah\\codes\\main_1_s.py"])
    # sleep(2)