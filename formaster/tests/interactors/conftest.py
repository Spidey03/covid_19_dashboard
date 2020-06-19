import pytest
from formaster.interactors.storages.dtos import *

@pytest.fixture()
def questions():
    questions = [
        QuestionDto(
            question_id=1,
            options=[1,2,3,4]
        ),
        QuestionDto(
            question_id=2,
            options=[1,2,3,4]
        )
    ]
    return questions

@pytest.fixture()
def inactive_form(questions):
    form = FormDto(
        form_id=1,
        is_live=False,
        questions=questions
    )
    return form

@pytest.fixture()
def live_form(questions):
    form = FormDto(
        form_id=1,
        is_live=True,
        questions=questions
    )
    return form

@pytest.fixture()
def user_mcq_response():
    user_response_dto = UserMCQResponseDto(
        user_id=1,
        question_id=1,
        option_id=4
    )
    return user_response_dto

@pytest.fixture()
def user_fib_response():
    user_response_dto = UserFIBResponseDto(
        user_id=1,
        question_id=1,
        answer="India"
    )
    return user_response_dto
