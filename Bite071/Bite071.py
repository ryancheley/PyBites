class RecordScore():
    """Class to track a game's maximum score"""
    def __init__(self):
        self.score = None

    def __call__(self, *args, **kwargs):
        if self.score == None:
            self.score = args[0]
        if self.score < args[0]:
            self.score = args[0]
        return self.score
