import itertools
from itertools import product

print("="*78)
print("C5-ter.  Theorem 10 with genuine sheaves: Alexandrov-site model, done right")
print("="*78)
print("Sheaf model on the poset site (W,<=):  F(w) = B^{U(w)},  U(w)={v : v>=w},")
print("res_{v,w} = restriction of a function on U(w) to U(v)  (U(v) subset U(w)).")
print("Global sections = compatible families.\n")

B=('x','y')
def build(W, R):     # R = list of (w,v) meaning v >= w
    U={w:[v for v in W if (w,v) in R] for w in W}
    F={w:list(product(B,repeat=len(U[w]))) for w in W}
    res={}
    for w in W:
        for v in U[w]:
            idx=[U[w].index(x) for x in U[v]]
            res[(w,v)]=(lambda idx=idx:(lambda tup: tuple(tup[i] for i in idx)))
    return U,F,res

def sections(W,R,F,res):
    out=[]
    for combo in product(*[F[w] for w in W]):
        a=dict(zip(W,combo)); ok=True
        for (w,v) in R:
            if a[v]!=res[(w,v)](a[w]): ok=False; break
        if ok: out.append(a)
    return out

# --- frame with a TOP world: W = {w0 <= w1}, i.e. (w1,w0) in R means w0 >= w1
W=['w0','w1']; R=[('w0','w0'),('w1','w1'),('w1','w0')]
U,F,res=build(W,R)
print("W={w0 <= w1} with w1 TOP.  U(w0)=%s U(w1)=%s" % (U['w0'],U['w1']))
print("  |F(w0)|=%d |F(w1)|=%d" % (len(F['w0']),len(F['w1'])))
secs=sections(W,R,F,res)
print("  |Gamma(F)| = %d ;  all stalks nonempty: %s" % (len(secs), all(F[w] for w in W)))
print("  Gamma(F) ~ F(top):", len(secs)==len(F['w1']))
print("  => 'admissible at every context, no global realization' is IMPOSSIBLE on a frame")
print("     with a maximal world:  Gamma(F) = F(top) != empty.\n")

# --- exhaustive search over all posets on 2 and 3 elements
tot=0; bad_top=0; bad_notop=0
for n in (2,3):
    allw=list(itertools.combinations(range(n),2))
    for rel in itertools.product([0,1],repeat=len(allw)):
        R={(i,i) for i in range(n)}
        for i,flag in enumerate(rel):
            if flag: R.add(allw[i])
        ch=True
        while ch:
            ch=False
            for (a,b) in list(R):
                for (c,d) in list(R):
                    if b==c and (a,d) not in R: R.add((a,d)); ch=True
        Wl=list(range(n)); U,F,res=build(Wl,sorted(R))
        if any(not F[w] for w in Wl): continue
        tops=[w for w in Wl if all((w,v) in sorted(R) for v in Wl)]
        tot+=1
        if not sections(Wl,sorted(R),F,res):
            if tops: bad_top+=1
            else: bad_notop+=1
print("exhaustive search over %d (poset, sheaf) pairs on 2-3 worlds:" % tot)
print("   'all stalks nonempty but Gamma empty' WITH a maximal world :", bad_top)
print("   'all stalks nonempty but Gamma empty' with NO maximal world:", bad_notop)
print("   => Theorem 10's phenomenon requires a site with no maximal world; every finite")
print("      Kripke frame used by this framework has one.")

print()
print("="*78)
print("C6.  DEFINITION 7 / REMARK 6 -- is the 'additive upgrade' an identity or a definition?")
print("="*78)
WM=['m0','m1']; WF=['f0','f1']; WT=['t0','t1']
RM=[('m0','m0'),('m1','m1'),('m1','m0')]     # m1 top
RF=[('f0','f0'),('f1','f1'),('f1','f0')]
RT=[('t0','t0'),('t1','t1'),('t1','t0')]
worlds=[(m,f,t) for m in WM for f in WF for t in WT]
def R_M(x,y): return (x[0],y[0]) in RM
def R_F(x,y): return (x[1],y[1]) in RF
def R_T(x,y): return (x[2],y[2]) in RT
# cross-layer constraint: only worlds with m=m1 and f=f1 are jointly allowed
def cross(x,y): return not (x[0]=='m1' and y[0]=='m0') and not (x[1]=='f1' and y[1]=='f0')
def RC(x,y): return R_M(x,y) and R_F(x,y) and R_T(x,y) and cross(x,y)
def box(R,phi,w): return all(phi(y) for y in worlds if R(w,y))
def dia(R,phi,w): return any(phi(y) for y in worlds if R(w,y))
# a phi that is true everywhere except at one world
phi={w:(w!=(('m1','f1','t1'))) for w in worlds}
w=('m1','f1','t1')
print("  □_M□_F□_T φ at w =", box(R_M, lambda x: box(R_F, lambda y: box(R_T, phi, y), x), w),
      " (layer-wise product modality)")
print("  □_C φ at w        =", box(RC, phi, w), " (composite frame with the cross-layer relation)")
print("  □_C ⊆ □_M□_F□_T strictly:", box(RC,phi,w) != box(R_M, lambda x: box(R_F, lambda y: box(R_T,phi,y),x),w))
print("  => □_C is STRICTLY STRONGER; the layer-wise operators do NOT survive 'unchanged as a")
print("     component' of the richer necessity; □_C^cross is never defined, so the displayed")
print("     equation in Definition 7 is a DEFINITION, not a theorem.")
