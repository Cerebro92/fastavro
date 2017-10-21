
class InvalidSchemaException(Exception):
    '''
    Invalid Schema Exception
    '''
    def __init__(self, name, val, records=[]):
        super(InvalidSchemaException, self).__init__()
        self.name = name
        self.val = val
        self.records = records

