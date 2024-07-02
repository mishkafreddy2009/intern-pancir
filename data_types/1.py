base = [0, "hello", 1.23, "world", 3, 4, 7]
nums = [n for n in base if isinstance(n, (int, float))]
strs = [s for s in base if isinstance(s, str)]
