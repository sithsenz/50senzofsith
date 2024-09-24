# Bayesian in Python

## Bayesian Theorem

### Theorem 1
>$$P(A | B) = \frac{P(A \cap B)}{P(B)}$$

### Theorem 2
>$$P(A | B) = \frac{P(B | A) \times P(A)}{P(B)}$$

### Theorem 3
>$$P(A) = \sum_i P(A | B_i) \times P(B_i)$$

## Cookies Problem
Bowl 1 has 30 chocolate and 10 vanilla cookies. Bowl 2 has 20 chocolate and 20 vanilla cookies.

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

![venn_cookies](images/venn_cookies.png "Venn's diagram illustrating the Cookies problem")
