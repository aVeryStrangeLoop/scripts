# Find population entropy for a set of genomes
import collections
import numpy as np

def site_entropy(site_chars):
    #####################################
    # Calculates the entropy of a site given the list of characters at that site
    # INPUTS
    # 1. site_chars (list of characters) found at a particular site # in the genome
    # 
    # OUTPUTS
    # 1. Entropy of that site defined as -sum(pi log(pi)) where i is the instruction type
    #####################################
    counter = collections.Counter(site_chars)
    counts = counter.values()
    cumulative = sum(counts)
    freqs = []
    for count in counts:
        freqs.append(float(count)/cumulative)
    
    freqs = np.array(freqs)

    entropy = np.sum(-np.multiply(freqs,np.log(freqs)))
    
    return entropy
    

def pop_entropy(genomes):
    ###############################
    # Calculates population entropy given all genomes in that population
    # INPUTS
    # 1. genomes (list of sequences) in a particular population (NOTE: These must either be equal in length or aligned)
    #
    # OUTPUTS
    # 1. Population entropy given as the sum of per site entropies
    ################################

    # Check all sequences are equal length

    SIZE = len(genomes[0])
    all_equal = all(len(sequence)==SIZE for sequence in genomes)
    if not all_equal:
            raise ValueError("Length of all sequences in genomes list not equal!")

    p_entropy = 0.0

    for i in range(SIZE):
        site_chars = []
        for genome in genomes:
            site_chars.append(genome[i])
        p_entropy += site_entropy(site_chars)

    return p_entropy



