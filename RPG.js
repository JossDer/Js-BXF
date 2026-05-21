const joueur = {
  nom: "",
  pv: 100,
  atk: 20,
};

const monstre = {
  pv: 50,
  atk: 15,
};

let tour = 0;
joueur.nom = prompt(`Quel est ton nom ?`).trim();

while (monstre.pv > 0 && joueur.pv > 0) {
  let action = prompt(`Que fais tu ? (attaquer ou soigner)`)
    .trim()
    .toLowerCase();

  if (action === "attaquer") {
    let multiplicateur = Math.random() * (1.5 - 0.5) + 0.5;
    let degats = Math.round(joueur.atk * multiplicateur);
    monstre.pv -= degats;
  } else if (action === "soigner") {
    joueur.pv += 25;
    console.log(`Plus 25 PV à ${joueur.nom}`);
  } else {
    alert(`Action inconnue`);
  }

  if (monstre.pv > 0) {
    let degatsMonstre = Math.floor(Math.random() * (monstre.atk - 5 + 1)) + 5;
    joueur.pv -= degatsMonstre;
  }

  tour++;
  joueur.pv = Math.max(joueur.pv, 0);
  monstre.pv = Math.max(monstre.pv, 0);

  console.log(`*******Résumé du tour ${tour}******* `);
  console.log(
    `
Il reste au monstre ${monstre.pv} points de vie`,
  );
  console.log(`Il te reste ${joueur.pv} points de vie\n `);
}

if (joueur.pv <= 0) {
  console.log(`Le monstre t'as vaincu au tour ${tour}...`);
} else if (monstre.pv <= 0) {
  console.log(
    `Bravo ${joueur.nom} ! Tu as vaincu le monstre au bout de ${tour} tours.`,
  );
}
