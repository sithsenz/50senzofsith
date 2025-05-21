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

but, $`PPV = \text{Post-Test Probability}`$  
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


*[Table of Content](../../index.md)*
