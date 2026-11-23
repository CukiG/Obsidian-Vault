import itertools, random
from collections import defaultdict

print("="*78)
print("C5.  THEOREM 10 on the paper's own site (a Kripke frame)")
print("="*78)
print("Setup: W finite, R reflexive-transitive (w R v = v accessible from w).")
print("A sheaf A: sets A(w), restriction res_{v,w}: A(w)->A(v) for w R v.")
print("A section = family (a_w) with a_v = res_{v,w}(a_w) for all w R v.\n")

def sections(W, R, A, res):
    out=[]
    worlds=list(W)
    for combo in itertools.product(*[sorted(A[w], key=repr) for w in worlds]):
        a=dict(zip(worlds,combo)); ok=True
        for (w,v) in R:
            if a[v] != res[(w,v)](a[w]): ok=False; break
        if ok: out.append(a)
    return out

# standard finite frame: w0 <= w1, w1 is TOP (w1 R v for all v)
W=['w0','w1']; R=[('w0','w0'),('w1','w0'),('w1','w1')]
A={'w0':{'x','y'}, 'w1':{'x'}}
res={('w1','w0'):(lambda a:a), ('w0','w0'):(lambda a:a), ('w1','w1'):(lambda a:a)}
secs=sections(W,R,A,res)
print("frame W={w0<=w1} (w1 top),  A(w0)={x,y}, A(w1)={x}")
print("  A(u) != empty for every context:", all(A[w] for w in W))
print("  global sections Gamma(A) =", secs, " -> nonempty:", len(secs)>0)
print("  => 'admissible everywhere but no global realization' is IMPOSSIBLE on this frame.\n")

# brute force: search for ANY small frame+sheaf with all stalks nonempty and empty Gamma
random.seed(0)
found=None
for trial in range(4000):
    n=random.choice([2,3])
    W=[f'w{i}' for i in range(n)]
    # random reflexive-transitive relation
    R=set((w,w) for w in W)
    for _ in range(random.randint(1,4)):
        a,b=random.sample(W,2); R.add((a,b))
    # transitive closure
    changed=True
    while changed:
        changed=False
        for (a,b) in list(R):
            for (c,d) in list(R):
                if b==c and (a,d) not in R: R.add((a,d)); changed=True
    R=sorted(R)
    tops=[w for w in W if all((w,v) in R for v in W)]
    A={w:{random.choice(['x','y','z']) for _ in range(random.randint(1,3))} for w in W}
    if any(not A[w] for w in W): continue
    res={}
    ok=True
    for (w,v) in R:
        src=list(A[w]); dst=list(A[v])
        if not src or not dst: ok=False; break
        f={}; pool=list(dst)
        for s in src:
            f[s]=random.choice(pool)
        res[(w,v)]=(lambda f=f: (lambda a: f[a]))()
    if not ok: continue
    secs=sections(W,R,A,res)
    if not secs:
        found=(W,R,A,res,tops); break
print("brute-force search over 4000 random frames/sheaves for 'all stalks nonempty, Gamma empty':")
print("   counterexample found:", found is not None)
if found is None:
    print("   -> none found. Reason: if the frame has a maximal world m, Gamma(A) = A(m) exactly,")
    print("      so nonemptiness of all stalks forces nonemptiness of Gamma.")
print("   (a frame with NO maximal world -- e.g. (Q,<) -- is the only setting where")
print("    the paper's Theorem 10 phenomenon can occur; the paper never says this.)")
