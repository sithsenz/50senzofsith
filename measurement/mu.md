---
title: Measurement Uncertainty
---


# Measurement Uncertainty

In a qualitative testing, the *target condition* (tc) is either pos or neg. *True Positive Rate* (TPR) and *True Negative Rate* (TNR) are distributed according to Bernoulli's distribution with parameter *p*:

> TPR ~ Bernoulli(SS), *p = sensitivity* (SS) when *tc = pos*  
TNR ~ Bernoulli(SP), *p = specificity* (SP) when *tc = neg*

From Bayes' Theorem,  
> $$P(\theta|\text{tc=pos}) \propto P(\theta) \times P(\text{tc=pos}|\theta)$$

Hence,  
> $$P(\theta|\text{tc=pos}) \propto p^1 (1-p)^1 \times p^{\text{tp}} (1-p)^{\text{fn}} = p^{1+\text{tp}} (1-p)^{1+\text{fn}}$$
> 
> $$P(\theta|\text{tc=neg}) \propto p^{1+\text{tn}} (1-p)^{1+\text{fp}}$$
