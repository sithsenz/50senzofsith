# Biostatistics Revisited: Practical Insights from an MLS
Biostatistics plays a crucial role in medical laboratories, extending far beyond its traditional application in research.
It is deeply embedded in our everyday operations, from quality control (QC) monitoring to method validation (MV) and routine data analysis.
This article seeks to revisit key biostatistical concepts through the lens of a Medical Laboratory Scientist (MLS),
offering insights into how these principles apply to the practical challenges we face in the lab.

Rather than a basic lesson, this article is aimed at those who already possess a foundational understanding of biostatistics.
The goal is not to cover elementary definitions or introduce new concepts from scratch, but to present a fresh,
more intuitive perspective on how to apply biostatistics in real-world laboratory settings.
This includes revisiting familiar concepts like probability distributions and confidence intervals (CI), but with an emphasis on their practical application—
especially in areas like QC and MV. Readers should expect to deepen their understanding of how biostatistics can be used to draw actionable insights
from the data they encounter daily, enhancing both accuracy and decision-making in lab practices.

## Data Collection in the Laboratory
In the lab, data collection is a routine activity. Whether we are validating a method or monitoring QC,
the data we generate through measurements plays a critical role in ensuring accuracy and reliability.
Here are four common scenarios:
1. Single Measurement on a Single Sample: Testing a patient’s specimen.
2. Repeated Measurements on a Single Sample: Internal Quality Control (IQC) monitoring.
3. Single Measurement on Multiple Samples: MV without replication.
4. Repeated Measurements on Multiple Samples: MV with replication.

<table>
  <tr>
    <td rowspan="2" colspan="2"></td>
    <td colspan="2">Measurement</td>
  </tr>
  <tr>
    <td>Single</td>
    <td>Repeated</td>
  </tr>
  <tr>
    <td rowspan="2">Sample</td>
    <td>Single</td>
    <td>Testing a patient's specimen</td>
    <td>IQC monitoring</td>
  </tr>
  <tr>
    <td>Multiple</td>
    <td>MV without replication</td>
    <td>MV with replication</td>
  </tr>
</table>

## Data Presentation
While there are many ways to present data, the histogram is particularly favored due to its simplicity and effectiveness in statistical analysis.
Let’s consider a histogram of HBsAg signal-to-cutoff (S/CO) readings from 1,000 patients as an example.
This representation can easily be expanded into more advanced statistical concepts.

![histkde](images/histkde.png "Histogram with KDE of HBsAg from 1,000 patients")

### Probability Distributions
Understanding probability distributions is fundamental to interpreting data in the laboratory.
While there are many different types of probability distributions—such as binomial, Poisson, and exponential—
the one most commonly encountered in lab work is the normal distribution.

A probability distribution provides a mathematical description of how data points are spread across different possible values.
Each distribution is characterized by specific parameters that help define its shape and behavior. For example,
a normal distribution is fully described by two key parameters: the mean (µ) and the standard deviation (σ).

The mean (µ) represents the central value of the distribution, often referred to as the "average".
It tells us the point around which the data tends to cluster. In the context of laboratory data, such as HBsAg (S/CO) readings,
the mean gives us an idea of the expected value from the data set.

The standard deviation (σ) reflects how spread out the data is around the mean. It measures the variability or dispersion of the data points.
A smaller standard deviation indicates that most values are close to the mean, while a larger standard deviation shows that the data points are more spread out.

In the example we previously discussed, the normal distribution of HBsAg (S/CO) readings is characterized by a mean of 0.612 and a standard deviation of 0.2031.
These two parameters are essential for interpreting the overall pattern of the data. The mean helps us understand the central tendency,
while the standard deviation tells us how much variability exists in the measurements. When these parameters are known,
we can predict how data points will behave, which is particularly useful for assessing laboratory QC and measurement uncertainty (MU).

#### Three-Sigma Rule
From the Kernel Density Estimation (KDE) plot, we gain a visual representation of how the data is distributed,
and this helps us apply a fundamental concept in statistics known as the three-sigma rule. The three-sigma rule is derived from the properties
of a normal distribution, which predicts that most data points will fall within certain ranges around the mean (μ), based on the standard deviation (σ). Specifically:
+ μ ± 1σ encompasses 68% of the data. This means that 68% of the values will lie within one standard deviation above or below the mean
+ μ ± 2σ includes 95% of the data. At this range, we capture most of the variability, as 95% of the data points will fall within two standard deviations
+ μ ± 3σ covers 99.7% of the data. Very few data points (just 0.3%) fall outside this range, making it a strong indicator of data consistency

