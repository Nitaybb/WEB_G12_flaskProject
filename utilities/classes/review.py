from utilities.db.db_manager import dbManager


class Review:
    def __init__(self, name=None, comment=None, rate=None):

        self.name = name
        self.comment = comment
        self.stars_rate = rate

    def createReview(self):
        query = "INSERT INTO reviews(name, Comment, stars_rate) VALUES (%s, %s, %s)"
        dbManager.commit(query, args=( self.name, self.comment, self.stars_rate))
        # dbManager.commit('''
        # INSERT INTO reviews(review_ID, name, Comment, stars_rate)
        # VALUES ('%s', '%s', '%s', '%s')
        # ''' % (self.review_ID, self.name, self.Comment, self.stars_rate))

    @staticmethod
    def getAllRevires():
        query = "SELECT * FROM reviews"
        result = dbManager.fetch(query)
        data = []
        for review in result:
            rv = Review(review.name,review.Comment, review.stars_rate)
            data.append(rv)
        return data
