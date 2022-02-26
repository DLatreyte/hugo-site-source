---
title: "Comment obtenir une numérotation automatique des sections, de la table des matières avec Hugo"
subtitle: ""
author: ""
type: ""
date: 2020-08-22T11:09:39+04:00
draft: true
toc: true
tags: ["HowTo"]
categories: ["Hugo"]
image: ""
solution_est_visible: true
auto_numbering: true
---

## Étapes à suivre

La méthode introduite dans ce document s'appuie sur les propriétés des CSS.

Trois étapes :
- Modification du fichier `default.md` afin d'y ajouter la variable booléenne `auto_numbering` ;
- Ajout de l'appel à une nouvelle classe, `auto_numbering`, dans le modèle de page `single.html` ;
- Définition de la classe `auto_numbering`.

## Mise en œuvre

### Modification de l'entête du fichier `default.md` 

- Ajouter la ligne suivante au fichier `archetypes > default.md` :

{{% highlight yaml %}}
---
...
auto_numbering: true
...
---
{{% /highlight %}}

- Adapter la syntaxe si le langage choisi pour l'entête n'est pas YAML.
- Par défaut la numérotation est active. Il faut affecter le booléen `false` à la propriété `auto_numbering`, dans chaque article, pour la désactiver.

### Appel de la classe `auto_numbering` par chaque article

- Copier le fichier `nom_thème > layouts > _default > single.html` dans le dossier `layouts > _default` ;
- Éditer le fichier de sorte à ce qu'il appelle la classe `auto_numbering` lorsque c'est nécessaire :
{{% highlight html %}}
...
<article role="main" class="blog-post" {{- if .Param "auto_numbering" }} auto_numbering {{- end }} >
...
{{% /highlight %}}

**Remarque :** tous les thèmes n'utilisent pas une classe `bolg-post`, on rencontre aussi souvent `blog` mais cela ne change rien à l'ajout à réaliser.

En fonction de la valeur du booléen `auto_numbering` le code HTML peut donc être :

{{% highlight html %}}
...
<article role="main" class="blog-post" >
...
{{% /highlight %}}
ou 
{{% highlight html %}}
...
<article role="main" class="blog-post auto_numbering" >
...
{{% /highlight %}}

### Définition de la classe `auto_numbering` 

- Copier le fichier de style `nom_thème > static > css > main.css` dans `static > css` (le nom peut varier en fonction du thème) ;
- Éditer le fichier et y ajouter à la fin la définition de la classe `auto_numbering` :

{{% highlight css %}}
/* Auto Numbering */
body {
  counter-reset: section;
}
h2 {
  counter-reset: subsection;
}

article[auto_numbering] h2:before {
  counter-increment: section; 
  content: counter(section) ". ";
}

article[auto_numbering] h3:before {
  counter-increment: subsection; 
  content: counter(section) "." counter(subsection) ". ";
}

article[auto_numbering] .toc__menu ul { 
  counter-reset: item ;
}

article[auto_numbering] .toc__menu li a:before { 
  content: counters(item, ".") ". "; 
  counter-increment: item ;
}
{{% /highlight %}}


