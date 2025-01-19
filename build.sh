#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
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
