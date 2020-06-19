from typing import List
from dataclasses import dataclass

@dataclass
class UserMCQResponseDto:
    user_id: int
    question_id: int
    option_id: int

@dataclass
class UserFIBResponseDto:
    user_id: int
    question_id: int
    answer: int

@dataclass
class QuestionDto:
    question_id: int
    options: List[int]

@dataclass
class FormDto:
    form_id: int
    is_live: bool
    questions: List[QuestionDto]