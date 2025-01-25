#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
git clone https://github.com/Homebrew/brew homebrew
eval "$(homebrew/bin/brew shellenv)"
brew update --force
chmod -R go-w "$(brew --prefix)/share/zsh"

brew upgrade
brew install python@3.13 --verbose
brew update
brew install watchman
watchman watch ./database/
watchman -j <<-EOT
["trigger", "./database", {
  "name": "test",
  "command": ["./commitDB.sh"]
}]
EOT
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate
