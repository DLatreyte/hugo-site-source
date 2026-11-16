/* QCM de fin de section (principe du livre Rust de Brown University).
   - une question à la fois, sans correction immédiate ;
   - à la fin : score ; si moins de 100 %, « Recommencer » ou « Voir les réponses » ;
   - une fois les réponses affichées, le QCM ne peut plus être retenté ;
   - l'état est conservé dans le navigateur de l'élève (localStorage). */
(function () {
  'use strict';
  var CLE = 'qcm:';

  function lire(id) { try { return JSON.parse(localStorage.getItem(CLE + id)) || {}; } catch (e) { return {}; } }
  function ecrire(id, etat) { try { localStorage.setItem(CLE + id, JSON.stringify(etat)); } catch (e) { /* stockage indisponible */ } }
  function melanger(liste) {
    for (var i = liste.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = liste[i]; liste[i] = liste[j]; liste[j] = t; }
    return liste;
  }
  function decoder(s) {
    try { return JSON.parse(decodeURIComponent(escape(atob(s)))); } catch (e) { return []; }
  }

  function initialiser(qcm) {
    var id = qcm.getAttribute('data-qcm');
    var solutions = decoder(qcm.getAttribute('data-s'));
    var questions = Array.prototype.slice.call(qcm.querySelectorAll('.qcm-q'));
    var accueil = qcm.querySelector('.qcm-accueil');
    var bilan = qcm.querySelector('.qcm-bilan');
    var b = {
      commencer: qcm.querySelector('.qcm-commencer'), valider: qcm.querySelector('.qcm-valider'),
      recommencer: qcm.querySelector('.qcm-recommencer'), reveler: qcm.querySelector('.qcm-reveler'),
      revoir: qcm.querySelector('.qcm-revoir')
    };
    var courante = 0, reponses = [], confirmation = false;

    function boutons(visibles) {
      Object.keys(b).forEach(function (k) { b[k].hidden = visibles.indexOf(k) < 0; });
    }
    function cacherQuestions() { questions.forEach(function (q) { q.hidden = true; }); }
    function choix(q) { return Array.prototype.slice.call(q.querySelectorAll('input')); }
    function selection(q) {
      return choix(q).filter(function (x) { return x.checked; }).map(function (x) { return +x.value; }).sort();
    }
    function juste(i) {
      var attendu = solutions[i].slice().sort(), donne = reponses[i] || [];
      return attendu.length === donne.length && attendu.every(function (v, k) { return v === donne[k]; });
    }
    function majValider() { b.valider.disabled = selection(questions[courante]).length === 0; }

    function preparer() {
      reponses = []; courante = 0;
      questions.forEach(function (q) {
        q.classList.remove('qcm-revue');
        var ul = q.querySelector('.qcm-choix');
        melanger(Array.prototype.slice.call(ul.children)).forEach(function (li) {
          li.classList.remove('qcm-juste', 'qcm-faux'); ul.appendChild(li);
        });
        choix(q).forEach(function (x) { x.checked = false; x.disabled = false; });
        var ex = q.querySelector('.qcm-explication'); if (ex) ex.hidden = true;
      });
    }
    function afficherQuestion() {
      cacherQuestions(); accueil.hidden = true; bilan.hidden = true;
      questions[courante].hidden = false;
      b.valider.textContent = courante === questions.length - 1 ? 'Valider et voir le résultat' : 'Valider';
      boutons(['valider']); majValider();
    }
    function commencer() { preparer(); afficherQuestion(); }

    function valider() {
      reponses[courante] = selection(questions[courante]);
      if (courante < questions.length - 1) { courante++; afficherQuestion(); return; }
      terminer();
    }
    function terminer() {
      var etat = lire(id);
      var bonnes = questions.filter(function (q, i) { return juste(i); }).length;
      etat.essais = (etat.essais || 0) + 1;
      cacherQuestions(); bilan.hidden = false;
      if (bonnes === questions.length) {
        etat.statut = 'reussi'; ecrire(id, etat);
        bilan.className = 'qcm-bilan qcm-ok';
        bilan.innerHTML = '<strong>Bravo, 100&nbsp;% de bonnes réponses !</strong> ' +
          (etat.essais > 1 ? '(en ' + etat.essais + ' essais)' : 'du premier coup.') +
          ' Vous pouvez revoir les questions et leurs explications.';
        boutons(['revoir', 'recommencer']);
      } else {
        ecrire(id, etat);
        bilan.className = 'qcm-bilan qcm-ko';
        bilan.innerHTML = '<strong>' + bonnes + '&nbsp;/&nbsp;' + questions.length + ' bonne' + (bonnes > 1 ? 's' : '') +
          ' réponse' + (bonnes > 1 ? 's' : '') + '.</strong> Relisez la section si besoin, puis recommencez : ' +
          'l\'objectif est d\'obtenir 100&nbsp;%.';
        confirmation = false; b.reveler.textContent = 'Voir les réponses';
        boutons(['recommencer', 'reveler']);
      }
    }
    function revue(avecReponsesEleve) {
      accueil.hidden = true;
      questions.forEach(function (q, i) {
        q.hidden = false; q.classList.add('qcm-revue');
        choix(q).forEach(function (x) {
          var li = x.closest('li'), v = +x.value, bon = solutions[i].indexOf(v) >= 0;
          x.disabled = true;
          x.checked = avecReponsesEleve ? (reponses[i] || []).indexOf(v) >= 0 : bon;
          li.classList.toggle('qcm-juste', bon);
          li.classList.toggle('qcm-faux', !bon && x.checked);
        });
        var ex = q.querySelector('.qcm-explication'); if (ex) ex.hidden = false;
      });
    }
    function reveler() {
      if (!confirmation) {
        confirmation = true;
        b.reveler.textContent = 'Confirmer (vous ne pourrez plus retenter ce QCM)';
        return;
      }
      var etat = lire(id); etat.statut = 'revele'; ecrire(id, etat);
      bilan.className = 'qcm-bilan qcm-revele';
      bilan.innerHTML = '<strong>Réponses affichées.</strong> Les bonnes réponses sont en vert, vos erreurs en rouge.';
      revue(true); boutons([]);
    }
    function revoir() {
      bilan.hidden = true; revue(false); boutons(['recommencer']);
    }

    b.commencer.addEventListener('click', commencer);
    b.valider.addEventListener('click', valider);
    b.recommencer.addEventListener('click', commencer);
    b.reveler.addEventListener('click', reveler);
    b.revoir.addEventListener('click', revoir);
    questions.forEach(function (q) { q.addEventListener('change', majValider); });

    // état mémorisé
    var etat = lire(id);
    if (etat.statut === 'reussi') {
      accueil.hidden = true; bilan.hidden = false; bilan.className = 'qcm-bilan qcm-ok';
      bilan.innerHTML = '<strong>QCM réussi à 100&nbsp;%.</strong> Vous pouvez revoir les questions ou le refaire pour vous entraîner.';
      boutons(['revoir', 'recommencer']);
    } else if (etat.statut === 'revele') {
      bilan.hidden = false; bilan.className = 'qcm-bilan qcm-revele';
      bilan.innerHTML = '<strong>Réponses déjà affichées</strong> : ce QCM ne peut plus être retenté.';
      revue(false); boutons([]);
    } else {
      boutons(['commencer']);
    }
  }

  document.querySelectorAll('.qcm').forEach(initialiser);
})();
