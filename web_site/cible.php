<?php
$bdd = new PDO('mysql:host=localhost;dbname=weekly_mail', 'weekly_mail', 'Mgfa23a.', array(PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION));
$requete = $bdd->prepare('INSERT INTO Users (name, surname, gender, birthday, email) VALUES(?, ?, ?, ?, ?)');
$requete->execute(array($_POST['name'], $_POST['surname'], $_POST['gender'], $_POST['birthday'], $_POST['email']));
header('Location: thanks.html');
exit();
?>
