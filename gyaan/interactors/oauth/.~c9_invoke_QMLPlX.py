from abc import ABC, abstractmethod

class O(ABC):

    @abstractmethod
    def create_user_auth_tokens(self, user_id: int):
        pass

class OAuth2SQLStorage(ABC):

    @abstractmethod
    def get_or_create_default_application(self, user_id):
        pass

    @abstractmethod
    def create_access_token(self, user_id, application_id, scopes,
                        expiry_in_seconds):
        pass

    @abstractmethod
    def create_refresh_token(self, user_id, application_id, access_token_id):
        pass