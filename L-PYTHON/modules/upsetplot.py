import upsetplot
from upsetplot import generate_counts
from upsetplot import from_memberships
example = generate_counts()
example = from_memberships( [[], ['cat2'], ['cat1'],  ['cat1', 'cat2'],   ['cat0'],['cat0', 'cat2'], ['cat0', 'cat1'],   ['cat0', 'cat1', 'cat2'], ], data=[56, 283, 1279, 5882, 24, 90, 429, 1957])
from upsetplot import plot
plot(example)
from matplotlib import pyplot
pyplot.show()