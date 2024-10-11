# Is it fair?
*Last updated 2024-10-11*

250 coin flips, produces 140 heads and 110 tails. What is the probability that this coin comes up head?

## Solution by Bayes Table

From Bayes Theorem:
> $$P(\text{head | obs}) = \frac{P(\text{prior}) \times L(\text{head})}{\text{normaliser}}$$

Assuming *P(head) = h*, then *P(tail) = 1 - h* and a uniform prior *P(prior) = p*,

if first flip produced head,
> $$P(\text{head | (1,0)}) = \frac{p \times h^1 \times (1-h)^0}{\text{normaliser}}$$

similarly, if the second and third produced 1 head and 1 tail
> $$P(\text{head | (2,0)}) = \frac{p \times h^2 \times (1-h)^0}{\text{normaliser}}$$
> $$P(\text{head | (2,1)}) = \frac{p \times h^2 \times (1-h)^1}{\text{normaliser}}$$

hence,
> $$P(\text{head | (H,T)}) = \frac{p \times h^H \times (1-h)^T}{\text{normaliser}}$$

```python
import pandas as pd

head: int = 140
tail: int = 110

bayes_table: pd.DataFrame = pd.DataFrame({
    "hypo_prb": np.linspace(0, 1, 101),  # 0.00, 0.01, 0.02, ... 0.98, 0.99, 1.00
    "head_prior": 1/100,  # uniform probability of 0.01
    "likeli_head": np.linspace(0, 1, 101)  # 0.00, 0.01, 0.02, ... 0.98, 0.99, 1.00
})

bayes_table.set_index("hypo_prb", inplace=True)

bayes_table["numerator"] = (bayes_table["head_prior"] *
                            (bayes_table["likeli_head"]**head) *
                            (1 - bayes_table["likeli_head"])**tail)

normaliser: float = bayes_table["numerator"].sum()
bayes_table["head_posterior"] = bayes_table["numerator"] / normaliser

bayes_table["head_posterior"].plot()
```
![](images/bayes_table_plot.png "Bayes Table Plot")

