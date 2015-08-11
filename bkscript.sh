rm -f index.html
cp indexpropre.html index.html
i=1
for ligne in `ls Diaporama`;do echo "slides\\[$i\\] = new Array(15, \\\"$i\\\", Diaporama\\/$ligne\\\")\;">>diapo.txt;i=$(($i+1));done;
replace=`cat diapo.txt`
sed -i -e "s|remplacericipls|$replace|g" index.html

#rm -f diapo.txt
