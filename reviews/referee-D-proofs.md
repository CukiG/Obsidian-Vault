# Referee D — Proof-check report

**Paper:** "Holonomy, Constraint, and the Unity of Opposites: A Categorical Formalization of Indexical Identity", v1.0, MiniMax-M3 (MCode) with CukiG.
**Source checked:** `/workspace/output/paper/paper.md` (read in full, 915 lines) and the rendered `paper.pdf` (21 pp.) for display fidelity.
**Scope:** whether the proofs establish the stated results. Not a check of the metaphysics, and not a check of the unpublished "draft notes" (which are not supplied; every claim about the draft's content is therefore unverifiable by this referee).

---

## 0. Summary judgement

The computable mathematics is sound. Every algebraic figure I was able to recompute (the two SU(4) characteristic polynomials, the traces, the SU(3) trace-completeness argument, the group-algebra index, the Heaviside/derivative signs) checks out — with two exceptions, both in Theorem 23, both minor. The paper is *not* in trouble on arithmetic.

The trouble is elsewhere. The paper's hardest four claims — the descent obstruction (Thm 10), the "constraint adds nothing" result (Thm 11), the "essential/contingent is derived" claim (Prop 14), and the "curvature as descent obstruction" characterization (Thm 4) — are the four claims whose proofs are shortest and whose supporting machinery is least specified. In three of those four cases the proof either asserts the phenomenon without constructing it (Thm 10), presupposes what it is supposed to show (Thm 11(iii), Prop 14), or uses a mechanism the paper's own setup forbids (Thm 4's "commutator region", applied to a map the paper defines as a functor). Prop 14 additionally does not deliver what the abstract says it delivers.

Quantitative summary over the 25 numbered items + 6 secondary items: **6 PROVEN, 12 PROVEN WITH GAPS, 5 NOT PROVEN, 2 MISSTATED (plus 4 MISSTATED secondary/table items).**

---

## 1. VERDICT TABLE

| # | Item | Stated result (abbreviated) | Verdict | Severity | Minimal repair |
|---|---|---|---|---|---|
| 1 | Definition 1 | `I_γ := [hol(γ)] ∈ 𝔤/Ad`; `τ(I_γ) := Tr(hol(γ))` | GAPS | Minor | State that `hol(γ)` must lie in a matrix group (a representation of the label groupoid) for `τ` to be defined; for a general groupoid `τ` is undefined — the same ill-typedness the paper charges the draft with (§4.3). |
| 2 | Theorem 1(i) | `I_γ` independent of trivialization | **PROVEN** | — | none |
| 3 | Theorem 1(ii) | Homotopic (rel. basepoint) loops ⇒ `I_γ = I_γ'` | GAPS | Moderate | Replace the circular "which we assumed" clause with the actual lemma (transport along rel.-endpoint-homotopic paths is conjugate by the holonomy of the swept region, *under Wess–Zumino*); state that `hol` is not assumed a functor on `Π₁(M)`. |
| 4 | Theorem 1(iii) | `I_γ` determines the conjugacy class of `hol(γ)` | **PROVEN** (tautological) | — | none (but see note 2.3 on what this does *not* give) |
| 5 | Corollary 2 | "Pointer survives" every content-change preserving homotopy class | GAPS | Minor | Add: `hol` is a genuine connection; the "pointer" *is* the conjugacy class, which is coarser than a pointer, so the corollary yields *survival of a class*, not survival of the pointer. |
| 6 | Proposition 3 | Trace is not injective on SU(4) conjugacy classes ⇒ trace-condition is not well-formed | **PROVEN** (computation) / trailing sentence MISSTATED | Minor | Recomputed: correct. Replace the last sentence: the trace-condition is *well formed but weaker*; what is ill-typed is the draft's "up to equivalence" applied to a number. |
| 7 | Remark 3a | In SU(3) trace is a complete conjugacy invariant | **PROVEN** | — | none (recomputed) |
| 8 | Remark 3b | Characters complete only for special groups; need 2-traces | GAPS | Minor | Add the hypothesis actually needed for the framework: `𝔤` must be an (∞,1)-group, not the discrete groupoid of Part I; otherwise no 2-trace machinery is required (paper admits this in Limitations §4). |
| 9 | Abstraction condition | Identity-preserving ⇔ injection on conjugacy classes | **PROVEN** (well-formed definition) | — | none |
| 10 | Theorem 4 | Flat ⇔ `P̃` descends to `Π₁(M)` ⇔ "holonomy depends only on homotopy class"; obstruction = curvature | **MISSTATED + NOT PROVEN** | **High** | See §2.1. Define "flat" independently (e.g. via curvature / holonomy representation), drop the false "i.e." clause, and replace the "commutator region" argument (invalid for a functor) with the actual descent criterion. |
| 11 | Ambrose–Singer paragraph | Holonomy algebra is spanned by curvature | GAPS | Minor | State the hypothesis the framework violates: the structure group is discrete (`Lie(Sym(I))=0`), so no holonomy Lie algebra and no curvature 2-form exist; AS is inapplicable, not merely "related". |
| 12 | Theorem 5 (Frobenius) | `Σ_t` integrable ⇔ `[Σ_t,Σ_t] ⊆ Σ_t` | GAPS | Low–Moderate | State: `Q` smooth finite-dimensional, `P_t` a **smooth submersion** (so `Σ_t` is a smooth distribution), "integrable" = leafwise (immersed leaves; embeddedness needs extra hypotheses), fixed `t`. |
| 13 | Remark 6 | Over a product frame, `□_M□_F□_T φ ⟺ ∀w_M∀w_F∀w_T φ` | **PROVEN** | — | Add the hypothesis that `R` is the componentwise product relation and `□` is universal quantification (true here). |
| 14 | Definition 7 | Composite frame; `□_C φ ⟺ □_M□_F□_T φ ∧ □_C^cross φ` | GAPS | Low | Fix `𝔠`/`C` symbol collision; define `C(⋯)` and `□_C^cross`; show `R_C` is a preorder (reflexive/transitive), which the cross-constraint may destroy. |
| 15 | Definition 8 | Assembly as a subsheaf `A ↪ X` | **PROVEN** (definition) | — | none |
| 16 | Theorem 9 | Φ unrealizable at `u` ⇔ `A(u) = ∅` | **PROVEN** but vacuous | Low–Moderate | Either re-label as a definition, or replace with the substantive global statement (β* ⇔ `Γ(F_C,A) = ∅`, cf. §10). Local emptiness ≠ CTT impossibility, which is global. |
| 17 | Theorem 10 | `A(u) ≠ ∅ ∀u` does **not** imply `Γ(F_C,A) ≠ ∅` | **NOT PROVEN — and FALSE in the paper's own formalism** | **High** | See §2.2. Replace the frame site by a genuine topological/locale site with specified covers; state the obstruction as Čech `H¹`; supply an explicit example. Note `Γ(F_C,A) ≅ A(top)` on a frame site. |
| 18 | Theorem 11 | `A ↪ X` mono; constraint adds no dynamics/constructor/law/energy | NOT PROVEN (only the mono part) | **High** | See §2.3. The dynamics is never defined, so (ii) is uncheckable; (iii) is circular and imports "energy" into CTT. Delete (ii)–(iii) or supply a dynamics object and a non-circular CTT argument. |
| 19 | Theorem 12 | Unity of opposites = the pair `(Σ_t,[Σ_t,·])`; equilibrium = commutation | **NOT PROVEN** | Moderate | No proof, no formal statement, undefined notions ("commutes", "equilibrium", "lower dynamics"). Either formalise or demote to a Remark (it is absent from the paper's own status table). |
| 20 | Definition 13 | Essential / Contingent | GAPS | Low | Define "irrelevant" (`p ∉ A(u)` ∀u) and state the trichotomy; note `W_C ≠ ∅` is required for disjointness arguments. |
| 21 | Proposition 14 | Draft's modal formulas = Definition 13 ⇒ trichotomy is **derived** from the sheaf structure | **NOT PROVEN as a derivation** | **High** | See §2.4. Equivalence holds only if Φ holds at every context and accessibility is total; the trichotomy is a logical fact about *any* family `(A(u))`, using no sheaf hypothesis — the abstract's headline claim is unsupported. |
| 22 | Remark (assembly theory) | Assembly reading; `|A(u)|` = assembly number | GAPS | Minor | Fix the broken cross-reference "Remark 14" (no such remark exists); justify "strictly more informative". |
| 23 | Fact 16 | LT-topology ⇔ interior operator ⇔ geometric morphism `E→E` | GAPS / partly MISSTATED | Moderate | Replace the axioms with the standard ones (`j∘⊤=⊤`, `j∘j=j`, `j∘∧=∧∘(j×j)`); the pair `j∘j=j, u∘j=id` is insufficient (and `u∘j=id` is ill-typed); require `j` to be a *natural transformation*. |
| 24 | Modeling proposal 17 | Constraint induces an LT-topology; essential = interior | Correctly flagged as a proposal (not proved) | Low | Honest labelling; but it inherits the missing site structure of `Sh(F_C)` and needs `Sh(F_C)` to be a topos with an internal Heyting algebra. |
| 25 | Observation 19 | `G = Iso(1,3) ⋊ R⁴ × U(1) × P_∞` is a 2-group, "not a group" | GAPS | Moderate | Make conditional on `P_∞` being genuinely higher (Limitations §4 concedes this, the Observation does not); say "2-groupoid", not "2-group"; reconcile `G` with Part I's structure groupoid `𝔤`. |
| 26 | Consequence 20 | Draft's `|G/H| = dim_Hopf(C[G]⊗_{C[H]}C)` is "in the wrong category" | NOT PROVEN / partly MISSTATED | Moderate | See §2.5. The displayed identity is numerically **true** (`dim_C = [G:H]`, recomputed); the real defect is the "Hopf" decoration, not the formula. Also fix the 2-holonomy codomain (`P₂(M) → 𝔤` should be `→ G`, a 2-group). |
| 27 | Definition 21 | Breaking states form the `G`-set `G/H(α)` | **PROVEN** (definition) | — | none |
| 28 | Proposition 22 | `|G/H|` = multiplicity; #sectors = #conjugacy classes of `H` = #irreps | GAPS | Low–Moderate | Require `G`, `H(α)` **finite** for the counts and for "irreps ↔ conjugacy classes"; fix the proof's first sentence (`G/H` is a *single transitive* `G`-set, so the "disjoint union of orbits" argument does not apply to it); cite the character-theory fact. |
| 29 | Theorem 23 | Three corrections to the dimensional-explosion formulae | GAPS (1); NOT PROVEN as an identity (2); GAPS with a sign slip (3) | Moderate | (1) sound (add `α_i > 0`, `N = 7`). (2) only sign-consistency is shown; the `1/λ` factor is unjustified — Pesin does not supply it. (3) for the *corrected* `D`, `dD/dα = −Σ δ(α−α_i)`, not `+Σ δ`. |
| 30 | Observation 24 | Formal–final potential = material–efficient curvature; ladder reads `𝔊 = d𝒜+𝒜∧𝒜`, `ℋ = dℬ+ℬ∧ℬ` | **MISSTATED** | Moderate | See §2.6. The displayed ladder contradicts the paper's own renaming (Appendix A: `ℱ,𝔊,ℋ` correspond to `𝒜,ℬ,𝒞`), so the claim "potential of `n+1` = curvature of `n`" is not exhibited; the "…" hides the step where the pattern would have to appear. |
| 31 | Status table (11), rows 2, 5, 9 | "Theorem (proved)" etc. | MISSTATED | Moderate | Row 2 says "(SU(3) counterexample)" — the counterexample is **SU(4)**; SU(3) is the *completeness* case (Remark 3a). Rows 5 and 9 certify as proved items that are not (Thms 10, 11, 23). |
| 32 | Correction log (18), row 2 | "`SU(3)` counterexample" | MISSTATED | Minor | Same error as row 31; should read "SU(4) counterexample + SU(3) completeness argument". |
| 33 | Abstract; §11; §13; Authors' note | "every theorem is stated with a proof"; "essential/contingent is derivable rather than stipulated"; "labels applied consistently" | MISSTATED | **High** | Thm 12, Obs 19, Obs 24, Consequence 20 carry no proof; Thm 10's "proof" is an assertion; Prop 14 does not derive the distinction. |
| 34 | Cross-references | "Remark 14" (§10); "correction log (§9, §16)" (Contributors) | MISSTATED | Minor | There is no Remark 14 (the assembly remark is unnumbered); in the PDF's numbering the correction log is **§18** (Appendix C), not §16 (Appendix A, Notation). |
| 35 | Notation | Structure group `𝔤` (Part I) vs `G` (Part V) vs `G_c` (Appendix A) | MISSTATED | Moderate | Three different "G"s, never reconciled; Part V's "structure group" contradicts Part I's. This is the same defect the paper charges the draft with (Correction log row 5). |

---

## 2. DETAILED NOTES ON EVERY ITEM NOT FULLY PROVEN

### 2.1 Theorem 4 (paper.md:270–285) — MISSTATED + NOT PROVEN

**Stated.** Let `M` be a smooth manifold and `𝔤` a groupoid; parallel transport defines `P̃ : P(M) → 𝔤`. "The connection is **flat** iff `P̃` descends to a functor `Π₁(M) → 𝔤`, i.e. iff the holonomy of a loop depends only on its homotopy class. The obstruction to this descent is the curvature."

**Three separate defects.**

(a) *The first clause is a tautology, not a theorem.* "Flat" is **defined** by descent; then the theorem asserts the definition. The only genuine content is the second equivalence, which is (as shown below) false as worded.

(b) *The "i.e." clause is either vacuous or false.* Descent means `P̃` is constant on the fibres of `q : P(M) → Π₁(M)`; i.e. parallel transport along two **rel.-endpoint-homotopic paths** is **equal as arrows** in `𝔤` (not merely conjugate), for all paths, not just loops. The paper's gloss only demands that the holonomy of a loop depend on its homotopy class — and by **the paper's own Theorem 1(ii)** the holonomy *conjugacy class* is homotopy-invariant for **every** connection, flat or not. So if the gloss is read as the definition of flatness, the theorem degenerates to "every connection is flat", contradicting the theorem's own conclusion that curvature obstructs descent. If the gloss is read as a *consequence* of descent, it is a strictly weaker statement than descent, and the "iff" is wrong. Either way the "i.e." cannot stand.

(c) *The proof sketch's mechanism is invalid in the paper's setup.* The sketch says transport along `γ₁γ₂` equals transport along `γ₁` then `γ₂` "composed with transport around the 'commutator' region swept out by the deformation of `γ₁γ₂` into `γ₂γ₁`", and that "the difference is exactly the holonomy of that region". But `P̃` is **a functor** `P(M) → 𝔤` (paper.md:271–274), and a functor satisfies `P̃(γ₁·γ₂) = P̃(γ₂) ∘ P̃(γ₁)` **by definition**. There can be no extra "commutator-region" factor — the very category error the paper identifies in the draft at paper.md:266–268 ("a functor preserves composition by definition"). The genuine obstruction to descent is not a commutator term but the failure of *path-homotopy invariance* of transport; the sketch never mentions it. As written, the "proof" cannot distinguish flat from non-flat connections.

(d) *A further mismatch with the paper's own setup.* Part I defines "a connection" as **a functor `P : Π₁(M) → 𝔤`** (paper.md:156–160) — i.e. the framework *assumes* descent. Part II then develops a notion of curvature on `P(M)`, a different object. Part I has no flatness/non-flatness distinction at all: in Part I's setup every connection is flat by construction, so Theorem 4 cannot deliver the framework's "curvature" talk.

(e) *"The obstruction to this descent is the curvature"* — no object called "the curvature" is ever defined for a discrete groupoid connection; the paper itself notes `Lie(Sym(I)) = 0` (paper.md:293–296). So the theorem's punchline names an undefined object.

**Minimal repair.** Define flatness independently, e.g. *flat* := the holonomy defines a genuine representation `Π₁(M,x) → Aut(x)` **and** transport is invariant under rel.-endpoint homotopy; state the theorem as: `P̃` descends **iff** parallel transport along rel.-endpoint-homotopic paths is equal as arrows; prove it directly from the definition of descent (no commutator argument); delete the "i.e." clause or replace it with the correct (stronger) one; and say explicitly that for the discrete structure group the obstruction is a descent class, not a 2-form.

### 2.2 Theorem 10 (paper.md:393–400) — NOT PROVEN, and false in the paper's own formalism

**Stated.** "Φ may be admissible at every context and still have no global realization: `A(u) ≠ ∅` for all `u` does not imply `Γ(F_C,A) ≠ ∅`."

**Proof given.** "By the sheaf gluing lemma, global sections of a sheaf are determined by descent data, not by the non-emptiness of stalks. A sheaf may have non-empty sections over every context and fail to admit a global section, the obstruction being a nontrivial descent class of the site — in the appropriate sense, a first-cohomology class."

**(a) The phenomenon asserted is false on the site the paper actually uses.** `𝔉_C` is a **Kripke frame** (paper.md:350–355, 367–372): a preorder `W_C` with a top world. On the canonical site of a frame/preorder, a sheaf `A` satisfies `A(top) ≅ ∏_{u ≤ top} A(u)`, and the global-section functor is `Γ(𝔉_C, A) ≅ A(top)`. Consequently, if `A(u) ≠ ∅` for **all** `u ∈ W_C` — including `top` — then `Γ(𝔉_C, A) ≠ ∅` **always**. So the paper's displayed implication is false for the paper's own formalism. The phenomenon only exists for a sheaf on a genuine **space/locale with a non-trivial cover**, where `Γ` is not computed by the value at a top (e.g. `O(−1)` on `P¹`: local sections everywhere, `H⁰ = 0`; or the nowhere-vanishing sub-sheaf of the tautological bundle on `S¹`, whose obstruction is `H¹(S¹,ℤ) = ℤ`).

**(b) The "proof" is an assertion, not a proof.** "A sheaf may have non-empty sections over every context and fail to admit a global section" is the very statement to be established; no example is constructed, no hypothesis is checked, and the site (`𝔉_C`) is never specified (no coverage, no topology). The phrase "in the appropriate sense, a first-cohomology class" concedes that the obstruction has not been identified — and Čech `H¹` of the *cover* (not of the frame) is the correct object, which requires the cover to be specified.

**(c) Downstream damage.** §10 (paper.md:628–630) defines the corrected CTT impossibility indicator as `β*(Φ) = 1 ⟺ Γ(𝔉_C, A) = ∅` and calls it "the descent obstruction of Theorem 10". Since `Γ(𝔉_C,A) ≅ A(top)`, that formula is equivalent to "Φ is unrealizable at the top context" — a local emptiness condition, not a global descent obstruction. The CTT claim it is supposed to support is thus not delivered.

**Minimal repair.** Replace the frame site by a locale/topological site with an explicit cover `{u_i}`; state: *for a sheaf `A` on a site with cover `𝒰`, local sections on `𝒰` glue iff the Čech cocycle class in `H¹(𝒰, A)` vanishes*; give a worked example (the winding-number example the paper's own §2.3 preamble already describes, paper.md:126–134); and note explicitly that on a frame site `Γ(F,A) ≅ A(top)`, so the framework's modal site must be a locale, not a Kripke frame, if the claimed obstruction is to exist.

### 2.3 Theorem 11 (paper.md:402–414) — NOT PROVEN

**Stated.** "The constraint morphism `A ↪ X` is a monomorphism; the constraint restricts the set of realizable states without altering the dynamics on them, and without introducing a new degree of freedom, a new constructor, or a new law."

**Proof given.** (i) every element of `A(u)` was already in `X(u)`; (ii) "the transport structure on `X(u)` — the interval ladder of §3 — is the same object before and after imposing `A`; what changes is the *reachable set*, not the equations of motion"; (iii) a CTT argument: "possibility is a property of a task under the laws… A constraint that introduces no constructor and no law can only remove possibilities; it cannot add energy."

**(a) The monomorphism clause is trivially true** — `A` is *defined* as a subsheaf, so `A ↪ X` is an inclusion, hence a monomorphism in `Sh(𝔉_C)`. Fine, but it carries none of the advertised content.

**(b) Clause (ii) is uncheckable, because there is no dynamics in the formalism.** Nothing in the paper defines a transport structure, a flow, or equations of motion on `X(u)`. The "interval ladder" of §3 (paper.md:164–166) is a *heuristic list of three connection 1-forms*; it is never an object of `Sh(𝔉_C)`, and no map is given from it to the sheaf. "The same object before and after imposing `A`" is therefore a design intention, not a proposition. Note also the internal tension: restricting a state space *does* change the set of admissible trajectories, and (ii)'s "the equations of motion are unchanged" has no content until "equations of motion" is an object of the formalism.

**(c) Clause (iii) is circular and imports an energy concept that CTT does not have.** The conclusion drawn is "it cannot add energy"; the premise used is "a constraint that introduces no constructor and no law". That the constraint introduces no constructor and no law is *itself* the claim, and it is never established. CTT (Deutsch–Marletto 2014) is a theory of tasks and transformations; it has no notion of energy, and "cannot add energy" is therefore not a theorem of CTT but a slogan imported from outside. The passage from "removes possibilities" to "adds no energy" requires an energy-accounting model that the paper never supplies.

**(d) The §12(i) gloss inherits the defect.** "Theorem 11 shows it can be made into a precise claim about monomorphisms in a topos of sheaves" — the monomorphism part is a fact about inclusions; the "precise claim" about via negativa is the unsupported part.

**Minimal repair.** Keep (i). Either (a) introduce an explicit object — a flow/trajectory structure on `X` — and prove that `A ↪ X` restricts it without altering it (i.e. show the restricted system has the same vector field), or (b) delete (ii) and (iii) and restate Theorem 11 as the (true, trivial) statement that a constraint is a restriction of the possibility space, with the CTT correspondence offered as a *conceptual* remark rather than a proof step. Add "no energy" to the list of things not established.

### 2.4 Proposition 14 (paper.md:437–453) — NOT PROVEN as a derivation

**Stated.** The draft's formulas
`Essential(p,Φ) := □_M□_F□_T (Φ → p ∈ A(w_M,w_F,w_T))` and
`Necessary(p,Φ) := (Φ → p ∈ A) ∧ ◇_M◇_F◇_T (Φ ∧ p ∉ A)`
"are, on the composite frame, exactly Definition 13 — and the trichotomy {essential, contingent, irrelevant} is therefore **derived** from the sheaf structure rather than stipulated."

**Proof given.** "`□_M□_F□_T` over the composite frame quantifies over all contexts, giving `p ∈ A` at every `u`; `◇_M◇_F◇_T` quantifies existentially over contexts, giving presence at some and absence at another."

**(a) The proof silently drops the antecedent `Φ →`.** In Kripke semantics, `□_M□_F□_T (Φ → p ∈ A(...))` evaluated at `w` is `∀w' (accessible) [Φ(w') → p ∈ A(w')]`. That is a **conditional**: "`p ∈ A` at every world where `Φ` holds". Definition 13's `Essential(p,Φ)` is the **unconditional** `p ∈ A(u)` for all `u ∈ W_C`. The two coincide only if Φ holds at every context. The proof's gloss ("quantifies over all contexts, giving `p ∈ A` at every `u`") is true only of the *consequent*, and is obtained by dropping the antecedent. **Silent hypothesis:** Φ is true at every context (and `□` is evaluated at a world from which every context is accessible — i.e. the accessibility relation is total, so that the box ranges over all of `W_C`; if some world has no successors the box is vacuous there).

**(b) The second formula needs the same hypothesis.** `Necessary(p,Φ) := (Φ → p ∈ A) ∧ ◇(Φ ∧ p ∉ A)` gives, at the current world `w`: `Φ(w) → p ∈ A(w)`, plus `∃w'` with `Φ(w') ∧ p ∉ A(w')`. To obtain `∃u. p ∈ A(u)` (Definition 13's first conjunct) one needs `Φ(w)` to be **true** at the current world — otherwise the first conjunct is vacuous and supplies no witness at all. And the diamond conjunct delivers `∃u'. p ∉ A(u')` ✓ (with the extra condition `Φ(u')` that Definition 13 does not require). So: Draft-`Necessary` ⇒ Definition-13-`Contingent` under the hypothesis `Φ(w)`; and Definition-13-`Contingent` ⇒ Draft-`Necessary` fails whenever `Φ` fails at every world where `p ∈ A` (e.g. `p ∈ A(u)` only at worlds where `Φ` is false) — the equivalence is not symmetric.

**(c) The "derived from the sheaf structure" claim is false.** Definition 13's three-way split is a purely logical fact about *any* family of sets `(A(u))_{u∈W_C}`:
- Essential: `∀u, p ∈ A(u)`; Contingent: `∃u p ∈ A(u) ∧ ∃u' p ∉ A(u')`; Irrelevant: `∀u p ∉ A(u)`.
These are exhaustive and mutually exclusive for any non-empty index set, with **no use of the sheaf condition, no use of gluing, no use of `X`**. (Note the paper never defines "irrelevant", and never proves exhaustiveness/disjointness; and if `W_C` were empty the trichotomy degenerates — another silent hypothesis.) So the distinction is *stipulated* in Definition 13, and Proposition 14 shows that two stipulations (the draft's modal formulas and the paper's set-theoretic definitions) coincide. That is a consistency check between two definitions, not a derivation of a distinction from a structure.

**This directly contradicts the abstract's headline claim:** "We prove that the framework's central distinction between essential and contingent conditions is **derivable rather than stipulated**". Nothing in the paper derives the distinction from the constraint principle, the sheaf, or the via-negativa structure. This is the single most consequential gap in the paper, because it is the claim the abstract and §6.4's title ("Essential and contingent, **derived**") advertise.

**Minimal repair.** (i) State the two hypotheses explicitly (Φ true at every relevant context; accessibility total) and redo the equivalence with the antecedent retained. (ii) Replace "derived from the sheaf structure" with the accurate statement: "the draft's modal formulas are *equivalent to* the set-theoretic definitions of Definition 13; the trichotomy is a logical partition of `W_C` and uses no sheaf hypothesis." (iii) If the paper wishes to claim a genuine derivation, it must exhibit a structure (e.g. the LT-topology of Modeling proposal 17) from which the essential/contingent split *follows*, and prove it.

### 2.5 Consequence 20 (paper.md:510–527) — NOT PROVEN / partly MISSTATED

The paper asserts that the draft's computation `|G/H(α)| = dim_Hopf(ℂ[G] ⊗_{ℂ[H]} ℂ)` "is in the wrong category", and offers a table of "correct objects".

**Recomputation.** `ℂ[G]` is a free right `ℂ[H]`-module with basis a set of coset representatives, so `ℂ[G] ⊗_{ℂ[H]} ℂ ≅ ⊕_{[G:H]} ℂ` and therefore `dim_ℂ(ℂ[G] ⊗_{ℂ[H]} ℂ) = [G:H] = |G/H|`. Verified numerically for `ℤ/4` over `⟨2⟩` (2 = 2) and `S₃` over `A₃` (2 = 2). **The draft's displayed identity is numerically true.** The defect is the decoration "dim_Hopf": the induced module is not a Hopf-algebra invariant, and `dim_Hopf` is not a standard notion. So the paper's charge ("in the wrong category") is misaimed; the correct diagnosis is "right number, wrong justification/label".

Two further defects in the replacement table:
- "2-holonomy `hol : P₂(M) → 𝔤`" — the codomain of a 2-holonomy must be the **2-group** `G` (Baez–Schreiber 2004; the 2-holonomy of a principal 2-bundle is a morphism `P₂(M) → G`), not the ordinary groupoid `𝔤` of Part I. The table as printed is ill-typed.
- "group algebra `ℂ[G]` → Hopf object (comonoid in a cartesian monoidal category)" — the correct object in the higher setting is a **Hopf crossed module**; the paper does not verify that the replacement is well-formed, nor that the corrected formula exists.

**Minimal repair.** Say: "the numerical identity is correct; the 'Hopf' reading is not — `ℂ[G] ⊗_{ℂ[H]} ℂ` is an induced module whose dimension is `[G:H]`; in the 2-group setting the correct object is a Hopf crossed module and the correct holonomy is `P₂(M) → G` with `G` a 2-group."

### 2.6 Observation 24 (paper.md:606–616) — MISSTATED

**Claim.** "the formal–final potential *is* the material–efficient curvature. Renaming potentials `𝒜,ℬ,𝒞` and curvatures `ℱ,𝔊,ℋ`, the ladder reads `𝔊 = d𝒜 + 𝒜∧𝒜,  ℋ = dℬ + ℬ∧ℬ, …` so that the potential of interval `n+1` is the curvature of interval `n`."

**Defect 1 — the display contradicts the paper's own renaming.** The renaming is fixed at paper.md:535–539 and in Appendix A (paper.md:877–878): potentials `𝒜,ℬ,𝒞` = material–efficient, efficient–formal, formal–final; curvatures `ℱ,𝔊,ℋ` = "corresponding to the above". Hence `ℱ = d𝒜+𝒜∧𝒜`, `𝔊 = dℬ+ℬ∧ℬ`, `ℋ = d𝒞+𝒞∧𝒞`. Observation 24 instead prints `𝔊 = d𝒜+𝒜∧𝒜` and `ℋ = dℬ+ℬ∧ℬ` — i.e. it has shifted the curvatures by one, so that `ℱ` never appears and `ℋ` is the curvature of `ℬ`, not of `𝒞`. Verified against the rendered PDF (p. 13): the display is exactly as in the Markdown.

**Defect 2 — the displayed equations do not exhibit the claimed pattern.** The claim is "the potential of interval `n+1` is the curvature of interval `n`", i.e. `ℬ = ℱ`, `𝒞 = 𝔊`. The display contains no such identity; it relates curvatures to curvatures and the "…" hides exactly the step where the pattern would have to be shown. The claim in the first sentence ("the formal–final potential **is** the material–efficient curvature", i.e. `𝒞 = ℱ`) is likewise never written down.

**Defect 3 — type mismatch, unaddressed.** A potential is a 1-form, a curvature a 2-form, and the three intervals are three different bundles. `𝒞 = ℱ` is not a well-formed equation of fields without a specified identification (e.g. a bundle morphism), and no such map is given. This is the same class of defect (ill-typed identification) the paper charges the draft with in Correction-log row 2.

**Defect 4 — no proof, and no theorem.** This is an *observation about a table in the source notes*, which the reader cannot inspect. As a mathematical claim it has no formal content and no proof. The paper's own status table (§11) does not list it, although the Contributors table claims Observations 19 and 24 as proved work.

**Minimal repair.** Either (a) restate with the paper's own convention: `ℱ = d𝒜+𝒜∧𝒜`, `𝔊 = dℬ+ℬ∧ℬ`, `ℋ = d𝒞+𝒞∧𝒞`, and then state the *additional, unproved* claim `ℬ = ℱ`, `𝒞 = 𝔊` as an explicit hypothesis about the ladder, with the bundle map that makes it type-correct; or (b) demote to a Remark about the draft's notation, which is what it is.

### 2.7 Theorem 1(ii) (paper.md:190–201) — GAPS

Two problems. (i) The proof's second clause — "equivalently, `hol` factors through the fundamental groupoid `Π₁(M)`, **which we assumed**" — is circular: the framework defines "a connection" to *be* a functor `P : Π₁(M) → 𝔤` (paper.md:156–160). So in the framework's own setup, homotopy-invariance of the holonomy is an assumption, not a conclusion; and the paper then presents it as proved. (ii) The first clause ("the same up to conjugation by the holonomy of the region swept out") is a genuine standard lemma, but it is (a) not stated with its hypotheses (it needs the Wess–Zumino/parallel-transport axioms and a *nice* homotopy region, i.e. a disk), and (b) it is precisely the non-trivial content of the theorem, so "so conjugacy classes agree" conceals it. Note also that this lemma yields **conjugacy** invariance, not equality; the stronger statement needed for Theorem 4's descent is *equality* of transports along rel.-endpoint-homotopic paths, which is never stated.

### 2.8 Theorem 5 (paper.md:334–339) — GAPS

The statement is the classical Frobenius theorem and is true; the proof is a one-line citation. Hypotheses silently used: `Q` is a smooth finite-dimensional manifold; `P_t` is a **smooth submersion** (so `Σ_t = ker P_t` is a smooth distribution of constant rank `dim Q − dim 𝔤`); the bracket `[Σ_t,Σ_t]` is taken in `TQ`. Two refinements: (i) "integrable — it is the tangent distribution of a submanifold of `Q`" should be "each point lies in an **immersed** integral leaf"; embeddedness requires extra hypotheses (e.g. properness), and the whole distribution is the tangent distribution of **no single** submanifold in general. (ii) The theorem is per-fixed-`t`; integrability of each `Σ_t` separately does not produce a constraint surface persisting in time, which is the point the paper's own §6.3 global section makes — the statement should say so. (iii) The proof's phrase "applied to the holonomic distribution generated by `Σ_t`" is a misuse of "holonomic" (which in Pfaffian-system terminology means *completely integrable*, i.e. the conclusion). **Repair:** add the hypotheses, say "leafwise integrable", and cite Frobenius properly.

### 2.9 Theorem 9 (paper.md:388–391) — vacuous as stated

"Φ is unrealizable at context `u` iff `A(u) = ∅`" with the proof "Immediate from the definition of `A(u)` as the admissible realizations at `u`". This is a definitional identity, not a theorem, and the paper's label "(impossibility)" overstates it: in CTT, impossibility of a task is a **global** property of the laws, whereas `A(u) = ∅` is a *local* emptiness at one context. The paper itself later replaces the local condition with the global `Γ(𝔉_C,A) = ∅` (§10, paper.md:628–630) — so Theorem 9 and the CTT correspondence are about different things. **Repair:** re-label Theorem 9 as a definition, or state the global version as the theorem and drop the local one.

### 2.10 Theorem 12 (paper.md:422–429) — NOT PROVEN

No proof, no formal statement, and the terms are undefined: "the constraint distribution is built out of the lower dynamics" (the lower dynamics is nowhere defined — `P_t` is *given*, not derived from any dynamics); "its failure of commutation with those dynamics"; "equilibrium, in this reading, is the condition that the higher constraint commutes with the lower transport" (no definition of "commutes" between a distribution and a transport, and no object in the formalism that could be a "lower transport"). The item is a re-description of the dialectical claim in formal-looking vocabulary; it is also absent from the paper's own status table (§11). **Repair:** formalise (define the lower transport as an object, define commutation, prove the claimed equivalence) or demote it to a Remark — but then §12(ii)'s admission that the adjunctions have not been exhibited should be extended to it.

### 2.11 Fact 16 (paper.md:471–475) — partly MISSTATED axiomatisation

The substance is standard and correct: interior operators/nuclei on the internal Heyting algebra of a topos correspond bijectively to Lawvere–Tierney topologies, which correspond bijectively to geometric morphisms `E → E`. But the axioms as given are wrong:
- The standard axiomatisation is `j∘⊤ = ⊤` (or inflationary `a ≤ j(a)`), `j∘j = j` (idempotent), and `j∘∧ = ∧∘(j×j)` (meet-preserving). The paper gives only idempotence plus `u∘j = id` with `u : Ω → 1` — and `u∘j : Ω → 1` cannot equal `id : Ω → Ω`; as written the equation is ill-typed, and in any case the pair is **insufficient**: on a Boolean algebra, `j(a) = a ∨ p` (`p ≠ ⊤`) is inflationary and idempotent but not meet-preserving, hence not a nucleus/LT-topology.
- `j` must be a **natural transformation** (an `E`-morphism) for the geometric-morphism bijection; the paper says only "an idempotent operator `j : Ω → Ω`".
- "interior operator — equivalently a projection on a Heyting algebra" conflates the nucleus/projection/local-operator notion with the lattice-theoretic interior operator (double negation) of a Boolean algebra; for a *Boolean* algebra these are different maps.

**Repair:** state the three standard axioms, require naturality, and drop or qualify the "equivalently a projection" gloss.

### 2.12 Observation 19 (paper.md:503–508) — GAPS

(i) "A product of a Lie group with an ∞-groupoid is **not a group**" is false as stated: the product of a group with a groupoid is a groupoid, and with a *discrete* group it is a group. The claim needs "`P_∞` is genuinely higher". The paper concedes exactly this in Limitations §4 (paper.md:766–769) — but Observation 19 and the status table (row 7) state it as "proved, contingent", so the conditionality is visible only if the reader cross-reads. (ii) A product of a (1,1)-group with an (∞,1)-groupoid is an **(∞,1)-group / 2-groupoid**, not a "2-group" (which is one-object); the paper's own gloss "group-like (∞,1)-stack" is the right term, and the two glosses are used interchangeably. (iii) `G = Iso(1,3) ⋊ ℝ⁴ × U(1) × P_∞` is never used again: Part I's structure group is the groupoid `𝔤` of label re-labellings, and Proposition 22 uses a generic `G` with subgroups `H(α)` — the three are never reconciled, and `Iso(1,3)` already contains `ℝ⁴` in the usual convention, so the expression double-counts. **Repair:** state the hypothesis on `P_∞` in the Observation itself, fix the terminology, and reconcile (or rename) the three `G`s.

### 2.13 Proposition 22 (paper.md:549–555) — GAPS

The counting statement is right in spirit: `|G/H|` is the size of the orbit of the broken vacuum, i.e. its multiplicity, whereas the residual-symmetry sectors are the irreducible representations of `H` (for a **finite** `H`, in bijection with its conjugacy classes). But: (i) the proof's first sentence — "A `G`-set is a disjoint union of orbits, each isomorphic to `G/H(α)`; hence the cardinality counts copies of a single breaking pattern" — is a **non sequitur applied to the wrong object**: `G/H(α)` *is* a single transitive `G`-set, so it has exactly one orbit; the "disjoint union" argument applies to a general `G`-set, not to `G/H`. The correct argument: the state space is `⋃_i G/H_i` over breaking patterns `H_i`, so the pattern with stabilizer `H` contributes `[G:H]` copies. (ii) "the number of conjugacy classes of `H(α)`, equivalently the number of its irreducible unitary representations" requires `H(α)` to be **finite** (for a compact Lie group with continuous parameters, both counts are infinite and the correspondence is not a bijection); `G` must be finite for `|G/H|` to be a finite "count" at all. Neither is stated, and the character-theory fact is imported with no citation. (iii) In physics, the sectors of the broken theory are irreps of `H` (or of its double cover), not of `G`; the paper's Correction paragraph (paper.md:557–562) mentions the draft's alternative phrasing but does not settle it.

### 2.14 Theorem 23 (paper.md:579–603) — mixed

**(1) The step is negated — PROVEN.** Recomputed: with `Θ(α−α_i)` and `α_i > 0`, `D(α→0⁺) = 1` (not 8) and `D(α→∞) = 1+N` (not 1), so the draft formula contradicts *both* stated behaviours; with `Θ(α_i−α)`, `D(α→0⁺) = 1+N` and `D(α→∞) = 1` ✓. The repair requires **all `α_i > 0`** and `N = 7` to reproduce "↗8" — both unstated. The proof "Immediate from the monotonicity of `Θ`" is adequate for the monotonicity point, but the *reason* the physics demands the direction is the draft's own (unsourced) statement of the behaviour, and Limitations §3 concedes that the axis orientation is unsettled in the source material (paper.md:760–765). So (1) is a *consistency* repair relative to an unsettled premise, not a derivation.

**(2) The derivative's sign — the sign argument is CORRECT; the corrected formula is NOT established.** The chain of reasoning checks out: with the corrected `D`, `dD/dα < 0`; the breaking pattern gives `H(α) = G` at `α→∞` (`|G/H| = 1`) and maximal breaking at `α = 0` (`|G/H|` large), hence `|G/H|` decreases with `α` and `d/dα log|G/H| < 0`; the draft's RHS `−(1/λ)(<0) = >0` for `λ > 0`, so the two sides have opposite signs and the draft pair is indeed inconsistent. **But** sign-agreement is a *necessary*, not sufficient, condition for an identity: the corrected formula `dD/dα = +(1/λ) d/dα log|G/H|` asserts a quantitative relation between the slope of a step function and the log-derivative of an index, and **nothing in the paper derives the constant `1/λ` or the proportionality**. The citation of Pesin supplies at most a link between holonomy and Lyapunov exponents for geodesic flows on hyperbolic surfaces; it does not supply this identity. Theorem 23 therefore establishes only that the draft pair is *mutually* inconsistent and that a sign-flipped pair would be *sign-consistent*; it does not establish that the flipped pair is true.

**(3) The distributional character — correct in substance, with a sign slip.** `D` is a step function, so `dD/dα` is a distribution, not a pointwise function ✓. But for the **corrected** `D = 1 + Σ Θ(α_i − α)`, the distributional derivative is `dD/dα = −Σ_i δ(α − α_i)` (since `d/dα Θ(α_i−α) = −δ(α−α_i)`), whereas the paper writes `+Σ_i δ(α−α_i)` — the sign of the *draft's* formula. The paper's own §9.2 text (verified in the PDF, p. 12) carries this inconsistency. The two proposed escapes (smooth `D` via a sigmoid, or a coarse-grained reading) are reasonable.

**Repair.** Add `α_i > 0` and `N = 7`; restate (2) as "the sign of the draft's relation is incompatible with the corrected `D`; a sign-consistent replacement is …", and drop the claim that the replacement is *the* corrected formula (or supply a derivation of the `1/λ` factor); fix the sign in (3) to `−Σ δ(α−α_i)`.

### 2.15 Theorem 1(iii) / Corollary 2 — what they do and do not give

Theorem 1(iii) is correct but tautological (`I_γ` *is* the conjugacy class of `hol(γ)`). Corollary 2 follows from it. What is missing is any argument that the conjugacy class is a *sufficient* statistic for "which pointer am I tracking?". In the framework's own Part I setup the structure group is a groupoid of re-labellings of a finite label set `I`; the conjugacy class of a permutation is determined by cycle type, so distinct pointers share a class — the same lossiness the paper charges the *trace* (Proposition 3) is present in the *conjugacy class* the paper adopts. Proposition 3 shows the trace is a lossy shadow; it does **not** show the conjugacy class is lossless. The paper silently treats "not the trace" as "therefore the conjugacy class", which is a leap: the correct conclusion from Proposition 3 is only "the draft's formula `I_γ ≡ Tr(...)` is ill-typed and lossy", not "the conjugacy class is the right notion of indexical identity". Corollary 2's "the pointer survives" is therefore the survival of an equivalence class, not of a pointer. **Repair:** state that the identification of "pointer" with "conjugacy class" is an interpretive proposal (as Limitations §1 requires of every Definition), and note that the class is coarser than the pointer.

### 2.16 Remark 6, Definitions 7–8, Definition 13, Abstraction condition, Definition 21, Remark 3b, Remark (assembly theory) — minor gaps

- **Remark 6** is correct standard Kripke semantics (over a componentwise product frame, iterated box collapses to universal quantification over the product); add the hypothesis that `R_C` is the componentwise product relation.
- **Definition 7**: symbol collision `𝔠` vs `𝒞`; `𝒞(⋯)` and `□_C^cross` are undefined; and `R_C` need not be a preorder (reflexivity/transitivity) unless `𝒞` is chosen to be compatible — a hypothesis the frame "Kripke" label requires.
- **Definition 8**: fine, but the *site* (`coverage`) is never specified — the single omission with the widest blast radius, since Theorems 9, 10, 11 and Proposition 14 all live over `Sh(𝔉_C)`.
- **Definition 13**: "irrelevant" is never defined; the trichotomy is never stated, and its exhaustiveness/disjointness is never shown (both are easy, but they are exactly what the paper claims to have "derived").
- **Abstraction condition**: well-formed ✓, but the paper's claim that the draft's condition "was neither" well-formed is only true of the "up to equivalence" part.
- **Remark 3b**: correct as a pointer to the literature, but the framework's own structure group (Part I) is discrete, so the 2-trace remedy applies only under the `P_∞` hypothesis of Limitations §4.
- **Remark (assembly theory)**: the "strictly more informative" claim is not argued; and §10 cites "Remark 14", which does not exist.

---

## 3. INDEPENDENT RECOMPUTATION OF EVERY CHECKABLE COMPUTATION

All recomputed numerically (Python/NumPy, exact rational arithmetic where applicable) and by hand; the rendered PDF was checked for each displayed formula.

### 3.1 Proposition 3 — SU(4) matrices, traces, characteristic polynomials

`θ = arccos(3/4)`, `A = diag(e^{iπ/3}, e^{-iπ/3}, 1, 1)`, `B = diag(e^{iθ}, e^{-iθ}, e^{iθ}, e^{-iθ})`.

*Unitarity/determinants.* Entries unimodular ✓. `det A = e^{iπ/3}e^{-iπ/3} = 1` ✓. `det B = e^{iθ}e^{-iθ}e^{iθ}e^{-iθ} = 1` ✓ (the paper writes `e^{2iθ}e^{-2iθ}`, equal to 1 ✓). Numerically: `det A = 1.000+0i`, `det B = 1.000+0i` ✓.

*Traces.* `tr A = 2cos(π/3) + 2 = 1 + 2 = 3` ✓. `tr B = 4cos θ = 4·(3/4) = 3` ✓. Numerically both `= 3+0i` ✓.

*χ_A.* `(t − e^{iπ/3})(t − e^{-iπ/3}) = t² − 2cos(π/3)·t + 1 = t² − t + 1` ✓; `(t−1)² = t² − 2t + 1` ✓.
Product: `(t² − t + 1)(t² − 2t + 1) = t⁴ − 3t³ + 4t² − 3t + 1` — expand term by term:
`t⁴ − 2t³ + t² − t³ + 2t² − t + t² − 2t + 1 = t⁴ − 3t³ + 4t² − 3t + 1` ✓ **matches the paper**. Numerical: coefficients `[1, −3, 4, −3, 1]` ✓.

*χ_B.* `(t − e^{iθ})²(t − e^{-iθ})² = [(t − e^{iθ})(t − e^{-iθ})]² = (t² − 2cos θ·t + 1)² = (t² − (3/2)t + 1)²`.
Expand: `t⁴ − 3t³ + ((9/4) + 2)t² − 3t + 1 = t⁴ − 3t³ + (17/4)t² − 3t + 1` ✓ **matches the paper**. Numerical: `t²` coefficient `4.25 = 17/4` ✓.

*Conclusion.* Same trace (3), different characteristic polynomials ⇒ not conjugate in `U(4)`, hence not conjugate in `SU(4)` ⇒ distinct conjugacy classes with equal trace ✓. **Proposition 3's computation is correct as printed.** (Its trailing sentence about well-formedness is a mis-statement; see the table.)

### 3.2 Remark 3a — SU(3) trace-completeness

Let `λ₁λ₂λ₃ = 1`, `|λᵢ| = 1`, `s₁ = λ₁+λ₂+λ₃`, `s₂ = λ₁λ₂+λ₂λ₃+λ₃λ₁`, `s₃ = λ₁λ₂λ₃ = 1`.

`S := (λ₁λ₂λ₃)(1/λ₁ + 1/λ₂ + 1/λ₃) = λ₂λ₃ + λ₁λ₃ + λ₁λ₂ = s₂` ✓ (expanding each term: `(λ₁λ₂λ₃)/λ₁ = λ₂λ₃`, etc.).
Since `1/λᵢ = λ̄ᵢ` (unimodular) and `λ₁λ₂λ₃ = 1`: `S = λ̄₁+λ̄₂+λ̄₃ = s̄₁` ✓. Hence `s₂ = s̄₁` ✓ as the paper states.

Characteristic polynomial: `χ(t) = t³ − s₁t² + s₂t − s₃ = t³ − s t² + s̄ t − 1` with `s = s₁` ✓ **exactly as printed**.

Therefore the characteristic polynomial (hence the eigenvalue multiset, hence the `SU(3)`-conjugacy class, since `SU(3)` conjugacy classes are the Weyl-group orbits on eigenvalue multisets with product 1) is determined by the trace. **Remark 3a is correct.**

*Cross-check on the paper's SU(4) remark.* In `SU(4)`, `e₂ = Σ_{i<j} λᵢλ_j` is real but otherwise free: `e₂ = conj(e₂)` because `1/(λ₁λ₂) = λ₃λ₄` (product = 1, unimodular), so `conj(e₂) = Σ 1/(λᵢλ_j) = Σ (complementary pair products) = e₂` ✓. Numerically `e₂(A) = 4.0`, `e₂(B) = 4.25` — both real ✓, distinct ✓. So "the second symmetric sum is no longer forced; a second free parameter appears" is accurate (it is real-valued and free).

### 3.3 Consequence 20 — the group-algebra index

`ℂ[G]` as a right `ℂ[H]`-module is free with basis a transversal of the cosets of `H`; hence `ℂ[G] ⊗_{ℂ[H]} ℂ ≅ ⊕_{G/H} ℂ` and `dim_ℂ = [G:H] = |G/H|`. Verified numerically: `ℤ/4` over `⟨2⟩` → index 2 = 2; `S₃` over `A₃` → index 2 = 2. **The draft's displayed identity is numerically true**; the paper's charge that it "is in the wrong category" is misaimed (the defect is the "Hopf" decoration, not the formula). See §2.5.

### 3.4 Theorem 23(1) — Heaviside monotonicity and the "↗ 8 / ↘ 1" behaviour

Let `Θ` be the step, `α_i > 0`, `N` = number of breaking points.
Draft: `D_draft(α) = 1 + Σ Θ(α − αᵢ)`. Then `D_draft(0⁺) = 1 + ΣΘ(−αᵢ) = 1` (all `α_i>0`), and `D_draft(∞) = 1 + N`. So the draft formula gives `D → 1` as `α→0` and `D → 1+N` as `α→∞` — the **opposite** of both stated behaviours (`↗8` at `α→0`, `↘1` at `α→∞`). ✓ The paper's diagnosis is right, and in fact stronger than the paper states (it contradicts *both* behaviours, not just the asymptotic one).
Corrected: `D(α) = 1 + Σ Θ(αᵢ − α)`: `D(0⁺) = 1 + N`, `D(∞) = 1`, and `D` is non-increasing ✓. Reproducing "`D ↗ 8`" requires `N = 7` and `α_i > 0` for all `i` — **unstated**. ✓ Item (1) verified.

### 3.5 Theorem 23(2) — signs

With `D` corrected and decreasing: `dD/dα < 0` (between the steps) ✓.
Breaking pattern: `α→∞` ⇒ `G` unbroken ⇒ `H(α)=G` ⇒ `|G/H| = 1`; `α=0` ⇒ maximal breaking ⇒ `H(α)` small ⇒ `|G/H|` large. Hence `|G/H|` decreases with `α` ⇒ `d/dα log|G/H| < 0` ✓.
Draft RHS: `−(1/λ)·(<0) = >0` for `λ>0`; LHS `< 0` ⇒ opposite signs ⇒ the draft pair is inconsistent ✓. Sign-flipped RHS `(1/λ)·(<0) = <0` is sign-consistent with the LHS ✓.
**But** this establishes only sign-consistency; the identity itself (and the `1/λ` factor) is not derived anywhere. ✓ See §2.14.

### 3.6 Theorem 23(3) — distributional derivative

`d/dα Θ(αᵢ − α) = −δ(α − αᵢ)`, so for the **corrected** `D`, `dD/dα = −Σᵢ δ(α − αᵢ)`. The paper prints `+Σᵢ δ(α − αᵢ)` (paper.md:595; PDF p. 12) — the sign of the *draft's* `Θ(α−αᵢ)`. **Sign slip.** The point that `dD/dα` cannot equal a smooth function pointwise ✓ is correct.

### 3.7 Remark 6 — product-frame modality collapse

For `W = W_M×W_F×W_T` with `R = R_M×R_F×R_T` and `□` = universal quantification over successors:
`□_M□_F□_T φ(w_M,w_F,w_T) = ∀w_M'∀w_F'∀w_T' φ(w_M',w_F',w_T')` ✓ (each box substitutes the successor's own coordinates). So the collapse holds ✓, and the remark's inference — that a product frame cannot express cross-layer constraint through the modality — follows ✓. Note this is *independent* of the draft's cross-constraint; adding `𝒞` to `R_C` changes `□_C` but the *product* collapse still holds for the componentwise part, so Definition 7's `□_C` is a stipulation layered on top, not a derivation.

### 3.8 Proposition 22 — counting

`G/H` is a single transitive `G`-set with `|G/H| = [G:H]`; the multiplicity of the breaking pattern with stabilizer `H` in a state space `⋃_i G/H_i` is `[G:H]` ✓. For a **finite** `H`, irreps ↔ conjugacy classes is the standard character-theory theorem ✓ (finite hypothesis unstated in the paper). The proof's "disjoint union of orbits" sentence is inapplicable to `G/H` itself (see §2.13).

### 3.9 Theorem 5 / Frobenius — no computation; hypotheses check

The classical statement is correct as quoted, given that `Σ_t = ker P_t` is a smooth distribution of constant rank (which requires `P_t` to be a **smooth submersion** on a finite-dimensional smooth `Q` — the paper's source spec, paper.md:315–326, supplies "smooth family of submersions", but the Theorem's own statement does not). ✓

### 3.10 Cited literature checked

- **Ambrose–Singer**: the paper's statement — "the Lie algebra of the holonomy group is spanned by the images of the curvature map" — is a correct rendering of the theorem ✓. But the framework's structure group is discrete, so there is no holonomy Lie algebra; the paper notes `Lie(Sym(I)) = 0` itself ✓.
- **Lawvere–Tierney**: the standard axioms are `j∘⊤ = ⊤`, `j∘j = j`, `j∘∧ = ∧∘(j×j)` (nucleus/local-operator form); the bijection LT-topologies ↔ geometric morphisms `E→E` ✓ and nuclei ↔ subtoposes ✓. The paper's Fact 16 axiomatisation is therefore insufficient/ill-typed (see §2.11).
- **Zucchini 2015**: 2-traces over crossed modules ✓ as described.
- **Baez–Schreiber 2004 / Martins–Picken 2008**: fake curvature governs the existence of a 2-holonomy ✓; `P₂(M)` = path 2-groupoid, objects rank-1 homotopy classes, morphisms rank-2 ✓; but the 2-holonomy's codomain must be the 2-group `G`, not `𝔤` (paper.md:520).
- **Cronin et al. 2017**: assembly number = number of distinct ways of assembling ✓; "parts present in every pathway vs some" ✓ — consistent with the paper's reading.
- **Deutsch–Marletto 2014**: possibility/impossibility relative to the laws ✓; **no energy notion** — the paper's Theorem 11(iii) imports one.
- **Pesin 1978**: Lyapunov exponents ↔ entropy/holonomy of geodesic flows ✓; does **not** supply the `1/λ` factor in Theorem 23.
- **Hinton–Salakhutdinov 2006**: PCA feature layers ✓ as described.
- **Harlow–Ooguri 2002** ✓ as motivation.

---

## 4. SILENT HYPOTHESES — used in proofs, absent from statements

Ordered by damage.

**S1. (Theorem 10, and everything over `Sh(𝔉_C)`) The site structure (coverage/topology) of `𝔉_C` is never specified.** Without it, `Γ(𝔉_C,A)` is undefined in detail, and the claimed local-but-not-global phenomenon is *false* on the canonical frame site, where `Γ(F,A) ≅ A(top)`. Affects Theorems 9, 10, 11 and Proposition 14.

**S2. (Theorem 10) That "contexts" are atoms/opens of a space with a genuine cover, rather than Kripke worlds.** On a preorder/frame, global sections are determined by the top world; the phenomenon requires a locale/topological site.

**S3. (Theorem 14/Proposition 14) That Φ is true at every context (and that accessibility is total, so `□` ranges over all of `W_C`).** Without this, `□(Φ → p ∈ A)` is a conditional and Definition 13 is not equivalent to it; and the first conjunct of the draft's second formula yields no witness.

**S4. (Theorem 11) That a "transport structure"/dynamics exists on `X(u)` at all.** The paper's formalism contains none, so "the equations of motion are unchanged" is vacuous. Also (iii) requires that the constraint introduces no constructor and no law — the conclusion itself — and requires an energy model that CTT does not provide.

**S5. (Theorem 4) That `𝔤` is group-like and that "flat" is a property of the connection independent of descent.** Without an independent definition, the theorem is a tautology; with the paper's own "i.e." gloss, it implies every connection is flat (by Theorem 1(ii)). Also required: that "curvature" denotes some object, which for a discrete structure group does not exist.

**S6. (Theorem 5) That `Q` is a smooth finite-dimensional manifold, that `P_t` is a *smooth submersion* (hence `Σ_t` a smooth distribution of constant rank), and that "integrable" means leafwise/immersed rather than embedded.** Also that the statement is per-fixed-`t`.

**S7. (Theorem 1(ii)) That the connection satisfies the Wess–Zumino parallel-transport axioms and that the homotopy region is nice (a disk).** The conjugation-of-transports lemma is used without statement or citation. And the paper's "which we assumed" reveals that, in the framework's own setup, homotopy invariance is *assumed* (a connection is a functor on `Π₁(M)`), so (ii) is circular there.

**S8. (Definition 1 / Proposition 3) That `hol(γ)` is a matrix** (or that the label groupoid has a faithful finite-dimensional unitary representation), so that `Tr(hol(γ))` exists. For the framework's own discrete groupoid of permutations of `I`, "the trace" is undefined unless a representation is chosen — and the choice is not innocuous (the trace of the permutation matrix is the number of fixed points).

**S9. (Theorem 4 / Theorem 1) That the structure group admits conjugation by the gauge group** — i.e. that `g_x^{-1} hol(γ) g_x` is well-typed (`𝔤` a group, or `hol(γ) ∈ Aut(x)` with `g_x ∈ Aut(x)`).

**S10. (Proposition 22) That `G` and `H(α)` are finite**, for `|G/H|` to be a finite count and for "conjugacy classes ≡ irreducible unitary representations" to be a bijective statement.

**S11. (Observation 19) That `P_∞` is a genuinely higher (∞,1)-groupoid**, not a discrete group; otherwise the product *is* an ordinary group and the observation is false as written. (Limitations §4 admits this; the Observation and the status table do not.)

**S12. (Theorem 23) That all `α_i > 0` and that there are exactly seven of them** (to reproduce "`D ↗ 8`"); and that the axis orientation is fixed (Limitations §3 says it is not). Also that the `1/λ` factor is *somewhere* justified — it is not.

**S13. (Definition 7) That `𝒞` is compatible with the componentwise relations so that `R_C` is a preorder** (as a Kripke frame requires); and that `𝒞` and `□_C^cross` exist at all (symbols `𝔠`/`𝒞` collide and are never defined).

**S14. (Fact 16 / Modeling proposal 17) That `j` is a natural transformation** (an `E`-morphism), not merely an endomorphism of the internal Heyting algebra; and that `Sh(𝔉_C)` is a topos whose internal Heyting algebra carries the proposed `j` (the induced `j` is never exhibited).

**S15. (Definition 13) That `W_C ≠ ∅`** and that "irrelevant" is `p ∉ A(u)` for all `u` — needed for the trichotomy to be a partition.

**S16. (Consequence 20) That the draft's §7 is available.** The paper critiques a document it does not reproduce; no reader can check "the draft recorded …" against anything. Same for "the draft notes observed that 'F is reused…'", "the draft gloss", "the draft's β* = …".

**S17. (Corollary 2) That "the pointer" is identified with the conjugacy class** — an interpretive stipulation, not a hypothesis of the theorem; and the class is strictly coarser than a pointer, so the conclusion is *survival of a class*.

**S18. (Observation 24) That `𝒞` (a 1-form on the formal–final interval) may be equated with `ℱ` (a 2-form on the material–efficient interval)** — a type mismatch requiring a bundle map that is never given.

**S19. (Part V / Part I) That the `G` of Observation 19 and Proposition 22 is the same object as the structure groupoid `𝔤` of Part I.** They are different (one is a Lie group × ∞-groupoid, the other a groupoid of label re-labellings), and `G_c` (Appendix A) is a third. The paper never reconciles them, while charging the draft with exactly this defect (Correction log row 5).

---

## 5. OVERALL ASSESSMENT: IS "EVERY THEOREM IS PROVED" TRUE?

**No.** The claim is false as stated, in three distinguishable ways.

**(a) Four numbered items carry no proof at all.** Theorem 12 (no proof; undefined notions), Observation 19 (no proof; a definitional remark about products), Observation 24 (no proof; a remark about a table in an unpublished document), Consequence 20 (no proof; a table of "correct objects" with an incorrect diagnosis, §2.5). The paper's own §11 status table lists only nine of its twenty-five numbered items and omits Theorem 12 entirely.

**(b) Three items are asserted rather than proved.** Theorem 10's proof is the statement of the theorem ("a sheaf may have non-empty sections over every context and fail to admit a global section") plus "in the appropriate sense, a first-cohomology class"; and its claim is *false* in the formalism the paper itself sets up. Theorem 11's clauses (ii)–(iii) rest on a dynamics that is never defined and on a CTT argument that presupposes its conclusion. Proposition 14's proof drops the antecedent of the formula it is comparing, and the conclusion it advertises (that the trichotomy is "derived from the sheaf structure") is false: the trichotomy is a partition of `W_C` that uses no sheaf hypothesis.

**(c) The paper's headline claim is unsupported.** The abstract's "the framework's central distinction between essential and contingent conditions is **derivable rather than stipulated**" is not what Proposition 14 shows. Proposition 14 shows that two *stipulations* (the draft's modal formulas, and Definition 13) coincide under additional hypotheses. The distinction is stipulated in Definition 13 and remains stipulated. This is the most damaging finding, because it is the claim the abstract, the §6.4 title ("Essential and contingent, **derived**") and the §12 conclusions advertise.

**What is solid.** The arithmetic and the elementary mathematics. The SU(4) counterexample is exact and correctly computed; the SU(3) trace-completeness argument is correct; the group-algebra index is correct; the Heaviside/derivative sign analysis of Theorem 23 is correct in substance; Remark 6 is correct; Proposition 22's counting intuition is right; Theorem 5 is a correct citation of Frobenius. The paper is not padding with false mathematics; it is padding with *assertions dressed as proofs*, and — worse — it advertises those assertions as proved in its status table.

**Severity ranking of the five worst problems.**
1. **Theorem 10 is false in the paper's own formalism** (`Γ(𝔉_C,A) ≅ A(top)` on a frame site), and it is the source of the paper's corrected CTT impossibility indicator `β*(Φ) = 1 ⟺ Γ(𝔉_C,A) = ∅`.
2. **Proposition 14 does not deliver the abstract's central claim**; the proof drops the antecedent `Φ →`, the equivalence needs extra hypotheses, and the "derived from the sheaf structure" claim is false.
3. **Theorem 11(ii)–(iii) are uncheckable and circular** — there is no dynamics in the formalism, and the CTT step presupposes "no constructor and no law" in order to conclude it.
4. **Theorem 4 is mis-stated and its proof mechanism is invalid** (a commutator-region factor cannot appear for a map the paper defines as a functor), and it is the paper's replacement for the draft's curvature claim — i.e. the framework's Part II rests on it.
5. **Theorem 23(2) is a sign-consistency argument presented as a corrected formula**, and Theorem 23(3) carries a sign slip (`−Σδ` vs `+Σδ`); Consequence 20 and Observation 24 additionally misdiagnose/misstate their targets.

**Recommended disposition:** major revision. The proof apparatus is adequate for §4.1–§4.3 (except the `τ` typing) and §6.2; it must be rebuilt for §5 (Theorem 4), §6.3–§6.4 (Theorems 9–11, Proposition 14) and §9 (Theorem 23, Observation 24), and the site structure of `Sh(𝔉_C)` must be specified before any of §6.3–§6.4 can be assessed at all. The status table and the abstract must be brought into line with what is actually proved. The paper's own framing — "a metaphysics should be able to lose" — is the right standard; it simply has not yet been applied to the formalization.

---

*Prepared by Referee D. All line references are to `/workspace/output/paper/paper.md` as rendered in `paper.pdf` (21 pp.); every displayed formula quoted above was checked in both.*
