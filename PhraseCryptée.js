const phraseUtilisateur = prompt(`Ecris ta phrase secrète`).trim();
if (phraseUtilisateur.length < 10) {
  alert(`Erreur phrase trop courte`);
} else {
  let phraseCryptée = phraseUtilisateur.split(" ").reverse().join("");
  phraseCryptée = phraseCryptée.replace("a", "4");
  phraseCryptée = phraseCryptée.replace("e", "3");
  phraseCryptée = phraseCryptée + (Math.floor(Math.random() * 9000) + 1000);
  console.log(phraseCryptée);
}
