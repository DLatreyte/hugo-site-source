---
title: Math Sample
subtitle: Using KaTeX
date: 2017-03-05
tags: ["example", "math"]
draft: true
solution_est_visible: true
---

KaTeX can be used to generate complex math formulas server-side. 

$$
\phi = \frac{(1+\sqrt{5})}{2} = 1.6180339887\cdots
$$

Additional details can be found on [GitHub](https://github.com/Khan/KaTeX) or on the [Wiki](http://tiddlywiki.com/plugins/tiddlywiki/katex/).
<!--more-->

### Example 1

If the text between $$ contains newlines it will rendered in display mode:
```
$$
f(x) = \int_{-\infty}^\infty\hat f(\xi)\,e^{2 \pi i \xi x}\,d\xi
$$
```
$$
f(x) = \int_{-\infty}^\infty\hat f(\xi)\,e^{2 \pi i \xi x}\,d\xi
$$


### Example 2
```
$$
\frac{1}{\Bigl(\sqrt{\phi \sqrt{5}}-\phi\Bigr) e^{\frac25 \pi}} = 1+\frac{e^{-2\pi}} {1+\frac{e^{-4\pi}} {1+\frac{e^{-6\pi}} {1+\frac{e^{-8\pi}} {1+\cdots} } } }
$$
```
​​$$
\frac{1}{\Bigl(\sqrt{\phi \sqrt{5}}-\phi\Bigr) e^{\frac25 \pi}} = 1+\frac{e^{-2\pi}} {1+\frac{e^{-4\pi}} {1+\frac{e^{-6\pi}} {1+\frac{e^{-8\pi}} {1+\cdots} } } }
$$
​​ 

### Example 3
{{< highlight latex >}}
$$
1 +  \frac{q^2}{(1-q)}+\frac{q^6}{(1-q)(1-q^2)}+\cdots = \prod_{j=0}^{\infty}\frac{1}{(1-q^{5j+2})(1-q^{5j+3})}, \quad\quad \text{for }\lvert q\rvert<1.
$$
{{< / highlight >}}
$$
1 +  \frac{q^2}{(1-q)}+\frac{q^6}{(1-q)(1-q^2)}+\cdots = \prod_{j=0}^{\infty}\frac{1}{(1-q^{5j+2})(1-q^{5j+3})}, \quad\quad \text{for }\lvert q\rvert<1.
$$

And now let's talk about chemistry $\ce{CO2 + C -> 2 CO}$ and 

$$\ce{Hg^2+ ->[I-] HgI2 ->[I-] [Hg^{II}I4]^2-}$$

$\ce{1/2 H2O}$, $\ce{(NH4)2S}$, $\ce{[\{(X2)3\}2]^3+}$, $\ce{NH4^+}$

$$\ce{Zn^2+  <=>[+ 2OH-][+ 2H+]  $\underset{\text{amphoteres Hydroxid}}{\ce{Zn(OH)2 v}}$  <=>[+ 2OH-][+ 2H+]  $\underset{\text{Hydroxozikat}}{\ce{[Zn(OH)4]^2-}}$}$$

I want to write code, now :


```python
def add(x: float, y: float) -> float:
    """
    Addition de deux nombres.
    """
    return x + y
```

<details>
<summary>
<b>test</b>
</summary>

{{< highlight py3 "linenos=table,hl_lines=5" >}}
def add(x: float, y: float) -> float:
    """
    Addition de deux nombres.
    """
    return x + y
{{< / highlight >}}

</details>

----

> Partie qui doit être mise en évidence et une << Une petite citation >>.

> Alors voilà, ...

{{% solution "Solution" %}}

$$\ce{Zn^2+  <=>[+ 2OH-][+ 2H+]  $\underset{\text{amphoteres Hydroxid}}{\ce{Zn(OH)2 v}}$  <=>[+ 2OH-][+ 2H+]  $\underset{\text{Hydroxozikat}}{\ce{[Zn(OH)4]^2-}}$}$$

{{% / solution %}}

----

# Essais

{{% solution "Solution" %}}

{{< highlight py3 "linenos=table,hl_lines=5" >}}
def add(x: float, y: float) -> float:
    """
    Addition de deux nombres.
    """
    return x + y
{{< / highlight >}}

{{% / solution %}}

