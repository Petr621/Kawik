@echo off

git checkout -- requirements.txt

git stash
if not %errorlevel%==0 (
    echo "Could not successfully stash current changes"
    exit /b 1
)

git pull --rebase origin main
if not %errorlevel%==0 (
    echo "Could not successfully pull the latest changes to your local repository"
    exit /b 1
)

git stash pop
if not %errorlevel%==0 (
    echo "Could not successfully pop the stash"
    exit /b 1
)

pip install -r requirements.txt
if not %errorlevel%==0 (
    echo "Could not successfully install packages"
    exit /b 1
)
