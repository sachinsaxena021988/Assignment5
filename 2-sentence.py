#define subject 
subjects=["Americans","Indians"]
#define verbs
verbs=["play","watch"]
#define objects
objects=["Baseball","Cricket"]

# list comprihansion
value = [" ".join([a,b,c+'.']) for a in subjects for b in verbs for c in objects]

#print value
for x in value:
    print(x+'\n')