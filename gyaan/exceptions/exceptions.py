
class DomainNotExists(Exception):
    pass

class UserIsNotFollwerOfDomain(Exception):
    pass

class InvalidPostIdsException(Exception):

    def __init__(self, invalid_post_ids: int):
        self.invalid_post_ids = invalid_post_ids

class InvalidValueForOffset(Exception):
    pass

class InvalidValueForLimit(Exception):
    pass