import subprocess

try:

    subprocess.run(["git", "pull"], check=True)
    print("=== Git Pull Success ===")

except subprocess.CalledProcessError:
    print("=== Git Pull Failed ===")