#!/bin/bash

str_now=`date +'%B %-d, %Y'`
echo $str_now

html_files="$(find . -type f -name "*.html")"

for file in $html_files; do 
    echo "Inserting date into: $file" 
    sed -i "s|<p class=\"paragraph-100\" id=\"last-updated\">.*</p>|<p class=\"paragraph-100\" id=\"last-updated\">Last updated: $str_now</p>|g" $file
done 
