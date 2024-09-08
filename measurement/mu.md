---
title: Measurement Uncertainty
---


# Estimation of Measurement Uncertainty in Qualitative Testing

*Measurement uncertainty* (MU) is crucial in ensuring the reliability of test results, particularly in medical laboratories. While the conventional framework, as laid out in JCGM-GUM-3, is well-suited for quantitative testing, its application in qualitative tests (e.g., positive/negative outcomes) presents certain challenges. For this reason, JCGM-GUM-7 offers a more appropriate approach, modeling MU using the principles of probability distribution and Bayesian Probability.

## JCGM-GUM-7 Framework and Bayesian Approach

In JCGM-GUM-7, MU is modeled using probability distributions, which can be used to quantify the MU in both qualitative and quantitative results. A significant aspect of this approach is the use of Bayesian Probability to integrate prior knowledge with observed data.

Unlike frequentist methods, which rely solely on the observed data, Bayesian methods combine prior information with data to update our beliefs about a hypothesis.

## Binary Outcomes in Qualitative Testing

Most qualitative tests produce binary outcomes, such as *positive vs negative* or *detected vs not detected*. These outcomes can be easily modeled using the Bernoulli distribution. A useful way to analyze such results is through a 2x2 contingency table, which compares the test results with the true *target condition* (TC). Conventionally, the columns represent the true TC, while the rows represent the test results.

Here is a typical contingency table:  
<table>
  <tr>
    <td rowspan="2" colspan="2"></td>
    <td colspan="2">Target Condition</td>
  </tr>
  <tr>
    <td>Positive</td>
    <td>Negative</td>
  </tr>
  <tr>
    <td rowspan="2">Test Result</td>
    <td>Detected</td>
    <td>tp</td>
    <td>fp</td>
  </tr>
  <tr>
    <td>Not Detected</td>
    <td>fn</td>
    <td>tn</td>
  </tr>
</table>

## True Positive Rate (TPR) and False Negative Rate (FNR)

According to Bayesian Probability, the analysis of binary outcomes should be carried out under the context of the true target condition. When the condition is positive, we can calculate:

The probability of a positive test given the condition is positive:
> $$P(\text{Test+}|\text{TC+}) = \text{TPR} = \frac{\text{tp}}{\text{tp} + \text{fn}}$$

The probability of a negative test given the condition is positive:
> $$P(\text{Test-}|\text{TC+}) = \text{FNR} = \frac{\text{fn}}{\text{tp} + \text{fn}}$$

Similarly, when the condition is negative, we can calculate:  
The probability of a negative test given the condition is negative:
> $$P(\text{Test-}|\text{TC-}) = \text{TNR} = \frac{\text{tn}}{\text{fp} + \text{tn}}$$

The probability of a positive test given the condition is negative:
> $$P(\text{Test+}|\text{TC-}) = \text{FPR} = \frac{\text{fp}}{\text{fp} + \text{tn}}$$

## Predictive Values vs. Likelihood Ratios

