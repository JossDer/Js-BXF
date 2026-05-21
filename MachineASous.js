let solde = 50.0;

const symboles = ["cerise", "cloche", "sept"];

let choix = prompt(`Que veux-tu faire ? (jouer ou stopper)`)
  .trim()
  .toLowerCase();

if (choix) {
  while (choix !== "stopper") {
    if (solde < 5.5) {
      alert(`Tu n'as plus assez de fonds`);
      break;
    }
    solde -= 5.5;
    let tirage = [];

    for (let i = 0; i < 3; i++) {
      tirage.push(symboles[Math.floor(Math.random() * 3)]);
    }

    if (tirage[0] === tirage[1] && tirage[0] === tirage[2]) {
      solde += 50.0;
    } else if (
      tirage[0] === tirage[1] ||
      tirage[0] === tirage[2] ||
      tirage[1] === tirage[2]
    ) {
      solde += 10.0;
    }
    console.log(tirage.join("-"));
    console.log("Solde :", solde.toFixed(2));

    choix = prompt(`Que veux-tu faire ? (jouer ou stopper)`)
      .trim()
      .toLowerCase();
  }
}
