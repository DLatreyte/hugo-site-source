<TeXmacs|1.99.11>

<style|<tuple|exam|french>>

<\body>
  <doc-data|<doc-title|Devoir surveill� n<degreesign>2>|<doc-misc|<strong|H�ron
  d'Alexandrie>>|<doc-exam-date|<em|Mercredi 20 novembre
  2019>>|<doc-exam-class|<em|1<rsup|�re> Sp�cialit� NSI>>>

  H�ron d'Alexandrie est un ing�nieur, un m�canicien et un math�maticien grec
  du premier si�cle apr�s J.-C.

  On ne sait pas grand chose de la vie d'H�ron, si ce n'est qu'il �tait
  originaire d'Alexandrie ; les historiens se sont m�me longtemps divis�s sur
  l'�poque o� il a v�cu. Leurs estimations allaient du 1<rsup|er> si�cle
  avant J.-C. au 3<rsup|�me> si�cle de notre �re. Aujourd'hui, la querelle
  est �teinte : il est clairement �tabli que H�ron est post�rieur � Vitruve
  mort en <math|-20>, et contemporain de Pline l'Ancien (23 \U 79), en �tant
  actif autour de l'an 62. Il a donc bien v�cu au 1<rsup|er> si�cle apr�s
  J.-C. et sans doute au d�but du 2<rsup|�me> si�cle, donc sous l'Empire
  romain, mais dans l'Alexandrie grecque.

  On attribue � H�ron d'Alexandrie plusieurs formules math�matiques et une
  m�thode efficace d'extraction de racine carr�e, c'est-�-dire de r�solution
  de l'�quation <math|x<rsup|2>=a>, avec <math|a> positif :

  <\enumerate>
    <item>Choisir une premi�re valeur raisonnable que l'on note <math|G>.

    <item>Am�liorer cette valeur en calculant la moyenne des valeurs <math|G>
    et <math|x/G>.

    <item>V�rifier si cette nouvelle valeur convient.

    <item>Reprendre l'�tape 2 tant que la valeur calcul�e n'est pas
    satisfaisante.
  </enumerate>

  <htab|><em|L'objectif de ce probl�me est de mettre en �uvre cette m�thode
  en Python.> <htab|>

  Votre fichier r�ponse devra se terminer par les instructions :

  <\python-code>
    if __name__ == "__main__":

    \ \ \ \ import doctest\ 

    \ \ \ \ doctest.testmod()
  </python-code>

  et chaque fonction devra incorporer dans sa documentation les informations
  qui vous permettront de tester sa validit� (reprendre donc syst�matiquement
  les sp�cifications que je vous donne).

  <\enumerate>
    <item>D�finir la fonction <python|moyenne> dont la sp�cification est

    <\python-code>
      def moyenne(a: float, b: float) -\<gtr\> float:\ 

      \ \ \ \ """ Calcule et retourne la moyenne des deux nombres a et b
      pass�s en argument.

      \ \ \ \ \<gtr\>\<gtr\>\<gtr\> moyenne(12, 16)\ 

      \ \ \ \ 14.0\ 

      \ \ \ \ \<gtr\>\<gtr\>\<gtr\> moyenne(0, 8)\ 

      \ \ \ \ 4.0\ 

      \ \ \ \ """
    </python-code>

    <item>D�finir la fonction <python|valeur_absolue> dont la sp�cification
    est :

    <\python-code>
      def valeur_absolue(x: float) -\<gtr\> float:\ 

      \ \ \ \ """\ 

      \ \ \ \ Calcule et retourne la valeur absolue du nombre x pass� en
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
      Il est interdit d'utiliser la fonction <python|abs> int�gr�e � Python.
    </remark*>

    <item>D�finir la fonction <python|puissance> dont la sp�cification est :

    <\python-code>
      def puissance(x: float, n: int) -\<gtr\> float:\ 

      \ \ \ \ """ calcule et retourne le r�sultat de x � la puissance enti�re
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
      Il est interdit d'utiliser l'op�rateur <python|**> int�gr� � Python ou
      la fonction <python|pow> du module <python|math>.
    </remark*>

    <item>D�finir la fonction <python|amelioration_essai> dont la
    sp�cification est :

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
      Cette fonction doit utiliser la fonction <python|moyenne> d�finie plus
      haut.
    </remark*>

    <item>D�finir le pr�dicat <python|est_suffisamment_bon> dont la
    sp�cification est :

    <\python-code>
      def est_suffisamment_bon(essai: float, x: float) -\<gtr\> float:\ 

      \ \ \ \ """\ 

      \ \ \ \ Retourne True si la valeur absolue de la diff�rence du carr� du
      nombre essai\ 

      \ \ \ \ et du nombre x est inf�rieure � une tol�rance donn�e (prendre
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
      <python|puissance> d�finies ci-dessus.
    </remark*>

    <item>D�finir la fonction <python|test> qui impl�mente l'algorithme de
    H�ron d'Alexandrie. La sp�cification de la fonction est :

    <\python-code>
      def test(essai: float, x: float) -\<gtr\> float:\ 

      \ \ \ \ """\ 

      \ \ \ \ Retourne la racine carr�e du nombre x. Le calcul est effectu�
      gr�ce � un

      \ \ \ \ raisonnement it�ratif depuis une premi�re valeur strictement
      positive not�e essai.

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

    <item>D�finir la fonction <python|racine_carree> dont la sp�cification
    est :

    <\python-code>
      def racine_carree(x: float) -\<gtr\> float:\ 

      \ \ \ \ """\ 

      \ \ \ \ Retourne le r�sultat de l'appel de la fonction test avec la
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

    <item>D�finir la fonction <python|main> qui affiche � l'�cran la liste
    des racines carr�es de tous les nombres pairs compris dans l'intervalle
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