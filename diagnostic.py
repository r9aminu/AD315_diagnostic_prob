def calculate_probabilities(prob_disease, prob_pos_has_disease, prob_neg_no_disease):
    
    prob_no_disease = 1 - prob_disease
    prob_pos_no_disease = 1 - prob_neg_no_disease

    # Calculate P(Test+)
    prob_test_positive = (prob_pos_has_disease * prob_disease) + (prob_pos_no_disease * prob_no_disease)

    # Calculate P(Test-)
    prob_test_negative = (prob_neg_no_disease * prob_no_disease) + ((1 - prob_pos_has_disease) * prob_disease)

    # Calculate P(Disease|Test+)
    prob_disease_given_test_positive = (prob_pos_has_disease * prob_disease) / prob_test_positive

    # Calculate P(Disease|Test-)
    prob_disease_given_test_negative = ((1 - prob_pos_has_disease) * prob_disease) / prob_test_negative

    return round(prob_disease_given_test_positive, 3), round(prob_disease_given_test_negative, 3)

    # p(test+) = (0.99*0.01) + (0.05*0.99) = 0.0594
    # p(test-) = (0.95*0.99) + ((1-0.99)*0.01) = 0.9406
    # p(disease, test+) = 0.99*0.01/0.0594 = 0.167
    # p(diseas, test-) = (1-0.99)*(0.01)/0.9406 = 0.000106

# Examples
prob_disease = 1
prob_pos_has_disease = 1
prob_neg_no_disease = 1

prob_disease_if_positive, prob_disease_if_negative = calculate_probabilities(prob_disease, prob_pos_has_disease, prob_neg_no_disease)

print("Probability of having the disease given a positive test result:", prob_disease_if_positive)
print("Probability of having the disease given a negative test result:", prob_disease_if_negative)
