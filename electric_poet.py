# find all variants assumed pattern

from itertools import permutations

SCHEME = {
    'pattern': '--+----+----+-',
    'words': [
        ['не', '-'],
        ['подскажут', '-+-', '---'],
        ['мне', '-', '+'],
        ['закатившиеся', '--+---'],
        ['эпохи', '-+-', '---'],
    ]
}

pattern = SCHEME["pattern"]

print(pattern)

words = SCHEME["words"]

variants_index_word = permutations(range(len(words)))

varaints_list = []

for variant in variants_index_word:
    pattern_copy = pattern
    for i in variant:
        for part_pattern in words[i][1:]:
            if pattern_copy.startswith(part_pattern):
                pattern_copy = pattern_copy[len(part_pattern):]
                break
        else:
            break
    else:
        varaints_list.append(variant)


for i in range(len(varaints_list)):
    for j in range(len(varaints_list[i])):
        print(words[varaints_list[i][j]][0], end=" ")
    print("\n", end="")
