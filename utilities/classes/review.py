from utilities.db.db_manager import dbManager

class reviews:
    def __init__(self, review_ID=None, name=None, Comment=None, stars_rate=None):
        self.review_ID = review_ID
        self.name = name
        self.Comment = Comment
        self.stars_rate = stars_rate
