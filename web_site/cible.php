<?php
$bdd = new PDO('mysql:host=127.0.0.1;dbname=elevage', 'greg', 'MgfssQWERTY eia24a.' array(PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION));
$requete = $bdd->prepare('INSERT INTO nimal(nom, possesseur) VALUES(?, ?)');
$requete->execute(array($_POST['nom'], $_POST['possesseur']));
?>
