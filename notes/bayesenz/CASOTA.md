# Translating Clinical Threshold to Laboratory Performance Specifications
*Last updated 2025-05-20*

## Two Forms of the Theorem
### The Probability Form

<img src="images/AnB.png" width="400">

The usual way of presenting Bayesian Theorem.

```math
\begin{gather*}
\text{When P(A) and P(B) is not mutually exclusive:}\\
P(A \cap B) = P(A) \times P(B | A)\\
P(B \cap A) = P(B) \times P(A | B)\\
\end{gather*}
```
but,

```math
P(B \cap A) = P(A \cap B)
```

hence,

```math
P(B) \times P(A | B) = P(A) \times P(B | A)
```

```math
P(A | B) = \frac{P(A) \times P(B | A)}{P(B)}
```

In diagnostic testing, probability of Diseased (D+) when Test (T) is positive:
```math
P(D+ | T+) = \frac{P(D+) \times P(T+ | D+)}{P(T+)}
```

Probability of Not Diseased (D-) when Test (T) is positive:
```math
P(D- | T+) = \frac{P(D-) \times P(T+ | D-)}{P(T+)}
```

### The Odds Form
What is the odds that the patient has the disease when the test is positive?

```math
\begin{align*}
\frac{P(D+|T+)}{P(D-|T+)} &= \frac{\frac{P(D+) \times P(T+ | D+)}{P(T+)}}{\frac{P(D-) \times P(T+ | D-)}{P(T+)}}\\
\\
\frac{P(D+|T+)}{P(D-|T+)} &= \frac{P(D+) \times P(T+ | D+)}{P(D-) \times P(T+ | D-)}\\
\\
\frac{P(D+|T+)}{P(D-|T+)} &= \frac{P(D+)}{P(D-)} \times \frac{P(T+ | D+)}{P(T+ | D-)}\\
\end{align*}
```

In odds terms:

```math
\text{Post-Test Odds} = \text{Pre-Test Odds} \times \text{Likelihood Ratio}
```

Likelihood Ratio (LR) when Test is positive:
```math
LR_{T+} = \frac{P(T+ | D+)}{P(T+ | D-)}
```

but Sensitivity (Sn) is $`Sn = P(T+|D+)`$  
while, Specificity (Sp) is $`Sp = P(T-|D-)`$  
and, $`P(T+|D-) + P(T-|D-) = 1`$

```math
LR_{T+} = \frac{Sn}{1-Sp}
```

### Probability :arrows_counterclockwise: Odds
Probability :arrow_right: Odds
```math
\text{Probability} = \frac{\text{Odds}}{1 + \text{Odds}}
```

Odds ➡️ Probability
```math
\text{Odds} = \frac{\text{Probability}}{1 - \text{Probability}}
```

## Clinical Threshold
If the desired clinical threshold ie Positive Predictive Value (PPV) is set as $`\theta`$
```math
PPV \ge \theta
```

but, the desired $`PPV = \text{Post-Test Probability}`$  
then, $`\text{Post-Test Odds} = \frac{\theta}{1 - \theta}`$

```math
LR_{T+} \times \text{Pre-Test Odds} \ge \frac{\theta}{1 - \theta}
```

but, Pre-Test Probability = Prevalence, $`\rho`$  
then, $`\text{Pre-Test Odds} = \frac{\rho}{1 - \rho}`$  
hence,
```math
LR_{T+} \times \frac{\rho}{1 - \rho} \ge \frac{\theta}{1 - \theta}
```

```math
LR_{T+} \ge \frac{\theta}{1 - \theta} \times \frac{1 - \rho}{\rho}
```

## Algorithmic Testing
For disease with low prevalence, the required likelihood ratio would be too high for existing tests or assays.
For example, if prevalence, $`\rho = \frac{1}{100,000}`$ (or 0.00001) and the desired PPV, $`\theta \ge 0.99`$ (or 99%),
the calculated likelihood ratio, $`LR_{\text{desired}} \ge 9,899,901`$. This high LR is not achievable in practice.
```math
\begin{gather*}
LR_{\text{desired}} \ge \frac{0.99}{1 - 0.99} \times \frac{1 - 0.00001}{0.00001}\\
LR_{\text{desired}} \ge 9,899,901
\end{gather*}
```

### Test A, followed by Test B, followed by Test C
After testing with Test A, the post-test odds can be calculated like this:
```math
\begin{gather*}
\text{Post-Test Odds} = \text{Pre-Test Odds} \times \text{Likelihood Ratio}\\
O(D+:D-|A+) = O(D+:D-) \times LR_{A+}\\
\end{gather*}
```

If we follow up with Test B, the new post-test odds (after Test B) can be calculated as follow:
```math
\begin{gather*}
O(D+:D-|A+) \text{becomes the new pre-test odds for Test B}\\
O(D+:D-:B+) = O(D+:D-|A+) \times LR_{B+}\\
O(D+:D-|B+) = O(D+:D-) \times LR_{A+} \times LR_{B+}\\
\end{gather*}
```

Again, if we follow up with Test C, the new post-test odds (after Test C) can be calculated like this:
```math
\begin{gather*}
O(D+:D-|B+) \text{becomes the new pre-test odds for Test C}\\
O(D+:D-|C+) = O(D+:D-|B+) \times LR_{C+}\\
O(D+:D-|C+) = O(D+:D-) \times LR_{A+} \times LR_{B+} \times LR_{C+}\\
\end{gather*}
```

A pattern emerges whereby likelihood ratio (LR) is actually the product of LR of each tests ran in sequence.
```math
\begin{gather*}
\text{Post-Test Odds} = \text{Pre-Test Odds} \times \text{Likelihood Ratio}\\
\text{Post-Test Odds} = \text{Pre-Test Odds} \times (LR_{A} \times LR_{B} \times LR_{C} ... )\\
\end{gather*}
```

### Serial Testing
Hence, to achieve a high $`LR_{\text{desired}} \ge 9,899,901`$, we can implement a serial testing until $`LR_{T+} \ge LR_{\text{desired}}`$.
Let's take for example, Test A, B, and C, each with their own performance specifications as follow:
| Test  | Sn    | Sp    |
| :---: | :---: | :---: |
| A     | 99.9% | 99.7% |
| B     | 99.8% | 99.8% |
| C     | 99.7% | 99.9% |

Starts with Test A,
```math
\begin{align*}
LR_{A+} &= \frac{0.999}{1-0.997}\\
&= 333\\
\end{align*}
```
after initial testing with Test A, $`LR_{A+} < LR_{\text{desired}}`$

Proceeds to Test B,
```math
\begin{align*}
LR_{A+} \times LR_{B+} &= 333 \times \frac{0.998}{1-0.998}\\
&= 333 \times 499\\
&= 166,167\\
\end{align*}
```
after serial testing with Test A and Test B, $`LR_{A+,B+} < LR_{\text{desired}}`$

Proceeds to Test C,
```math
\begin{align*}
LR_{A+} \times LR_{B+} \times LR_{C+} &= 333 \times 499 \times \frac{0.997}{1-0.999}\\
&= 333 \times 499 \times 997\\
&= 165,668,499\\
\end{align*}
```
after serial testing with Test A, Test B and Test C, $`LR_{A+, B+, C+} > LR_{\text{desired}}`$

Hence, to achieve the desired clinical threshold of PPV, $`\theta \geq 0.99`$ in a population with very low prevalence, $`\rho = \frac{1}{100,000}`$,
the laboratory would need to perform 3 consecutive testing using Test A, Test B and Test C.

*[Table of Content](../../index.md)*
