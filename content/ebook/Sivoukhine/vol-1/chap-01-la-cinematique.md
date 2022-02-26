---
title: "La Cinématique"
subtitle: "Chapitre 01"
author: "D. Sivoukhine"
type: ""
date: 2020-08-25T22:27:19+04:00
draft: false
toc: true
tags: []
categories: []
image: ""
solution_est_visible: true
auto_numbering: false
---
$
\global\def\dif#1{\dfrac{\mathrm{d} #1}{\mathrm{d} t}}
\global\def\diff#1{\dfrac{\mathrm{d}^2 #1}{\mathrm{d} t^2}}
$
## §1. L’espace et le temps

**1.** En mécanique on entend par *mouvement* le changement
avec le temps de la position spatiale d'un corps. La position du corps dont il est question est une *position relative*, définie par rapport à
d'autres corps. Le concept de position absolue, qui serait la position d'un corps dans un «&nbsp;espace absolu&nbsp;», donc sans aucune référence à celles d'autres corps, est dénué de sens.

Le corps ou le système de corps par rapport auxquels on définit les
positions d'autres corps sont désignés sous le nom de
*système de référence* ou *référentiel* ou
*repères*.

Il est dénué de sens d'affirmer que deux évènements
différents et non simultanés se sont produits dans un seul et même
point de l'espace si on ne précise pas le référentiel utilisé.
Soit un voyageur, assis dans un train en mouvement, qui retire à un
instant donné un objet de sa valise, puis le remet en place. On ne pourra
dire que ces deux actions du voyageur ont eu lieu au même endroit que si
on avait choisi comme référentiel le wagon du train en mouvement. Mais
si nous avions choisi pour référentiel la voie du chemin de fer, les
deux évènements en question auront lieu en des endroits
différents, par exemple l'un à Moscou et l'autre à Léningrad.

