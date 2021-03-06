count_valleys = lambda s: list(zip([0] + [sum([1 if x == 'U' else -1 for x in s[:e]]) for e in range(1, len(s))], [sum([1 if x == 'U' else -1 for x in s[:e]]) for e in range(1, len(s))])).count((0, -1))


assert count_valleys('UDDDUDUU') == 1
assert count_valleys('UUDDDUDDUU') == 2
assert count_valleys('DDUDUU') == 1
assert count_valleys('UDUUUDUDDD') == 0
assert count_valleys('DDUUDDUDUUUD') == 2
assert count_valleys('DDDUUUUUDDDUUDUDDDUUDUUDDDUUDDDDDUDDUUDUDDUDUDDUDDDUDUUDUDUDDUDDDDDDDUUUUUUUUDUUDUUUUDUDDDUDDUUDUDDUDUDUUUUUUDUDDDDDDUDDDUUUDDUDDUDDUUUUDDDDUDUUUUUDUUDUDDUUUDUUUDDUDDDDUUUUDDDDDDUUUUDDDDUDDUUDDDDUUDUDDUUDUUUDUUUUDDUDDDDUUDUDDDDDUDUDUDUUDDUDUDDUDDDDUDUDUDUUUDDDDDUUUDDDUDDDUDDDDUDUDUDDUDDDDDDUDUDUDDDDDDUUUDDDUDUUDDDDUDUDDDDDUDDUUDUDDDDUDDDUUUUUDUDDUDUUDUDDDDUUUUDDDUDUUUUUUUDUUDDDUDUDDDDUDDUUDDDDDUDDUUUUDUUDUDDUDUUDDUUUDUUUUDDUUUUDDUUDUUUDUDUUUDUDDUDDDUDUUUUUUUUUUUDUDDUDDDDDUUDUDDUDDUDUDUUDDDDUUUDDUDDUDDUUDUUUDUDUUUUUDDUUDUUDUDDUDUUUUUUDDDDUUUDDUDUUUUUUUDDUUDDUUUUUDDUUDUUUDDUDUDUUDDDUDUUUUUUUDUUUUDDUDDDUDUUDUDDDUDUUUDUUUDDDUDDUUUUUDUUDDDDDDUUDDUDUDDUDUDUDDUDUDUUUDUDUUDUDUUDUDUDDDDUUUUDDDUUDUUDDUDUDUUDUDUUUDDUUUDUDUDDDUDDUUUDUDUUUDDUDUDUDDUUDDDDUUUUUDUDUUDUDUUDDDDUDDDUDUUUUUDDDUDDDDUUDDUUDUUUUUUDDUUDDUUUUUUUDUDDUDDDDDDDUDDDDUDUDUDUUDUDDDUDUUUUDDUUUDUDUDUUDDDDDUUUUUUDUDDUDUDDUDDUDUUDUDUUUUUDUDDDDUUUDDUUDDDUUUUDUDDDUDDUUUDDDDUDDDUDDDUUDDDDUUDDDUDDDUUUUUUDUDUUDUUDUDDDUDUUDDUDDDDUDUDUUUUUUUUUU') == 18

