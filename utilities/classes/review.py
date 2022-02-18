from utilities.db.db_manager import dbManager


class reviews:
    def __init__(self, name=None, Comment=None):
        self.review_ID = 1
        self.name = name
        self.Comment = Comment
        self.stars_rate = 4

    def info(self):
        query = "INSERT INTO reviews(review_ID, name, Comment, stars_rate) VALUES ('%s', '%s', '%s', '%s') % (self.review_ID, self.name, self.Comment, self.stars_rate)"
        dbManager.commit(query)
        # dbManager.commit('''
        # INSERT INTO reviews(review_ID, name, Comment, stars_rate)
        # VALUES ('%s', '%s', '%s', '%s')
        # ''' % (self.review_ID, self.name, self.Comment, self.stars_rate))
