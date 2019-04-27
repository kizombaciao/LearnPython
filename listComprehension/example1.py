def to_locust_units(population):
    return population / LOCUST_PLAGUE_POPULATION

world_population = [
      585_000_000, # 1500
      660_000_000, # 1600
      740_000_000, # 1700
      978_000_000, # 1800
    1_650_000_000, # 1900
    6_008_000_000, # 1999
    7_052_000_000  # 2012 
]

LOCUST_PLAGUE_POPULATION = 30_000_000_000
POPULATION_THRESHOLD = 1_000_000_000

l = []
for p in world_population:
    if p < POPULATION_THRESHOLD:
        continue
    l.append(to_locust_units(p))
print(l)