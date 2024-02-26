### main function
def ord_prefixspan(filename, minsup):
    freq_sequences = {} # default initialization
    
    # complete your code

    # step 1: read data from txt
    seqs = []  # a list of sequences only
    with open(filename, "r") as f:
        for row in f:  # split item name and content
            row = row.strip().replace(" <", "").replace(">", "").split(",")
            seqs.append(row[1])

    # step 2: main loop

    ### Helper function, given a string and minsup, find single character to add to pattern
    def find_pattern(prefix, remains):
        # sanity check
        if len(remains) < minsup:
            return
        char_sup = {}  # char : support
        for string in remains:
            for char in set(string):
                if char in char_sup.keys():
                    char_sup[char] += 1
                else:
                    char_sup[char] = 1
        for char in char_sup.keys():  # check larger than minsup
            if char_sup[char] >= minsup:
                freq_sequences[prefix + char] = char_sup[char]
                new_prefix = prefix + char
                new_remains = []
                for string in remains:
                    if char in string:
                      new_remains.append(string[string.find(char) + 1:])
                find_pattern(new_prefix, new_remains)
        return

    find_pattern("", seqs)
    return freq_sequences

# ### my test ###
# print(ord_prefixspan("a5_sample_input.txt", 4))




    
    