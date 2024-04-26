import unittest
from inmemorydb import InMemoryDB

class TestInMemoryDB(unittest.TestCase):

    # should return null, because A doesn’t exist in the DB yet
    def test_get_keyDoesNotExist(self):
        db = InMemoryDB()
        self.assertIsNone(db.get('A'))

    # should throw an error because a transaction is not in progress
    def test_put_transactionNotInProgress(self):
        with self.assertRaises(ValueError):
            db = InMemoryDB()
            db.put('A', 5)

    # should return 6, that was the last value of A to be committed
    def test_put_notCommited(self):
        db = InMemoryDB()
        db.begin_transaction()
        db.put('A', 5)
        self.assertIsNone(db.get('A'))
        db.put('A', 6)
        db.commit()
        self.assertEqual(db.get('A'), 6)
    
    # throws an error, because there is no open transaction
    def test_commit_error(self):
        with self.assertRaises(RuntimeError):
            db = InMemoryDB()
            db.commit()
    
    # throws an error because there is no ongoing transaction
    def test_rollback_early(self):
        with self.assertRaises(RuntimeError):
            db = InMemoryDB()
            db.rollback()
    
    # should return null because B does not exist in the database
    def test_get_badKey(self):
        db = InMemoryDB()
        self.assertIsNone(db.get('B'))
        
    # Should return null because changes to B were rolled back
    def test_rollback_function(self):
        db = InMemoryDB()
        db.begin_transaction()
        db.put('B', 10)
        db.rollback()
        self.assertIsNone(db.get('B'))

    def test_transaction_singlton(self):
        db = InMemoryDB()
        db.begin_transaction()
        with self.assertRaises(RuntimeError):
            db.begin_transaction()

if __name__ == '__main__':
    unittest.main()