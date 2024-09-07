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
|||Target Condition||
|:---:|:---:|:---:|:---:|
|||Positive|Negative|
|Test Result|Detected|tp|fp|
||Not Detected|fn|tn|

## True Positive Rate (TPR) and False Negative Rate (FNR)

According to Bayesian Probability, the analysis of binary outcomes should be carried out under the context of the true target condition. When the condition is positive, we can calculate:

The probability of a positive test given the condition is positive:
> $$P(\theta+|\text{TC+}) = \text{TPR} = \frac{\text{tp}}{\text{tp} + \text{fn}}$$

The probability of a negative test given the condition is positive:
> $$P(\theta-|\text{TC+}) = \text{FNR} = \frac{\text{fn}}{\text{tp} + \text{fn}}$$

Similarly, when the condition is negative, we can calculate:  
The probability of a negative test given the condition is negative:
> $$P(\theta-|\text{TC-}) = \text{TNR} = \frac{\text{tn}}{\text{fp} + \text{tn}}$$

The probability of a positive test given the condition is negative:
> $$P(\theta+|\text{TC-}) = \text{FPR} = \frac{\text{fp}}{\text{fp} + \text{tn}}$$

## Predictive Values vs. Likelihood Ratios

Although *Positive Predictive Value* (PPV) and *Negative Predictive Value* (NPV) are commonly used in diagnostic tests, these metrics are significantly influenced by the prevalence of the condition in the population. On the other hand, *Positive Likelihood Ratios* (LR+) and *Negative Likelihood Ratios* (LR-) are much more robust indicators, as they are not directly affected by prevalence.

> $$\text{LR+} = \frac{\text{TPR}}{\text{FPR}}$$
>
> $$\text{LR-} = \frac{\text{TNR}}{\text{FNR}}$$
>
> $$\text{PPV} = \frac{\text{tp}}{\text{tp}+\text{fp}}$$
>
> $$\text{NPV} = \frac{\text{tn}}{\text{tn}+\text{fn}}$$

### Example of Prevalence Impact

Let's compare PPV, NPV, and likelihood ratios at different prevalence levels.

#### Case 1: Prevalence = 0.1%

Given the same test sensitivity and specificity, the PPV will be low due to the low prevalence, but the likelihood ratios remain constant.

#### Case 2: Prevalence = 50%

In this case, the PPV will be high, but again, the likelihood ratios will remain stable, showing their superiority in understanding diagnostic performance.

## Sources of Data for MU Analysis

Data for constructing the contingency table in the context of measurement uncertainty analysis can come from several sources:

1. Validation studies conducted by the manufacturer and the user.
2. Published literature on the performance of similar tests.
3. Participation in external quality assurance (EQA) programs.
4. Routine internal quality control (QC) checks.
5. Prior estimation of measurement uncertainty (MU).

These data sources can be combined using Bayes' Theorem, which is particularly useful in pooling information from different sources. When starting with minimal prior information, we often use a uniform non-informative prior such as Beta(1,1).

### Example of Combining Data Using Bayes' Theorem
|*(prior values)*||Target Condition||
|:---:|:---:|:---:|:---:|
|||Positive|Negative|
|Test Result|Detected|1|1|
||Not Detected|1|1|

Now, if the actual observed data are a, b, c, and d, the likelihood is combined with the prior as follows:
> Using index law:
> 
> Posterior tp=1+a, Posterior fp=1+b, Posterior fn=1+c, Posterior tn=1+d

## Applications of Bayes' Theorem in Clinical Diagnosis

Let's consider two examples where Bayes' Theorem is applied in clinical diagnosis using likelihood ratios.

### Example 1: Low Prevalence Condition (0.1%)

For a condition with a low prevalence (e.g., rare genetic disorder), the LR+ can be used to adjust the pre-test probability and arrive at a more accurate post-test probability. Even with a high LR+, the post-test probability might remain low due to the low prevalence.

### Example 2: High Prevalence Condition (50%)

For a condition with higher prevalence (e.g., common infection), the LR- helps adjust the pre-test probability downward if the test is negative, allowing for a more nuanced understanding of the result.

## References
+ [JCGM-GUM-3](https://www.bipm.org/documents/20126/2071204/JCGM_100_2008_E.pdf/cb0ef43f-baa5-11cf-3f85-4dcd86f77bd6?version=1.16&t=1716986360859&download=true)
+ [JCGM-GUM-7](https://www.bipm.org/documents/20126/2071204/JCGM_101_2008_E.pdf/325dcaad-c15a-407c-1105-8b7f322d651c?version=1.16&t=1716986453493&download=true)
