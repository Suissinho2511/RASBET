import sqlite3


class Outcome:  # Outcome of a bet

    def __init__(self, id, name, price):  # Constructor
        self.id = id  # Outcome id
        self.name = ""  # Name of the outcome
        self.price = 0  # Price of the outcome

    def getId(self):  # Get id of the outcome
        return self.id

    def getName(self):  # Get name of the outcome
        return self.name

    def getPrice(self):  # Get price of the outcome
        return self.price

    def setName(self, name):  # Set name of the outcome
        self.name = name

    def setPrice(self, price):  # Set price of the outcome
        self.price = price

    def outcomeToDB(self, marketId):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("INSERT INTO Outcome VALUES (?, ?, ?)",
                  (self.name, self.price, marketId))
        conn.commit()
        conn.close()

    def DBtoOutcome(self, id):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM Outcome WHERE id=?", (id,))
        row = c.fetchone()
        self.id = row[0]
        self.name = row[1]
        self.price = row[2]
        conn.close()

    def updateOutcomeDB(self, name, price):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("UPDATE Outcome SET name=?, price=? WHERE id=?",
                  (name, price, self.id))
        conn.commit()
        conn.close()

    def __eq__(self, other):  # Compare two outcomes
        return self.name == other.name and self.price == other.price

    def __str__(self):  # String representation of outcome
        return self.name + " " + str(self.price)
