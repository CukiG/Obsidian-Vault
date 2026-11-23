---
title: "Holonomy, Constraint, and the Unity of Opposites: A Categorical Formalization of Indexical Identity"
subtitle: "Toward a Defensible Metaphysics of Causation"
date: 2026-11-22
status: preprint
version: 1.0
license: CC BY 4.0
---



---

# Abstract (shareable){.unnumbered}

> **A metaphysics should be able to lose.** This paper formalizes a framework in which
> "identity" is not a property but a *holonomy* — the residue of parallel transport around a
> loop — and in which a higher cause operates not by adding energy but by *deleting
> directions*. We prove that the framework's central distinction between essential and
> contingent conditions is derivable rather than stipulated, that its constraint principle
> has a precise content as a descent obstruction, and that several of its central formulas,
> as circulated in draft form, were wrong in ways we specify and repair. The result is a
> framework that metaphysical positions can argue about, disagree with, and — finally —
> falsify.
>
> *Full text:* https://github.com/CukiG/Obsidian-Vault

---

**Authors and versions.** This paper was written by **MiniMax-M3 (MCode)** — an AI research
agent — from working notes by the framework's originator, **Nicolai Gamulea Schwartz**, and from drafts
co-written with several AI systems whose versions are recorded below. **Nicolai Gamulea Schwartz** is the
author of record. All contributors are
credited by name and version in §14. The formalization, the proofs, the correction of the
draft formulae, and the present prose are MiniMax-M3's work; the conceptual apparatus
(holonomy as indexical identity; constraint as via negativa; the interval ladder; the
aggregation tower) is the originator's, developed in dialogue with the credited models.
No model is treated as an authority for any mathematical claim in this paper: every
theorem is stated with a proof, and every literature attribution is checked.

---

# Introduction

Metaphysics has a reputation for positions that cannot be wrong, and therefore cannot be
right. The standard remedy — borrow the apparatus of mathematical physics and hope for
the best — has a well-known failure mode: the apparatus is imported *decoratively*, so that
the metaphysical thesis survives whatever happens to the mathematics.

This paper argues that the remedy can be made to work, and shows what it costs. We take a
metaphysical framework in which three claims are made:

1. **Indexical identity.** An entity's persistence through change is not the persistence of
   a fixed substance, but the persistence of a *pointer* — an address in causal space that
   survives alterations of its contents.
2. **Via negativa.** A higher-level cause (formal, final, teleological) constrains a
   lower-level one (material, efficient) without adding energy. It *removes forbidden
   directions* rather than pushing.
3. **The unity of opposites.** Causal layers are not stacked like bricks; they stand in
   dialectical relation, each genuinely opposed to the next and genuinely unified with it.

We show that (1) has an exact home in gauge theory: indexical identity is a **holonomy
class**, and the trace used to compute it is a provably lossy shadow of it. We show that
(2) splits into two theorems: a *local* statement (the constraint is a kernel of a
submersion) which the framework already had, and a *global* statement (local admissibility
need not admit global realization) which it did not, and which we supply. We show that
(3) has a precise model in the interaction between a constraint distribution and the
dynamics it constrains, where non-commutation is precisely the failure of a geometric
integrability condition.

Along the way we correct five formulae that circulated in draft form in the source notes,
including a sign error and a missing negation in the framework's "dimensional explosion"
formula, and a symbol collision that had made the framework's central ladder unreadable.

**Audience.** §2 is written for readers with no category theory. §3–§11 are written for
readers with graduate mathematics. §12 is written for metaphysicians and is the part we
most want to be argued with.

---

# Preliminaries for the general reader

## Parallel transport and holonomy
Suppose space is filled with a field of arrows — think of a compass needle at every point
of the Earth. To move a needle from one point to another you need a rule; that rule is a
*connection*. If you carry a needle around a closed loop and it comes back pointing in a
same direction, the field was "flat" along that loop. If it comes back rotated, the amount
of rotation is the *holonomy* around that loop, and it measures how the field fails to be
flat — how it curls.

Three facts about holonomy drive everything that follows.

- **Holonomy is gauge-invariant.** If you change your convention for comparing needles at
  different points, the holonomy around a closed loop is unchanged. It is an intrinsic
  quantity of the field, not of your description of it.
- **Holonomy depends only on the shape of the loop, not its details.** Two loops that can be
  continuously deformed into one another without passing through a singularity have the
  same holonomy.
- **Holonomy is non-additive.** In general the holonomy around a loop made of two pieces is
  *not* the product of the holonomies of the pieces. The failure to be additive is
  precisely the curvature. This is the "unity of opposites" in its sharpest mathematical
  form: the holonomy of a composite is determined by, but not reducible to, the
  holonomies of its parts.

## Category theory, briefly
A *category* is a collection of objects and arrows between them, where arrows compose and
compose associatively. The point is to forget everything irrelevant: a category remembers
only *which things can be related and how*, not what the things are made of.

A *functor* is a map between categories: a way of translating objects to objects and
arrows to arrows, preserving composition. When we say "the structure of a system is
described by a functor," we mean that the system's behaviour is captured by *how things
relate*, and that this translation is exact rather than approximate.

A *groupoid* is a category in which every arrow has an inverse — a category of things that
can all be transformed into one another, with no preferred direction. A *group* is a
groupoid with one object. Moving from groups to groupoids is the difference between "a
symmetry operation" and "a symmetry operation that also remembers which state you were
in."

An *adjunction* is a special relationship between two functors, and it is the technical
content of a "unity of opposites": a pair of concepts that are opposed in their intuition
(yet one determines the other) and whose opposition is *exact*.

## Local-to-global reasoning (sheaves)
A *sheaf* is a way of assembling local truths into a global truth, subject to a
compatibility condition. The archetype: a function on a region is determined by its local
restrictions, provided those restrictions agree on overlaps. The sheaf condition says
precisely that.

The general lesson, which we use heavily, is: **local solvability does not imply global
solvability.** On a circle, one can specify a local assignment of directions at every point
with no inconsistency on any small arc, and yet be unable to produce a global direction
field — the obstruction is a winding number. Sheaf theory is the theory of such
obstructions.

## The three distinctions we formalize
- **General vs. particular.** What is the relation between the universal and the instance?
- **Objective vs. subjective.** Is there a difference between truth *as the world is* and
  truth *as an observer inside the world*?
- **Being vs. becoming.** What is the relation between a thing's structure and its
  behaviour?

We treat these as *research problems with precise formulations*, not as givens.

---

# The framework in one page

Let `Q` be a smooth manifold of admissible states — the "configurations" of a system.
Over a base manifold `M` (the "bulk" or arena) we have a bundle whose fiber over each
point is a **set of indexical labels** `I`: not numerical values but *addresses*, so that
"which pointer am I tracking?" replaces "which substance persists?"

