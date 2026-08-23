from dataclasses import dataclass

@dataclass
class City:
    prefecture: str
    year: int
    id: int = 0

N, M = map(int, input().split())

cities = [] * M
for i in range(M):
    p, y = map(int, input().split())
    cities.append(City(p, y))

sorted_cities = sorted(cities, key=lambda c: c.year)

city_num = [1] * (N + 1)
for city in sorted_cities:
    id = 0
    id_up = 0
    id_down = 0
    id_up = f"{city.prefecture:06}"
    id_down = f"{city_num[city.prefecture]:06}"
    city_num[city.prefecture] += 1
    id = id_up + id_down
    city.id = id


for city in cities:
    print(city.id)