# Bayesian Regression
*Last updated 2025-06-01*

## Classical Linear Regression
### Data
<table>
  <tr>
    <th></th>
    <th>x</th>
    <th>y</th>
  </tr>
  <tr>
    <td>1</td>
    <td>0.500</td>
    <td>0.500</td>
  </tr>
  <tr>
    <td>2</td>
    <td>2.372</td>
    <td>2.376</td>
  </tr>
  <tr>
    <td>3</td>
    <td>4.247</td>
    <td>4.248</td>
  </tr>
  <tr>
    <td>4</td>
    <td>6.118</td>
    <td>6.131</td>
  </tr>
  <tr>
    <td>5</td>
    <td>7.996</td>
    <td>7.990</td>
  </tr>
</table>

### Linear Regression Model
OLS Model produced using `statsmodel` *code not shown*

$$Y = 0.0031 + 0.9998X$$
$$\text{95% CI of intercept} = \text{[-0.018 , 0.025]}$$
$$\text{95% CI of slope} = \text{[0.996 , 1.004]}$$

## Bayesian Regression (Simple)
### Modelling Using PyMC
Same import throughout this article
```python
import arviz as az
import pymc as pm
```

```python
with pm.Model() as linmodel:
  # prior
  intercept = pm.Normal("intercept", mu=0, sigma=1)
  slope = pm.Normal("slope", mu=1, sigma=1)
  sigma = pm.HalfNormal("sigma", sigma=1)

  # model
  y_pred = pm.Deterministic("model", intercept + slope * (X))

  # likelihood
  pm.Normal("y_pred", mu=y_pred, sigma=sigma, observed=Y)

  # inference data
  idata = pm.sample(2000, cores=4, nuts_kwargs={"target_accept": 0.95})
```

Always use *Arviz*
- to produce the summary of the analysis / model
- hdi_prob always set to 0.95

### linmodel

$$Y = 0.003 + 1.000X$$
$$\text{95% CI of intercept} = \text{[-0.039 , 0.038]}$$
$$\text{95% CI of slope} = \text{[0.993 , 1.008]}$$

## Heteroscedasticity in Bayesian
Heteroscedasticity = proportional error in the Y variable
![](images/heteroscedasticity.jpg)

*[Table of Content](../../index.md)*
