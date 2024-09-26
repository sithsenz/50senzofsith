# Bayesian in Python
*Last updated 2024-09-26*

## Bayesian Theorem
The Bayesian Theorem is the foundation of Bayesian analysis. It allows us to update the probability of a hypothesis (event A) given new evidence (event B). In this article, three key forms of the theorem are presented:
### Theorem 1
This is the basic formula for conditional probability. It tells us how to find the probability of A happening given that B has happened by using the joint probability of A and B.
>$$P(A | B) = \frac{P(A \cap B)}{P(B)}$$

### Theorem 2 (Bayes' Theorem)
This is Bayes' Theorem, which is essential in Bayesian inference. It shows how the `P(A)` (the prior probability) can be updated given new evidence B. The term `P(B∣A)` is the likelihood, which describes how likely it is to observe B given that A is true. The denominator `P(B)` normalizes the result and ensures that the updated probability (posterior) is valid.
>$$P(A | B) = \frac{P(B | A) \times P(A)}{P(B)}$$

### Theorem 3 (Law of Total Probability)
This theorem helps in computing the overall probability of A by considering all possible events $B_i$​ that could lead to A. Each $B_i$​ represents a different scenario, and their probabilities are weighted by how likely they are.
>$$P(A) = \sum_i P(A | B_i) \times P(B_i)$$

## Cookies Problem
The Cookies Problem is a well-known Bayesian puzzle designed to show how Bayes’ Theorem works in practice. In this problem, we have two bowls with different proportions of chocolate and vanilla cookies. Bowl 1 contains 30 chocolate cookies and 10 vanilla cookies, while Bowl 2 contains 20 chocolate cookies and 20 vanilla cookies.

The goal is to determine the probability that a chocolate cookie came from Bowl 1, given that a chocolate cookie was selected.
$P(\text{bowl}_1 | \text{cookies}_c)$

```mermaid
---
title: Cookies Problem
---
flowchart LR
  bowl_1(bowl 1)
  bowl_2(bowl 2)
  bowl_1---choco_30(30 chocolate)
  bowl_1---van_10(10 vanilla)
  bowl_2---choco_20(20 chocolate)
  bowl_2---van_20(20 vanilla)
```

### Solution: By Diagram
![venn_cookies](images/venn_cookies.png "Venn's diagram illustrating the Cookies problem")

We start with a visual representation of the problem using a Venn diagram. The diagram illustrates the relationship between the two bowls and the distribution of chocolate and vanilla cookies.

The probability that a chocolate cookie was chosen from Bowl 1 can be simply calculated by:
>$$P(\text{bowl}_1 | \text{cookies}_c) = \frac{30}{30 + 20} = \frac{3}{5}$$

This quick method gives a straightforward answer, but it assumes that we already know some of the probabilities, such as the total number of chocolate cookies in both bowls.

### Solution: By Formula
To arrive at the same answer using Bayes' Theorem:
>$$P(\text{bowl}_1 | \text{cookies}_c) = \frac{P(\text{cookies}_c | \text{bowl}_1) \times P(\text{bowl}_1)}{P(\text{cookies}_c)}$$

We calculate the likelihood that a chocolate cookie came from Bowl 1 as $P(\text{cookies}_c ∣ \text{bowl}_1) = \frac{30}{30+10}$​, the prior probability that the cookie came from Bowl 1 as $P(\text{bowl}_1) = \frac{1}{2}$​, and the marginal probability of selecting a chocolate cookie from either bowl $P(\text{cookies}_c)$ as a weighted sum of the probabilities of choosing a chocolate cookie from each bowl.

Thus:
>$$P(\text{bowl}_1 | \text{cookies}_c) = \frac{\frac{30}{30 + 10} \times \frac{1}{2}}{\frac{30}{30 + 10} \times \frac{1}{2} + \frac{20}{20 + 20} \times \frac{1}{2}} = \frac{3}{5}$$

This more rigorous approach shows how Bayes' Theorem calculates posterior probabilities using evidence.

```python
from fractions import Fraction as frac

p_c_b1: frac = frac(30,(30+10))
p_b1: frac = frac(1, 2)
p_c: frac = frac((30+20), (30+10+20+20))

p_b1_c: frac = p_c_b1 * p_b1 / p_c
print(p_b1_c)
```

>Fraction(3, 5)

### Solution: By Bayes Table
In this approach, we construct a Bayes table, which is another useful method to solve Bayesian problems systematically.
1. First list the priors: the initial probability of each bowl, $\frac{1}{2}$​ for both.
2. Then, add the likelihoods: the probability of drawing a chocolate cookie from each bowl. For Bowl 1, it's $\frac{30}{40}$​, and for Bowl 2, it's $\frac{20}{40}$​.
3. The numerator for each row is the product of the prior and the likelihood.
4. Normalize by dividing by the sum of the numerators, which gives the posterior probabilities.