![kdecover](images/kdecover.png "Normal distribution with coverage")

#### Coverage and MU
In practical terms, the coverage provided by the three-sigma rule has direct implications for MU in laboratory settings.
MU refers to the range within which the true value of a measurement is expected to fall. When the data follows a normal distribution,
we can estimate this uncertainty by using a coverage factor. For example, a coverage factor of 2 (which corresponds to μ ± 2σ) provides 95% confidence
that the true value lies within this range.

However, not all data sets are normally distributed. When the data follows other types of distributions — such as Binomial or Poisson — a modeling approach
is required to estimate MU. In these cases, we still rely on the underlying concept of a probability distribution to assess
the likelihood of different measurement values. By fitting the appropriate probability model, we can then determine the coverage interval
that best represents the uncertainty in our measurements, even if the data is not normally distributed.

#### Relating to Levey-Jennings Charts in QC Monitoring
The KDE plot can also be used to demonstrate a connection to LJ Charts, which are a common tool for QC monitoring in the lab.
If we take the KDE plot and rotate it 90°, the result closely resembles an LJ chart. In QC, we plot individual data points, such as daily QC results,
on an LJ chart, which shows how these data points vary over time.

On an LJ chart, the mean (µ) serves as the central line, and standard deviations (σ) are marked above and below the mean to create control limits.
These control limits help us quickly assess whether the lab results are within acceptable ranges or if there is a need for further investigation.
The three-sigma rule also applies here: results that fall within ±3σ are considered normal, while results outside this range may indicate an issue
with the test system.

Though QC data comes in individual measurements over time, when viewed collectively, the data often follows a normal distribution.
This is why QC monitoring and LJ charts are such effective tools in the lab. By plotting each data point individually, we can monitor daily variations,
but in the long run, the aggregated data tends to align with a normal distribution. Understanding this relationship between individual QC data and
the underlying normal distribution is key to maintaining laboratory accuracy and detecting potential errors.

![lj](images/lj.png "The familiar LJ-Chart")

## Central Limit Theorem
The Central Limit Theorem (CLT) is fundamental to understanding the behavior of sample means in statistics. It states that as the sample size increases,
the sample mean (𝑥̅) will converge towards the true population mean (µ), and the sample standard deviation (s) will approach the population standard deviation (σ).
This phenomenon is closely tied to the Law of Large Numbers (LLN), which guarantees that, given enough data points,
the average of the sample will get closer to the population average.

In simpler terms, the LLN explains that with a large enough sample size, any random fluctuations will "average out",
and the sample mean will stabilize around the true mean. The CLT builds on this by showing that, regardless of the population’s underlying distribution,
the distribution of the sample mean will approximate a normal distribution as the sample size grows larger.

![clt](images/clt.png "The Central Limit Theorem (CLT)")

However, when performing repeated measurements, we may not always have the benefit of large sample sizes. In these situations,
the CLT still helps us estimate the population mean accurately. The mean of the sample means — such as 6 replicates over 5 days — provides
a good approximation of the population mean, even when the overall sample size is small. This is because repeated measurements within smaller datasets
act similarly to having a larger sample. By averaging these repeated measurements, the variability is reduced, and the estimates become more stable and reliable.

In essence, even though we don’t have a large sample size, the repetition of measurements allows us to achieve the same effect:
the sample mean converges toward the true population mean. This is the strength of the CLT — it allows us to make meaningful inferences
about the population mean, even with smaller datasets, as long as we can take multiple measurements or replicate the data collection process.

### Practical Applications of CLT
+ CLT allows for convergence of almost any distribution, making it a powerful tool for estimating the population mean with a relatively small number of samples.

![](images/cltgrouping.png "Mean of group means converges to population means even with low number of samples")

+ However, improper use of CLT can distort data. For example, CLT can transform a spiky distribution into a normal distribution, potentially leading to misleading analysis.

![spikyclt](images/spikyclt.png "CLT can converge almost any distribution")

## Confidence Intervals
Confidence Intervals (CI) are a key concept in statistics, commonly used in research, but they are also implicitly applied in routine laboratory processes.
A CI provides a range of values within which we expect the true population mean to lie, based on our sample data. However, the actual meaning of CI
is often misunderstood, and it's important to differentiate it from the concept of coverage.

To clarify, let's consider an example. Imagine we run 20 different experiments, all sampling from the same population. For each experiment,
we calculate a confidence interval. Now, a 50% CI means that, in 50% of these 20 experiments, the calculated confidence interval will contain
the true population mean. In this case, 10 out of the 20 CIs will include the population mean, while the other 10 will not.
Extending this to a 95% CI, 19 out of the 20 calculated intervals will include the population mean, and only 1 will not.
This reflects the confidence level associated with the CI: 95% of the intervals, if repeated many times in different experiments,
will capture the true population mean.

![manyCI](images/manyCI.png "Repeated estimation (20 experiments) of CI from the same population")
*source: [Wikipedia](https://en.wikipedia.org/wiki/Confidence_interval)*

### Understanding Confidence Intervals in Frequentist Statistics
In frequentist statistics, we assume that the population mean is fixed, and it is the data and the resulting confidence intervals that vary
from one experiment to another. Once an experiment is conducted, the confidence interval is also fixed, and it either contains the true population mean
or it doesn’t. The interval does not give us a probability that the true mean is within this range; instead, it expresses our confidence
based on repeated sampling. If we repeated the experiment 100 times, 95 of those intervals would likely include the population mean — this is
the true interpretation of a 95% CI.

### CI vs. Coverage
It's important not to confuse CI with coverage. Coverage refers to the proportion of data points that lie within a certain range, such as µ ± 2σ,
which captures 95% of the data points in a normal distribution. In contrast, a CI refers to the likelihood that the true population mean
falls within a calculated interval based on our sample data. While coverage provides a range that includes the majority of data points,
CI gives a range based on statistical inference, reflecting how often the true mean is expected to be within this interval across repeated experiments.

### CI in Laboratory Practice
CI are widely used in laboratory studies, even if not explicitly recognized by practitioners. They help us make decisions regarding the reliability
and equivalence of methods, reagents, and processes. In this section, we’ll explore how CIs are applied in two common laboratory scenarios:
Method Comparison and Lot-to-Lot Verification (LTLV) studies.

#### Method Comparison Study
In a Method Comparison Study, the goal is to evaluate whether two analytical methods, Method A and Method B, produce comparable results.
To do this, we often derive a regression equation that links the results of the two methods. The equation takes the form:
> Method B=slope×Method A+bias

##### Slope Distribution and Proportionality
The slope in this regression equation tells us whether the two methods are proportional — whether they give similar results across the range of measurements.
+ If the 95% CI of the slope distribution contains the value 1, we conclude that Method A and Method B are proportional. In other words, they behave similarly across the measured range, with no proportional bias
+ If the CI of the slope does not include 1, we infer that the two methods are not proportionally comparable, and further investigation or calibration is needed

![slope](images/slope.png "Probability distribution of slopes with CI, in relation to the value slope=1")

##### Bias Distribution and Systematic Difference
Next, we examine the bias (or intercept) in the regression equation, which represents any systematic difference between the two methods.
+ If the 95% CI of the bias distribution contains the value 0, we conclude that there is no systematic difference between Method A and Method B
+ However, if the CI does not include 0, it indicates that there is a significant systematic bias between the two methods, meaning that one method consistently over- or underestimates relative to the other

![bias](images/bias.png "Probability distribution of bias with CI, in relation to the value bias=0")

#### Lot-to-Lot Verification Study
Another common use of CIs in the lab is in LTLV study, where we compare the performance of a new reagent lot to an existing (old) lot. In LTLV, we test the same set of specimens using both reagent lots and compare the resulting distributions.

##### Comparing Distributions of Two Lots
We can visualize the results of testing with the old and new reagent lots by plotting their respective distributions using KDE plots.
The key here is to examine the overlap of the CIs for the two distributions.
+ If the 95% CIs of the two distributions overlap, we conclude that there is no significant difference between the old and new lots, and the LTLV passes. This means the new reagent lot performs equivalently to the old one, and it can be accepted for use
+ On the other hand, if the CIs do not overlap, we conclude that the new lot is significantly different, and the LTLV fails. In this case, the new lot is rejected, and further validation or troubleshooting is required

![ltlv](images/ltlv.png "Probability distribution of readings from different lots with CI, in relation to each other, showing an overlapping zone")

## Closing Thoughts
Understanding the overarching concepts in biostatistics, rather than memorizing formulas, is essential for applying these principles in a laboratory setting.
With practice, laboratory professionals can build intuition and proficiency, allowing for more accurate interpretation of data and improved decision-making.

*[Table of Content](../index.md)*
