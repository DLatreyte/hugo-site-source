<TeXmacs|1.99.11>

<style|<tuple|exam|french>>

<\body>
  <doc-data|<doc-title|Devoir surveillé n<degreesign>2>|<doc-misc|<strong|Héron
  d'Alexandrie>>|<doc-exam-date|<em|Mercredi 20 novembre
  2019>>|<doc-exam-class|<em|1<rsup|ère> Spécialité NSI>>>

  Héron d'Alexandrie est un ingénieur, un mécanicien et un mathématicien grec
  du premier siècle après J.-C.

  On ne sait pas grand chose de la vie d'Héron, si ce n'est qu'il était
  originaire d'Alexandrie ; les historiens se sont même longtemps divisés sur
  l'époque où il a vécu. Leurs estimations allaient du 1<rsup|er> siècle
  avant J.-C. au 3<rsup|ème> siècle de notre ère. Aujourd'hui, la querelle
  est éteinte : il est clairement établi que Héron est postérieur à Vitruve
  mort en <math|-20>, et contemporain de Pline l'Ancien (23 \U 79), en étant
  actif autour de l'an 62. Il a donc bien vécu au 1<rsup|er> siècle après
  J.-C. et sans doute au début du 2<rsup|ème> siècle, donc sous l'Empire
  romain, mais dans l'Alexandrie grecque.

  On attribue à Héron d'Alexandrie plusieurs formules mathématiques et une
  méthode efficace d'extraction de racine carrée, c'est-à-dire de résolution
  de l'équation <math|x<rsup|2>=a>, avec <math|a> positif :

  <\enumerate>
    <item>Choisir une première valeur raisonnable que l'on note <math|G>.

    <item>Améliorer cette valeur en calculant la moyenne des valeurs <math|G>
    et <math|x/G>.

    <item>Vérifier si cette nouvelle valeur convient.

    <item>Reprendre l'étape 2 tant que la valeur calculée n'est pas
    satisfaisante.
  </enumerate>

  <htab|><em|L'objectif de ce problème est de mettre en ÷uvre cette méthode
  en Python.> <htab|>

  Votre fichier réponse devra se terminer par les instructions :

  <\python-code>
    if __name__ == "__main__":

    \ \ \ \ import doctest\ 

    \ \ \ \ doctest.testmod()
  </python-code>

  et chaque fonction devra incorporer dans sa documentation les informations
  qui vous permettront de tester sa validité (reprendre donc systématiquement
  les spécifications que je vous donne).

  <\enumerate>
    <item>Définir la fonction <python|moyenne> dont la spécification est

    <\python-code>
      def moyenne(a: float, b: float) -\<gtr\> float:\ 

      \ \ \ \ """ Calcule et retourne la moyenne des deux nombres a et b
      passés en argument.

      \ \ \ \ \<gtr\>\<gtr\>\<gtr\> moyenne(12, 16)\ 

      \ \ \ \ 14.0\ 

      \ \ \ \ \<gtr\>\<gtr\>\<gtr\> moyenne(0, 8)\ 

      \ \ \ \ 4.0\ 

      \ \ \ \ """
    </python-code>

    <item>Définir la fonction <python|valeur_absolue> dont la spécification
    est :

    <\python-code>
      def valeur_absolue(x: float) -\<gtr\> float:\ 

      \ \ \ \ """\ 

      \ \ \ \ Calcule et retourne la valeur absolue du nombre x passé en
      argument.

      \;

      \ \ \ \ \<gtr\>\<gtr\>\<gtr\> valeur_absolue(3)\ 

      \ \ \ \ 3\ 

      \ \ \ \ \<gtr\>\<gtr\>\<gtr\> valeur_absolue(0)\ 

      \ \ \ \ 0\ 

      \ \ \ \ \<gtr\>\<gtr\>\<gtr\> valeur_absolue(-3)\ 

      \ \ \ \ 3\ 

      \ \ \ \ """
    </python-code>

    <\remark*>
      Il est interdit d'utiliser la fonction <python|abs> intégrée à Python.
    </remark*>

    <item>Définir la fonction <python|puissance> dont la spécification est :

    <\python-code>
      def puissance(x: float, n: int) -\<gtr\> float:\ 

      \ \ \ \ """ calcule et retourne le résultat de x à la puissance entière
      n :

      \ \ \ \ x^n = x . x . x . ... . x (n fois)

      \ \ \ \ 

      \ \ \ \ \<gtr\>\<gtr\>\<gtr\> puissance(2, 8)\ 

      \ \ \ \ 256\ 

      \ \ \ \ \<gtr\>\<gtr\>\<gtr\> puissance(0, 2)\ 

      \ \ \ \ 0\ 

      \ \ \ \ \<gtr\>\<gtr\>\<gtr\> puissance(3, 0)\ 

      \ \ \ \ 1\ 

      \ \ \ \ """
    </python-code>

    <\remark*>
      Il est interdit d'utiliser l'opérateur <python|**> intégré à Python ou
      la fonction <python|pow> du module <python|math>.
    </remark*>

    <item>Définir la fonction <python|amelioration_essai> dont la
    spécification est :

    <\python-code>
      def amelioration_essai(essai: float, x: float) -\<gtr\> float:\ 

      \ \ \ \ """ Calcule et retourne la moyenne des nombres essai
      (strictement positif)\ 

      \ \ \ \ et x/essai.

      \;

      \ \ \ \ \<gtr\>\<gtr\>\<gtr\> amelioration_essai(1, 2)\ 

      \ \ \ \ 1.5\ 

      \ \ \ \ \<gtr\>\<gtr\>\<gtr\> amelioration_essai(2, 1)\ 

      \ \ \ \ 1.25\ 

      \ \ \ \ """
    </python-code>

    <\remark*>
      Cette fonction doit utiliser la fonction <python|moyenne> définie plus
      haut.
    </remark*>

    <item>Définir le prédicat <python|est_suffisamment_bon> dont la
    spécification est :

    <\python-code>
      def est_suffisamment_bon(essai: float, x: float) -\<gtr\> float:\ 

      \ \ \ \ """\ 

      \ \ \ \ Retourne True si la valeur absolue de la différence du carré du
      nombre essai\ 

      \ \ \ \ et du nombre x est inférieure à une tolérance donnée (prendre
      0.001).

      \ \ \ \ Retourne False sinon.

      \;

      \ \ \ \ \<gtr\>\<gtr\>\<gtr\> est_suffisamment_bon(1.9, 4)\ 

      \ \ \ \ False\ 

      \ \ \ \ \<gtr\>\<gtr\>\<gtr\> est_suffisamment_bon(1.999, 4)\ 

      \ \ \ \ False\ 

      \ \ \ \ \<gtr\>\<gtr\>\<gtr\> est_suffisamment_bon(1.9999, 4)\ 

      \ \ \ \ True\ 

      \ \ \ \ """
    </python-code>

    <\remark*>
      Cette fonction doit utiliser les fonctions <python|valeur_absolue> et
      <python|puissance> définies ci-dessus.
    </remark*>

    <item>Définir la fonction <python|test> qui implémente l'algorithme de
    Héron d'Alexandrie. La spécification de la fonction est :

    <\python-code>
      def test(essai: float, x: float) -\<gtr\> float:\ 

      \ \ \ \ """\ 

      \ \ \ \ Retourne la racine carrée du nombre x. Le calcul est effectué
      grâce à un

      \ \ \ \ raisonnement itératif depuis une première valeur strictement
      positive notée essai.

      \;

      \ \ \ \ \<gtr\>\<gtr\>\<gtr\> test(2, 4)\ 

      \ \ \ \ 2\ 

      \ \ \ \ \<gtr\>\<gtr\>\<gtr\> test(1, 4)\ 

      \ \ \ \ 2.0000000929222947\ 

      \ \ \ \ \<gtr\>\<gtr\>\<gtr\> test(7, 4)\ 

      \ \ \ \ 2.0000000271231317\ 

      \ \ \ \ """
    </python-code>

    <\remark*>
      Cette fonction doit utiliser les fonctions
      <python|est_suffisamment_bon> et <python|amelioration_essai>.
    </remark*>

    <item>Définir la fonction <python|racine_carree> dont la spécification
    est :

    <\python-code>
      def racine_carree(x: float) -\<gtr\> float:\ 

      \ \ \ \ """\ 

      \ \ \ \ Retourne le résultat de l'appel de la fonction test avec la
      valeur 1\ 

      \ \ \ \ pour l'argument essai.

      \ \ \ \ 

      \ \ \ \ \<gtr\>\<gtr\>\<gtr\> racine_carree(4)\ 

      \ \ \ \ 2.0000000929222947\ 

      \ \ \ \ \<gtr\>\<gtr\>\<gtr\> racine_carree(9)\ 

      \ \ \ \ 3.00009155413138\ 

      \ \ \ \ \<gtr\>\<gtr\>\<gtr\> racine_carree(16)\ 

      \ \ \ \ 4.000000636692939\ 

      \ \ \ \ """
    </python-code>

    <item>Définir la fonction <python|main> qui affiche à l'écran la liste
    des racines carrées de tous les nombres pairs compris dans l'intervalle
    <math|<around*|[|1;100|]>>.
  </enumerate>
</body>

<\initial>
  <\collection>
    <associate|font-base-size|11>
    <associate|page-medium|paper>
    <associate|page-screen-margin|false>
    <associate|page-width-margin|true>
    <associate|par-kerning-margin|true>
    <associate|par-width|18.5cm>
  </collection>
</initial>