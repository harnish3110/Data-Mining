
# coding: utf-8

# In[1]:

import Orange


# raw_data = ["Blacklist, The Flash, FRIENDS",
#             "The Flash, Game of Thrones, Da Vinci Demons",
#             "Blacklist, Criminal Minds, Santa Clara Diet",
#             "Blacklist, The Flash, Game of Thrones",
#             "Blacklist, FRIENDS, Criminal Minds",
#             "The Flash, FRIENDS"]
raw_data = ["Cupcake, Hot Chocolate, Juice",
            "Hot Chocolate, Milk, Fruits",
            "Cupcake, Cereals, Ice Cream",
            "Cupcake, Hot Chocolate, Milk",
            "Cupcake, Juice, Cereals",
            "Hot Chocolate, Juice"]


# write data to the text file: data.basket
f = open('data2.basket', 'w')
for item in raw_data:
    f.write(item + '\n')
f.close()

# Load data from the text file: data.baske
data = Orange.data.Table("data2.basket")

# Identify association rules with supports at least 0.3
rules = Orange.associate.AssociationRulesSparseInducer(data, support = 0.3)

    # print out rules
print "%4s %4s  %s" % ("Supp", "Conf", "Rule")
for r in rules[:]:
    print "%4.1f %4.1f  %s" % (r.support, r.confidence, r)

rule = rules[0]
for idx, d in enumerate(data):
    print '\nUser {0}: {1}'.format(idx, raw_data[idx])
    for r in rules:
        if r.applies_left(d) and not r.applies_right(d):
            print "%4.1f %4.1f  %s" % (r.support, r.confidence, r)

