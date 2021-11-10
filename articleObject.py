class articleParams:
    def __init__(self, BSobj):
        self.json = {}
        self.html = BSobj
        # אפשר לא להחזיק את הפרמטרים ופשוט להכניס אותם לתוך הJSON לפי הסדר בכל פונקציה

        self.articleRef = self.setArticleRef()

        self.id = self.setId()
        self.creator = self.setCreator()
        self.title = self.setTitle()
        self.dollarsPledged = self.setDollarsPledged()
        self.dollarsGoal = self.setDollarsGoal()
        self.numBackers = self.setNumBackers()
        self.daysToGo = self.setDaysToGo()

        self.allOrNothing = self.setAllOrNothing()
        self.text = self.setText()

    def setId(self):
        pass

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
        # soup = self.articleRef
        # allOrNothing = soup.find_all('span', {'data-test-id': "deadline-exists"})  # finds all or nothing text
        pass

    def setArticleRef(self):
        pass

    def jsonCreator(self):
        pass

    def getJson(self):
        return self.json