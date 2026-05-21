let numMax = Number(prompt(`Donne moi un nombre maximum`));
let compteur = 0;

while (isNaN(numMax) || numMax <= 0) {
  numMax = Number(prompt(`Donne moi un nombre valide, supérieur à 0`));
}

const numAleatoire = Math.floor(Math.random() * numMax) + 1;

let essai = Number(prompt(`Devine le nombre entre 1 et ${numMax}`));

while (essai !== numAleatoire) {
  if (!isNaN(essai)) {
    compteur++;
  }

  if (isNaN(essai)) {
    alert(`Cette réponse n'est pas valide`);
  } else if (essai < numAleatoire) {
    alert(`Le nombre aléatoire est plus grand que ${essai}`);
  } else if (essai > numAleatoire) {
    alert(`Le nombre aléatoire est plus petit que ${essai}`);
  }
  essai = Number(prompt(`Devine le nombre entre 1 et ${numMax}`));
}

alert(
  `Félicitations ! Le nombre aléatoire était ${numAleatoire}. Tu l'as trouvé en ${compteur} tentatives`,
);
