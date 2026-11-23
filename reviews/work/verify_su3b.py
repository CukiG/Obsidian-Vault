import numpy as np
rng = np.random.default_rng(7)
print("="*78)
print("C2c-ii.  CONSTRUCTIVE test: is the trace a complete conjugacy invariant in SU(3)?")
print("="*78)
print("For a fixed trace s, every SU(3) triple (l1,l2,l3) with prod=1 must satisfy")
print("  l2+l3 = s - l1 and l2*l3 = 1/l1, so l1 must satisfy |s - l1| = |1/l1| = 1.")
print("Solve for all such l1 on the unit circle, build each triple, compare char polys.\n")
bad = 0; tested = 0; maxsplit = 0
for _ in range(4000):
    a,b = rng.uniform(0,2*np.pi,2)
    l1,l2 = np.exp(1j*a), np.exp(1j*b); l3 = 1/(l1*l2)
    s = l1+l2+l3
    # |s - l1| = 1 with |l1| = 1  ->  Re(l1 conj(s)) = |s|^2/2  (from |s-l1|^2=1)
    # write l1 = e^{i t}:  |s|^2 - 2 Re(s e^{-it}) + 1 = 1  ->  Re(s e^{-it}) = |s|^2/2
    st = s
    # solve  Re(s e^{-it}) = |s|^2/2  =>  |s| cos(arg(s) - t) = |s|^2/2
    r = abs(st); target = r*r/2
    if r == 0: continue
    c = target/r
    if abs(c) > 1+1e-12: continue
    c = min(max(c,-1),1)
    phi = np.angle(st)
    t1 = phi - np.arccos(c); t2 = phi + np.arccos(c)
    cps = set()
    for t in (t1,t2):
        m1 = np.exp(1j*t)
        # m2,m3 = roots of z^2 - (s-m1) z + 1/m1
        B = s - m1; C = 1/m1
        disc = np.sqrt(B*B - 4*C)
        for m2 in (B+disc)/2, (B-disc)/2:
            if abs(abs(m2)-1) < 1e-9:
                m3 = C/m2
                if abs(abs(m3)-1) < 1e-9:
                    cps.add(tuple(np.round(np.poly(np.diag([m1,m2,m3])),8)))
    tested += 1
    if len(cps) > 1:
        bad += 1; maxsplit = max(maxsplit, len(cps))
print("triples examined:", tested, " with >1 characteristic polynomial:", bad, " (max distinct:", maxsplit,")")
print("=> trace IS a complete conjugacy invariant in SU(3):", bad == 0)

print()
print("="*78)
print("C2e.  g ~ g^-1 ? (does I_gamma distinguish a loop from its reverse?)")
print("="*78)
def conj_closure(eigs):
    s = sorted([complex(round(v.real,6),round(v.imag,6)) for v in eigs])
    c = sorted([complex(round(v.real,6),round(-v.imag,6)) for v in eigs])
    return s == c
l2 = [np.exp(1j*0.9), np.exp(-1j*0.9)]
l3 = [np.exp(1j*0.3), np.exp(1j*0.5), np.exp(-1j*0.8)]
l4 = [np.exp(1j*np.pi/3), np.exp(-1j*np.pi/3), 1+0j, 1+0j]
print(" SU(2) {e^{i.9},e^{-i.9}} closed under conjugation:", conj_closure(l2), "-> g ~ g^-1 ALWAYS in SU(2)")
print(" SU(3) {e^{i.3},e^{i.5},e^{-i.8}} closed under conjugation:", conj_closure(l3), "-> g ~ g^-1 NOT automatic in SU(3)")
print(" SU(4) paper's A closed under conjugation:", conj_closure(l4), "-> A ~ A^-1 (the paper's own counterexample element!)")
