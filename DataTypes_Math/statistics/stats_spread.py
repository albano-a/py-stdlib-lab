import statistics as stats

pop = [2, 3, 1, 5]

pvar = stats.pvariance(pop)
var = stats.variance(pop)
pstdev = stats.pstdev(pop)
stdev = stats.stdev(pop)

print(f"The population variance of {pop} is {pvar}")
print(f"The sample variance of {pop} is {var}")
print(f"The population standard deviation of {pop} is {pstdev}")
print(f"The sample standard deviation of {pop} is {stdev}")

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [1, 2, 3, 1, 2, 3, 1, 2, 3]

cov = stats.covariance(list1, list2)
cor = stats.correlation(list1, list2)

print(f"Covariance of {list1} and {list2} is {cov}")
print(f"Correlation of {list1} and {list2} is {cor}")

year = [1971, 1975, 1979, 1982, 1983]
films_total = [1, 2, 3, 4, 5]

slope, intercept = stats.linear_regression(year, films_total)
print(f"Linear Regression Results:")
print(f"  Years: {year}")
print(f"  Films Total: {films_total}")
print(f"  Slope: {slope:.2f}")
print(f"  Intercept: {intercept:.2f}")
