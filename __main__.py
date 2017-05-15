from dictionary import DJ

class gamelogic:

    boolGameloop = True
    p_score = 0
    p_ronde = 1
    p_name = ''
    p_lastname = ''
    p_user = p_name + ' ' + p_lastname
    p_user_id = str(0)
    p_file = ''
    p_lastresult = 3
    p_djprevsong = ''
    # p_name = ""
    # p_score = 0
    # p_ronde = 0

    dj = DJ()

    # functions go here

    def songs(self, option):
        return self.dj.dictChosen[option].name

    def assignvars(self):
        self.p_djprevsong = self.dj.trackChosen
        self.dj.randomizeArray()
        self.dj.chooseListing()
        self.dj.chooseTrack()
        self.p_file = self.dj.trackChosen.path
