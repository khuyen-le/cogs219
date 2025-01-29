# Visualization of Skordos et al. (2017)
Reference: Skordos, D., Feiman, R., Bale, A., & Barner, D. (2020). Do children interpret ‘or’conjunctively?. *Journal of Semantics, 37*(2), 247-267. https://doi.org/10.1093/jos/ffz022

Online app: https://khuyenle.shinyapps.io/disjunction_skordos/ (for some reason, the error bars are not shown in the app). 

## Background
This line of work investigates how chilren interpret sentences with disjunctive 'or'. 
For example, adults interpret the sentence "Anne eats pizza or ice cream." as meaning that Anne will eat either pizza or ice cream, but not both. This is considered the 'exclusive' interpretation.
Previous work has found that unlike adults, most chilren (preschool age) interpret such sentences inclusively (i.e., Anne eats only pizza, or only ice cream, or both.) Notably, this 'inclusive' interpretation is the logical interpretation of 'or'. One interpretation of this developmental trajectory is that exclusive-OR (the adult-like interpretation) requires pragmatic reasoning, which children are still developing. 

Previous work has also found children who interpret 'or' conjunctively (i.e., Anne eats both pizza and ice cream, and it is not the case that Anne eats only pizza, or only ice cream.). An ongoing question is whether these conjunctive children exist, or if some coding scheme mistook children who were answer 'randomly' as being conjunctive.

### Study Design
This paper (and similar studies) asked children to make Truth-Value Judgments for some sentences with 'or' (e.g., "Anne eats pizza or ice cream."). They made these judgments when shown different scenarios -- the critical ones are when only 1 disjunct is true (1-Disjunct-True, e.g., Anne eats only pizza), and when both disjuncts are true (2-Disjunct-True, e.g., Anne eats both pizza and ice cream).

An exclusive interpretation would accept the case where only 1 disjunct is true, and reject the case where both disjuncts are true.
An inclusive interpretation would accept both the case where only 1 disjunct is true, and the case where both disjuncts are true.
A conjunctive interpretation would reject the case where only 1 disjunct is true, and accept the case where both disjuncts are true.

A problem with this design is that there are too few trials per scenario type to fully distinguish between 'random' behavior and any systematic interpretation. Most of these studies (including the current study) have 4 trials per scenario type. This means that on a binomial test with alpha = 0.05, a child has to answer consistently on all 4 trials to be significantly different from random choosing. Because children usually do not answer perfectly consistently, most studies use a threshold of 3/4 consistent answers to be considered 'systematic'. E.g., to be considered 'exclusive', a child has to accept 3 out of 4 scenarios where only 1 disjunct is true, and reject 3 out of 4 scenarios were both disjuncts are true.

This paper also tested different presentation of disjunctions to investigate whether children's interpretations are sensitive to the presentation context. I only have the data for two of three conditions tested. They found that when more than 2 disjuncts were presented, then children were more likely to accept the case where only 1 disjunct is true when they hear a sentence with 'or' (i.e., possibly becoming less conjunctive and more exclusive).

## Figure from Paper
(Figure 4 from the original paper)

### Strength
- Clearly showed difference between different presentations. 
- Showed error bars (but it was not clear what the error bars represented, probably SE).

### Weakness
- Did not show distribution of responses. 
- It was not clear from the figure that the scenario types (1-Disjunct-True and 2-Disjunct-True) were tested within-subjects.

## My Figure

### Response Tab
I plotted proportion of acceptance for each scenario type, and for each presentation condition. Error bars represent bootstrapped 95% CI. I also included half violin plots to show the distribution of responses (a trick from Martin!). I used a line plot to demonstrate that the scenario types were tested within-subjects. Viewers can choose which presentation condition and which scenario type to display. I wanted to include the control scenario types (e.g., 0-Disjunct-True) to help with understanding the data (there should not be a large difference between the presentation conditions).

I also included a table with the mean proportion of acceptance for each scenario type and presentation condition that were selected. 

### Category Tab
I plotted the number of children in each category (exclusive, inclusive, conjunctive) for each presentation condition. Critically, the categorization depends on a threshold set by the viewer, so they can observe firsthand the impact of threshold seletion. is I also included a table with the number of children in each category in each presentation condition, and I also added the categorization results from Tieu et al. (2017), which was an older, frequently-cited paper for the idea that some children are 'conjunctive'. 
