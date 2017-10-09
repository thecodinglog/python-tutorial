class Cache:
    def __init__(self, cacheSize):
        self.cacheSize = cacheSize
        self.innerCache = []

    def process_city(self, city):
        cached = self.get_city_from_cache(city.lower())
        if cached == '':
            return 5
        else:
            return 1

    def get_city_from_cache(self, city):
        if city in self.innerCache:
            self.innerCache.remove(city)
            self.innerCache.append(city)
            return city
        else:
            if len(self.innerCache) > 0 and len(self.innerCache) == self.cacheSize:
                del self.innerCache[0]

            self.innerCache.append(city)
            return ''


test_cases = []
test_cases.append((3, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA'], 50))
test_cases.append((3, ['Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul'], 21))
test_cases.append((2, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju',
                       'NewYork', 'Rome'], 60))
test_cases.append((5, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju',
                       'NewYork', 'Rome'], 52))
test_cases.append((2, ['Jeju', 'Pangyo', 'NewYork', 'newyork'], 16))
test_cases.append((0, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA'], 25))


for case in test_cases:
    city_processor = Cache(case[0])
    running_time = 0
    for city in case[1]:
        running_time = running_time + city_processor.process_city(city)

    if running_time == case[2]:
        print('success')
    else:
        print('failed')

