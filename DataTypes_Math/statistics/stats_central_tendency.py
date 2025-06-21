import statistics as stats

grades = [6.7, 5.4, 9.9, 8.7, 7.8]
numbers = [1, 2, 3, 4]
numbers2 = [1, 1, 1, 2, 3, 4, 5, 5, 5, 6]

# Central tendency calculations
mean = stats.mean(grades)
fmean = stats.fmean(grades)  # Always returns float
median = stats.median(numbers)
low_median = stats.median_low(numbers)
high_median = stats.median_high(numbers)
mode = stats.mode(numbers2)
multimode = stats.multimode(numbers2)

# Quantile calculations
quantil = stats.quantiles(grades, n=4)

# Mean calculations
geo_mean = stats.geometric_mean(grades)
har_mean = stats.harmonic_mean(grades)

# Probability density function calculations
kde = stats.kde(grades, h=1.5)
kde_ram = stats.kde_random(grades, h=1.5)
xarr = [i for i in range(0, 5)]
yarr = [kde(x) for x in xarr]
yarr2 = [kde_ram() for x in xarr]

print(f"The arithmetic mean of grades {grades} is {mean}")
print(f"The float arithmetic mean is {fmean}")
print(f"The middle value (or mean of two middles) of {numbers} is {median}")
print(f"The lower of two middle values of {numbers} is {low_median}")
print(f"The higher of two middle values of {numbers} is {high_median}")
print(f"The most common value of {numbers2} is {mode}")
print(f"The list of most common values of {numbers2} is {multimode}")
print(f"The {grades} list split into {4} equal groups is {quantil}")
print()
print(f"Geometric mean of {grades} is {geo_mean}")
print(f"Harmonic mean of {grades} is {har_mean}")
print(f"The probability density function of {grades} is {yarr}")
print(f"The probability density function of {grades} is {yarr2}")
