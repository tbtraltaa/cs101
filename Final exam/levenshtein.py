def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)
    if not s1:
        return len(s2)
 
    previous_row = xrange(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
 
    return previous_row[-1]
#For example:

# Delete the 'a'
#print levenshtein('audacity', 'udacity')
#>>> 1

# Delete the 'a', replace the 'u' with 'U'
#print levenshtein('audacity', 'Udacity')
#>>> 2

# Five replacements
#print levenshtein('peter', 'sarah')
#>>> 5

# One deletion
print levenshtein('pete', 'peter')

print levenshtein('ltaa','altansuren')
