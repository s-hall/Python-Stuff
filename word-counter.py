tstring = """ setting the raised porch of joe clark store and the street in
front porch stretches almost completely across the stage with a
plank bench at either end at the center of the porch three steps
leading from street rear of porch center door to the store on
either side are single windows on which signs at left post office
and at right general store are painted soap boxes axe handles
small kegs etc on porch on which townspeople sit and lounge during
action above the roof of the porch the false front or imitation
second story of the shop is seen with large sign painted across it
joe clark general store large kerosine street lamp on post at
right in front of porch

saturday afternoon and the villagers are gathered around the store
several men sitting on boxes at edge of porch chewing sugar cane
spitting tobacco juice arguing some whittling others eating
peanuts during the act the women all dressed up in starched dresses
parade in and out of store people buying groceries kids playing in
the street etc general noise of conversation laughter and children
shouting but when the curtain rises there is momentary lull for
cane-chewing at left of porch four men are playing cards on a soap
box and seated on the edge of the porch at extreme right two children
are engaged in a checker game with the board on the floor between
them

when the curtain goes up the following characters are discovered on
the porch mayor joe clark the storekeeper deacon hambo deacon
goodwin old man matt brazzle will cody sykes jones lum boger the
young town marshall lige mosely and walter thomas two village wags
tom nixon and sam mosely and several others seated on boxes kegs
benches and floor of the porch tony taylor is sitting on steps of
porch with empty basket mrs taylor comes out with her arms full of
groceries empties them into basket and goes back in store all the
men are chewing sugar cane earnestly with varying facial expressions
the noise of the breaking and sucking of cane can be clearly heard in
the silence occasionally the laughter and shouting of children is
heard nearby off stage"""

print 'aber'

def word_counter(string):
    words = {}    

    a_words = string.split()
    print len(a_words)
    for word in a_words:
        if word not in words.keys():
	    words[word] = 1
            #print words
        else:
	    words[word] += 1
    print words

word_counter(tstring)

