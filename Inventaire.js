const inventaire = [
  { nom: "eau", qte: 2 },
  { nom: "ration", qte: 1 },
];

let action = prompt("Que veux tu faire ? (ramasser, utiliser ou stopper)")
  .trim()
  .toLowerCase();

while (action !== "stopper") {
  if (action === "ramasser") {
    let objet = prompt("Quel est le nom de l'objet à ramasser ?")
      .trim()
      .toLowerCase();

    let existe = inventaire.find((item) => item.nom === objet);

    if (!objet) {
      alert("Ceci n'est pas un objet valide");
    } else if (existe) {
      existe.qte++;
    } else {
      inventaire.push({
        nom: objet,
        qte: 1,
      });
    }
  } else if (action === "utiliser") {
    let utiliser = prompt("Quel est le nom de l'objet à utiliser ?")
      .trim()
      .toLowerCase();

    let existe = inventaire.find((item) => item.nom === utiliser);

    if (!utiliser) {
      alert("Ceci n'est pas un objet valide");
    } else if (existe && existe.qte > 0) {
      existe.qte--;

      if ((existe.qte = 0)) {
        let indexObjet = inventaire.findIndex((item) => item.nom === utiliser);

        inventaire.splice(indexObjet, 1);
      }
    } else {
      alert("Objet introuvable");
    }
  } else {
    console.log("Veuillez entrer une action valide");
  }

  action = prompt("Que veux tu faire ? (ramasser, utiliser ou stopper)")
    .trim()
    .toLowerCase();
}

console.log("***** Inventaire *****");

for (let index = 0; index < inventaire.length; index++) {
  console.log(`${inventaire[index].nom} : ${inventaire[index].qte}`);
}
