# Bayesian in Python

## Bayesian Theorem

### Theorem 1
>$$P(A | B) = \frac{P(A \cap B)}{P(B)}$$

### Theorem 2
>$$P(A | B) = \frac{P(B | A) \times P(A)}{P(B)}$$

### Theorem 3
>$$P(A) = \sum_i P(A | B_i) \times P(B_i)$$

## Cookies Problem

```mermaid
flowchart LR
  bowl---bowl1
  bowl---bowl2
  bowl1---choco1(30 chocolate cookies)
  bowl1---vanila1(10 vanila cookies)
  bowl2---choco2(20 chocolate cookies)
  bowl2---vanila2(20 vanila cookies)
```
