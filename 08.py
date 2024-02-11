garden = ('ромашка', 'роза', 'одуванчик', 
          'ромашка', 'гладиолус', 'подсолнух', 'роза', )
meadow = ('клевер', 'одуванчик', 
          'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )
garden_set = set(garden)
meadow_set = set(meadow)
all_set = garden_set.union(meadow_set)
print(all_set)
print(garden_set & meadow_set) #и там и там
print(garden_set - meadow_set) #которые растут в саду, но не растут на лугу  
print(meadow_set - garden_set) #растут на лугу, но не растут в саду
