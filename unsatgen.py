import sat_tools as sat

alp = "123"
k = 16
while True:
    s = sat.generateCNF(alp, k=k)
    r = sat.resolveCNF(s)
    if r is None:
        print(f"Generated an UNSAT instance with {k} clauses:")
        print("Alphabet: " + alp)
        print(sat.stringifyCNF(s))
        print("Solution: " + str(r))
        break

