#rm -f /var/www/index.html
#cp /var/www/indexpropre.html /var/www/index.html

i=1

for ligne in `ls Diaporama`;do echo "slides[$i] = new Array(15, \"$i\", \"Diaporama/$ligne\");">>diapo.txt;i=$(($i+1));done
cat diapo.txt | tr -d '\r\n' > diapo2.txt
sed -i -e "s|remplacericipls|`cat diapo2.txt`|" index.html

rm -f diapo.txt
rm -f diapo2.txt

service apache2 restart