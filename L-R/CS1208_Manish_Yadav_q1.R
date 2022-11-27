# when sigma is not known
# interval, mean(x)+t_(a/2).S/root(n)
# s = sample standard deviation
n=100
x = c(1:n)
y = sum((x-mean(x))**2)
S = sqrt( y/(n-1))
alpha = 0.05
# using standard t distribution table at df=n-1=100-1=99, and margin 0.025
a =  1.984  
u = mean(x) - (a*S/sqrt(n)) 
v = mean(x) + (a*S/sqrt(n))
u
v