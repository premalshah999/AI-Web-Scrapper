import os

# Navigate to your Git repository
os.chdir(os.path.expanduser("~/Desktop/GitProject/AI-Web-Scrapper"))  # Change path if needed

# Fetch latest changes
os.system("git fetch --all")

# Create a backup branch before modifying history
os.system("git checkout -b backup-before-2025-removal")

# Find the last commit of 2024
commit_2024 = os.popen('git rev-list -1 --before="2025-01-01" main').read().strip()

if not commit_2024:
    print("❌ No valid 2024 commit found. Aborting process.")
    exit(1)

# Reset to the last commit of 2024 (deleting all 2025 commits)
os.system(f"git reset --hard {commit_2024}")

# Force push to update remote
os.system("git push origin main --force")

print("✅ Successfully removed all 2025 commits.")
