# Bayesian Regression
*Last updated 2025-06-02*

## Classical Linear Regression
### Data
Here’s a simple dataset with a nearly perfect linear relationship between `X` and `Y`:

<table>
  <tr>
    <th></th>
    <th>X</th>
    <th>Y</th>
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
Using ordinary least squares (OLS) via `statsmodels`(*code not shown*), we obtain:

>$$Y = 0.0031 + 0.9998X$$

With 95% confidence intervals:
- Intercept: [-0.018, 0.025]
- Slope: [0.996 , 1.004]

This frequentist approach assumes that the only uncertainty lies in the dependent variable `Y`, and that the residuals are independent, normally distributed, and homoscedastic.

## Bayesian Regression (Simple)
Let’s now reframe the same linear model in a Bayesian framework using PyMC.

### Model in PyMC
Imports (used throughout this article):

```python
import arviz as az
import pymc as pm
```

Model definition:
```python
with pm.Model() as linmodel:
  # Priors
  intercept = pm.Normal("intercept", mu=0, sigma=1)
  slope = pm.Normal("slope", mu=1, sigma=1)
  sigma = pm.HalfNormal("sigma", sigma=1)

  # Linear model
  y_pred = pm.Deterministic("model", intercept + slope * (X))

  # Likelihood
  pm.Normal("y_pred", mu=y_pred, sigma=sigma, observed=Y)

  # Inference
  idata = pm.sample(2000, cores=4, nuts_kwargs={"target_accept": 0.95})
```

>ArviZ is used for model diagnostics and summaries.  
>Set `hdi_prob` = 0.95 to compute the 95% highest density intervals (HDIs).

### Posterior Summary

The estimated regression line is:

>$$Y = 0.003 + 1.000X$$

With 95% credible intervals:
- Intercept: [−0.039, 0.038]
- Slope: [0.993, 1.008]

The Bayesian approach treats the model parameters as distributions, not fixed values. The result is a full posterior distribution over all parameters, giving us more than just point estimates -- it gives us uncertainty.

## Heteroscedasticity in Bayesian

### What is Heteroscedasticity?
Heteroscedasticity occurs when the variability of the residuals (errors) depends on the value of `X`. In simpler terms, the spread of `Y` increases (or decreases) along the range of `X`. This violates a key assumption of classical OLS regression: constant variance (homoscedasticity).

OLS is not well-equipped for heteroscedastic data. In frequentist settings, one workaround is weighted least squares (WLS) -- a method that can get quite nuanced and brittle.

In Bayesian modelling, heteroscedasticity is straightforward to implement.

![](images/heteroscedasticity.jpg)

### Data
In this example, each `Y` value is the average of three repeated measurements (`y1`, `y2`, `y3`​), and the standard deviation (`sdy`) at each point reflects measurement error that increases with `X`:

<table>
  <tr>
    <th></th>
    <th>X</th>
    <th>y1</th>
    <th>y2</th>
    <th>y3</th>
    <th>Y</th>
    <th>sdy</th>
  </tr>
  <tr>
    <td>1</td>
    <td>0.500</td>
    <td>0.549</td>
    <td>0.549</td>
    <td>0.550</td>
    <td>0.549</td>
    <td>0.001</td>
  </tr>
  <tr>
    <td>2</td>
    <td>2.372</td>
    <td>2.614</td>
    <td>2.616</td>
    <td>2.615</td>
    <td>2.615</td>
    <td>0.001</td>
  </tr>
  <tr>
    <td>3</td>
    <td>4.251</td>
    <td>4.667</td>
    <td>4.691</td>
    <td>4.680</td>
    <td>4.680</td>
    <td>0.010</td>
  </tr>
  <tr>
    <td>4</td>
    <td>6.134</td>
    <td>6.751</td>
    <td>6.735</td>
    <td>6.736</td>
    <td>6.741</td>
    <td>0.007</td>
  </tr>
  <tr>
    <td>5</td>
    <td>7.998</td>
    <td>8.791</td>
    <td>8.784</td>
    <td>8.813</td>
    <td>8.796</td>
    <td>0.013</td>
  </tr>
</table>

### Frequentist WLS (Weighted Least Squares)

Using WLS in `statsmodels` (*code not shown*):
>$$Y = 0.0057 + 1.0989X$$

With 95% confidence intervals:
- Intercept: [−0.014, 0.025]
- Slope: [1.096, 1.102]

### Bayesian Modelling with Heteroscedasticity

All we need to do in `PyMC` is replace the constant error term `sigma` with a known, data-derived `sdy`:

```python
with pm.Model() as hetmodel:
  # Priors
  intercept = pm.Normal("intercept", mu=0, sigma=1)
  slope = pm.Normal("slope", mu=1, sigma=1)
  
  # Linear model
  y_pred = pm.Deterministic("model", intercept + slope * (X))

  # Likelihood using observed heteroscedastic error
  pm.Normal("y_pred", mu=y_pred, sigma=sdy, observed=Y)

  # inference data
  idata = pm.sample(2000, cores=4, nuts_kwargs={"target_accept": 0.95})
```

