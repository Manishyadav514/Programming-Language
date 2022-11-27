y = dbinom(0:50,50,0.4)
plot(y)

# binomial esimation
x = rbinom(1000, 1, 0.6)
x
mean(x)

# uniform esimation
x = runif(100, 0, 3)
x
2*mean(x)
max(x)


# normal esimation
x = rnorm(100,2,3)
x
mean(x)
sd(x)

# poisol esimation
x = rpois(100,2,3)
x

# interval esimation
m = 4
sigma = 3
n = 100
x = rnorm(n, m, sigma)
alpha = 0.05
# a = z_(a/2)
a = qnorm(1-(alpha/2), mean=0, sd=1)
u = mean(x) - ((a*sigma)/sqrt(n))
v = mean(x) + ((a*sigma)/sqrt(n))
u
v