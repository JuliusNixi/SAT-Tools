import sat_tools as sat

alp = "123"
while True:
    s = sat.generateCNF(alp, k=16)
    r = sat.resolveCNF(s)
    if r is None:
        print("No solution")
        print(sat.stringifyCNF(s))
        print(r)
        break