#### Posterior Summary

Bayesian model estimates:
>$$Y = -0.001 + 1.102X$$

With 95% credible intervals:
- Intercept: [−0.003, 0.001]
- Slope: [1.101, 1.103]

Bayesian models allow you to model heteroscedasticity directly and transparently by encoding the varying uncertainty directly in the likelihood -- no special workaround needed.

## Error-in-variables (Uncertainty in Both X and Y)
Now let’s address a more challenging scenario: both `X` and `Y` have measurement error. This situation frequently arises in real-world experiments.

![](images/ODRA.jpg)

### Why Frequentist Methods Struggle
In the frequentist framework, accounting for measurement error in the independent variable `X` leads to nontrivial models. One commonly used solution is Deming regression, which assumes known variances in both `X` and `Y` and minimizes orthogonal distances rather than vertical residuals.

Even with Deming regression, generalizing to weighted, multivariable, or non-Gaussian cases becomes increasingly messy.

### Data
Each `X` and `Y` value below is the average of three measurements, with associated standard deviations:

<table>
  <tr>
    <th></th>
    <th>x1</th>
    <th>x2</th>
    <th>x3</th>
    <th>y1</th>
    <th>y2</th>
    <th>y3</th>
    <th>X</th>
    <th>sdx</th>
    <th>Y</th>
    <th>sdy</th>
  </tr>
  <tr>
    <td>1</td>
    <td>0.701</td>
    <td>0.701</td>
    <td>0.699</td>
    <td>0.746</td>
    <td>0.750</td>
    <td>0.749</td>
    <td>0.700</td>
    <td>0.001</td>
    <td>0.749</td>
    <td>0.002</td>
  </tr>
  <tr>
    <td>2</td>
    <td>2.575</td>
    <td>2.577</td>
    <td>2.577</td>
    <td>2.814</td>
    <td>2.809</td>
    <td>2.814</td>
    <td>2.576</td>
    <td>0.001</td>
    <td>2.812</td>
    <td>0.002</td>
  </tr>
  <tr>
    <td>3</td>
    <td>4.449</td>
    <td>4.440</td>
    <td>4.452</td>
    <td>4.876</td>
    <td>4.881</td>
    <td>4.878</td>
    <td>4.447</td>
    <td>0.005</td>
    <td>4.878</td>
    <td>0.002</td>
  </tr>
  <tr>
    <td>4</td>
    <td>6.334</td>
    <td>6.328</td>
    <td>6.318</td>
    <td>6.946</td>
    <td>6.939</td>
    <td>6.932</td>
    <td>6.327</td>
    <td>0.007</td>
    <td>6.939</td>
    <td>0.006</td>
  </tr>
  <tr>
    <td>5</td>
    <td>8.198</td>
    <td>8.197</td>
    <td>8.206</td>
    <td>9.004</td>
    <td>9.001</td>
    <td>9.005</td>
    <td>8.200</td>
    <td>0.004</td>
    <td>9.003</td>
    <td>0.002</td>
  </tr>
</table>

### Weighted Deming Regression (Frequentist)
Estimated model:
>$$Y = -0.0227 + 1.1008X$$

95% confidence intervals:
- Intercept: [−0.0268, −0.0186]
- Slope: [1.0995, 1.1020]

### Bayesian Error-in-Variables Model

Here’s where Bayesian methods shine. We simply:
- Add a latent variable for the true `X` values, modeled with a normal prior centered at the observed `X`, with standard deviation `sdx`.
- Retain the `sdy` information in the likelihood, as before.

```python
with pm.Model() as errmodel:
  # Priors
  intercept = pm.Normal("intercept", mu=0, sigma=5)
  slope = pm.Normal("slope", mu=1, sigma=5)

  # Latent variable: true X values
  x_mean = pm.Normal("x_mean", mu=X, sigma=sdx)
  
  # Linear model
  y_pred = pm.Deterministic("model", intercept + slope * (x_mean))

  # Likelihood with observed error in Y
  pm.Normal("y_pred", mu=y_pred, sigma=sdy, observed=Y)

  # Inference
  idata = pm.sample(2000, cores=4, nuts_kwargs={"target_accept": 0.95})
```

#### Posterior Summary
Estimated model:
>$$Y = -0.022 + 1.101X$$

95% credible intervals:
- Intercept: [−0.026, −0.018]
- Slope: [1.099, 1.102]

With PyMC, extending your model to account for measurement uncertainty in both `X` and `Y` is seamless. This is a powerful advantage over frequentist approaches that require special-case solutions.

## Summary
Bayesian regression provides a natural and extensible framework to handle various forms of uncertainty:
- Basic linear regression is straightforward and gives full posterior distributions.
- Heteroscedasticity is easily handled by plugging in known sigma values per observation.
- Error-in-variables becomes a simple matter of introducing latent variables.

Unlike frequentist solutions that often require entirely new techniques or approximations, Bayesian modelling with PyMC evolves incrementally, retaining model transparency and interpretability.

*[Table of Content](../../index.md)*
