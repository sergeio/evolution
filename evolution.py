from random import gauss, shuffle, random

from statistics import median, stdev


CHANCE_TO_PASS_TRAIT = .6
CHANCE_KILLED_WITHOUT_TRAIT = .1
CHANCE_KILLED_WITH_TRAIT = .01
SUSTAINABLE_POPULATION = 10000
MAX_AGE = 10


def main():
    """Run simulations on population to see how the trait spreads."""
    NUM_SIMULATIONS = 20

    results = {'dominates': [], 'dies out': []}
    for i in xrange(NUM_SIMULATIONS):
        result, years = run_simulation()
        results[result].append(years)

    print
    for result, age_list in results.iteritems():
        print '    {0} {1}% of the time, in {2} +/- {3} years'.format(
            result,
            int(len(age_list) / float(NUM_SIMULATIONS) * 100),
            round(median(age_list), 1),
            round(stdev(age_list), 1),
        )

def run_simulation():
    """Go forward one year at a time until the trait is dominant or gone."""
    # TODO: Better age distribution
    creatures = [(True, 0)] + [(False, int(gauss(50, 25))) for _ in xrange(999)]
    year = 0
    result = 'dominates'
    while percent_with_trait(creatures) < .9:
        creatures = go_one_year_forward(creatures)
        year += 1
        if not creatures_with_trait(creatures):
            result = 'dies out'
            break
    return result, year

def go_one_year_forward(creatures):
    """Advance the population one year.  Add new children, and remove dead."""
    shuffle(creatures)
    creatures = increment_age(creatures)
    creatures = creatures + breed(creatures)
    creatures = kill_some_creatures(creatures)
    return creatures

def percent_with_trait(creatures):
    """What percent of the population has the trait?"""
    return creatures_with_trait(creatures) / float(len(creatures))

def increment_age(creatures):
    """All creatures age one year."""
    return [(trait, age + 1) for trait, age in creatures]

def breed(creatures):
    """Return new children from population of creatures."""
    # Our creatures can breed with any other creature.  No gender.
    # Everyone breeds once a year
    children = []
    for lover1, lover2 in zip(creatures[0::2], creatures[1::2]):
        child_has_trait = False

        if has_trait(lover1) and has_trait(lover2):
            child_has_trait = True

        elif (has_trait(lover1) or has_trait(lover2)) and trait_passes():
            child_has_trait = True

        children.append([child_has_trait, 0])

    return children

def kill_some_creatures(creatures):
    """Kill some creatures by predators, starvation, or age."""
    def killed(creature):
        # TODO: Death might depend on age
        if has_trait(creature):
            killed = random() < CHANCE_KILLED_WITH_TRAIT
        else:
            killed = random() < CHANCE_KILLED_WITHOUT_TRAIT
        return killed

    def too_old(creature):
        return creature[1] > MAX_AGE

    def starves(creature):
        """Does the creature starve this year.

        Simulate natural resource scarcity to control the population.
        The total population should starve down to a max of
        `SUSTAINABLE_POPULATION`.

        """
        # TODO: Figure out why I need to divide by 5
        chance_to_starve = len(creatures) / float(SUSTAINABLE_POPULATION)
        return random() < chance_to_starve / 5

    def survives(creature):
        return not (killed(creature) or too_old(creature) or starves(creature))

    return filter(survives, creatures)

def has_trait(creature):
    """Does the `creature` have the trait?"""
    return creature[0]

def trait_passes():
    """Does the trait pass to a given child?"""
    return random() < CHANCE_TO_PASS_TRAIT

def creatures_with_trait(creatures):
    """How many creatures have the trait?"""
    return len(filter(has_trait, creatures))


if __name__ == '__main__':
    main()
