#!/bin/bash
# Use macOS's built-in sed to update HTML files in place.

str_now=$(date +'%B %-d, %Y')
echo "$str_now"

while IFS= read -r -d '' file; do
    echo "Inserting date into: $file"
    sed -i '' "s|<p class=\"paragraph-100\" id=\"last-updated\">.*</p>|<p class=\"paragraph-100\" id=\"last-updated\">Last updated: $str_now</p>|g" "$file"
done < <(find . -type f -name "*.html" -print0)
