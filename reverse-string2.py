q = 'Hello i am boy'


def r_str(n):
    l = []
    sl = n.split()
   
    for w in reversed(sl):
	l.append(w)

    ns = ' '.join(l)
    print ns

r_str(q)

"""
def r_str(n):

    return sorted(n,reverse = True)

print r_str(q)
"""
