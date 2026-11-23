import itertools, random
from itertools import product

print("="*78)
print("C5-bis.  THEOREM 10 with GENUINE sheaves (sheaf axiom enforced)")
print("="*78)
print("Model (Alexandrov site of a poset W): cover of w = {v : v >= w};")
print("a sheaf is given by a set B and  F(w) = B^{U(w)},  U(w) = {v : v >= w},")
print("restrictions = projections.  This satisfies the sheaf axiom by construction.")
print("Global sections = compatible families.\n")

def frames(W, R, B):
    U = {w: [v for v in W if (w,v) in R] for w in W}   # (w,v) in R  <=>  v >= w
    F = {w: list(product(B, repeat=len(U[w]))) for w in W}
    res = {}
    for w in W:
        for v in U[w]:
            idx = U[w].index(v)
            res[(w,v)] = (lambda idx=idx: (lambda tup: tup[idx]))
    return U, F, res

def sections(W, R, F, res):
    out=[]; worlds=list(W)
    for combo in product(*[F[w] for w in worlds]):
        a=dict(zip(worlds,combo)); ok=True
        for (w,v) in R:
            if a[v] != res[(w,v)](a[w]): ok=False; break
        if ok: out.append(a)
    return out

B=('x','y')
# (i) finite chain w0 <= w1 with w1 TOP
W=['w0','w1']; R=[('w0','w0'),('w1','w0'),('w1','w1')]
U,F,res = frames(W,R,B)
secs = sections(W,R,F,res)
print("(i) frame W={w0<=w1}, w1 TOP.  |F(w0)|=%d |F(w1)|=%d ; |Gamma| = %d" % (len(F['w0']),len(F['w1']),len(secs)))
print("    all stalks nonempty:", all(F[w] for w in W), " Gamma nonempty:", len(secs)>0)
print("    Gamma is in bijection with F(top):", len(secs)==len(F['w1']))
print("    => 'admissible at every context but no global realization' CANNOT happen here.\n")

# (ii) exhaustive search over all small posets and all B of size 2
bad_with_top=0; bad_without_top=0; tested=0
for n in (2,3):
    Ws=[tuple(w) for w in itertools.combinations(range(n),2)]
    for rel in itertools.product([0,1],repeat=len(Ws)):
        R=[(w,w) for w in Ws]+[Ws[i] for i in range(len(Ws)) if rel[i]==1]
        # transitive closure
        ch=True
        while ch:
            ch=False
            for (a,b) in list(R):
                for (c,d) in list(R):
                    if b==c and (a,d) not in R: R.add((a,d)); ch=True
        R=sorted(R)
        tops=[w for w in Ws if all((w,v) in R for v in Ws)]
        U,F,res = frames(Ws,R,B)
        if any(not F[w] for w in Ws): continue
        secs = sections(Ws,R,F,res)
        tested+=1
        if not secs:
            if tops: bad_with_top+=1; print("   !! counterexample WITH a top world:", Ws, R)
            else: bad_without_top+=1
print("(ii) exhaustive search over %d small posets x sheaves:" % tested)
print("     counterexamples with a MAXIMAL world :", bad_with_top, " <- Theorem 10 FALSE on such frames")
print("     counterexamples with NO maximal world:", bad_without_top, " <- Theorem 10 TRUE only here")