Although *Positive Predictive Value* (PPV) and *Negative Predictive Value* (NPV) are commonly used in diagnostic tests, these metrics are significantly influenced by the prevalence of the condition in the population. On the other hand, *Positive Likelihood Ratios* (LR+) and *[Negative Likelihood Ratios](# 'as defined by Eurachem / CITAC')* (LR-)  are much more robust indicators, as they are not directly affected by prevalence.

> $$\text{LR+} = \frac{P(\text{Test+}|\text{TC+})}{P(\text{Test+}|\text{TC-})} = \frac{\text{TPR}}{\text{FPR}}$$
>
> $$\text{LR-} = \frac{P(\text{Test-}|\text{TC-})}{P(\text{Test-}|\text{TC+})} = \frac{\text{TNR}}{\text{FNR}}$$
>
> $$\text{PPV} = P(\text{TC+}|\text{Test+}) = \frac{\text{tp}}{\text{tp}+\text{fp}}$$
>
> $$\text{NPV} = P(\text{TC-}|\text{Test-}) = \frac{\text{tn}}{\text{tn}+\text{fn}}$$

### Example of Prevalence Impact

<table>
  <th>
    <td>Equal Prevalence</td>
    <td>Unbalanced Prevalence</td>
    <td>Low Prevalence</td>
    <td>Very Low Prevalence</td>
  </th>
  <tr>
    <td>Prevalence %</td>
    <td>50.00</td>
    <td>33.33</td>
    <td>9.09</td>
    <td>0.99</td>
  </tr>
  <tr>
    <td>Contingency Table</td>
    <td><table><tr><td>264</td><td>17</td></tr><tr><td>26</td><td>273</td></tr></table></td>
    <td><table><tr><td>264</td><td>34</td></tr><tr><td>26</td><td>546</td></tr></table></td>
    <td><table><tr><td>264</td><td>170</td></tr><tr><td>26</td><td>2730</td></tr></table></td>
    <td><table><tr><td>264</td><td>1700</td></tr><tr><td>26</td><td>27300</td></tr></table></td>
  </tr>
  <tr>
    <td>Sensitivity %</td>
    <td colspan="4">91.03</td>
  </tr>
  <tr>
    <td>Specificity %</td>
    <td colspan="4">94.14</td>
  </tr>
  <tr>
    <td>FNR %</td>
    <td colspan="4">8.97</td>
  </tr>
  <tr>
    <td>FPR %</td>
    <td colspan="4">5.86</td>
  </tr>
  <tr>
    <td>LR+ %</td>
    <td colspan="4">15.53</td>
  </tr>
  <tr>
    <td>LR- %</td>
    <td colspan="4">10.49</td>
  </tr>
  <tr>
    <td>PPV %</td>
    <td>93.95</td>
    <td>88.59</td>
    <td>60.83</td>
    <td>13.44</td>
  </tr>
  <tr>
    <td>NPV %</td>
    <td>91.30</td>
    <td>95.45</td>
    <td>99.06</td>
    <td>99.90</td>
  </tr>
  <tr>
    <td>Accuracy %</td>
    <td>92.59</td>
    <td>93.10</td>
    <td>93.86</td>
    <td>94.11</td>
  </tr>
</table>

Let's compare PPV, NPV, and likelihood ratios at different prevalence levels. Given the same test sensitivity, specificity and likelihood ratios, the PPV will be low due to the low prevalence, while the NPV and accuracy will be high due to the low prevalence.

## Sources of Data for MU Analysis

Data for constructing the contingency table in the context of measurement uncertainty analysis can come from several sources:

1. Validation studies conducted by the manufacturer and the user.
2. Published literature on the performance of similar tests.
3. Participation in external quality assurance (EQA) programs.
4. Routine internal quality control (QC) checks.
5. Prior estimation of measurement uncertainty (MU).

These data sources can be combined using Bayes' Theorem, which is particularly useful in pooling information from different sources. When starting with minimal prior information, we often use a uniform non-informative prior such as Beta(1,1) for both TC.

### Example of Combining Data Using Bayes' Theorem
<table>
  <tr>
    <td rowspan="2" colspan="2">Prior Values</td>
    <td colspan="2">Target Condition</td>
  </tr>
  <tr>
    <td>Positive</td>
    <td>Negative</td>
  </tr>
  <tr>
    <td rowspan="2">Test Result</td>
    <td>Detected</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>Not Detected</td>
    <td>1</td>
    <td>1</td>
  </tr>
</table>

<table>
  <tr>
    <td rowspan="2" colspan="2">Likelihood Values</td>
    <td colspan="2">Target Condition</td>
  </tr>
  <tr>
    <td>Positive</td>
    <td>Negative</td>
  </tr>
  <tr>
    <td rowspan="2">Test Result</td>
    <td>Detected</td>
    <td>a</td>
    <td>b</td>
  </tr>
  <tr>
    <td>Not Detected</td>
    <td>c</td>
    <td>d</td>
  </tr>
</table>

Given the above observation, the posterior probability according to Bayes' Theorem is:  
> $$P(\text{posterior}) \propto P(\text{prior}) \times P(\text{likelihood})$$

given probability of Binomial(n, p) is:
> $$P(x) = \left( \begin{array}{c}
> n \\
> x \end{array} \right) \centerdot p^x \centerdot (1-p)^{n-x}$$
>
> $$P(x) \propto p^x \centerdot (1-p)^{n-x}$$

hence, for TC+
> $$P(\text{posterior}) \propto (p^1 \centerdot (1-p)^1) \centerdot (p^a \centerdot (1-p)^c)$$
>
> $$P(\text{posterior}) \propto p^{1+a} \centerdot (1-p)^{1+c}$$

similarly, for TC-
> $$P(\text{posterior}) \propto p^{1+d} \centerdot (1-p)^{1+b}$$

which can be shown in this table:

<table>
  <tr>
    <td rowspan="2" colspan="2">Posterior Values</td>
    <td colspan="2">Target Condition</td>
  </tr>
  <tr>
    <td>Positive</td>
    <td>Negative</td>
  </tr>
  <tr>
    <td rowspan="2">Test Result</td>
    <td>Detected</td>
    <td>1 + a</td>
    <td>1 + b</td>
  </tr>
  <tr>
    <td>Not Detected</td>
    <td>1 + c</td>
    <td>1 + d</td>
  </tr>
</table>

## Applications of Bayes' Theorem in Clinical Diagnosis

Let's consider two examples where Bayes' Theorem is applied in clinical diagnosis using likelihood ratios.

### Example 1: Low Prevalence Condition (0.1%)

For a condition with a low prevalence (e.g., rare genetic disorder), the LR+ can be used to adjust the pre-test probability and arrive at a more accurate post-test probability. Even with a high LR+, the post-test probability might remain low due to the low prevalence.

### Example 2: High Prevalence Condition (50%)

For a condition with higher prevalence (e.g., common infection), the LR- helps adjust the pre-test probability downward if the test is negative, allowing for a more nuanced understanding of the result.

## References
+ [Eurachem / CITAC](https://www.eurachem.org/index.php/publications/guides/performance-and-uncertainty-in-qualitative-analysis)
+ [JCGM-GUM-3](https://www.bipm.org/documents/20126/2071204/JCGM_100_2008_E.pdf/cb0ef43f-baa5-11cf-3f85-4dcd86f77bd6?version=1.16&t=1716986360859&download=true)
+ [JCGM-GUM-7](https://www.bipm.org/documents/20126/2071204/JCGM_101_2008_E.pdf/325dcaad-c15a-407c-1105-8b7f322d651c?version=1.16&t=1716986453493&download=true)
