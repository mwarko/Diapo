#rm -f /var/www/index.html
#cp /var/www/indexpropre.html /var/www/index.html

i=1
for element in `ls Diaporama`; do echo "slides[$i] = new Array(15, \"$i\", \"Diaporama/$element\");" >> diapo.txt && $i=$i+1; done