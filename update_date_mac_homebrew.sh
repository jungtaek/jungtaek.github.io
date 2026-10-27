#!/bin/bash
# Install gnu-sed using brew

str_now=`date +'%B %-d, %Y'`
echo $str_now

for file in $(find . -type f -name "*.html"); do 
    echo "Inserting date into: $file" 
    gsed -i "s|<p class=\"paragraph-100\" id=\"last-updated\">.*</p>|<p class=\"paragraph-100\" id=\"last-updated\">Last updated: $str_now</p>|g" $file
done 
