# More strings and text

x = "there are %d types of people." % 10
binary = "binary"
doNot = "don't"
y = "Those who know %s and those who %s" % (binary, doNot)

print(x)
print(y)

print("I said: %r.:" % x)
print("I also said: '%s'.")

hilarius = True
jokeEvolution = "Isn't that joke so funny?! %r"

print(jokeEvolution % hilarius)

w = "This is the left side of..."
e = "a string with a right side."
print(w+e)

# More printing fun
print("Mary had a little lamb.")
print("Its fleece was white as %s." 'snow')
print("And everywhere that Mary went.")
print("." * 10)
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print(end1 + end2 + end3 + end4 + end5 + end6)
print(end7 + end8 + end9 + end10 + end11 + end12)

# But wait! There's more:
formatter = "%r %r %r"
print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two", "three", "four"))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))

# why do I use %r instead of %s in the above example

# which should I use on a regular basis?

# why does %r sometimes give me single quotes around things?

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nJun\nJul\nAug"

print("Here are the days: ", days)
print("Here are the days: ", months)

print("""
There's something going on here.
With the three doubles-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")

# examine closely the differance
print("Here are the months: %r")


# escape sequences redux












print(backslashCat)
print(topCat)

# Escape Seq       What it does?
# \\
# \'
# \"
# \a
# \b
# \f
# \n
# \N{name}
# \r
# \t
# \uxxxx
# \Uxxxxxxxx
# \v
# \ooo
# \xhh

# What does the following code block do:
# while True:
#      for i in ["/", "-", "|", "\\", "|"]:
#           print("%s\r" % i, end='')

# Can you use ''' instead of """ ?

age = input("How old are you?")
height = input("How tall are you?")

print("So, you are %r old and %r tall." %(age, height))

# Ask 4 more questions and handle those responses
