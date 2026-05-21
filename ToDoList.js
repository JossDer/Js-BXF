let commande = prompt(`Que veux tu faire ? (new, list, delete, quit)`)
  .trim()
  .toLowerCase();
const taches = [];

while (commande !== "quit") {
  if (commande === "new") {
    const nouvelleTache = prompt(`Quelle tâche veux tu ajouter ?`);

    if (nouvelleTache) {
      taches.push(nouvelleTache);

      console.log(`La tâche : ${nouvelleTache} a été ajoutée à la liste`);
    } else {
      console.log(`Aucune tâche ajoutée`);
    }
  } else if (commande === "list") {
    console.log(`******** LISTE DE TÂCHES ********`);

    for (let i = 1; i <= taches.length; i++) {
      console.log(`${i}. ${taches[i - 1]}`);
    }
  } else if (commande === "delete") {
    let supprimer = Number(
      prompt(`Quel est le numéro de la tâche que vous voulez supprimer ?`),
    );

    while (isNaN(supprimer) || supprimer > taches.length || supprimer < 1) {
      supprimer = Number(prompt(`Donnez un numéro de tâche valide ?`));
    }

    const tacheSupprimée = taches.splice(supprimer - 1, 1);
    console.log(`La tâche ${tacheSupprimée[0]} a été supprimée`);
  } else {
    alert(`Commande inconnue`);
  }

  commande = prompt(`Que veux tu faire maintenant ? (new, list, delete, quit)`)
    .trim()

    .toLowerCase();
}

console.log(`Fin du programme`);
