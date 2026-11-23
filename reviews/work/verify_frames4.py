import itertools
from itertools import product
print("="*78); print("C5-qua.  Theorem 10 on Kripke frames  (convention: w R v = v accessible from w)")
print("="*78)
B=('x','y')
def build(W,R):
    U={w:[v for v in W if (w,v) in R] for w in W}          # U(w) = worlds w sees
    F={w:list(product(B,repeat=len(U[w]))) for w in W}
    res={}
    for w in W:
        for v in U[w]:
            idx=[U[w].index(x) for x in U[v]]
            res[(w,v)]=(lambda idx=idx:(lambda tup: tuple(tup[i] for i in idx)))()
    return U,F,res
def sections(W,R,F,res):
    out=[]
    for combo in product(*[F[w] for w in W]):
        a=dict(zip(W,combo)); ok=True
        for (w,v) in R:
            if a[v]!=res[(w,v)](a[w]): ok=False; break
        if ok: out.append(a)
    return out
W=['w0','w1']; R=[('w0','w0'),('w1','w1'),('w1','w0')]
U,F,res=build(W,R); secs=sections(W,R,F,res)
tops=[w for w in W if all((w,v) in R for v in W)]
print("frame: w1 sees w0 and w1 -> maximal world m =", tops)
print("  |A(w0)|=%d  |A(w1)|=%d  |Gamma(A)|=%d  == |A(top)| ? %s" %
      (len(F['w0']),len(F['w1']),len(secs), len(secs)==len(F[tops[0]])))
print("  all stalks nonempty:",all(F[w] for w in W))
print("  => on a frame with a maximal world, Gamma(A) = A(m) EXACTLY, so")
print("     'A(u)!=empty for all u  but  Gamma(A)=empty'  is IMPOSSIBLE.\n")
tot=0;bt=0;bn=0
for n in (2,3):
    allw=list(itertools.combinations(range(n),2))
    for rel in itertools.product([0,1],repeat=len(allw)):
        Rr={(i,i) for i in range(n)}
        for i,f in enumerate(rel):
            if f: Rr.add(allw[i])
        ch=True
        while ch:
            ch=False
            for (a,b) in list(Rr):
                for (c,d) in list(Rr):
                    if b==c and (a,d) not in Rr: Rr.add((a,d)); ch=True
        Rs=sorted(Rr); Wl=list(range(n)); U,F,res=build(Wl,Rs)
        if any(not F[w] for w in Wl): continue
        tot+=1
        if not sections(Wl,Rs,F,res):
            tops=[w for w in Wl if all((w,v) in Rs for v in Wl)]
            if tops: bt+=1
            else: bn+=1
print("exhaustive search over %d (poset,sheaf) pairs on 2-3 worlds:"%tot)
print("   Gamma empty although all stalks nonempty, WITH a maximal world:",bt)
print("   ... with NO maximal world:",bn)
print("   (the B^{U(w)} model only admits 'locally constant' sheaves; a Gamma-empty sheaf")
print("    needs a site without a maximal world, e.g. the open-site of S^1 with the")
print("    tautological bundle -- never mentioned in the paper)")
print()
print("="*78); print("C6.  DEFINITION 7 -- is the 'additive upgrade' an identity or a definition?"); print("="*78)
WM=['m0','m1'];WF=['f0','f1'];WT=['t0','t1']
RMm={(m,m) for m in WM}|{('m1','m0')}; RFf={(f,f) for f in WF}|{('f1','f0')}; RTt={(t,t) for t in WT}|{('t1','t0')}
worlds=[(m,f,t) for m in WM for f in WF for t in WT]
def cross(x,y): return not(x[0]=='m1' and y[0]=='m0') and not(x[1]=='f1' and y[1]=='f0')
def bM(phi,w): return all(phi[y] for y in worlds if (w[0],y[0]) in RMm)
def bF(phi,w): return all(phi[y] for y in worlds if (w[1],y[1]) in RFf)
def bT(phi,w): return all(phi[y] for y in worlds if (w[2],y[2]) in RTt)
def prod(phi,w): return bM(lambda x: bF(lambda y: bT(phi,y),x), w)
def bC(phi,w): return all(phi[y] for y in worlds if (w[0],y[0]) in RMm and (w[1],y[1]) in RFf
                                                and (w[2],y[2]) in RTt and cross(w,y))
phi={w:(w!=(('m1','f1','t1'))) for w in worlds}
w=('m1','f1','t1')
print("  □_M□_F□_T φ at w =", prod(phi,w))
print("  □_C φ        at w =", bC(phi,w))
print("  □_C strictly stronger than the layer-wise product:", prod(phi,w)!=bC(phi,w))
print("  => the layer-wise operators do NOT 'survive unchanged as a component' of □_C;")
print("     □_C^cross is never defined, so Definition 7's displayed equation is a")
print("     DEFINITION of □_C^cross, not a theorem about it.")
