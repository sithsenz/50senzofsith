# Bayesian Derivation of Diagnostic Test Requirements
#### Technical Derivations Supporting the CASOTA Framework
*Last updated 2025-05-22*

## Purpose of this Document
This document presents the mathematical foundation underlying the CASOTA (Clinically Acceptable State Of The Art) framework. It provides a step-by-step derivation of key formulas used to translate clinician-defined predictive value thresholds (such as PPV or NPV) into laboratory test performance requirements (sensitivity and specificity), using Bayes’ Theorem.

The content here is intended as a technical supplement to the CASOTA poster presentation. It focuses solely on the theoretical basis and derivations without clinical commentary or implementation guidance.

## 1. Bayes’ Theorem: Probability and Odds Forms
Bayes’ Theorem provides the foundational link between disease prevalence (pre-test probability), test characteristics (sensitivity and specificity), and the resulting predictive values (post-test probabilities).

There are two algebraically equivalent forms of Bayes’ Theorem that will be used throughout this document:

### 1.1 Probability Form
This is the classic form, expressing conditional probabilities directly:  
>$$P(A | B) = \frac{P(A) \times P(B | A)}{P(B)}$$

In the context of diagnostic testing:  
>$$P(D+ | T+) = \frac{P(D+) \times P(T+ | D+)}{P(T+)}$$

where:
- `P(D+ | T+)`: probability of disease given a positive test result (PPV)
- `P(T+ | D+)`: sensitivity
- `P(D+)`: d$iease prevalence
- `P(T+)`: m$aginal probability of a positive test

### 1.2 Odds Form
Rewriting the theorem in odds form is useful for evaluating serial tests and simplifying multiplicative relationships:
>1. Divide both posterior probabilities as fractions using Bayes’ Theorem  
>$$\frac{P(D+|T+)}{P(D-|T+)} = \frac{\frac{P(D+) \times P(T+ | D+)}{P(T+)}}{\frac{P(D-) \times P(T+ | D-)}{P(T+)}}$$
>
>2. Cancel out the common term `P(T+)`  
>$$\frac{P(D+|T+)}{P(D-|T+)} = \frac{P(D+) \times P(T+ | D+)}{P(D-) \times P(T+ | D-)}$$
>
>3. Group terms into Pre-Test Odds and Likelihood Ratio  
>$$\frac{P(D+|T+)}{P(D-|T+)} = \frac{P(D+)}{P(D-)} \times \frac{P(T+ | D+)}{P(T+ | D-)}$$

or more compactly:
>$$\text{Post-Test Odds} = \text{Pre-Test Odds} \times \text{Likelihood Ratio}$$

The Positive Likelihood Ratio can be rewritten in terms of sensitivity and specificity:
>1. Sensitivity, `Sn = P(T+|D+)`  
>2. Specificity, `Sp = P(T-|D-)`  
>3. `P(T+|D-) + P(T-|D-) = 1`  
>4. $$LR_{T+} = \frac{P(T+|D+)}{P(T+|D-)} = \frac{P(T+|D+)}{1-P(T-|D-)}$$

hence,
>$$LR_{T+} = \frac{Sn}{1-Sp}$$

### 1.3 Probability–Odds Conversion
To move between probability and odds representations:  
>From Odds to Probability:  
>$$\text{Probability} = \frac{\text{Odds}}{1 + \text{Odds}}$$  
>
>From Probability to Odds:  
>$$\text{Odds} = \frac{\text{Probability}}{1 - \text{Probability}}$$

## 2. Applying a Clinical Predictive Value Threshold
In diagnostic test evaluation, the post-test probability is often expressed as Positive Predictive Value (PPV).
When a minimum acceptable PPV is defined by clinical requirements, we can convert this into a minimum required
Likelihood Ratio (LR) using odds transformation.

### 2.1 Threshold-Based Requirements
Assuming that clinicians define a minimum acceptable PPV, say $$PPV \geq \theta$$, for a test result to be considered actionable.
>1. Since:  
>$$PPV = P(D+|T+) = \text{Post-Test Probability}$$  
>
>2. Convert this to post-test odds:  
>$$\text{Post-Test Odds} \geq \frac{\theta}{1 - \theta}$$  
>
>3. Using the odds form of Bayes’ theorem, the inequality for satisfying the PPV threshold becomes:  
>$$LR_{T+} \times \text{Pre-Test Odds} \geq \frac{\theta}{1 - \theta}$$  
>
>4. Pre-test odds can be derived from prevalence, ρ:  
>$$\text{Pre-Test Odds} = \frac{\rho}{1 - \rho}$$  
>$$LR_{T+} \times \frac{\rho}{1 - \rho} \geq \frac{\theta}{1 - \theta}$$  

