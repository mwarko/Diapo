<?php
if ($_GET['run']) {
	exec("sudo /bin/bash /var/www/script.sh");
}
elif {
	exec("sudo service apache2 restart");
?>
<a href="?run=true"> Récupération des diapositives </a>
<a href="?run=false"> Redémarrage du service apache </a>

