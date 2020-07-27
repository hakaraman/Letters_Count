from collections import Counter
sentence = ("hippo runs to us!")
counts = Counter(sentence)
numbers = dict(sorted(counts.items()))
numbers
