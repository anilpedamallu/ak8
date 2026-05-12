import subprocess

try:
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "update content"], check=True)
    subprocess.run(["git", "push"], check=True)
    print("========== Git PUSH Success ==========")

except subprocess.CalledProcessError:
    print("========== Git PULL Failed ==========")