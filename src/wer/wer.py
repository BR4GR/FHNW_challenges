import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp

t = np.array([
    148, 163, 116, 169, 87, 123, 114, 104, 136, 78,
    133, 113, 143, 100, 120, 169, 221, 173, 133, 156,
    126, 110, 149
])
n = np.array([
    7, 9, 8, 8, 8, 5, 13, 12, 7, 8,
    6, 11, 6, 7, 8, 9, 6, 10, 8, 9,
    9, 6, 6
])
x = np.linspace(n.min(), n.max(), 100)
plt.hist(n, bins=20, density=True, cumulative=True)

norm_params = sp.norm.fit(n)
plt.plot(x, sp.norm(*norm_params).cdf(x), label='normal')

exp_params = sp.expon.fit(n)
plt.plot(x, sp.expon(*exp_params).cdf(x), label='exponential')

gamma_params = sp.gamma.fit(n)
plt.plot(x, sp.gamma(*gamma_params).cdf(x), label='gamma')

plt.legend()
plt.show()

mu, std = norm_params
print(mu)
print(std)
SEM  = std / np.sqrt(len(n))
#%%
import scipy.stats as sp
help(sp.poisson)

