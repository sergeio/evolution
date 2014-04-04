Evolution
=========

Simulate the propagation of a trait through a population of creatures.

Definitions
-----------

Trait has no affect on mortality means:
`CHANCE_KILLED_WITH_TRAIT = CHANCE_KILLED_WITHOUT_TRAIT = .1`

Trait is very helpful means:
`CHANCE_KILLED_WITHOUT_TRAIT = .1 and CHANCE_KILLED_WITH_TRAIT = .01`

Trait is deadly means:
`CHANCE_KILLED_WITHOUT_TRAIT = .1 and CHANCE_KILLED_WITH_TRAIT = .2`

Trait is very deadly means:
`CHANCE_KILLED_WITHOUT_TRAIT = .1 and CHANCE_KILLED_WITH_TRAIT = .5`

Trait is dominant means:
`more than 90% of the population has trait`

Results
=======

If the trait always passes
--------------------------
`CHANCE_TO_PASS_TRAIT = 1`

The trait will spread quickly even if it has no effect on mortality.  In It
takes 26 years to become dominant.

    dominates 100% of the time, in 26 +/- 1.7 years

If the trait is helpful, it spreads more quickly.  In 20 years, it is dominant.

    dominates 100% of the time, in 20 +/- 0.7 years

If the trait is deadly, it will still spread through the population, but more
slowly.  It takes about 40 generations to become dominant.

    dominates 90% of the time, in 41.0 +/- 2.6 years
    dies out 10% of the time, in 1.0 +/- 0.0 years

If it is very deadly, then it will die out in usually less than 10 generations.

    dies out 100% of the time, in 3.5 +/- 6.2 years

Keeping our deadliness rates, in order to have the trait be evolved out of the
gene pool almost always, the `CHANCE_TO_PASS_TRAIT needs to be <= .6`


If the trait usually passes
---------------------------
`CHANCE_TO_PASS_TRAIT = .6`

If the trait has no effect, it takes 131 years to become dominant.

    dominates 70% of the time, in 118.0 +/- 17.0 years
    dies out 30% of the time, in 3.0 +/- 3.6 years

If the trait is helpful, it takes 50 years to become dominant.

    dominates 85% of the time, in 50.0 +/- 3.7 years
    dies out 15% of the time, in 1.0 +/- 0.5 years

If the trait is deadly, it dies out in usually less than 100 years.

    dies out 100% of the time, in 11.0 +/- 24.0 years

If the trait is very deadly, it dies out in usually less than 5 years.

    dies out 100% of the time, in 2.0 +/- 2.3 years


If the trait seldom pases
-------------------------
`CHANCE_TO_PASS_TRAIT = .4`

If the trait has no effect:

    dies out 100% of the time, in 37 +/- 17.9 years

If the trait is helpful, it

    dominates 55% of the time, in 162 +/- 15.1 years
    dies out 45% of the time, in 3 +/- 5.3 years

If the trait passes even less rarely
------------------------------------
`CHANCE_TO_PASS_TRAIT = .3`

Even if the trait is helpful, it dies out, usually in 50 years.

    dies out 100% of the time, in 29.5 +/- 19.1 years

If the trait makes you unable to be killed (`CHANCE_KILLED_WITH_TRAIT = 0`),
the trait will still die out in our environment.

    dies out 100% of the time, in 33.0 +/- 26.1 years
