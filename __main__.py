import time
import random
from dictionary import DJ
from texts import *
from Layout import Layout

class gamelogic:

    boolGameloop = True
    p_score = 0
    p_ronde = 0
    p_user = ''
    p_name = ''
    p_lastname = ''
    p_user_id = str(0)
    p_file = 'chris.ogg'
    # p_name = ""
    # p_score = 0
    # p_ronde = 0

    dj = DJ()

    # functions go here

    def startround(self):
        print textBlank
        print Layout.bold + textRonde1.format(self.p_ronde)
        self.dj.chooseListing()
        self.dj.chooseTrack()
        # dj.trackChosen.playsound()()
        print "The song is {0}.".format(self.dj.trackChosen.name)

        def internalround():
            global p_score
            print textRonde2
            for i in xrange(4):
                print  "{0} - ".format(i + 1) + self.dj.dictChosen[i].name
            answer = raw_input(textRonde3 + Layout.end)
            if answer > '4':
                print Layout.bold + Layout.red + textError2 + Layout.end
                raw_input(textEnter)
                internalround()
            elif answer == str(self.dj.trackKey):
                self.dj.soundCorrect.playsound()
                print Layout.bold + Layout.green + textRonde5 + Layout.end
                print Layout.bold + textRonde6 + Layout.end
                self.p_score += 1
                raw_input(textEnter)
            elif answer == '1' or '2' or '3' or '4':
                self.dj.soundIncorrect.playsound()
                print Layout.bold + Layout.red + textRonde4.format(self.dj.trackChosen.name) + Layout.end
                raw_input(textEnter)
            else:
                print Layout.bold + Layout.red + textError2 + Layout.end
                raw_input(textEnter)
                internalround()
        internalround()

    # while boolGameloop:
    #     # all the functions executed in their respective order
    #     startround()
    #     p_ronde += 1
    #     if p_ronde == 10:
    #         boolGameloop = False