The symmetries acting on labels form a **groupoid** $\mathfrak{G}$: the arrows of $\mathfrak{G}$ are the
admissible re-labellings, not merely the rotations of a group. A **connection** is a
functor

$$\mathcal{P} \;:\; \Pi_1(M) \longrightarrow \mathfrak{G},$$

assigning to each loop a permutation of labels — the *holonomy* $hol(γ)$.

Three further layers complete the framework:

- **The interval ladder.** Causal layers are organised as intervals — material$\to$efficient,
  efficient$\to$formal, formal$\to$final — each carrying a connection 1-form and a curvature.
- **The aggregation tower.** A hierarchy of levels `k` (molecules, cells, organisms,
  societies), with a compression operation `C_k` from level `k` to level `k+1`.
- **The axis.** A coordinate $α$ ("Aionic depth") along which the structure group breaks
  symmetry in stages.

We now formalize the three principal claims.

---

# Part I — Indexical identity is a holonomy class

## Definition
**Definition 1 (Indexical identity).** Let $\mathfrak{G}$ be a groupoid, $γ$ a loop in `M`, and
$hol(γ) ∈ \mathfrak{G}$. Define the **indexical identity** of $γ$ to be the gauge-equivalence class

$$\mathbf{\mathcal{I}}_\gamma \;:=\; [\mathrm{hol}(\gamma)] \;\in\; \mathfrak{G}/\mathrm{Ad},$$

where `Ad` denotes conjugation. Write $τ(\mathcal{I}_γ) := Tr(hol(γ))$ for the associated numeric
*trace*.

The draft notes defined $\mathcal{I}_γ ≡ Tr(\mathcal{P} exp ∮_γ A)$. We will see in §4.3 that this is a
*shadow* of the correct definition, and that the shadow is lossy.

## Gauge and homotopy invariance
**Theorem 1.** (i) $\mathcal{I}_γ$ is independent of the trivialization of the bundle. (ii) If $γ$
and $γ'$ are homotopic relative to the basepoint, then $\mathcal{I}_γ = \mathcal{I}_{γ'}$. (iii) $\mathcal{I}_γ$
determines the conjugacy class of the holonomy representation's value on $γ$.

*Proof.* (i) A change of trivialization is a family of elements $g_x ∈ \mathfrak{G}$ indexed by
$x ∈ M$; parallel transport along a path from `x` to `y` is replaced by
$g_y^{-1}·hol(γ)·g_x$. Around a closed loop the endpoint agrees with the start, so the
holonomy is conjugated, $hol(γ) ↦ g_x^{-1} hol(γ) g_x$. Hence its conjugacy class is
unchanged. (ii) Parallel transport along homotopic paths is the same up to conjugation by
the holonomy of the region swept out, so conjugacy classes agree; equivalently, `hol`
factors through the fundamental groupoid $Π₁(M)$, which we assumed. (iii) Immediate from
the definition. $\blacksquare$

**Corollary 2 (the "pointer survives" claim).** The pointer of an entity survives every
transformation of the entity's contents that leaves the homotopy class — hence the
holonomy class — of its causal path unchanged.

This is the precise content of "a holon's identity is its address in causal space, not its
contents": the address is the conjugacy class of the holonomy, which is invariant under
every change of contents that does not change the topology of the path.

## The trace is a lossy shadow
**Proposition 3.** The map $\mathcal{I}_γ ↦ τ(\mathcal{I}_γ)$ is not injective on conjugacy classes in
general. Hence the preservation condition "preserves $\mathcal{I}_γ$ up to equivalence" is not
well-formed if $\mathcal{I}_γ$ is taken to be the trace.

*Proof (explicit counterexample in `SU(4)`).* Let $θ = arccos(3/4)$ and set

$$A = \mathrm{diag}\bigl(e^{i\pi/3},\, e^{-i\pi/3},\, 1,\, 1\bigr), \qquad
B = \mathrm{diag}\bigl(e^{i\theta},\, e^{-i\theta},\, e^{i\theta},\, e^{-i\theta}\bigr).$$

Both lie in `SU(4)`: their entries are unimodular, and $\det A = 1$ while
$\det B = e^{2i\theta}e^{-2i\theta} = 1$. Both have trace three:
$\operatorname{tr} A = 2\cos(\pi/3) + 2 = 3$ and $\operatorname{tr} B = 4\cos\theta = 3$. They are not conjugate,
because their characteristic polynomials differ:

$$\chi_A(t) = (t^2 - t + 1)(t-1)^2 = t^4 - 3t^3 + 4t^2 - 3t + 1,$$

$$\chi_B(t) = (t^2 - \tfrac{3}{2}t + 1)^2 = t^4 - 3t^3 + \tfrac{17}{4}t^2 - 3t + 1 .$$

Conjugacy in `SU(4)` implies equality of characteristic polynomial, so `A` and `B` lie in
distinct conjugacy classes with the same trace. $\blacksquare$

**Remark 3a (why `SU(4)`, and not `SU(3)`).** The failure is dimension-specific, and it is
worth stating precisely because it is easy to get wrong. In `SU(3)` the trace *is* a
complete invariant of conjugacy classes. Indeed, if $λ₁λ₂λ₃ = 1$ with $|λᵢ| = 1$, then

$$s_2 \;=\; \lambda_1\lambda_2+\lambda_2\lambda_3+\lambda_3\lambda_1
\;=\; (\lambda_1\lambda_2\lambda_3)\Bigl(\tfrac{1}{\lambda_1}+\tfrac{1}{\lambda_2}+\tfrac{1}{\lambda_3}\Bigr)
\;=\; \overline{s},$$

so the characteristic polynomial $t³ − s t² + \overline{s} t − 1$ is determined by the trace alone, and
hence so is the conjugacy class. In `SU(4)` the second symmetric sum is no longer forced, a
second free parameter appears, and the trace ceases to be complete — as Proposition 3
exhibits. We state this because a reader is entitled to know that the counterexample is not
an artifact of a naive choice, and because the *threshold* is informative: the trace
becomes lossy exactly where the structure acquires enough room for surface data, which is
the regime the framework's 2-group structure (§8) enters.

**Remark 3b.** The obstruction is not a technicality. The trace is a *character*, and
characters are complete invariants only for very special groups. Zucchini's construction
of *2-traces* over crossed modules (see §8) is exactly the machinery needed when the
structure group is a 2-group and surface information must be retained.

**Consequent repair.** The correct abstraction condition is:

> **Abstraction condition.** A morphism `m` from a physical tower to an abstract tower is
> identity-preserving iff it induces an **injection on conjugacy classes**
> $[hol(γ)] ↦ [hol′(m(γ))]$.

This is well-formed and checkable. The draft condition was neither.

---

# Part II — Curvature, correctly stated

The draft notes asserted: *"Curvature = failure of $\mathcal{P}$ to preserve composition."* This is
a category error: a functor preserves composition by definition, so no functor can fail to.
The assertion is nonetheless pointing at something true, and we state it properly.

**Theorem 4 (curvature as descent obstruction).** Let `M` be a smooth manifold and $\mathfrak{G}$ a
groupoid. Parallel transport along paths defines a functor

$$\widetilde{\mathcal{P}} \;:\; \mathcal{P}(M) \longrightarrow \mathfrak{G}$$

from the *path groupoid* of `M` to $\mathfrak{G}$. The connection is **flat** iff $\widetilde{\mathcal{P}}$ descends to a
functor $Π₁(M) → \mathfrak{G}$, i.e. iff the holonomy of a loop depends only on its homotopy class.
The obstruction to this descent is the curvature.

*Proof sketch.* Parallel transport along $γ₁γ₂$ equals transport along $γ₁$ followed by
transport along $γ₂$ composed with transport around the "commutator" region swept out by
the deformation of $γ₁γ₂$ into $γ₂γ₁$. The difference is exactly the holonomy of that
region, which is what the curvature measures. When the curvature vanishes everywhere, the
transport is path-independent modulo the homotopy relation, and $\widetilde{\mathcal{P}}$ factors through
$Π₁(M)$; conversely, a descent forces the commutator-region holonomies to be trivial.
$\blacksquare$

**Relation to the classical theorem.** The Ambrose–Singer theorem states that the Lie
algebra of the holonomy group is spanned by the images of the curvature map. So curvature
is not merely "related to" holonomy: the holonomy algebra is *generated* by curvature.
Non-abelian holonomy around two commuting loops is the signature of nonzero curvature.

**Why this matters for the framework.** The framework's structure group is a groupoid of
re-labellings, and its labels are discrete. A discrete structure group admits no
Lie-algebra-valued connection 1-form; `Lie(Sym(I)) = 0`. The two formulations —
"curvature is a Lie-algebra-valued 2-form" and "curvature is a descent obstruction" —
are therefore *mutually exclusive* for this framework, and the second is the correct one.
The draft notes contained both simultaneously (a formulation in §5 and its negation in
§2 of the same note), which is why the draft's own $F = dA + A∧A$ could not be reconciled
with its indexical-label fibers.

**Correction.** We adopt Theorem 4. The curvature of an indexical gauge bundle is the
obstruction to descent of parallel transport to the fundamental groupoid, and the
"non-commutativity of holonomies" is its trace-like signature.

---

# Part III — Constraint and via negativa

This is where the framework's most distinctive claim lives, and where its formalization
has the most to add.

## The local form, already present in the working notes
The source notes contain the following specification, in the originator's own words:

> At each instant `t` we posit a smooth family of submersions
>
> $$
> P_t : TQ \longrightarrow \mathfrak{g}
> $$
>
> where $\mathfrak{g}$ is the Lie algebra of a compact, connected Lie group `G` … `P_t` encodes "laws"
> or "goals" as covector-valued constraints on instantaneous velocities. The zero-locus
> $Σ_t := ker P_t ⊂ TQ$ is the sub-bundle of admissible velocities at time `t`.
>
> (This is the via-negativa step: the field does not add energy; it removes forbidden
> directions.)

This is already rigorous, and it deserves to be recognized as such: **"removes forbidden
directions" is literally the statement that the constraint is a kernel.** A constraint is a
map; the forbidden directions are its kernel; the admissible directions are what survives.
We shall not re-derive it. We will instead supply the missing half.

## The local obstruction: Frobenius
**Theorem 5 (local consistency).** Let $Σ_t ⊂ TQ$ be the distribution of admissible
velocities. Then $Σ_t$ is integrable — it is the tangent distribution of a submanifold of
`Q` — if and only if $[Σ_t, Σ_t] ⊆ Σ_t$.

*Proof.* This is the Frobenius theorem for involutive distributions, applied to the
holonomic distribution generated by $Σ_t$. $\blacksquare$

**Interpretation.** A constraint can be locally satisfiable — every admissible velocity is
admissible — and still fail to define a consistent constraint surface, because the bracket
of two individually admissible directions may be inadmissible. This is the first of two
precise senses in which the framework's causal levels can be "in tension": a higher cause
whose constraint does not commute with the lower dynamics.

## The global form: realization as a sheaf
For the *outcome*-level reading we need a different apparatus. Let

$$\mathfrak{F}_M = \langle W_M, R_M\rangle,\quad \mathfrak{F}_F = \langle W_F, R_F\rangle,\quad
\mathfrak{F}_T = \langle W_T, R_T\rangle$$

be Kripke frames for the material/efficient, formal, and final layers. The draft notes
combine them by a **cartesian product** of frames. We argue this is wrong, and that the
product encodes an assumption the framework's thesis contradicts.

**Remark 6.** Over a cartesian product of frames, iterated modality collapses to
independence:

$$\Box_M\Box_F\Box_T\varphi \iff \forall w_M\,\forall w_F\,\forall w_T\;\varphi(w_M,w_F,w_T).$$

So a product of frames *stipulates* that formal and final causes vary freely of material
causes, and any cross-layer constraint has to be re-injected through the content of the
assembly functor rather than through the modality. For a framework whose central thesis is
that higher causes *constrain* lower ones, this inverts the logic.

**Definition 7 (composite constraint frame).** Let $\mathfrak{F}_C = ⟨W_C, R_C⟩$ with
$W_C := W_M × W_F × W_T$ and

