#!/usr/bin/env bash
# Exit on error
set -o errexit

git clone https://github.com/Homebrew/brew homebrew
eval "$(homebrew/bin/brew shellenv)"
echo $(homebrew/bin/brew shellenv)>>~/.bash_profile
brew update --force
chmod -R go-w "$(brew --prefix)/share/zsh"
git clone https://HananiahKao:$GITHUB_ACCESS_TOKEN@github.com/HananiahKao/Database.git database

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate
