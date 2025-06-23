from statistics import NormalDist

dist = NormalDist(mu=100, sigma=15)

# You can see the core properties like this

print(
    f"""Mean: {dist.mean}
Stdev: {dist.stdev}
Var: {dist.variance}
Median: {dist.median}
Mode: {dist.mode}"""
)

# PDF - Probability Density Function
print(dist.pdf(100))

# CDF - Cumulative Distribution Function
print(f"{dist.cdf(115) * 100:.2f}%") # prob of X <= 115

# Inverse CDF (Percentile)
print(dist.inv_cdf(0.95)) # Value at the 95th percentile

# Z-score
print(dist.zscore(115)) # 1.0 (1 std above mean)

# Quantiles
print(dist.quantiles(n=4)) # Quartiles: [Q1, Q2, Q3]

# Overla between two dists
d1 = NormalDist(mu=100, sigma=15)
d2 = NormalDist(mu=110, sigma=15)
print(d1.overlap(d2)) # Value between 0.0 and 1.0

# Generate random samples
samples = dist.samples(5, seed=42)
print(samples)  # 5 random values following the distribution

# Estimate from data
data = [98, 102, 101, 97, 99, 103]
estimated = NormalDist.from_samples(data)
print(estimated.mean, estimated.stdev)


