counts = dict()
names = ['nahid', 'abul', 'kabul', 'jabul', 'habul']
for name in names:
    if name not in counts:
        counts[name] = name
    else:
        counts[name] = counts[name]+1
print(counts)
