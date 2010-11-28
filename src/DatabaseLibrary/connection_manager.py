#  Copyright (c) 2010 Franz Allan Valencia See
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

class ConnectionManager(object):
    """
    Connection Manager handles the connection & disconnection to the database.
    """

    def __init__(self):
        """
        Initializes _dbconnection to None.
        """
        self._dbconnection = None
        
    def connect_to_database(self, db2apiModuleName, dbName, username, password):
        """
        Loads the db2api module given `db2apiModuleName` then uses it to 
        connect to the database using `dbName`, `username`, and `password`. 
        """
        db2api = __import__(db2apiModuleName);
        self._dbconnection = db2api.connect (database=dbName, user=username, password=password)
        
    def disconnect_from_database(self):
        """
        Disconnects from the database.
        """
        self._dbconnection.close()
        
