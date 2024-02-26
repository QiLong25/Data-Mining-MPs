import math
import numpy as np

def my_Bayes_candy(pi_list, p_list, c_list):
    posterior_probabilities = [[0] * 5 for _ in range(10)] # Default initialization with 0s
    
    # Implement your code to calculate the posterior probabilities here
    p_conds = [1, 1, 1, 1, 1]           # record cumulative conditional probabilities of all rows before, each index is a bag

    # Main Loop
    for round in range(10):               # loop over each pick from bag

        # Step 1: denominator P(C1, C2, C3, ...)
        num_lime = 0
        for round_idx in range(round+1):
            num_lime += c_list[round_idx]
        p_candies = 0
        for bag in range(5):            # loop over all bags
            if p_list[bag] == 0:                        # bag only have lime
                if round+1-num_lime == 0:                # only lime appears
                    p_candies += pi_list[bag]
                else:
                    continue
            elif p_list[bag] == 1:                       # bag only have cherry
                if num_lime == 0:                       # only cherry appears
                    p_candies += pi_list[bag]
                else:
                    continue
            else:
                p_candies += ((1 - p_list[bag])**num_lime) * ((p_list[bag])**(round+1-num_lime)) * pi_list[bag]

        for bag in range(5):            # loop over 5 bags

            # Step 2: nominator left P(C1|pi) * P(C2|pi) * ...
            if c_list[round] == 0:            # cherry is picked
                p_conds[bag] *= p_list[bag]
            else:                           # lime is picked
                p_conds[bag] *= (1 - p_list[bag])

            # Step 3: generate output
            posterior_probabilities[round][bag] = p_conds[bag] * pi_list[bag] / p_candies

    return posterior_probabilities

# Test
# pi_list = [0.1, 0.2, 0.4, 0.2, 0.1]
# p_list = [1, 0.75, 0.5, 0.25, 0]
# c_list = [1, 0, 0, 0, 1, 0, 0, 0, 0, 0]
# result = my_Bayes_candy(pi_list, p_list, c_list)
# for i in range(len(result)):
#     print(sum(result[i]))