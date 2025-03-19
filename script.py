import os
import random
import datetime

# 🔹 Change this to your AI-Web-Scrapper repository path
REPO_PATH = os.path.expanduser("~/Desktop/GitProject/AI-Web-Scrapper")  # Update if needed

# 🔹 Number of commits to generate
NUM_COMMITS = random.randint(30, 60)  # Random between 200-400 commits

# 🔹 Your GitHub username (SSH will handle authentication)
GIT_USERNAME = "premalshah999"

# 🔹 AI Web Scraper-Specific Commit Messages
COMMIT_MESSAGES = [
    "Implemented dynamic web scraping with Selenium",
    "Optimized BeautifulSoup parsing for speed",
    "Fixed user-agent rotation issue",
    "Enhanced proxy support for better anonymity",
    "Added real-time data extraction feature",
    "Refactored scraping pipeline for efficiency",
    "Fixed missing data handling in scrapers",
    "Added support for scraping JavaScript-rendered content",
    "Implemented headless browser automation",
    "Updated documentation with latest scraping techniques",
    "Improved CAPTCHA bypass mechanism",
    "Enhanced multi-threading for parallel scraping",
    "Refactored data storage logic for scalability",
    "Added AI-based content extraction model",
    "Fixed pagination issue in scrapers",
    "Updated README with new usage examples",
    "Implemented rate-limiting to avoid bans",
    "Added logging for better debugging",
    "Optimized data parsing for large datasets",
    "Fixed authentication flow for restricted content",
]

# Function to create and push commits
def make_commit(commit_date, commit_message):
    os.chdir(REPO_PATH)  # Move to repo folder

    # Create or update a dummy file
    with open("commit_log.txt", "a") as file:
        file.write(f"{commit_date}: {commit_message}\n")

    # Add changes to Git
    os.system("git add .")
    os.system(f'GIT_AUTHOR_DATE="{commit_date}" GIT_COMMITTER_DATE="{commit_date}" git commit -m "{commit_message}"')

# Set Git username (SSH handles authentication)
os.system(f'git config user.name "{GIT_USERNAME}"')

# Get the current branch name
branch_name = os.popen("git rev-parse --abbrev-ref HEAD").read().strip()

# Generate commits for 2024 & 2025
for _ in range(NUM_COMMITS):
    random_year = random.choice([2024, 2025])  # Choose either 2024 or 2025
    random_days = random.randint(0, 364)  # Random day of the year
    random_time = datetime.timedelta(hours=random.randint(0, 23), minutes=random.randint(0, 59))

    commit_date = datetime.datetime(random_year, 1, 1) + datetime.timedelta(days=random_days) + random_time
    commit_message = random.choice(COMMIT_MESSAGES)  # Choose a random commit message

    make_commit(commit_date.strftime("%Y-%m-%dT%H:%M:%S"), commit_message)

# Push all commits to GitHub using SSH
os.system(f"git push origin {branch_name}")
