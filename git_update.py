import subprocess

try:
    # Run git add .
    subprocess.run(["git", "add", "."], check=True)

    # Run git commit
    subprocess.run(
        ["git", "commit", "-m", "update content"],
        check=True
    )

    # Run git push
    subprocess.run(["git", "push"], check=True)

    print("=== Git Operation Success ===")

except subprocess.CalledProcessError:
    print("=== Git Operation Failed ===")