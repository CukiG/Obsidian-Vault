import numpy as np
from fractions import Fraction as F
print("="*78)
print("C4-bis.  Is Theorem 23's corrected pair compatible with the framework's own numbers?")
print("="*78)
print("Framework numbers: D: 8 -> 1  =>  exactly 7 unit steps; |G/H|: 8 -> 1.")
print("The corrected identity  dD/dα = +(1/λ) d/dα log|G/H|  read distributionally forces")
print("  (i) the 7 step locations to coincide, and")
print("  (ii) EVERY breaking step to satisfy  log(n_i/n_{i+1}) = λ, i.e. n_i/n_{i+1} = e^λ = r")
print("  for a single constant r.  With 7 steps: 8 = r^7  =>  r = 8^(1/7) = %.6f" % (8**(1/7)))
r = 8**(1/7)
print("  then the intermediate coset counts must be 8/r, 8/r^2, ... :")
vals = [8/r**k for k in range(8)]
print("   ", [round(v,4) for v in vals])
print("  these are NOT integers (nor are they integers for any k>=2), so for a genuine")
print("  coset count |G/H| (an integer index) the corrected identity CANNOT hold:")
bad = all(F(8,1)/F(int(round(v*10**9)),10**9) for v in [])  # placeholder
from math import isclose
integers = [v for v in vals if isclose(v, round(v), rel_tol=1e-9)]
print("  intermediates that are integers:", integers, "-> none (for k>=1):", integers==[])
print()
print("  Conclusion: the corrected identity is compatible with D:8->1 over 7 steps ONLY if")
print("  the coset 'count' is allowed to be a non-integer quantity (e.g. a measure/volume).")
print("  With |G/H| an integer index (as Prop 22 treats it), the identity is FALSE.")
print()
print("  Also: the smooth antiderivative with the asymptotic D->1 forces the constant C=1:")
for lam in [np.log(2), np.log(8)/7]:
    print("   λ=%.4f : D(0) = 1 + log(8)/λ = %.4f   (framework claims D->8)" % (lam, 1+np.log(8)/lam))
print("   => with C=1 the corrected relation reproduces D->8 only for λ = log8/7 exactly,")
print("      and then only because log|G/H| is itself a step function (piecewise constant),")
print("      so the 'differential' relation is not a differential relation at all.")
