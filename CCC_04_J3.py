n, m = int(input()), int(input())
adjectives = []
nouns = []
for i in range(n):
    adjectives.append(input())
for i in range(m):
    nouns.append(input())
for adj in adjectives:
    for noun in nouns:
        print(adj + " as " + noun)

