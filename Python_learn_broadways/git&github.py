# ==========================================================
# DAY 8
# 12/03/2026
# Git and GitHub Notes - Detailed Terminal Workflow
# ==========================================================

# -----------------------------
# 1️⃣ Version Control Basics
# -----------------------------
"""
Git is a version control system (VCS) to track changes in your project files.
GitHub is a remote server to store your Git repositories.

Other platforms:
- Bitbucket
- GitLab
- Gitea

Key Terms:
-------------
local      -> Your PC (your working files)
remote     -> GitHub server (or any remote repository)
repo       -> Project folder being tracked
remote URL -> Link to your remote repository
SSH key    -> Pair of public/private keys for secure authentication
"""

# -----------------------------
# 2️⃣ SSH Keys Setup
# -----------------------------
"""
SSH keys allow secure connection to GitHub without typing passwords.

# Command to generate key
ssh-keygen

Creates:
- Private key: id_ed25519 (never share this)
- Public key:  id_ed25519.pub (add this to GitHub)

Important:
- If a new key is generated, it must be added to GitHub again.
- Public key can be shared safely; private key must stay secret.
"""

# -----------------------------
# 3️⃣ Git Installation Check
# -----------------------------
"""
If 'git' is not recognized:
- Restart VS Code or terminal after installing Git
- Add Git to PATH (Windows): C:\Program Files\Git\cmd
- Test: git --version
"""

# -----------------------------
# 4️⃣ Initialize Git Repository
# -----------------------------
"""
# Go to your project folder
cd C:\Users\budha\OneDrive\Desktop\Python learning\feb22\Python_learn_broadways

# Initialize Git in this folder
git init .

# What it does:
- Creates a hidden .git folder
- Starts tracking your files
- Sets up a local repository
"""

# -----------------------------
# 5️⃣ Check Repository Status
# -----------------------------
"""
Command:
git status

# Output explained:
On branch master             -> Current branch name
No commits yet               -> No commits in repo
Untracked files:             -> Files not yet added to Git
- .gitignore
- day1.py, day2.py ...       -> Files in folder

Use 'git add <file>' or 'git add .' to start tracking these files.
"""

# -----------------------------
# 6️⃣ Staging Files
# -----------------------------
"""
Command to stage all files:
git add .

# Or stage specific files:
git add day1.py

# What it does:
- Moves files to the 'staging area'
- These are ready to be committed
"""

# -----------------------------
# 7️⃣ Commit Changes
# -----------------------------
"""
Command:
git commit -m "initial commit"

# What it does:
- Saves a snapshot of staged files in Git history
- Requires author identity

# If you get:
Author identity unknown

Do this once:
git config --global user.name "Bishal Budhakhsetri"
git config --global user.email "id.kshetri@gmail.com"

# This sets your name and email for all Git projects
"""

# -----------------------------
# 8️⃣ View Commit History
# -----------------------------
"""
Command:
git log

# Output shows:
- commit hash (unique ID for commit)
- author name/email
- date/time
- commit message

# Example:
commit 2c70737df171fc43a5bdd2a255b103986095e695 (HEAD -> master)
Author: Bishal Budhakshetri <id.kshetri@gmail.com>
Date:   Thu Mar 12 07:48:44 2026 +0545
    initial commit
"""

# -----------------------------
# 9️⃣ Connecting to Remote Repository
# -----------------------------
"""
Command:
git remote add origin git@github.com:BishalKshetri/python-feb22.git

# What it does:
- Links your local repo to remote GitHub repo
- 'origin' is the name of the remote
- git@github.com:... is the SSH URL

Check remote URL:
git remote -v

# Output:
origin  git@github.com:BishalKshetri/python-feb22.git (fetch)
origin  git@github.com:BishalKshetri/python-feb22.git (push)
"""

# -----------------------------
# 🔟 Check Branches
# -----------------------------
"""
Command:
git branch

# Output:
* master

# Explanation:
- * indicates current branch
- 'master' (or 'main') is default branch
- You can create more branches with git branch <name>
"""

# -----------------------------
# 1️⃣1️⃣ Push to GitHub
# -----------------------------
"""
Command:
git push origin master

# First time SSH push may show:
The authenticity of host 'github.com (IP)' can't be established.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes

# What it does:
- Pushes local commits to GitHub
- First push adds master branch remotely
- After confirmation, GitHub remembers your SSH host
"""