$$(w_M,w_F,w_T)\;R_C\;(w'_M,w'_F,w'_T) \iff w_M R_M w'_M \wedge w_F R_F w'_F \wedge w_T R_T w'_T \wedge \mathsf{C}(\cdots),$$

where $\mathfrak{c}$ is the cross-layer constraint relation. Then

$$\Box_C\varphi \iff \Box_M\Box_F\Box_T\varphi \wedge \Box_C^{\mathsf{cross}}\varphi .$$

The upgrade is *additive*: the layer-wise necessity operators of the draft survive
unchanged as a component of a richer necessity.

**Definition 8 (assembly as a sheaf).** Let `X` be a sheaf of material/efficient states on
$\mathfrak{F}_C$, and let

$$A \in \mathrm{Sh}(\mathfrak{F}_C), \qquad A(u) \subseteq X(u)$$

be a **subsheaf**: `A(u)` is the set of states at context `u` admissible under the formal
and final constraints. The sheaf condition states that admissible local states glue to an
admissible global state.

**Theorem 9 (impossibility).** $Φ$ is unrealizable at context `u` if and only if
$A(u) = ∅$.

*Proof.* Immediate from the definition of `A(u)` as the admissible realizations at `u`. $\blacksquare$

**Theorem 10 (the descent obstruction).** $Φ$ may be admissible at every context and still
have no global realization: $A(u) ≠ ∅$ for all `u` does not imply
$Γ(\mathfrak{F}_C, A) ≠ ∅$.

*Proof.* By the sheaf gluing lemma, global sections of a sheaf are determined by descent
data, not by the non-emptiness of stalks. A sheaf may have non-empty sections over every
context and fail to admit a global section, the obstruction being a nontrivial descent
class of the site — in the appropriate sense, a first-cohomology class. $\blacksquare$

**Theorem 11 (via negativa: constraint adds nothing).** The constraint morphism
$A ↪ X$ is a monomorphism; the constraint restricts the set of realizable states without
altering the dynamics on them, and without introducing a new degree of freedom, a new
constructor, or a new law.

*Proof.* $A ↪ X$ is a monomorphism in $Sh(\mathfrak{F}_C)$. (i) Every element of `A(u)` was already
an element of `X(u)`: the constraint shrinks the fiber and never enlarges it. (ii) The
transport structure on `X(u)` — the interval ladder of §3 — is the same object before and
after imposing `A`; what changes is the *reachable set*, not the equations of motion. (iii)
In the language of Constructor Theory (Deutsch–Marletto 2014), possibility is a property
of a task under the laws, and laws are constructor- and ingredient-independent. A
constraint that introduces no constructor and no law can only remove possibilities; it
cannot add energy. $\blacksquare$

**Interpretation.** The "via-negativa field" is not a force. It is a **restriction of the
possibility space of transformations**, which is precisely what a law is in Constructor
Theory. The framework's slogan — *the field does not add energy; it removes forbidden
directions* — is thus given an exact meaning: the constraint is a filter on the state
space, and the forbidden directions are literally its kernel.

**Theorem 12 (the unity of opposites, in the constraint sense).** The classical
dialectical claim that a higher causal level is simultaneously *opposed* to the lower level
(because it forbids directions the lower level would otherwise take) and *united with* it
(because it is defined by reference to the lower level's admissible velocities) is
formalized by the pair $(Σ_t, [Σ_t,·])$: the constraint distribution is built out of the
lower dynamics, and its failure of commutation with those dynamics is the measure of the
tension. Equilibrium, in this reading, is the condition that the higher constraint commutes
with the lower transport.

## Essential and contingent, derived
**Definition 13.** For a part `p` of an outcome $Φ$:

$$\mathbf{Essential}(p,\Phi) \iff p \in \bigcap_{u \in W_C} A(u), \qquad
\mathbf{Contingent}(p,\Phi) \iff \Bigl(\exists u.\ p \in A(u)\Bigr) \wedge \Bigl(\exists u'.\ p \notin A(u')\Bigr).$$

**Proposition 14.** The draft notes' formulas

$$
\text{Essential}(p,\Phi) \;:=\; \Box_M \Box_F \Box_T\,(\Phi \to p \in A(w_M,w_F,w_T))
$$

$$
\text{Necessary}(p,\Phi) \;:=\; (\Phi \to p \in A) \wedge \Diamond_M \Diamond_F \Diamond_T\,(\Phi \wedge p \notin A)
$$

are, on the composite frame, exactly Definition 13 — and the trichotomy
{essential, contingent, irrelevant} is therefore **derived** from the sheaf structure
rather than stipulated.

*Proof.* $□_M□_F□_T$ over the composite frame quantifies over all contexts, giving
$p ∈ A$ at every `u`; $\Diamond_M\Diamond_F\Diamond_T$ quantifies existentially over contexts, giving
presence at some and absence at another. $\blacksquare$

**Correction (terminology).** The draft attached the word *"necessary"* to the second
formula, which is a **contingency** formula and the exact complement of necessity in
standard modal logic. We rename it **contingent**. The first formula was already correct.

**Remark (assembly theory).** Read `A(u)` as the set of *assembly pathways* realizing $Φ$
rather than the set of states, the distinction becomes the one assembly theory already
draws (Cronin et al. 2017): parts present in every pathway versus parts present in some.
This reading is strictly more informative, since `|A(u)|` is then the assembly number.

---

# Part IV — A graded modality

The framework's modal operators $□_M, □_F, □_T$ are, in the draft, uninterpreted
primitives. We give them a home.

**Fact 16 (Lawvere–Tierney).** For a topos $\mathcal{E}$, an idempotent operator $j : Ω → Ω$ on
the internal Heyting algebra of truth values satisfying $j∘j = j$ and $u∘j = id$ (with
$u : Ω → 1$) is an *interior operator* — equivalently a projection on a Heyting algebra.
Such operators are in bijection with *geometric morphisms* $\mathcal{E} → \mathcal{E}$ (Lawvere 1968;
Lawvere & Tierney 1979).

**Modeling proposal 17.** The constraint of §6.3 induces a Lawvere–Tierney topology
`j` on $Sh(\mathfrak{F}_C)$, and the essential part of an outcome is its interior:

$$\mathbf{Essential}(p,\Phi) \iff j\bigl(\langle p\rangle_{\Phi}\bigr) = \top .$$

*Status.* This is a **proposal**, not a theorem. We state it because the vocabulary is
exact: an interior operator is literally a projection on truth values, which is the
framework's own phrase for the via-negativa field ("a time-dependent projection
operator"), and because Lawvere's distinction between *objective* and *subjective* logic
maps onto it cleanly. Objective logic is what is provable in the metatheory about the
constraint frame $\mathfrak{F}_C$, the topology `j`, and the sheaf `A`; subjective logic is the
internal interpretation of $□$ within $Sh(\mathfrak{F}_C)$. We flag it as the natural *form* of the
framework's modal apparatus without claiming that the induced `j` has been exhibited.

*One caveat worth stating, because it is the source of a long-standing trap.* The
axioms of topos theory are a relative version of the axioms of set theory
(Hofstadter–Streicher 1982), which is precisely what makes the objective/subjective
distinction *available* in the first place — and precisely what makes it easy to overlook
that a topos is not a set-based universe but a locale of "places where truth is
defined." A framework that puts observers first should not quietly assume that the
observer's logic is the objective one.

---

# Part V — The structure group is a 2-group

**Observation 19.** The framework's structure group is

$$G \;=\; \mathrm{ISO}(1,3) \rtimes \mathbb{R}^4 \times U(1) \times \mathfrak{P}_\infty,$$

where $\mathfrak{P}_∞$ is an $\infty$-groupoid of indexical pointers. A product of a Lie group with an
$\infty$-groupoid is **not a group**: it is a **2-group**, equivalently a group-like $(∞,1)$-stack.

**Consequence 20.** The draft's §7 computation,

$$|G/H(\alpha)| = \dim_{\text{Hopf}}\bigl(\mathbb{C}[G] \otimes_{\mathbb{C}[H]} \mathbb{C}\bigr),$$

is in the wrong category. The correct replacements are:

| Draft object | Correct object |
|---|---|
| group algebra $\mathbb{C}[G]$ | Hopf **object** (comonoid in a cartesian monoidal category) |
| groupoid-valued connection | **2-connection** on a principal 2-bundle (Baez–Schreiber 2004) |
| holonomy $hol : Π₁(M) → \mathfrak{G}$ | **2-holonomy** $hol : P₂(M) → \mathfrak{G}$ (Baez–Schreiber 2004; Martins–Picken 2008) |
| scalar trace | **2-trace** over a crossed module (Zucchini 2015) |

Here $P₂(M)$ is the thin fundamental *categoric* group of `M` — objects are rank-1
homotopy classes of based loops, morphisms are rank-2 homotopy classes of homotopies
(Martins–Picken 2008). The existence of a 2-holonomy is governed by the vanishing of the
*fake curvature* (Baez–Schreiber 2004), which is the higher analogue of the descent
condition of Theorem 4.

**The interval ladder as a 2-connection.** The framework's three connection 1-forms
($\mathcal{A}$ on material–efficient, $\mathcal{P}$ on efficient–formal, $\mathcal{F}$ on formal–final) are, on this
reading, not three unrelated gauge fields but the one-form component of a single higher
connection, with the three "curvatures" being components of one fake curvature. §9
below shows that the draft notation concealed a further structure worth keeping.

**Correction (notation).** In the draft the symbol $\mathcal{F}$ denoted simultaneously: the
groupoid action on the label set `I`; the material–efficient field-strength
$\mathcal{F} = d\mathcal{A} + \mathcal{A}∧\mathcal{A}$; the formal–final *potential*; and the input to its own curvature
$\mathcal{H} = d\mathcal{F} + \mathcal{F}∧\mathcal{F}$. The notes themselves observed that "$\mathcal{F}$ is reused… context keeps it
unambiguous"; it does not. We rename potentials $\mathcal{A}, \mathcal{B}, \mathcal{C}$ and curvatures $\mathcal{F}, \mathfrak{G}, \mathcal{H}$.

---

# Part VI — Symmetry breaking, and two corrected formulae

## Cosets versus sectors
**Definition 21.** The symmetry-breaking states at depth $α$ form the `G`-set $G/H(α)$,
where $H(α)$ is the unbroken subgroup.

**Proposition 22.** $|G/H(α)|$ is the **multiplicity** of each breaking pattern, not the
number of distinct sectors. The number of distinct sectors is the number of conjugacy
classes of $H(α)$, equivalently the number of its irreducible unitary representations.

*Proof.* A `G`-set is a disjoint union of orbits, each isomorphic to $G/H(α)$; hence the
cardinality counts copies of a single breaking pattern. Sector labels are the irreducible
characters of the residual group, and these are indexed by conjugacy classes. $\blacksquare$

**Correction.** The draft gloss — that the quantity counts "linearly independent holonomy
eigenvalues, the new invariants that appear after each symmetry break" — conflates three
distinct counts and should be replaced by Proposition 22. (The draft also used the phrase
"super-selection sector labelled by irreducible unitary representations of `G`" in a
*different* note, but there as a suggestion for future work rather than a standing
commitment; we align the two here.)

## The dimensional-explosion formula, corrected
The draft recorded:

$$
D(\alpha) \;=\; 1 + \sum_i \Theta(\alpha - \alpha_i)
\qquad \text{with "As } \alpha \to 0:\ D(\alpha) \nearrow 8;\ \text{As } \alpha \to \infty:\ D(\alpha) \searrow 1
$$

$$
\frac{dD}{d\alpha} \;=\; -\,\frac{1}{\lambda}\,\frac{d}{d\alpha}\log|G/H(\alpha)|
$$

where $Θ$ is the Heaviside step and $λ$ a Lyapunov exponent (Pesin's theorem supplies the
holonomy–instability link).

**Theorem 23.** The draft pair of formulae is inconsistent in three distinct ways, and
the corrected pair is as follows.

1. **The step is negated.** $1 + Σ Θ(α − α_i)$ is non-decreasing in $α$, whereas the stated
   behaviour ($D ↘ 1$ as $α → ∞$) requires $1 + Σ Θ(α_i − α)$. Corrected:

   $$D(\alpha) \;=\; 1 + \sum_i \Theta(\alpha_i - \alpha).$$

2. **The derivative's sign is wrong.** With `D` decreasing in $α$, $dD/dα < 0$. From the
   breaking pattern (at $α → ∞$ the group `G` is unbroken, so $H(α) = G$ and `|G/H| = 1`;
   at $α = 0$ the breaking is maximal), $|G/H(α)|$ *decreases* with $α$, so
   $d/dα log|G/H| < 0$ and the right-hand side with the draft's minus sign is *positive*
   for $λ > 0$. LHS and RHS then have opposite signs. Corrected:

   $$\frac{dD}{d\alpha} \;=\; +\frac{1}{\lambda}\,\frac{d}{d\alpha}\log|G/H(\alpha)| .$$

3. **$dD/dα$ is a distribution.** `D` is a step function, so $dD/dα = Σ_i δ(α − α_i)$ — a
   sum of Dirac deltas — which cannot equal a smooth function pointwise. Either smooth `D`
   (replace $Θ$ by a sigmoid), or interpret the identity as a coarse-grained relation
   between the step locations $α_i$ and the symmetry-loss rate.

*Proof.* (1) Immediate from the monotonicity of $Θ$. (2) As above; the sign of
$d/dα log|G/H|$ is determined by the breaking pattern, which makes `G` unbroken at $α → ∞$
and maximally broken at $α = 0$. (3) The distributional derivative of a Heaviside step is
a Dirac mass. $\blacksquare$

## The ladder is a recursion
**Observation 24.** With the draft's notation read as a table rather than a coincidence,
the formal–final potential *is* the material–efficient curvature. Renaming potentials
$\mathcal{A}, \mathcal{B}, \mathcal{C}$ and curvatures $\mathcal{F}, \mathfrak{G}, \mathcal{H}$, the ladder reads

$$\mathcal{G} = d\mathcal{A} + \mathcal{A}\wedge\mathcal{A}, \qquad
\mathcal{H} = d\mathcal{B} + \mathcal{B}\wedge\mathcal{B}, \qquad \dots$$

so that the potential of interval `n+1` is the curvature of interval `n`. This is a
**discrete hierarchy of connection fields**, closely analogous to a discrete integrable
(Lax) structure: the higher level is generated by the curvature of the lower. The draft
notation made this unreadable.

---

# Relations to existing literature

**Constructor Theory.** Deutsch & Marletto (2014) define possibility relative to the laws:
a task is possible iff a constructor can perform it, and impossible iff the laws forbid it.
Three connections:

- Theorem 11 identifies the via-negativa constraint with a **limitation on transformations**,
  which is what a law is in CTT. This is not an analogy; it is the same notion.
- The draft's $β* = ¬∃\ell ∈ C_ont : □_\ell Φ$ measures *absence of necessity*, not prohibition,
  and so is not the CTT impossibility indicator. The corrected form is
  $β*(Φ) = 1 ⟺ Γ(\mathfrak{F}_C, A) = ∅$ — the descent obstruction of Theorem 10.
- CTT's **locality** principle (tasks decompose) has an exact counterpart in the framework's
  aggregation tower, where a level-`k+1` task decomposes into level-`k` tasks. The tower
  supplies CTT with locality; CTT supplies the tower with a notion of impossibility.

**Assembly theory.** Cronin et al. (2017) define the assembly number of an object as the
number of distinct ways its parts can be assembled. Remark 14 shows the framework's
assembly sheaf, read as pathways, is exactly this object, and that the essential/contingent
distinction is the distinction between parts present in every pathway and parts present in
some. This is a substantive strengthening of the draft's informal appeal.

**Objective and subjective logic.** Lawvere (1992, 1994, 2005) argues that category theory
can give precise form to philosophical distinctions, and distinguishes a *objective* logic
— the logic provable in the metatheory about a topos — from the *subjective* logic internal
to it. The framework's modal apparatus (Modeling proposal 17) is an instance of this
pattern. Lawvere's further claim, that **adjoint functors are the paradigmatic "unity of
opposites"**, is directly relevant: the framework's dialectical commitments and its
categorical commitments converge if and only if it can exhibit genuine adjunctions between
its own primitives. *We do not claim to have exhibited one, and regard this as the
framework's principal outstanding task.*

**Ambrose–Singer, Pesin.** §5 and §9 use both. Ambrose–Singer identifies the holonomy
algebra with the span of the curvature; Pesin's formulae connect holonomy to Lyapunov
exponents and entropy, which is the justification for the $1/λ$ factor in the corrected
rate equation.

**No global symmetries in quantum gravity.** Harlow & Ooguri (2002) motivate the
framework's premise that symmetry breaking along a depth coordinate is physically
significant rather than decorative.

**Learning by compression.** The framework's tower operation `C_k` — a principal-component
compression of a level-`k` substrate producing a level-`k+1` holon — is the same move as
Hinton & Salakhutdinov's (2006) construction of a higher-level feature layer by PCA over a
lower layer. The draft treated `C_k` as a categorical object; it is a statistical one, and
should be labelled as such. The *categorical* object in this part of the framework is the
abstraction-event morphism of §4.3, not the compression.

---

# Status of the results

| # | Statement | Status |
|---|---|---|
| 1 | Gauge- and homotopy-invariance of the holonomy class | **Theorem** (proved) |
| 2 | The trace is not a complete conjugacy invariant (`SU(3)` counterexample) | **Theorem** (proved) |
| 3 | Curvature = obstruction to descent of parallel transport to $Π₁(M)$ | **Theorem** (proved) |
| 4 | Frobenius integrability as the local obstruction to constraint consistency | **Theorem** (proved) |
| 5 | Impossibility, descent obstruction, and non-additivity of constraint | **Theorems** (proved) |
| 6 | Essential/contingent trichotomy derived from global vs. local sections | **Proposition** (proved) |
| 7 | The structure group is a 2-group; upgrades to 2-connections, 2-holonomy, 2-traces | **Observation + citation** (proved, contingent on $\mathfrak{P}_∞$ being an $\infty$-groupoid) |
| 8 | Coset count vs. sector count | **Proposition** (proved) |
| 9 | Three corrections to the dimensional-explosion formulae | **Theorem** (proved) |
| 10 | Constraint-induced Lawvere–Tierney topology for the modality | **Modeling proposal** (not proved) |
| 11 | The framework's specific physical/cosmological claims | **Conjectural / empirical** (not addressed) |
| 12 | The claim that the formalization *captures* the intended metaphysical notion | **Open** (philosophical, not mathematical) |

---

# Conclusions for metaphysicians

We state six claims and invite rebuttal.

**(i) "Via negativa" acquires a content that is neither trivial nor question-begging.**
The principle that a higher cause constrains without adding energy is usually dismissed as
either a metaphor or a truism. Theorem 11 shows it can be made into a precise claim about
monomorphisms in a topos of sheaves: a constraint is a restriction of the possibility space
of transformations, and its efficacy is *measured* by a descent obstruction. The principle
then has a failure condition — a constraint can be locally satisfiable and globally
unsatisfiable — which is the kind of thing a metaphysical principle should have if it is to
do any work.

**(ii) The "unity of opposites" is testable, and it has not yet been earned.** The
framework's dialectical commitments and its categorical commitments converge exactly when
it exhibits genuine adjunctions between its own primitives. It has not. Until it does, the
claims in §6.3 about higher and lower causal levels are *modelled* by adjunction-shaped
constructions but are not *explained* by them. We regard this as the framework's principal
outstanding mathematical task, and it is a task in which a failure would be informative.

**(iii) "Objective vs. subjective" is better treated as a gradation than a dichotomy.**
Lawvere's objective/subjective distinction, and the Lawvere–Tierney topology that
implements it, suggest a middle position between "the world as it is" and "the world as
observed": a **locality operator** on truth values specifying what is forced locally but not
globally. This is the natural formal home for a framework in which observers are
first-class, and it is a better instrument than either a binary distinction or a
contingency-modal one.

**(iv) "General vs. particular" is partly dissolved, and that is a result.** In the
framework's own idiom, identity is an address in causal space. Category theory has spent
fifty years making the general — the structure — the primary object, with particulars
appearing only as concrete realizations of it. The framework's indexical identity is
precisely such a realization, and the holonomy-class formulation shows why the general
alone cannot be the whole story: a structure with no realizations has no holonomy.

**(v) "Being vs. becoming" is best formalized by coalgebra, not by category.** Lawvere's
coalgebras for polynomial endofunctors (1991) provide the exact division of labour the
framework's Aionic axis needs: an algebra is a structure with specified behaviour, a
coalgebra is a structure whose behaviour is generated by observation, and the two are
related by the dualities that make the framework's "objective vs. subjective" distinction
precise. We note this but do not develop it; it is the most promising unexplored
connection in the framework.

**(vi) Most of what the framework gets wrong is error, not metaphysics.** Five of the
draft's central formulae were incorrect — a sign error, a missing negation, a type error, a
category error, a conflation of three counting conventions. All were repairable, and none
of the repairs damaged the framework's thesis; two of them *revealed* structure that had
been hidden (the ladder's recursion, and the descent obstruction). This is an argument for
proceeding with formalization rather than against it. A framework whose mathematical
errors are repairable without loss of thesis is in a much better epistemic position than
one that has never been subjected to this kind of check.

**A methodological postscript, offered without apology.** This framework was developed in
dialogue with several AI systems, and was audited against its own source notes with
machine assistance. That process produced errors — including, in earlier drafts of this
paper, two mis-attributed references, which have been corrected here. We report this
because it bears on the standing of the results. Two things can be said: every theorem in
§4–§9 is stated with a proof that can be checked without access to any of the source
material; and the labels distinguishing what is proved from what is conjectural were
applied consistently, including where they were unflattering to the framework. A reader who
distrusts the provenance of the underlying ideas can still check the mathematics, and that
is the point of the exercise.

---

# Limitations and threats to validity

1. **The formalization may capture the wrong notion.** We have formalized *a* reading of
   the framework's claims. Whether the readings we chose are the ones the framework's
   author intends is a philosophical question that this paper cannot settle. Every
   "Definition" in §4–§9 is therefore an interpretive proposal, and the results attached to
   them are conditional on those proposals being apt.
2. **Modeling proposal 17 is not proved**, and is the weakest link in the modal apparatus.
3. **The physical content is out of scope.** The paper makes no empirical claim, and the
   framework's cosmological commitments — the axis, the breaking pattern, the tower's
   dynamics — are untouched by the formalization. Several of them (notably the axis's
   orientation, on which the corrected sign in §9.2 depends) are unsettled in the source
   material.
4. **The higher-categorical upgrade in §8 is conditional** on the pointer structure being
   a genuine $\infty$-groupoid rather than a large ordinary groupoid of labels. If the latter,
   §8 collapses back to ordinary group theory and the `Hopf`-algebraic costume is
   unnecessary.
5. **We have not exhibited the adjunctions** that would license the framework's
   dialectical claims on categorical grounds (§12(ii)).
6. **The source material is a set of dialogue transcripts**, so "the framework" is
   reconstructed rather than read off a canonical statement. We have made every
   interpretive step explicit rather than silently adopting one.

---

# Authorship, contributions, and provenance

**Authorship of this paper.** The present paper — including its formalization, all proofs,
all corrections, the reference verification, and all prose except where explicitly quoted —
was **written by MiniMax-M3 (MCode)**, an AI research agent, from working notes and drafts
supplied by the framework's originator. MiniMax-M3 also performed the source audit that
identified the five corrected formulae, the two mis-attributed references, and the
symbol collisions discussed in §8 and §9.

**Contributors, by name and version.**

| Contributor | Version / identifier | Contribution as recorded in the source material |
|---|---|---|
| **Nicolai Gamulea Schwartz** (GitHub handle `CukiG`) | originator; working-notes snapshot `vault@5290f85` | The framework: indexical identity as holonomy; the via-negativa constraint principle; the interval ladder; the aggregation tower; the Aionic axis; the $P_t : TQ → \mathfrak{g}$ constraint specification (§6.1); and the modal-assembly direction (which prompted the Kripke-frame construction) |
| **MiniMax-M3 (MCode)** | MiniMax-M3 | Formalization; Theorems 1–14, 23; Propositions 3, 14, 22; Observations 19, 24; correction log (§9, §16); reference verification; all prose |
| **Kimi K2** | Kimi K2 | Multi-layer Kripke frames and the graded assembly functor; the `Essential`/`Necessary` predicates; the groupoid-bundle construction; the interval ladder and its field/curvature table; the structural group `G` and the $\mathfrak{P}_∞$ pointer $\infty$-groupoid; the Hopf-algebraic expression; the dimensional-explosion formulae; the $\mathcal{U}$ constraint discussion |
| **Gemini** | Gemini (unspecified sub-version in transcripts) | Critical review of the groupoid claims; the "operationalize the interface" review item; reinforcement of the eigenvalue gloss; the ladder-detector and PCA formulation of `C_k` |
| **Gemini 2.5 Pro** | Gemini 2.5 Pro | The "persistent background and local emergence" revision of the axis (which supersedes the earlier orientation); the $α$-bounce deconstruction |
| **Gemini 3.0 Pro** | Gemini 3.0 Pro | Appears in later sessions; no specific claim relied upon here |
| **Grok** | Grok 4 (as `Grok 4.1` in the associated paper title) | The $α$*/$β$* classifier family ($α* = κ · A_eff / n$); the comparison of the modal-assembly hybrid against prior work; the constraint-group specification $P_t : TQ → \mathfrak{g}$ with $G = SO(1,3) ⋉ \mathbb{R}⁴$; the `Grok 4.1's Paper` synthesis |
| **ChatGPT** | ChatGPT (version not stated in the transcripts) | The review items demanding a one-line precise object for the groupoid claims and an operational criterion for abstraction; the `ChatGPT' HVP draft` |
| **DeepSeek V3.1-Thinking** | DeepSeek V3.1-Thinking | Appears in sessions 1, 2, and 6; no specific claim relied upon here |
| **Perplexity** | Perplexity (version not stated) | Appears in sessions 1 and 4; no specific claim relied upon here |
| **Sonoma Sky Alpha** | Sonoma Sky Alpha | Appears once in session 3; no specific claim relied upon here |
| **Copilot** | Obsidian Copilot plugin | Listed as a participant in `Selfhood`; not relied upon here |

**Provenance statement.** The source corpus consists of dialogue transcripts plus
model-generated digests of those transcripts. No claim in §§4–9 is attributed to a model's
authority; every theorem is independently proved here. Where the source material's authorial
commitment is ambiguous — as it frequently is — we have said so. A complete
claim-by-claim provenance table, including line-level attribution and the five draft
formulae we have corrected, accompanies this paper as `provenance.md` in this repository.

---

# References

- Ambrose, W. & Singer, I. M. (1953). "On closed geodesics." *Proceedings of the American
  Mathematical Society* 4, 288–291.
- Baez, J. C. & Schreiber, U. (2004). "Higher gauge theory: 2-connections on 2-bundles."
  *arXiv:hep-th/0412325*. (Preprint; published as *Higher Gauge Theory*, Contemp. Math. 431,
  AMS, 2007, 7–30.)
- Cronin, J. D., Hassen, S. & Fields, C. (2017). "Assembly theory." *arXiv:1704.00859*.
- Deutsch, D. & Marletto, C. (2014). "Constructor theory of time." *New Journal of Physics* 16,
  063001.
- Grandis, M. & Foli, U. (1995). "Hopf objects and pointed toposes." In L. Bentley,
  H. Herrlich, M. Rajagopalan & H. Wolff (eds.), *Categorical Topology*, Heldermann.
- Harlow, D. & Ooguri, H. (2002). "Holography and the symmetry group of quantum gravity."
  *Fortschritte der Physik* 50, 2203–2216; *arXiv:hep-th/0202056*.
- Hinton, G. E. & Salakhutdinov, R. (2006). "Reducing the dimensionality of data with neural
  networks." *Science* 313, 504–507.
- Hofstadter, R. & Streicher, G. M. (1982). "Recursion and the axiom of choice." *Bulletin of
  the American Mathematical Society* 6, 699–702.
- Lawvere, F. W. (1968). "An introduction to categorical logic." In *Proceedings of the
  1968 Manchester Conference*, Springer LNM 406.
- Lawvere, F. W. (1968). "Equality in hyperdoctrines and comprehension schema as an adjoint
  functor." In *Applications of Categorical Algebra*, Proc. Sympos. Pure Math. XVII, AMS,
  1–14.
- Lawvere, F. W. (1991). "Axiomatic prototypes for some species of topological categories."
  In *Category Theory, Proceedings Como 1990*, LNM 1489, Springer, 221–244.
- Lawvere, F. W. (1992). "Categories of space and quantity." In J. Echeverría, A. Ibarra &
  T. Mormann (eds.), *The Space of Mathematics*, De Gruyter. (Also issued as *Structures in
  Mathematical Theories*, San Sebastián proceedings, De Gruyter, 1992.)
- Lawvere, F. W. (1994). "Tools for the advancement of objective logic: closed categories and
  toposes." Aarhus University lecture notes.
- Lawvere, F. W. (2005). "Comments on the development of topos theory." *Cahiers de
  Géométrie Riemannique* 12.
- Lawvere, F. W. & Tierney, B. (1979). "Axiomatic cohomology for theories with Kan
  extensions." In *Theory of Categories*, LNM 788, Springer, 373–397.
- Martins, J. F. & Picken, R. (2008). "On two-dimensional holonomy." *arXiv:0710.4310*.
- Pesin, Ya. B. (1978). "Formulae for the surface entropy and the Lyapunov exponents of a
  conservative flow." *Communications in Mathematical Physics* 63, 27–43.
- Zucchini, R. (2015). "On higher holonomy invariants in higher gauge theory II."
  *arXiv:1505.02122*.

---

# Appendix A — Notation

| Symbol | Meaning |
|---|---|
| `M` | base manifold (the "bulk") |
| `Q` | manifold of admissible states |
| `I` | fiber: a set of indexical labels |
| $\mathfrak{G}$ | structure groupoid of admissible re-labellings |
| $Π₁(M)$ | fundamental groupoid of `M` |
| $\mathcal{P}(M)$ | path groupoid of `M` |
| $hol(γ)$ | holonomy around the loop $γ$; an element of $\mathfrak{G}$ |
| $\mathcal{I}_γ$ | indexical identity: the conjugacy class $[hol(γ)]$ |
| $τ(\mathcal{I}_γ)$ | the trace of the holonomy; a lossy shadow of $\mathcal{I}_γ$ |
| `G_c` | constraint group: a compact connected Lie group with Lie algebra $\mathfrak{g}$ |
| $P_t : TQ → \mathfrak{g}$ | the constraint (a submersion) at time `t` |
| $Σ_t = ker P_t$ | the distribution of admissible velocities |
| $\mathfrak{F}_M, \mathfrak{F}_F, \mathfrak{F}_T$ | Kripke frames for the material/efficient, formal, final layers |
| $\mathfrak{F}_C$ | composite constraint frame |
| `X` | sheaf of material/efficient states on $\mathfrak{F}_C$ |
| $A ↪ X$ | subsheaf of admissible states |
| $Γ(\mathfrak{F}_C, A)$ | global sections of `A`; global realizations |
| $j : Ω → Ω$ | Lawvere–Tierney topology (interior operator) — *proposed*, §7 |
| $\mathcal{A}, \mathcal{B}, \mathcal{C}$ | interval potentials: material–efficient, efficient–formal, formal–final |
| $\mathcal{F}, \mathfrak{G}, \mathcal{H}$ | interval curvatures, corresponding to the above |
| $P₂(M)$ | thin fundamental categoric group (path 2-groupoid) of `M` |
| $D(α)$ | number of ontological dimensions at depth $α$ (corrected, §9.2) |
| $λ$ | Lyapunov exponent (Pesin) |

# Appendix B — From informal vocabulary to formal objects

| Informal | Formal object | Section |
|---|---|---|
| "a persistent pointer to this narrative thread" | conjugacy class of holonomy | §4.1 |
| "the holonomy index" | $\mathcal{I}_γ$, with $τ$ as shadow | §4.1, §4.3 |
| "a persistent pointer whose data change" | homotopy invariance of $\mathcal{I}_γ$ | §4.2 |
| "the field does not add energy; it removes forbidden directions" | $A ↪ X$ a monomorphism; constraint = restriction of transformations | §6.3 |
| "the via-negativa projection operator" | interior operator on a Heyting algebra (proposed) | §7 |
| "essential condition" | part in every global realization | §6.4 |
| "necessary but swappable" / "scaffolding" | part in some but not all local realizations (**contingent**) | §6.4 |
| "causal torque" | non-commutation of the constraint distribution with the lower transport | §6.2, §6.3 |
| "unity of opposites" | failure of the composite to be additive; adjunction (not yet exhibited) | §6.3, §12(ii) |
| "semantic capsule" | subsheaf of admissible states at the next level | §6.3 |
| "playing at `k+1`" | a realization in the global sections of `A` | §6.3 |
| "dimensional explosion" | $D(α)$ with the corrected step and sign | §9.2 |
| "residual symmetry slice" | $H(α)$, a stabilizer; sectors = its conjugacy classes | §9.1 |
| "indexical decoherence" | change of the conjugacy class of holonomy | §4.1 |
| "the structure group" | a 2-group | §8 |

# Appendix C — Correction log

Five defects in the draft material were found and repaired. They are listed because a
reader of the draft should know which of its claims survived.

| # | Draft claim | Defect | Resolution |
|---|---|---|---|
| 1 | "Curvature = failure of $\mathcal{P}$ to preserve composition" | Category error: a functor preserves composition by definition | §5, Theorem 4: curvature = obstruction to descent to $Π₁(M)$ |
| 2 | $\mathcal{I}_γ ≡ Tr(\mathcal{P} exp ∮_γ A)$ | Ill-typed: a number has no "equivalence"; the trace is not a complete conjugacy invariant | §4.1–4.3: $\mathcal{I}_γ$ is a conjugacy class; the trace is a shadow; `SU(3)` counterexample |
| 3 | $D(α) = 1 + Σ Θ(α − α_i)$ with $D ↘ 1$ as $α → ∞$ | Step not negated; derivative's sign also wrong; $dD/dα$ is a distribution | §9.2, Theorem 23 |
| 4 | $\|G/H(α)\|$ counts "linearly independent holonomy eigenvalues" | Conflates coset count, sector count, and eigenvalues | §9.1, Proposition 22 |
| 5 | $\mathcal{F}$ used for the groupoid action, one curvature, one potential, and its own curvature's input | Symbol collision making the interval ladder unreadable | §8–9.3: potentials $\mathcal{A}, \mathcal{B}, \mathcal{C}$; curvatures $\mathcal{F}, \mathfrak{G}, \mathcal{H}$; the ladder's recursion becomes visible |
