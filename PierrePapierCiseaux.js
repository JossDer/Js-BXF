const tableau = ["pierre", "papier", "ciseaux"];
let choixUtilisateur = prompt(`Choisis : pierre, papier, ciseaux ou stop`)
  .trim()
  .toLowerCase();
let choixPc = tableau[Math.floor(Math.random() * tableau.length)];
while (choixUtilisateur !== "stop") {
  if (choixPc === choixUtilisateur) {
    console.log(`L'ordinateur a choisi ${choixPc}.\n Résultat : Egalité !`);
  } else if (
    (choixPc === "pierre" && choixUtilisateur === "ciseaux") ||
    (choixPc === "ciseaux" && choixUtilisateur === "papier") ||
    (choixPc === "papier" && choixUtilisateur === "pierre")
  ) {
    console.log(`L'ordinateur a choisi ${choixPc}.\n Résultat : Perdu !`);
  } else {
    console.log(`L'ordinateur a choisi ${choixPc}.\n Résultat : Gagné !`);
  }
  choixUtilisateur = prompt(`Choisis : pierre, papier, ciseaux ou stop`)
    .trim()
    .toLowerCase();
  choixPc = tableau[Math.floor(Math.random() * tableau.length)];
}
