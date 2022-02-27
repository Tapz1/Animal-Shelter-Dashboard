from pymongo import MongoClient
from bson.objectid import ObjectId
from pprint import pprint
import Credentials

class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(self, username, password):
        # initializes the MongoClient
        # grants access to MongoDB databases & collections
        # super(AnimalShelter, self).__init__(username, password)
        self.client = MongoClient('mongodb://%s:%s@localhost:55032' % (username, password))
        self.database = self.client['AAC']

    # this create method implements the C in CRUD
    def create(self, data):
        if data is not None:
            result = self.database.animal.insert_one(data).acknowledged # acknowledged is a boolean result
            print("Successfully created document")
            return result
        else:
            raise Exception("Nothing to save, data parameter is empty")

    # creates method to implement the R in CRUD
    def read(self, data):
        if data is not None:
            # result = (self.database.animal.find(data, {"_id":False})) # returns all that match
            result = (self.database.animal.find_one(data, {"_id":False})) # returns one for testing purposes
            print("\nDocument(s) matching your search: %s" % (data))
        # print iter for testing purposes, does not work with dash
            #for document in result: 
            #    print(document)
            return result

        else:
            raise Exception("Nothing to read here, it's empty inside!")
            
    # creates method to implement the R in CRUD for all
    def readAll(self, data={}):
        result = (self.database.animal.find(data, {"_id":False})) 
        
        return result
    


    def update(self, data_lookup, set_data_insert):
        """
            this updates a document by finding the document via data_lookup &
            set_data_insert to update through $set with a specifc parameter
        """

        if data_lookup is not None:
            result = (self.database.animal.update_one(data_lookup, set_data_insert))
            document = (self.database.animal.find(data_lookup))
            print("\nupdate successful:\n")
            for item in document:
                print(item)
            return result
        else:
            raise Exception("Nothing to update")

    def delete(self, data):
        if data is not None:
            result = (self.database.animal.delete_one(data))
            print("\nSuccesfully deleted %s documents" % (result.deleted_count))
            return result
        else:
            raise Exception("Nothing to do delete")
