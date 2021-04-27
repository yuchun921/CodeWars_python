def dna_to_rna(dna):
    s = ''
    for i in dna:
        if i == 'T':
            s = s + "U"
        else:
            s = s + i
    return s
