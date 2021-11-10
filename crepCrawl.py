class articleParams:
    def __init__(self, id, BSobj):
        self.id = id
        self.html = BSobj
        self.toJson = {'id': self.id}

        self.creator = self.setCreator()
        self.title = self.setTitle()
        self.dollarsPledged = self.setDollarsPledged()
        self.daysToGo = self.setDaysToGo()

        self.articleRef = ''

        self.text = ''
        self.dollarsGoal = ''
        self.numBackers = ''
        self.allOrNothing = ''

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

    def setDaysToGo(self):
        pass

    def setAllOrNothing(self):
        pass

    def setArticleRef(self):
        pass