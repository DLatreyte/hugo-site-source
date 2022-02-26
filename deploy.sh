#!/bin/sh

# If a command fails then the deploy stops
set -e

printf "\033[0;32mDeploying updates to GitHub...\033[0m\n"

# Build the project.
hugo # if using a theme, replace with `hugo -t <YOURTHEME>`

# Go To Public folder
cd public

# Add changes to git.
git add .

# Commit changes.
msg="rebuilding site $(date)"
if [ -n "$*" ]; then
	msg="$*"
fi
git commit -m "$msg"

# Push source and build repos.
github push origin master

# Remarque sur la création du submodule pour git
# La procédure du site n'a pas fonctionné
# Commande utilisée : 
# git submodule add -f https://github.com/Dlatreyte/dlatreyte.github.io.git public