```python
import pandas as pd
from fractions import Fraction as frac

data: dict = {
  "bowl": ["bowl 1", "bowl 2"],
  "prior": [frac(1, 2), frac(1, 2)],
  "likelihood": [frac(30, 40), frac(20, 40)]
}

bayes_table: pd.DataFrame = pd.DataFrame(data)

bayes_table["numerator"] = bayes_table["prior"] * bayes_table["likelihood"]
normaliser: float = bayes_table["numerator"].sum()
bayes_table["posterior"] = bayes_table["numerator"] / normaliser

print(bayes_table)
```

>| | bowl   | prior | likelihood | numerator | posterior |
>|-|:------:|:-----:|:----------:|:---------:|:---------:|
>|0| bowl 1 | 1/2   | 3/4        | 3/8       | 3/5       |
>|1| bowl 2 | 1/2   | 1/2        | 1/4       | 2/5       |

The table shows the posterior probabilities as $\frac{3}{5}$ for Bowl 1 and $\frac{2}{5}$ for Bowl 2, confirming the previous calculations.

### Solution: By empiricaldist.Pmf
The `empiricaldist` Python library is another method that we could use. Here, we create a prior distribution (which assumes both bowls are equally likely) and multiply it by the likelihood of selecting a chocolate cookie from each bowl. After normalizing the results, we get the same posterior probabilities: 60% (0.6) for Bowl 1 and 40% (0.4) for Bowl 2.

```python
import numpy as np
from empiricaldist import Pmf

prior: Pmf = Pmf.from_seq(["bowl 1", "bowl 2"])
likelihood_chocolate: np.ndarray = np.array([30/40, 20/40])
posterior: Pmf = prior * likelihood_chocolate
posterior.normalize()
print(posterior)
```

><table>
>  <tr>
>    <td>bowl 1</td>
>    <td>0.6</td>
>  </tr>
>  <tr>
>    <td>bowl 2</td>
>    <td>0.4</td>
>  </tr>
></table>

This approach is useful for practical coding implementations where distributions and normalizing operations are needed.

### Solution: By PyMC (Approximation)
We also see how to use PyMC, a probabilistic programming framework, to solve the problem. This method uses sampling to estimate the posterior probability through approximation.
1. Define a prior distribution: there’s a 50% chance that the cookie came from Bowl 1.
2. Set up the conditional likelihood based on which bowl the chocolate cookie might have come from.
3. Using Monte Carlo sampling, simulate the posterior probability distribution.

```python
import pymc as pm

prob_bowl_1: float = 1 / 2
choco_likeli_bowl_1: float = 30 / 40
choco_likeli_bowl_2: float = 20 / 40

with pm.Model() as model_choco:
  # prior
  bowl_1 = pm.Bernoulli("bowl_1", p=prob_bowl_1)
  
  # conditional likelihood
  choco_likelihood = pm.Deterministic(
      "choco_likelihood",
      pm.math.switch(bowl_1, choco_likeli_bowl_1, choco_likeli_bowl_2)
  )

  # observation
  pm.Bernoulli("obs", p=choco_likelihood, observed=1)
  
  # inference
  ichoco = pm.sample()

print(az.summary(ichoco, round_to=3, kind="stats"))
```

|                  | mean  | sd    | hdi_3% | hdi_97% |
|:----------------:|:-----:|:-----:|:------:|:-------:|
| bowl_1           | 0.601 | 0.490 | 0.00   | 1.00    |
| choco_likelihood | 0.650 | 0.122 | 0.50   | 0.75    |

The results give a posterior of around 0.601 for Bowl 1, which closely matches the analytical solution.

The PyMC approach is beneficial when exact formulas become difficult to apply or when working with more complex models. It allows for Bayesian inference through simulations, offering an approximate but powerful solution.

## Summary of Methods
+ Diagram: A quick visual approach, useful for small problems.
+ Formula: The core application of Bayes’ Theorem.
+ Table: A systematic way to organize and solve Bayesian problems step-by-step.
+ `empiricaldist`: A practical implementation in Python for handling Bayesian distributions and probabilities.
+ `PyMC`: A probabilistic programming approach that handles more complex models with sampling.

## Conclusion

This article provides a clear, structured approach to understanding Bayesian inference through both mathematical theory and practical examples. The different methods of solving the Cookies Problem show the flexibility and applicability of Bayesian analysis. By demonstrating the same problem through multiple methods, including traditional formulas and modern probabilistic programming tools, we effectively illustrate how Bayesian thinking can be applied to a variety of problems, making it accessible for a wide audience, especially those working in Python and data analysis.

## References
+ [Bayesian Data Analysis 3rd Ed.](http://www.stat.columbia.edu/~gelman/book/)
+ Martin Osvaldo A, Bayesian Analysis with Python. Packt Publishing. 2024. ISBN 978-1-80512-716-1
+ [Think Bayes 2](http://allendowney.github.io/ThinkBayes2/index.html)

*[Table of Content](../index.md)*