**2.** On peut choisir comme référentiel un corps solide auquel
seraient liés des *axes de coordonnées*, par exemple un
trièdre trirectangle constitué par des tiges rigides. Dans ce
référentiel la position de tout point pourrait être définie
par trois nombres que sont les *coordonnées* $x$, $y$ et $z$ de ce
point ; ces coordonnées représentent respectivement les distances de
ce point aux trois plans $YZ$, $ZX$ et $XY$ de notre référentiel
([fig. 1](#fig-01)). Les trois coordonnées $x$, $y$, $z$ peuvent être
combinées pour définir un *rayon vecteur* $\mathbf{r}$, qui
est un segment de droite pointant de l'origine du trièdre de
référence vers le point considéré. Les coordonnées $x$,
$y$, $z$ sont les projections du rayon vecteur sur les axes de
coordonnées. Aussi écrira-t-on

$$ \mathbf{r} = x\\, \mathbf{i} + y\\, \mathbf{j} + z\\, \mathbf{k}$$

où $\mathbf{i}$, $\mathbf{j}$, $\mathbf{k}$ sont des *vecteurs
unitaires* orientés le long des axes $X$, $Y$, $Z$.

<figure>
  <img id="fig-01" src="/ebook/sivoukhine/vol-1/chap-1/fig01.svg" >
  <img id="fig-02" src="/ebook/sivoukhine/vol-1/chap-1/fig02.svg" >
</figure>

On utilise deux trièdres de référence qui se laissent distinguer
par application de la *règle du tire-bouchon*. Prenons un
tire-bouchon normal (filetage à droite) et tournons-le de manière que
son manche soit dans le plan $X Y$. Dans un trièdre de référence
de *sens direct* ([fig. 1](#fig-01)) le tire-bouchon avance dans le
sens des $z$ positifs et dans un trièdre de *sens inverse* ([fig. 2](#fig-02)) il avance dans le sens des $z$ négatifs. Aucune rotation ne
permet de faire coïncider ces deux trièdres qui se distinguent l'un de
l'autre comme la main gauche se distingue de la main droite. Mais on
transforme un trièdre de sens direct en trièdre de sens inverse en
inversant le sens d'un seul ou des trois axes de coordonnées. Dans ce
dernier cas on effectue une *inversion des axes de coordonnées* ou
encore une *réflexion par rapport à l'origine*. L'image dans un
miroir plan d'un trièdre de sens direct est un trièdre de sens
inverse. En physique on n'utilise que le trièdre de référence
direct.

**3.** Les coordonnées $x$, $y$, $z$ servant à définir la
position d'un point dans le référentiel choisi sont des nombres.
*La détermination quantitative des coordonnées d'un point
implique, comme d'ailleurs de n'importe quelle grandeur physique, la
définition du principe du procédé de leur mesure.* Il importe de
souligner qu'il s'agit bien du principe de la méthode de mesure et non du
procédé pratique de la détermination de la valeur de la grandeur
considérée. Ces méthodes de mesure ne doivent que dévoiler la
signification ou mieux le principe de détermination de $x$, $y$, $z$ ou
des nombres servant à caractériser quantitativement toute autre
grandeur physique. Aussi nous est-il loisible de supposer que les
procédés de mesure utilisés sont *parfaits* et les
résultats ainsi obtenus sont d'une précision absolue. Les
coordonnées $x$, $y$, $z$ sont des longueurs, de sorte que leur
détermination se ramène à des mesures des longueurs, donc à
des nombres caractérisant les longueurs. En parlant de la mesure des
longueurs, nous avons en vue l'opération suivante. Par convention on
adopte pour étalon de longueur une certaine tige rigide dont la longueur
est prise pour une unité de longueur. Pour mesurer la dimension d'un
corps, nous cherchons le nombre qui indique de combien de fois cette dimension
du corps est plus grande que notre tige étalon. C'est ce nombre que l'on
appelle dimension du corps le long d'une direction donnée. Si ce nombre
n'est pas entier, on devra diviser préalablement notre tige étalon en
parties plus petites&nbsp;: dixièmes, centièmes, etc., de l'unité de
longueur. Nous pouvons utiliser maintenant l'unité étalon munie de ses
subdivisions pour caractériser n'importe quelle dimension par un nombre
décimal ou par un nombre entier suivi de décimales.

**4.** Le procédé consistant à déterminer la dimension
d'un corps par application à celui-ci de l'étalon ou de ses
subdivisions constitue la *mesure directe*. Or, il n'est pas toujours
possible d'effectuer une mesure directe ; on ne peut le faire lorsqu'il s'agit
de déterminer la distance jusqu'à un corps extrêmement
éloigné, par exemple les planètes, les étoiles et les autres
objets célestes. La mesure directe est tout aussi irréalisable pour
les très petites dimensions auxquelles sont confrontés les physiciens
étudiant les atomes, les noyaux atomiques ou les particules
élémentaires. On devra alors avoir recours à des
*méthodes de mesure indirectes*. La pertinence de ces méthodes
doit être vérifiée par des méthodes directes (lorsque
celles-ci sont possibles). Mais lorsque les méthodes directes cessent
d'être utilisables, ne subsistent que les méthodes indirectes. Dans
toute méthode indirecte les opérations de mesure directes, à
l'aide desquelles fut initialement introduit le concept quantitatif de
longueur, prennent un caractère abstrait ; aussi ce sont les méthodes
indirectes qui assument alors le rôle des opérations de mesure
fondamentales susceptibles de dégager la signification des longueurs
elles-mêmes ou plus exactement des nombres caractérisant les longueurs
mesurées.

<figure>
  <img id="fig-03" src="/ebook/sivoukhine/vol-1/chap-1/fig03.svg" >
</figure>

Un exemple de méthode de mesure indirecte est la *triangulation*
qui est le procédé généralement utilisé pour
déterminer les distances jusqu'à des objets éloignés. Par une
mesure directe on détermine la longueur de la «&nbsp;*base*&nbsp;» $A B$ ([fig. 3](#fig-03)) ; en se plaçant
aux extrémités de cette base $A B$ on effectue des pointages vers
l'objet éloigné $C$, ce qui a pour but de mesurer les angles $\alpha$
et $\beta$ que forment les droites $A C$ et $B C$ avec la base $A B$.
Disposant de ces données numériques, la distance inconnue à
laquelle se trouve le point $C$ peut être calculée par une
construction ou par un calcul géométrique. Si la base $A B$ choisie
est trop grande pour que sa longueur puisse être déterminée par
une mesure directe, on commencera par adopter une base plus courte, mesurer sa
longueur puis déterminer la longueur de la base $A B$ par le
procédé de la triangulation. En principe cela ne change rien à
notre affaire. Il est beaucoup plus important d'établir les fondements
théoriques de la méthode considérée. Celle-ci postule que les
côtés du triangle $A B C$ sont des *droites satisfaisant aux
axiomes de la géométrie d'Euclide*. Mais on doit encore établir
quels sont les constituants matériels délimitant ce triangle ; ce sont
les rayons lumineux issus de l'objet $C$ et parvenant aux points $A$ et $B$.
On en conclut que notre méthode repose sur l'hypothèse que les rayons
lumineux sont rigoureusement rectilignes et satisfont donc aux mêmes
axiomes de la géométrie d'Euclide que les droites
géométriques. Cette hypothèse n'est nullement évidente à
priori et le seul moyen de la confirmer ou de l'infirmer est l'expérience.
Ce que l'on a en vue en faisant cette hypothèse c'est la propagation des
rayons lumineux dans le vide et non pas dans l'atmosphère terrestre où
ils s'incurvent effectivement par suite des variations locales de l'indice de
réfraction de l'air. Il est possible de tenir compte de ces écarts
à la propagation rectiligne des rayons lumineux et on le fait dans les
mesures de haute précision.

Une autre question vient encore à l'esprit : comment peut-on s'assurer que
la géométrie d'Euclide est applicable dans des circonstances
réelles ? La méthode directe que l'on peut utiliser pour répondre
à cette question consiste à soumettre à une vérification
expérimentale les corollaires des axiomes de la géométrie
euclidienne. Un des corollaires est le théorème affirmant que la somme
des angles internes d'un triangle est égale à 180°. Le
célèbre mathématicien Gauss (1777-1855) s'est attaché, de
1821 à 1823, à mesurer avec précision les angles internes d'un
triangle formé par trois pics de montagne. Les longueurs des côtés
de ce triangle étaient d'environ $\pu{100 km}$. Il en conclut qu'aux erreurs de
mesure près ce théorème se trouvait vérifié. Cette
méthode ne peut être utilisée à l'échelle du système
solaire et à fortiori à plus grande échelle puisque, toutes les
mesures s'effectuant sur Terre, on ne peut mesurer directement les trois
angles internes d'un triangle dont les sommets se trouvent, à part la
Terre, sur deux planètes ou deux étoiles quelconques. Dans ce cas nous
concluons à l'applicabilité de la géométrie euclidienne en
nous fondant sur des données indirectes ― la concordance des
différents résultats obtenus par la mise en oeuvre de cette
géométrie. On peut, par exemple, prédéterminer par le calcul
le mouvement des planètes du système solaire pour plusieurs années
et vérifier ensuite la validité des résultats. Au cas où les
résultats du calcul seraient erronés, une des raisons en pourrait
être l'inadéquation de la géométrie d'Euclide à des
espaces d'étendue comparable à celle du système solaire. Par
contre, l'accord entre calcul et observation (ce qui est le cas effectivement)
témoigne de ce qu'il n'y a pas de raison de mettre en doute la
validité de la géométrie euclidienne. Sans plus nous attarder sur
cette question, nous noterons simplement que cette géométrie ne laisse
pas apparaître d'écarts notables dans des régions de l'espace de
la taille de notre *Galaxie* ($\sim 10^{20}  \text{ m}$) ou même de
celle de la *Métagalaxie* qui est la région de l'Univers que
l'on arrive à observer à l'aide des plus puissants télescopes
($\sim 10^{26}  \text{ m}$). De même il n'y a aucune raison de mettre en
doute la géométrie euclidienne lorsqu'il s'agit d'étendues
subatomiques, de l'ordre de $10^{- 15}  \text{ m}$.

Dans les mesures de la position des corps lointains les rayons lumineux
assument la fonction d'objets matériels constituant le référentiel
réel. Comme on ne peut construire des tiges indéfiniment longues,
elles ne peuvent servir à marquer les axes de coordonnées
s'étendant loin dans l'espace. Ce rôle est alors assumé par les
rayons lumineux qui prolongent au loin les axes de coordonnées
initialement réalisés en tiges rigides.

**5.** Ces considérations appellent à faire quelques remarques
sur les liens entre physique et mathématiques. Les mathématiques
jouent un rôle tellement important en physique que sans mathématiques
celle-ci est impensable. Il importe cependant de situer correctement la place
des mathématiques en physique ; cette question nous semble à tel point
importante que nous y reviendrons à de nombreuses occasions. Les
mathématiques pures ont affaire à des objets et à des notions
abstraits qui sont régis par une axiomatique. La seule condition à
laquelle doivent satisfaire les notions et les axiomes des mathématiques
est celle d'être *logiquement consistants*. Les mathématiques
pures tirent tous leurs résultats de ces axiomes à l'aide de
raisonnements logiques fondés sur les règles de la logique formelle.
Il est bien évident que le contenu de ces résultats ne saurait
dépasser le cadre des liens logiques existant entre les divers objets et
notions des mathématiques pures. On peut dire que les mathématiques
pures constituent une *discipline logiquement cohérente*. Formant
un système clos où tout est logiquement cohérent, les
mathématiques ont leur esthétique propre à laquelle les
mathématiciens sont sensibles.

On ne doit cependant pas perdre de vue que les mathématiques pures,
formant de par leur rigueur même un domaine fermé sur lui-même,
sont détachées du monde réel et ne peuvent être directement
mises en œuvre dans d'autres sciences ou dans la pratique humaine. Afin
que les mathématiques puissent constituer un puissant appareil d'étude
et de description des phénomènes naturels, il faut établir des
liens entre les objets et notions abstraits des mathématiques d'une part
et les objets et les phénomènes naturels d'autre part. En physique les
objets et les notions mathématiques doivent figurer non comme des
catégories purement logiques, mais comme des *abstractions d'objets
réels ou de processus naturels*. Ainsi le point est l'abstraction d'un
corps physique de faible étendue, la ligne droite est l'abstraction d'une
tige rigide de faible section ou celle d'un faisceau lumineux se propageant
dans un milieu homogène. La question de la légitimité des
mathématiques se réduit a celle de ses axiomes. Or la
légitimité des axiomes ne peut être établie que par
l'expérience.

Il est vrai qu'on ne peut soumettre à l'expérimentation les objets
mathématiques eux-mêmes, puisque ce sont des objets idéalisés
que l'on ne trouve pas dans la Nature. Toute expérience porte sur des
objets réels. La rigueur mathématique dont sont tellement satisfaits,
et à juste titre, les mathématiciens, doit être
interprétée comme la concordance logique des conclusions auxquelles on
parvient et non comme une justification de ses axiomes.

La seule rigueur mathématique ne peut suffire à la physique ou toute
autre science ayant affaire à des objets réels et a des
phénomènes naturels. *Aucune étude théorique, même
si elle est mathématiquement rigoureuse, ne peut être
considérée comme étant physiquement rigoureuse*, et ce pour les
raisons suivantes. Premièrement, toute recherche ou étude se fonde sur
certaines lois dont la validité est en dernière instance toujours
vérifiée par l'expérience&nbsp;; or toute expérimentation et toute
mesure physique sont entachées d'erreurs et ne sont effectuées qu'avec
un certain degré de précision. Au-delà du degré de
précision atteint dans une expérience, la loi physique concernée
peut cesser d'être juste. Deuxièmement, tout objet physique réel
possède une infinité de déterminations. Il est impossible
d'expliciter toutes les déterminations d'un objet réel, d'une part
parce qu'elles sont en nombre infini, et d'autre part, parce qu'on les ignore.
*En construisant ses théories, le physicien substitue aux objets
réels leurs modèles idéalisés qui reposent sur un nombre
restreint de déterminations explicites et essentielles pour traiter le
problème étudié. Seule l'expérimentation permet de décider
du choix des déterminations faites pour passer de l'objet réel à
son modèle. C'est toujours l'expérience qui tranche la question de la
justesse d'une théorie physique et des limites de sa validité*. Toute
mise en œuvre d'une loi physique en dehors de son domaine de validité
et d'un modèle ne spécifiant pas l'ensemble des
déterminations de l'objet réel qui importent pour une étude
donnée, conduit à des vices théoriques qui ne sauraient être
corrigés par des raisonnements et des calculs mathématiques, aussi
rigoureux soient-ils.

Cette assertion importe aussi pour la pratique. Il est bien évident qu'une
fois le modèle construit, il n'est pas interdit d'effectuer les calculs
ultérieurs avec toute la rigueur mathématique, même si les lois
physiques pertinentes ne sont qu'approximatives. Mais bien souvent le calcul
rigoureux est trop encombrant et trop ardu pour être effectué. Le
degré de précision auquel il tend est déjà dévalorisé
par le caractère approximatif des lois physiques et par l'imperfection du
modèle théorique servant de base aux calculs. Dans cette situation on
peut et on doit même avoir recours au calcul approché. Un calcul
approché est tout aussi valable qu'un calcul dit exact, à condition
que les erreurs qu'il introduit ne dépassent pas les erreurs dues aux
imperfections des lois physiques et des modèles théoriques.

Nombre de notions et de découvertes que les mathématiciens estiment
primordiales sont dénuées de sens lorsqu'il s'agit de les appliquer
à des objets réels. Un exemple en est le nombre irrationnel. Dire
qu'une grandeur physique a une valeur irrationnelle est un contresens
puisqu'une telle assertion ne peut être vérifiée. Les nombres
rationnels suffisent amplement pour représenter les résultats des
mesures avec toute la précision requise. En outre, la notion même de
grandeur physique perd toute sa signification lorsqu'on impose que sa mesure
soit effectuée à un degré de précision injustifié. Ainsi,
par exemple, on ne saura plus de quoi il s'agit si on mesure la longueur d'une
tige rigide, à un atome près. Une précision illimitée de la
mesure des longueurs est en principe utile pour les segments de droite
considérés en géométrie mais ne l'est plus pour les corps
réels caractérisés par une structure atomique.

## §2. Description cinématique du mouvement. Le concept du point matériel

## §3. Vitesse et accélération dans le cas du mouvement rectiligne. Vitesse et accélération angulaires

<a name="eq-3-4"></a>
$$
\dot{x} = \dif{x} = \lim_{\Delta t \to 0} \dfrac{\Delta x}{\Delta t}  \hspace{1cm} \text{(3.4)}
$$

## §4. Vitesse et accélération dans le mouvement curviligne

## §5. Limites de validité de la description classique du mouvement {#sec-05}

*En mécanique classique on caractérise, à tout instant, l’état de mouvement d'une particule par sa position* (coordonnée $x$ pour le mouvement rectiligne) *et par sa vitesse* . À la place de la vitesse on peut utiliser également l'impulsion $p=mv$, grandeur égale au produit de la masse de la particule $m$ par sa vitesse[^2]. L’image d’une particule élémentaire est le point géométrique qui décrit dans le temps une trajectoire continue. On démontre en mécanique quantique que ce procédé de description du mouvement a en principe une application limitée. Il est encore prématuré de s’engager dans une discussion de cette question, mais on peut donner ici un exposé succinct du résultat fondamental auquel conduit la mécanique quantique, sans le justifier d’aucune manière.  
*Selon la mécanique quantique, l'état d'une particule ne peut être caractérisé à aucun moment par les valeurs précises de sa coordonnée et de son impulsion instantanées*. Si on connaît, pour un certain état de la particule, la valeur de sa coordonnée avec une incertitude $\delta x$ et celle de son impulsion avec une incertitude $\delta p$, il est impossible de rendre simultanément ces deux quantités aussi petites que l’on veut, car elles sont liées l’une à l’autre par la relation <a id="eq-5-1"></a>
$$
\delta x \cdot \delta p \geqslant h  \hspace{1cm} \text{(5.1)}
$$
où $h$ est une constante universelle appelée *constante de Planck* (1858-1947). Cette constante joue un rôle de premier plan dans tous les phénomènes quantiques ; sa valeur numérique est <a id="eq-5-2"></a>
$$
h = \pu{6,63e-27 erg}  \hspace{1cm} \text{(5.2)}
$$
La relation ([5.1](#eq-5-1)) exprime le *principe d'incertitude de Heisenberg* (né en 1901) qui fixe une limite de principe à la précision d’une mesure simultanée de la coordonnée et de l’impulsion d’une particule ; cette limite ne peut être dépassée par aucun perfectionnement des appareils et des procédés de mesure. Il ne s’agit pas ici des erreurs de mesure, car c’est une manifestation de la nature des particules réelles dont les caractéristiques instantanées de mouvement ne se laissent pas déterminer par le procédé classique, c’est-à-dire par des valeurs exactes de leurs coordonnées et impulsions. Les particules ont un comportement plus compliqué que celui des points matériels de la mécanique classique. L’image classique du mouvement suivant des trajectoires continues ne reflète qu’approximativement les lois de la Nature. Les limites de validité de la mécanique classique sont fixées par la relation d’incertitude ([5.1](#eq-5-1)) selon laquelle l’état de mouvement d’une particule ne peut être décrit à un instant donné par des valeurs parfaitement exactes de sa coordonnée et de sa vitesse. Les indéterminations de ces grandeurs doivent satisfaire à la condition <a id="eq-5-3"></a>
$$
\delta x \cdot m\\, \delta v \geqslant h \hspace{1cm} \text{(5.3)}
$$
Pour des corps macroscopiques le procédé de description classique ne saurait être mis en doute. Supposons, par exemple, qu’il s’agisse du mouvement d’une bille ayant une masse $m=\pu{1 g}$. Dans les conditions usuelles la position de la bille peut être déterminée à $\pu{0,1}$ ou $\pu{0,01 mm}$ près. Plus généralement il serait dénué de sens de vouloir préciser la position de la bille avec une précision inférieure à la dimension de l’atome. On posera donc $\delta x = \pu{10^{-8} cm}$. L’application de la relation d’incertitude ([5.1](#eq-5-1)) donne alors
$$
\delta v \geqslant \dfrac{\pu{6,63e-27}}{10^{-8}} \approx \pu{10^{-18} cm/s}
$$
Comme les quantités $\delta x$ et $\delta v$ sont toutes deux et simultanément très petites, on en conclut que le procédé classique est pratiquement utilisable pour la description du mouvement des corps macroscopiques. Il en va tout autrement avec les phénomènes atomiques qui impliquent des particules de très petites masses et se produisent dans de très petites régions de l’espace. Considérons, par exemple, le mouvement de l’électron dans l’atome d’hydrogène. La masse de l’électron est $m=\pu{9,11e-28 g}$. L’erreur commise dans la détermination de la position de l’électron ne doit pas être supérieure à la dimension de l’atome, donc on doit avoir $\delta x < \pu{10^{-8} cm}$. On tire alors de la relation d’incertitude
$$
\delta v > \dfrac{h}{m\\, \delta x} = \dfrac{\pu{6,63e-27}}{\pu{9,11e-28} \times 10^{-8}} \approx \pu{7e8 cm/s}
$$
L’incertitude sur la valeur de la vitesse est déjà plus grande que la vitesse de l’électron au sein de l’atome, qui est égale à $\pu{10^8 cm/s}$. Dans cette situation la description classique du mouvement est dénuée de sens.

## §6. Sur la signification de la dérivée et de l'intégrale en physique

**1.**  Le procédé de passage à la limite ([3.4](#eq-3-4)) qui sert à définir la
    dérivée porte le nom de *dérivation.* La notion de dérivée est d'un
    emploi courant en mécanique et dans les autres domaines de la
    physique. C'est précisément l'étude du problème de la détermination
    de la vitesse d'un mouvement arbitraire qui a conduit Newton à
    définir la notion de dérivée ; Newton et Leibniz (1646-1716) sont
    les fondateurs du calcul différentiel et intégral. La notation
    $\dif{x}$ de la dérivée fut introduite par
    Leibniz. En mathématiques le symbole $\dif{x}$
    doit être pris comme une entité et non comme le rapport de deux
    accroissements « infiniment petits » $dx$ et $dt$.
    La signification de la dérivée
    $\dot{x} = \dif{x}$ est définie par la relation
    ([3.4](#eq-3-4)). Pour arriver à la dérivée on commence par former le rapport
    des accroissements finis $d\frac{\Delta x}{\Delta t}$, $\Delta t$
    étant différent de zéro. Ensuite, mettant en œuvre des
    transformations convenables de ce rapport ou tout autre moyen, on
    doit déterminer la limite de ce rapport. Mais on ne peut en aucun
    cas concevoir qu'on effectue d'abord un passage à la limite de
    $\Delta x$ et de $\Delta t$ aux quantités « infiniment petites »
    $dx$ et $dt$ et qu'après on forme le rapport
    $\dif{x}$ de ces différentielles. Néanmoins
    c'est cette approche qui était en vigueur tout au début du
    développement du calcul différentiel ; notons qu'elle ne peut
    satisfaire à la condition de clarté des concepts mathématiques et
    est complètement dénuée de sens, bien que l'on puisse déterminer les
    différentielles $dx$ et $dt$ de manière que leur
    rapport devienne égal à la dérivée $\dot{x}$. En mathématiques on
    définit la différentielle $dt$ comme un accroissement
    arbitraire de la variable $t$, et la différentielle $dx$ de
    la fonction $x(t)$ par la relation $dx = \dot{x}\\,dt$. Avec cette
    dernière définition l'assertion que la dérivée est le rapport de
    deux quantités finies $dx$ et $dt$ devient évidente,
    puisque c'est une autre manière d'exprimer une notion. *La notion
    primaire est toujours celle de dérivée et non de la différentielle*.

Néanmoins dans les applications des mathématiques à la physique, on doit
tenir compte de ce que la connaissance des grandeurs physiques résulte
en fin de compte de mesures concrètes qui sont toutes entachées
d'erreurs et perturbent l'évolution naturelle des phénomènes. C'est
cette circonstance qui, en toute rigueur, ne permet pas de mettre en
œuvre le passage à la limite $\Delta t \rightarrow 0$,
$\Delta x \rightarrow 0$, qui en mathématiques conduit à la définition
de la dérivée. Supposons, par exemple, que l'on cherche à mesurer la
vitesse dans l'air d'une balle tirée par une arme à feu. Il s'agit de
mesurer la distance $\Delta x$ que parcourt la balle dans l'intervalle
de temps $\Delta t$. Si on prend un intervalle de temps $\Delta t$ trop
long, la vitesse de la balle peut diminuer notablement du fait de la
résistance de l'air, et le rapport $\dfrac{\Delta x}{\Delta t}$ peut
avoir une valeur plus petite que la vitesse réelle de la balle à
l'instant considéré. Si on diminue $\Delta t$ on remarquera qu'à partir
d'une certaine valeur, le rapport $\dfrac{\Delta x}{\Delta t}$ reste
constant, aux erreurs expérimentales près, abstraction faite des erreurs
fortuites. Il est inutile de réduire davantage $\Delta t$ car alors le
rapport recommencera à varier et ce d'une façon de plus en plus
irrégulière ; ce rapport prendra toutes sortes de valeurs, grandes ou
très petites. Cela tient à ce que l'erreur relative de toute mesure est
d'autant plus grande que la grandeur mesurée est petite. Il est, par
exemple, assez facile de mesurer une longueur de $\pu{1 m}$ à $\pu{1 mm}$ près, donc
avec une précision relative de 1/1000. Mais mesurer avec cette même
précision relative une longueur de $\pu{1 mm}$ est beaucoup plus difficile.
Plus $\Delta t$ est petit, plus l'erreur commise dans le calcul de
$\dfrac{\Delta x}{\Delta t}$ est grande. Même si on diminuait
indéfiniment $\Delta t$, les valeurs calculées de
$\dfrac{\Delta x}{\Delta t}$ ne tendraient pas vers une limite
déterminée. Ces remarques montrent que dans notre exemple, du fait des
erreurs de mesure, on ne peut réaliser le passage à la limite
$\Delta t \rightarrow 0$ dans son sens mathématique. Partant des
résultats de mesures physiques, on ne peut calculer la vitesse vraie ou
la dérivée $v = \dot{x}$ que de façon approchée, en l'identifiant au
rapport des accroissements finis $\dfrac{\Delta x}{\Delta t}$.
L'intervalle de temps $\Delta t$ optimum, pour lequel la précision du
calcul de la vitesse vraie serait la meilleure, ne se laisse déterminer
qu'en tenant compte des conditions concrètes. Les accroissements petits
mais finis $\Delta x$ et $\Delta t$, dont le rapport fournit avec une
approximation suffisante la valeur de la dérivée $\dot{x}$, sont pour le
physicien des infiniment petits ou plus précisément des quantités
physiquement infiniment petites. Le physicien les désigne par
$dx$ et $dt$ et les traite comme des différentielles du
mathématicien. Ainsi, *en physique, la dérivée apparaît comme le rapport
des accroissements finis et petits de la variable et de la fonction et
non comme la limite de ce rapport.*

Ce ne sont pas seulement les erreurs de mesures qui s'opposent à ce que
soit réalisé dans la pratique le passage à la vraie limite mathématique
; il se peut aussi que ce passage à la limite soit impossible par
principe, pour des raisons inhérentes à la nature des grandeurs ou des
lois de la physique. Ainsi, par exemple, un passage à la limite ne peut
être rigoureux en vertu de la relation d'incertitude ([5.1](eq-5-1)). Si, en
effet, l'intervalle de temps $\Delta t$ tend vers zéro, le chemin
parcouru $\Delta x$ tendra aussi vers zéro. L'indétermination
$\delta x$ dans la mesure du chemin parcouru ne doit pas dépasser
$\Delta x$, sinon le calcul de la vitesse moyenne par application de la
formule $v_{\text{moy}} = \dfrac{\Delta x}{\Delta t}$ serait dénué de
sens. Ainsi lorsque $\Delta t \rightarrow 0$ l'indétermination sur la
coordonnée $\delta x$ doit tendre aussi vers zéro. Mais selon la
relation ([5.1](eq-5-1)) l'indétermination sur la vitesse $\delta v$ doit
tendre alors vers l'infini, ce qui signifie que l'erreur que nous
commettons en appliquant la formule ([3.3](eq-3-3)) pour calculer la vitesse $v$
est infiniment grande comparativement à la vitesse du mobile $v$.

**6.**  Ces considérations s'appliquent non seulement à la dérivée de la
    coordonnée, mais aussi aux dérivées de toutes les autres grandeurs
    physiques. Soit à déterminer, par exemple, la densité d'une
    substance en un point de l'espace. Pour ce faire nous pouvons
    procéder comme suit. Entourons le point choisi par une surface
    fermée délimitant un volume $\Delta V$. Soit $\Delta m$ la masse de
    substance contenue dans ce volume. Le rapport

$$\rho_{\text{moy}} = \dfrac{\Delta m}{\Delta V}$$

est appelé *densité moyenne de la substance dans le volume* 
$\Delta V$. Comme la densité moyenne dépend, en général, de la
dimension et de la forme du volume $\Delta V$, on introduit la notion de
*densité vraie* de la substance que l'on détermine en faisant tendre
$\Delta V$ vers zéro. On dit alors que la densité moyenne
$\rho_{\text{moy}}$ tend vers une limite déterminée $\rho$ qui est la
densité vraie de la substance au point considéré de l'espace :<a id="eq-6-1"></a>

$$
\rho = \lim_{\Delta V \rightarrow 0}\\, \dfrac{\Delta m}{\Delta V} = \dfrac{\text{d}m}{\text{d}V}  \hspace{1cm} \text{(6.1)}
$$

La *densité vraie est donc définie comme la dérivée de la masse par
rapport au volume.* Elle ne dépend que de la position du point concerné.
Si cependant on voulait appliquer à la formule ([6.1](#eq-6-1)) le concept de
passage à la limite dans le sens mathématique rigoureux, on ne pourrait
le faire du fait de la structure atomique de la matière. À mesure que
l'on ferait décroître le volume, il arriverait un moment où ce volume
n'engloberait qu'un petit nombre de molécules, une par exemple, ou même
aucune. D'autre part, comme les molécules sont animées de mouvements
d'agitation thermique désordonnés, certaines molécules s'échappent du
volume $\Delta V$, d'autres y pénètrent. Par suite, le nombre de
molécules contenues dans un petit volume $\Delta V$ invariable varie
rapidement et de manière désordonnée. Aussi lorsqu'on diminue le volume
$\Delta V$, le rapport $\dfrac{\Delta m}{\Delta V}$ subira des variations
rapides entre la valeur zéro, si le volume $\Delta V$ ne contient aucune
molécule, et une très grande valeur si ce même volume contient une ou
plusieurs molécules. Il est clair que si on diminue indéfiniment le
volume $\Delta V$, le rapport $\dfrac{\Delta m}{\Delta V}$ ne tendra pas
vers une limite bien déterminée. On en conclut que pour déterminer la
densité vraie d'une substance, on ne doit pas rendre les quantités
$\Delta m$ et $\Delta V$ infiniment petites. Le volume $\Delta V$ doit
être macroscopique et contenir donc un très grand nombre de molécules,
tout en étant suffisamment petit pour que l'on puisse considérer la
substance qu'il renferme comme macroscopiquement homogène. Si on
satisfait à ces deux conditions, le rapport $\dfrac{\Delta m}{\Delta V}$
prendra une valeur bien déterminée ne changeant pas si on diminue encore
le volume macroscopique $\Delta V$. C'est ce rapport que nous assimilons
en physique à la dérivée de la masse $m$ par rapport au volume $V$. Les
quantités $\Delta m$ et $\Delta V$ qui satisfont aux deux conditions
ci-dessus sont considérées en physique comme des quantités *physiquement
infiniment petites*, et le physicien les assimile aux différentielles du
mathématicien. Du point de vue des mathématiques, cela revient à
substituer au corps réel un modèle idéalisé avec une répartition
continue de la masse.

**7.**  La situation est exactement la même en ce qui concerne la notion
    d'intégrale. En mathématiques l'intégrale est définie par le passage
    à la limite

$$\int_{a}^{b}{f\left( x \right)\ dx = \lim_{\Delta x_{i} \rightarrow 0}{\sum_{}^{}{f\left( x_{i} \right)\text{\ Δ}x_{i}}}}$$

L'intervalle numérique $(a, b)$ est divisé en $n$ intervalles plus
petits $\Delta x_{1}, \Delta x_{2}, \ldots, \Delta x_{n}$. La
longueur de chaque intervalle $\Delta x_{i}$ est multipliée par la
valeur que prend la fonction $f(x)$ en un point quelconque situé à
l'intérieur du petit intervalle des valeurs de la variable. Ensuite on
forme la somme $\sum_{}^{}{f\left( x_{i} \right)\\, \Delta x_{i}}$ et on
passe à la limite $n \rightarrow \infty$ en admettant que la longueur de
chacun des petits intervalles tend vers zéro. Mais en physique, par
suite d'erreurs de mesure ou de questions de principe (telles que la
nature atomique de la matière), la subdivision de l'intervalle $(a, b)$
en des intervalles plus petits qu'une certaine longueur (dépendant de
conditions concrètes) est dénuée de sens. Il s'ensuit que le passage à
la limite $\Delta x_{i} \rightarrow 0$ ne peut être entièrement réalisé
et doit s'arrêter à une certaine valeur. Ainsi, *en physique,
l'intégrale apparaît non comme la limite d'une somme, mais comme la
somme d'un grand nombre de termes suffisamment petits*
$\sum_{}^{}{f\left( x_{i} \right)\ \Delta x_{i}}$.

## §7. Remarques sur les vecteurs et la composition des mouvements

## §8. Degrés de liberté et coordonnées généralisée


[^2]: Nous supposons que le lecteur est déjà familier avec le concept de masse. Les concepts de masse et d’impulsion sont interprétés en détail au [§10]({{% ref "chap-02-les-lois-de-newton.md#sec-10" %}}).