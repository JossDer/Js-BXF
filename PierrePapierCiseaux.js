const tableau = ["pierre", "papier", "ciseaux"];
let choixUtilisateur = prompt(`Choisis : pierre, papier, ciseaux ou stop`)
  .trim()
  .toLowerCase();
let egalite = 0
let victoire = 0
let defaite = 0
while (choixUtilisateur !== "stop") {
  let choixPc = tableau[Math.floor(Math.random() * tableau.length)];
    if (!tableau.includes(choixUtilisateur)) {
    console.log("Choix invalide !");
      choixUtilisateur = prompt("Choisis : pierre, papier, ciseaux ou stop")
    .trim()
    .toLowerCase();
  } else {

  if (choixPc === choixUtilisateur) {
    console.log(`L'ordinateur a choisi ${choixPc}.\n Résultat : Egalité !`);
    egalite++
  } else if (
    (choixPc === "pierre" && choixUtilisateur === "ciseaux") ||
    (choixPc === "ciseaux" && choixUtilisateur === "papier") ||
    (choixPc === "papier" && choixUtilisateur === "pierre")
  ) {
    console.log(`L'ordinateur a choisi ${choixPc}.\n Résultat : Perdu !`);
    defaite++
  } else {
    console.log(`L'ordinateur a choisi ${choixPc}.\n Résultat : Gagné !`);
    victoire++
  }
  choixUtilisateur = prompt(`Choisis : pierre, papier, ciseaux ou stop`)
    .trim()
    .toLowerCase();
}} 
console.log(`*****Résultats*****`)
console.log(`Victoires : ${victoire}\n Défaites : ${defaite}\n Égalité : ${egalite}\n `)
