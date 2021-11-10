class articleParams:
    def __init__(self, id, BSobj):
        self.id = id
        self.html = BSobj
        self.articleRef = self.setArticleRef()
        self.toJson = {'id': self.id}

        self.creator = self.setCreator()
        self.title = self.setTitle()
        self.text = self.setText()
        self.dollarsPledged = self.setDollarsPledged()
        self.dollarsGoal = self.setDollarsGoal()
        self.numBackers = self.setNumBackers()
        self.daysToGo = self.setDaysToGo()
        self.allOrNothing = self.setAllOrNothing()

    def setCreator(self):
        pass

    def setTitle(self):
        pass

    def setText(self):
        pass

    def setDollarsPledged(self):
        pass

    def setDollarsGoal(self):
        pass
    
    def setNumBackers(self):
        pass
    
    def setDaysToGo(self):
        pass

    def setAllOrNothing(self):
        pass

    def setArticleRef(self):
        pass