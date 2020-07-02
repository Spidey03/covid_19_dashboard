from dataclasses import dataclass

@dataclass()
class UserDto:
    user_id: int
    is_admin: bool
