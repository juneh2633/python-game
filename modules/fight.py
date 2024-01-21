from classes.entities import Monster


def fight(a, b, a_skill, b_skill):
    if a.spd < b.spd:
        a, b = b, a

    a.use_skill(a_skill, b)
    if b.is_alive():
        b.use_skill(b_skill, a)
