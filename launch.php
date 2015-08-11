<!DOCTYPE html>
<html>
	<head>
		<link type="text/css" rel="stylesheet" href="stylesheet.css"/>
	</head>
	<body>
			<h1>chargement des diapos patientez et appuyez sur le bouton ci-dessous pour redemarrer</h1>
		<div>
			<a href="reboot.php"><span>REBOOT</span></a>
			<br/>
			<br/>
		</div>
	</body>
</html>




<?php echo exec('sudo /bin/bash -x /var/www/script.sh'); ?>