# -----------------------------
# 1️⃣2️⃣ Common Git Commands Summary
# -----------------------------
"""
git init               -> Initialize repository
git status             -> Check status of files
git add <file>         -> Stage a specific file
git add .              -> Stage all files
git commit -m "msg"    -> Commit staged changes
git log                -> Show commit history
git branch             -> Show or create branches
git remote add origin <url> -> Link to remote repo
git remote -v          -> Verify remote URL
git push origin master -> Push commits to remote
git rm --cached <file> -> Unstage a file
git reset --soft HEAD~1 -> Undo last commit but keep changes
"""

# -----------------------------
# 1️⃣3️⃣ Undo / Reset Notes
# -----------------------------
"""
Undo git init:
- Delete .git folder:
  rmdir /s /q .git   # Windows
  rm -rf .git        # Linux/Mac
  Remove-Item -Recurse -Force .git # PowerShell

# Undo staged file:
git rm --cached <file>

# Undo last commit but keep changes:
git reset --soft HEAD~1
"""

# -----------------------------
# 1️⃣4️⃣ VS Code Terminal Tips
# -----------------------------
"""
- Restart VS Code after Git installation
- Terminal commands are the same as Command Prompt
- If Git not recognized, add Git to PATH: C:\Program Files\Git\cmd
"""

# -----------------------------
# 1️⃣5️⃣ Summary of Today’s Practice
# -----------------------------
"""
1. Created SSH key and added it to GitHub
2. Initialized local repo with git init
3. Added files with git add .
4. Configured user name/email for commits
5. Committed first snapshot with git commit -m "initial commit"
6. Viewed commit history with git log
7. Linked local repo to GitHub with git remote add origin
8. Checked branch with git branch
9. Pushed commits to GitHub via SSH
10. Learned how to fix 'git not recognized' and identity errors
"""

# ==========================================================
# Keep this file as a reference for all Git/GitHub operations
# ==========================================================
# ==========================================================
# Git & GitHub Additional Notes for Beginners
# ==========================================================

# 1️⃣ Branching & Merging
# ------------------------
# Branching allows working on new features without affecting master/main.
# Commands:
# git branch feature-1       # Create a new branch
# git checkout feature-1     # Switch to the branch
# git merge feature-1        # Merge changes back to main
# Tip: Always use branches for new work, then merge when ready.

# 2️⃣ Git Pull
# ------------
# Always pull changes before pushing to avoid conflicts with remote.
# Command:
# git pull origin master     # Update local repo with remote changes

# 3️⃣ Ignoring Files
# -----------------
# Use a .gitignore file to prevent Git from tracking unnecessary files.
# Example for Python projects:
# __pycache__/
# *.pyc
# env/
# .vscode/

# 4️⃣ Git Diff
# ------------
# Review what has changed before staging/committing.
# Command:
# git diff                   # Shows unstaged changes

# 5️⃣ Undoing Mistakes
# -------------------
# Undo unstaged changes:
# git checkout -- <file>     # Discards local edits
# Unstage a file but keep changes:
# git reset <file>           
# Undo last commit but keep changes staged:
# git reset --soft HEAD~1    

# 6️⃣ Cloning Repositories
# -----------------------
# Copy someone else’s GitHub project locally.
# Command:
# git clone git@github.com:username/repo.git
# Creates a local copy with full history.

# 7️⃣ SSH vs HTTPS
# ----------------
# SSH: Secure, no password needed after setup (preferred long-term)
# HTTPS: Easier initially, may ask password for each push.

# 8️⃣ GitHub Pages / Repo Settings
# --------------------------------
# GitHub can host websites via gh-pages branch.
# Learn repo settings: collaborators, branch protection, secrets for automation.

# 9️⃣ Commit Messages Best Practices
# ----------------------------------
# Keep messages short and clear:
# Add login validation
# Fix bug in data parser
# Update README with instructions
# Use imperative tense (“Add” not “Added”) for consistency.

# 🔟 Useful Shortcuts & Tips
# --------------------------
# git log --oneline          # Compact commit history
# git branch -a              # All local & remote branches
# git remote show origin     # Remote tracking info
# git stash                  # Temporarily save changes without committing

# 💡 Pro Tip
# ----------
# Once basics are mastered, learn:
# rebase, cherry-pick, tags, pull requests
# to make workflow more professional.


# DAY 8 : 13/3/2026

# ======================================

# PROCESS: CREATE FILE → PUSH TO BRANCH

# ======================================

# 1. Create a python file

# Example:

# bishal.py

# 2. Check git status

# git status

# 3. Create and switch to a new branch

# git checkout -b branch-name

# 4. Add the file to git

# git add bishal.py

# or

# git add .

# 5. Commit the file

# git commit -m "Added bishal.py file"

# 6. Push the branch to GitHub

# git push origin branch-name

# 7. Verify branch on GitHub repository


