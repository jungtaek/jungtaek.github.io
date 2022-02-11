#!/bin/bash

git_last_commit_date="$(git log -1 --format=%cd)"
echo "Git last commit date: $git_last_commit_date"

html_files="$(find . -type f -name "*.html")"

for file in $html_files; do 
    echo "Inserting date into: $file" 
    sed -i "" "s|<p class=\"paragraph-100\" id=\"last-updated\">*</p>|<p class=\"paragraph-100\" id=\"last-updated\">Last updated: $git_last_commit_date</p>|g" "$file"
done 