So the requirement on the test's likelihood ratio becomes:
>$$LR_{T+} \ge \frac{\theta}{1 - \theta} \times \frac{1 - \rho}{\rho}$$

This inequality defines the minimum diagnostic strength needed from the test, as dictated by the prevalence
of disease and the clinician's acceptable predictive threshold.

## 3. Implications for Testing Strategy
### 3.1 Limitation of a Single Test
In low-prevalence settings, the required likelihood ratio can be extremely high. For example, if:
- Prevalence, $$\rho = \frac{1}{100,000}$$ or 0.00001
- Desired PPV, $$\theta \geq 0.99$$ or 99%

> Then,  
> $$LR_{\text{desired}} \geq \frac{0.99}{1 - 0.99} \times \frac{1 - 0.00001}{0.00001} = 9,899,901$$  

Such an LR is unattainable by any single diagnostic test currently available, regardless of high sensitivity and specificity.
This illustrates that when prevalence is very low, an extremely high likelihood ratio is required — often far beyond 
the capabilities of any single diagnostic test.

### 3.2 Serial Testing and the Multiplicative Property of LRs
In sequential or algorithmic testing, the result of one test updates the pre-test odds for the next.

>First Test (Test A)  
>Let $$O_0$$​ be the initial pre-test odds, derived from prevalence  
>$$O_A = O_0 \times LR_{A+}$$
>
>Second Test (Test B)  
>The post-test odds from Test A becomes the new pre-test odds for Test B  
>$$O_B = O_A \times LR_{B+} = (O_0 \times LR_{A+}) \times LR_{B+}$$  
>
>Third Test (Test C)  
>Continuing the sequence
>$$O_C = O_B \times LR_{C+} = (O_0 \times LR_{A+} \times LR_{B+}) \times LR_{C+}$$  
>
>General Form  
>By induction, for n serial tests:  
>$$O_n = O_0 \times (LR_{A+} \times LR_{B+} \times ... \times LR_{n+})$$

This derivation shows that likelihood ratios are multiplicative when diagnostic tests are applied in series,
each step refining the estimate of disease probability.

### 3.3 Worked Example
Continuing from 3.1, the required LR is impractically high for any single test. Now consider three tests in series:
<table>
  <th>
    <td>Test</td><td>Sn</td><td>Sp</td><td>LR</td>
  </th>
  <tr>
    <td>First Test</td><td>A</td><td>99.9%</td><td>99.7%</td><td>$$\frac{0.999}{1-0.997} = 333$$</td>
  </tr>
  <tr>
    <td>Second Test</td><td>B</td><td>99.8%</td><td>99.8%</td><td>$$\frac{0.998}{1-0.998} = 499$$</td>
  </tr>
  <tr>
    <td>Third Test</td><td>C</td><td>99.7%</td><td>99.9%</td><td>$$\frac{0.997}{1-0.999} = 997$$</td>
  </tr>
</table>

>Clinically desired LR  
>$$LR_{\text{desired}} = 9,899,901$$  
>
>Multiply the LRs:  
>$$LR_{A+} = 333 < LR_{\text{desired}}$$  
>$$LR_{A+, B+} = 333 \times 499 =  166,167 < LR_{\text{desired}}$$  
>$$LR_{A+, B+, C+} = 333 \times 499 \times 997 = 165,668,499 > LR_{\text{desired}}$$  

The combined LR exceeds the required LR of 9,899,901, meaning that serial testing with A, B, and C meets the clinical threshold of PPV ≥ 0.99.

## Closing
This technical note derives and formalizes the mathematical relationships that underpin the CASOTA framework. The key result is the
inequality linking diagnostic test likelihood ratios to clinically defined PPV thresholds and disease prevalence. These results serve
as the foundation for evaluating whether a given test strategy can meet predefined clinical expectations.

*[Table of Content](../../index.md)*
