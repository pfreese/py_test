
def all_binary(k):
    if k == 0:
        return []
    if k == 1:
        return ["0", "1"]
    return [f"0{x}" for x in all_binary(k - 1)] + [f"1{x}" for x in all_binary(k - 1)]


def all_k_in_str(str, k):
    kmersFound = {}
    for kmer in all_binary(k):
        kmersFound[kmer] = False
    n_kmers_found = 0
    n_kmers_needed = int(2 ** k)
    for start_idx in range(len(str) - k + 1):
        kmer = str[start_idx:(start_idx+k)]
        if not kmersFound[kmer]:
            kmersFound[kmer] = True
            n_kmers_found += 1
            if n_kmers_found == n_kmers_needed:
                return True
    return False
