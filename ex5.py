name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print ( "Let's talk about %s." % name )
print ( "He's %r inches tall." % height )
print ( "  Which is %f cm." % ( height * 30.48 ) )
print ( "He's %r pounds heavy." % weight )
print ( "  Which is %f kilograms." % ( weight * 0.453592 ) )
print ( "Actually that's not too heavy." )
print ( "He's got %s eyes and %s hair." % (eyes, hair) )
print ( "His teeth are usually %s depending on the coffee." % teeth )

# this line is tricky, try to get it exactly right
print ( "If I add %r, %r, and %r I get %r." % (
    age, height, weight, age + height + weight )
    )
