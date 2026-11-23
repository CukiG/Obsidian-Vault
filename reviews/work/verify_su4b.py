import numpy as np
from collections import defaultdict
rng = np.random.default_rng(1)
print("="*78)
print("C2c-bis.  SU(4) with FULLY GENERAL eigenvalue sampling (fixing the earlier")
print("           degenerate sampling that pinned lambda_4 = 1)")
print("="*78)
buckets = defaultdict(list)
for _ in range(60000):
    a,b,c = rng.uniform(0,2*np.pi,3)
    l1,l2,l3 = np.exp(1j*a), np.exp(1j*b), np.exp(1j*c)
    l4 = 1.0/(l1*l2*l3)
    M = np.diag([l1,l2,l3,l4])
    assert abs(np.linalg.det(M)-1) < 1e-9
    buckets[round(np.trace(M).real,9)].append(np.round(np.poly(M),9).tolist())
split = [(k,v) for k,v in buckets.items() if len(set(map(tuple,v)))>1]
print("SU(4): trace-buckets that SPLIT into >1 characteristic polynomial:", len(split))
if split:
    k,v = split[0]
    cps = sorted(set(map(tuple,v)))
    print("  example trace bucket", k)
    for cp in cps[:3]:
        print("    chi(t) =", list(cp))
    print("  -> trace is NOT a complete conjugacy invariant in SU(4): CONFIRMED")

print()
print("="*78)
print("C3.  Conjugacy class vs holonomy: what information is LOST by [hol(gamma)]")
print("="*78)
# in SU(2): g and g^-1 are always conjugate  (=> the reversed loop has the same I_gamma)
th = 0.9
g = np.diag([np.exp(1j*th), np.exp(-1j*th)])
h = np.array([[0,1],[-1,0]], dtype=complex)      # Weyl element, det = 1
print("SU(2): det h =", np.linalg.det(h), " unitary:", np.allclose(h@h.conj().T, np.eye(2)))
print("h g h^-1 =", np.round(np.diag(h@g@h.conj().T),8), "  g^-1 =", np.round(np.diag(g.conj().T),8))
print("=> g ~ g^-1 in SU(2): [g] = [g^-1].  In SU(2) EVERY holonomy has the same class as its inverse.")
# eigenvalue multiset argument (general SU(n), n=2): {l, l^-1} invariant under inversion
print("eigenvalue multiset of g :", sorted([round(np.exp(1j*th).real,6), round(np.exp(-1j*th).real,6)]),
      "-> invariant under inversion => class of g = class of g^-1")
# SU(3): g ~ g^-1 does NOT hold in general
a,b = 0.3, 1.9
l1,l2 = np.exp(1j*a), np.exp(1j*b); l3 = 1/(l1*l2)
g3 = np.diag([l1,l2,l3])
m  = sorted([round(l.real,6) for l in [l1,l2,l3]])
mi = sorted([round((1/l).real,6) for l in [l1,l2,l3]])
print("SU(3) example: eigenvalues of g :", m, "  of g^-1:", mi,
      "  -> same multiset?", m==mi, " (g ~ g^-1 in SU(3) is NOT automatic)")
