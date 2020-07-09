function checkEmail(nom) {
	// Recherche d'un "@"dans la chaine de caractères saisie nom.value dans Email
	var atPos = nom.value.indexOf('@'); //indexOf retourne le n° de position ou -1
	// Recherche du dernier ".":
	var lastDotPos = nom.value.lastIndexOf('.');
	// Vérifier qu'il y a bien un "@" suivi d'un "." encadré par 
	// au moins un caractère
	if (atPos != -1 && atPos < lastDotPos && lastDotPos < nom.value.length-1 && lastDotPos-atPos > 1) {
		// Si la vérification est réussie, mettre le texte en vert
		nom.style.color = "green";
		return true; //sera utile pour envoyer ou non le formulaire
	}
	else {
		// Si la vérification échoue, mettre le texte en rouge
		nom.style.color = "red";
		return false;//sera utile pour envoyer ou non le formulaire
	}
}

function back2Black(nom) {
	nom.value = '';
	nom.style.color = "black";
}

function valider(form) {
	if (!checkEmail(form.email)) {
		alert("Email invalide");
		return false;
	}

	else {
		return true;
	}
}

