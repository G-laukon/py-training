def has_duplicates(t):
    for x in t:
        t_copy = t + []
        t_copy.remove(x)
        for y in t_copy :
            if x == y:
