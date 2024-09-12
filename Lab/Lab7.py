#def menu(list, question):
#    for entry in list:
#        print 1 + list.index(entry),
#        print ") " + entry
#
#    return input(question) - 1
def menu(list, question):
    for entry in list:
        print 1 + list.index(entry),
        print ") " + entry
    try:
        return input(question) - 1
    except NameError:
        print "Enter a correct number"

# main program
#answer = menu(['Red','Blue','Purple','Gray','Black','Orange','White','Yellow'],\
#'Which is your favorite color?')

#print 'You picked answer ' + (answer + 1)

answer = menu(['Red','Blue','Purple','Gray','Black','Orange','White','Yellow'],\
'Which is your favorite color?')
try:
    print 'You picked answer', (answer + 1)
except:
    print '\nincorrect answer.'
