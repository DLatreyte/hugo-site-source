#!/bin/sh

# If a command fails then the deploy stops
set -e

printf "\033[0;32mDeploying updates to GitHub...\033[0m\n"

# Build the project.
hugo # if using a theme, replace with `hugo -t <YOURTHEME>`

# Go To Public folder
cd public

# Add changes to git dlatreyte.GitHub.io
git add .

# Commit changes to git dlatreyte.gitHub.io
msg="rebuilding dlatreyte.gitHub.io $(date)"
if [ -n "$*" ]; then
	msg="$*"
fi
git commit -m "$msg"

printf "\033[0;32m# Commit changes to git dlatreyte.gitHub.io...\033[0m\n"

# Return to base folder
cd ..

# Add changes to git hugo-site-source
git add .

# Commit changes to git hugo-site-source
msg="rebuilding hugo-site-source $(date)"
if [ -n "$*" ]; then
	msg="$*"
fi
git commit -m "$msg"

printf "\033[0;32m# Commit changes to git hugo-site-source...\033[0m\n"

# Push source and build repos.
git push -u origin master --recurse-submodules=on-demand

