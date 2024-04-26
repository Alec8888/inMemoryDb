import copy

class InMemoryDB:
    def __init__(self):
        self.database = {}
        self.workingDatabase = {}
        self.transInProg = False

    def put(self, key, value):
        if self.transInProg:
            self.workingDatabase[key] = value
        else:
            raise ValueError("Transaction must be in progress.")
    
    def get(self, key):
        return self.database.get(key)
        
    def begin_transaction(self):
        if self.transInProg:
            raise RuntimeError("Transaction already in progress")
        else:
            self.workingDatabase = copy.deepcopy(self.database)
            self.transInProg = True

    def commit(self):
        if self.transInProg:
            self.database = copy.deepcopy(self.workingDatabase)
            self.transInProg = False
        else:
            raise RuntimeError("Transaction must be in progress to commit.")
    
    def rollback(self):
        if self.transInProg:
            self.transInProg = False
            self.workingDatabase = {}
        else:
            raise RuntimeError("No transaction to rollback.")