import random
from Track import Track
import pygame
pygame.init()

class DJ:
    # game sounds
    soundCorrect = Track("", 'sounds/correct.ogg')
    soundIncorrect = Track("", 'sounds/incorrect.ogg')

    # put song variables here in this format: trackName = Track("string of song to be displayed", 'music/filename.ogg')
    trackShootingStars = Track("Shooting Stars", 'music/shooting.ogg')
    trackFeelGoodInc = Track("Feel Good Inc", 'music/feelgood.ogg')
    trackArcticMonkeys = Track("Do I Wanna Know", 'music/arctic.ogg')
    trackRayParkerJr = Track("Ghostbusters", 'music/rayparker.ogg')
    trackMCHammer = Track("U Can t Touch This", 'music/hammer.ogg')
    trackNirvana = Track("Smells Like Teen Spirit", 'music/nirvana.ogg')
    trackMoDo = Track("Eins Zwei Polizei", 'music/modo.ogg')
    trackBloodhoundGang = Track("The Bad Touch", 'music/bloodhound.ogg')
    trackSmashMouth = Track("All Star", 'music/smashmouth.ogg')
    trackBobSinclar = Track("Love Generation", 'music/bobsinclar.ogg')
    trackScatmanJohn = Track("Scatman", 'music/scatman.ogg')
    trackBobbyMcFerrin = Track("Dont Worry Be Happy", 'music/mcferrin.ogg')
    trackToto = Track("Africa", 'music/tot.ogg')
    trackYvesLarock = Track("My dream is to fly", 'music/larock.ogg')
    trackRustedRoot = Track("Send Me On My Way", 'music/rustedroot.ogg')
    trackGramatik = Track("Just Jammin", 'music/gramatik.ogg')
    trackCaravanPalace = Track("Lone Digger", 'music/caravan.ogg')
    trackRasputin = Track("Rasputin", 'music/rasputin.ogg')
    trackVulfpeck = Track("Dean Town", 'music/vulfpeck.ogg')
    trackJoyDivision = Track("Atmosphere", 'music/division.ogg')
    trackCageTheElephant = Track("Aint No Rest For The Wicked", 'music/elephant.ogg')
    trackBillyJoel = Track("We didnt start the fire", 'music/billy.ogg')
    trackDeanMartin = Track("Aint that a kick in the head", 'music/kickinthehead.ogg')
    trackFalloutNewVegas = Track("Jingle Jangle Jingle", 'music/fallout.ogg')
    trackFiveStars = Track("Atom bomb baby", 'music/fivestars.ogg')

    arraySongs = [
        # put songs here as: varName,
        trackShootingStars,
        trackFeelGoodInc,
        trackArcticMonkeys,
        trackRayParkerJr,
        trackMCHammer,
        trackNirvana,
        trackMoDo,
        trackBloodhoundGang,
        trackSmashMouth,
        trackBobSinclar,
        trackScatmanJohn,
        trackBobbyMcFerrin,
        trackToto,
        trackYvesLarock,
        trackRustedRoot,
        trackGramatik,
        trackCaravanPalace,
        trackRasputin,
        trackVulfpeck,
        trackJoyDivision,
        trackCageTheElephant,
        trackBillyJoel,
        trackDeanMartin,
        trackFalloutNewVegas,
        trackFiveStars

    ]

    arrayRandomSongs = []
    dictChosen = {}
    trackChosen = ""
    trackKey = ""

    def randomizeArray(self):
        del self.arrayRandomSongs[:] # wipes array of all contents without making a new one
        self.arrayRandomSongs = self.arraySongs[:]
        random.shuffle(self.arrayRandomSongs)

    def chooseListing(self):
        self.dictChosen.clear() # same here
        for i in xrange(4):
            self.dictChosen.update({i: self.arrayRandomSongs[i]})
        del self.arrayRandomSongs[0:3]

    def chooseTrack(self):
        rdnumber = random.randint(0,3)
        self.trackChosen = self.dictChosen.get(rdnumber)
        self.trackKey = rdnumber + 1