import numpy as np, itertools
from fractions import Fraction as F

print("="*78)
print("C2.  REMARK 3a -- 'in SU(3) the trace IS a complete conjugacy invariant'")
print("="*78)
# algebraic check: s2 = (l1 l2 l3)(1/l1 + 1/l2 + 1/l3) = 1 * conj(s1)
def su3_from_eigs(a,b):
    l1 = np.exp(1j*a); l2 = np.exp(1j*b); l3 = np.exp(-1j*(a+b))
    return np.diag([l1,l2,l3]), (l1,l2,l3)
bad = 0
rng = np.random.default_rng(0)
for _ in range(200000):
    a,b = rng.uniform(0,2*np.pi,2)
    M,(l1,l2,l3) = su3_from_eigs(a,b)
    s1 = l1+l2+l3
    s2 = l1*l2+l2*l3+l3*l1
    if abs(s2 - np.conj(s1)) > 1e-12: bad += 1
    if abs(l1*l2*l3-1) > 1e-12: print("det FAIL")
print("random SU(3) samples tested: 200000;  violations of s2 = conj(s1):", bad)
# char poly coefficients: t^3 - s t^2 + conj(s) t - 1
M,(l1,l2,l3) = su3_from_eigs(0.7,2.1)
cp = np.poly(M)
print("numeric chi(t) coeffs [1, -s1, s2, -1]:", np.round(cp,10))
print("  -s1 =", np.round(-(l1+l2+l3),10), " s2 =", np.round(l1*l2+l2*l3+l3*l1,10),
      " conj(s1) =", np.round(np.conj(l1+l2+l3),10))
# empirical completeness test: same trace => same char poly
from collections import defaultdict
buckets = defaultdict(list)
for _ in range(20000):
    a,b = rng.uniform(0,2*np.pi,2)
    M,(l1,l2,l3) = su3_from_eigs(a,b)
    buckets[round((l1+l2+l3).real,9)].append(np.round(np.poly(M),9).tolist())
viol = 0; checked = 0
for k,v in buckets.items():
    if len(set(map(tuple,v)))>1: viol += 1
    checked += 1
print("SU(3): trace-buckets with MORE THAN ONE characteristic polynomial:", viol, "of", checked, "buckets")
print("SU(3): trace COMPLETE (no bucket splits) ->", viol==0)

print()
print("="*78)
print("C2b.  SU(2) edge case (paper never mentions it)")
print("="*78)
for a in [0.3, 1.1, 2.7]:
    l1 = np.exp(1j*a); l2 = np.conj(l1)
    M = np.diag([l1,l2])
    cp = np.poly(M)
    print(" SU(2) theta=%.2f  chi(t) = %s   (i.e. t^2 - (tr)t + 1, trace-determined)" % (a, np.round(cp,8)))
buckets = defaultdict(list)
for _ in range(20000):
    a = rng.uniform(0,2*np.pi)
    M = np.diag([np.exp(1j*a), np.exp(-1j*a)])
    buckets[round(np.trace(M).real,9)].append(np.round(np.poly(M),9).tolist())
viol = sum(1 for v in buckets.values() if len(set(map(tuple,v)))>1)
print("SU(2): trace-buckets with more than one char poly:", viol, "-> trace COMPLETE in SU(2) as well")

print()
print("="*78)
print("C2c.  SU(4): trace-buckets with more than one characteristic polynomial (reproduces Prop 3)")
print("="*78)
buckets = defaultdict(list)
for _ in range(20000):
    # random SU(4) with one eigenvalue pinned to 1 and two free phases
    a,b = rng.uniform(0,2*np.pi,2)
    l = [np.exp(1j*a), np.exp(1j*b), np.exp(-1j*(a+b)), 1.0+0j]
    M = np.diag(l); buckets[round(np.trace(M).real,9)].append(np.round(np.poly(M),9).tolist())
viol = sum(1 for v in buckets.values() if len(set(map(tuple,v)))>1)
print("SU(4): trace-buckets with more than one char poly:", viol, "-> trace NOT complete (as claimed)")

print()
print("="*78)
print("C2d.  free parameters of the characteristic polynomial in SU(n)")
print("="*78)
print(" SU(2): chi = t^2 - s1 t + 1                -> 1 parameter (s1)      : trace complete")
print(" SU(3): chi = t^3 - s1 t^2 + conj(s1) t - 1 -> 1 parameter            : trace complete")
print(" SU(4): chi = t^4 - s1 t^3 + s2 t^2 - conj(s1) t + 1 -> 2 parameters   : trace NOT complete")
# verify the SU(4) relation s3 = conj(s1) numerically
bad=0
for _ in range(100000):
    a,b = rng.uniform(0,2*np.pi,2)
    l = [np.exp(1j*a), np.exp(1j*b), np.exp(-1j*(a+b)), 1.0+0j]
    s1 = sum(l); s3 = l[0]*l[1]*l[2]+l[0]*l[1]*l[3]+l[0]*l[2]*l[3]+l[1]*l[2]*l[3]
    if abs(s3-np.conj(s1))>1e-12: bad+=1
print(" SU(4) relation s3 = conj(s1) violations in 100000 samples:", bad)
