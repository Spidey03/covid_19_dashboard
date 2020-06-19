import pytest
from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions \
    import NotFound, Forbidden, BadRequest
from formaster.interactors.submit_form_response.base \
    import BaseSubmitFormResponseInteractor
from formaster.interactors.submit_form_response.fib_question \
    import FIBQuestionSubmitFormResponseInteractor
from formaster.interactors.storages.storage_interface \
    import StorageInterface
from formaster.interactors.presenters.presenter_interface \
    import PresenterInterface
from formaster.interactors.mixins import FormValidationMixin
from formaster.exceptions.exceptions\
    import FormDoesNotExist, FormClosed, QuestionDoesNotBelongToForm,\
        InvalidUserResponseSubmit


class TestFIBQusetionInteractor:

    def test_when_invalid_form_given_raise_form_does_not_exist(self):

        # Arrange
        form_id = 3
        question_id = 1
        answer = "India"
        user_id = 1

        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = FIBQuestionSubmitFormResponseInteractor(storage=storage,
            form_id=form_id, question_id=question_id, user_id=user_id,
            answer=answer)

        storage.get_form.side_effect = FormDoesNotExist
        presenter.raise_form_does_not_exist.side_effect = NotFound

        # Act
        with pytest.raises(NotFound):
            interactor.submit_form_response_wrapper(presenter=presenter)

        # Assert
        storage.get_form.assert_called_once_with(form_id=form_id)

    def test_when_form_is_not_active_raise_form_is_closed(self, inactive_form):

        # Arrange
        form_id = 1
        question_id = 1
        answer = "India"
        user_id = 1

        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = FIBQuestionSubmitFormResponseInteractor(storage=storage,
            form_id=form_id, question_id=question_id, user_id=user_id,
            answer=answer)

        storage.get_form.return_value = inactive_form
        presenter.raise_form_is_closed.side_effect = Forbidden

        # Act
        with pytest.raises(Forbidden):
            interactor.submit_form_response_wrapper(presenter=presenter)

        # Assert
        storage.get_form.assert_called_once_with(form_id=form_id)

    def test_when_invalid_question_id_given_raise_question_does_not_exist(self, live_form):

        # Arrange
        form_id = 1
        question_id = 1
        answer = "India"
        user_id = 1

        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = FIBQuestionSubmitFormResponseInteractor(storage=storage,
            form_id=form_id, question_id=question_id, user_id=user_id,
            answer=answer)

        storage.get_form.return_value = live_form
        storage.validate_question_id_with_form.side_effect = \
            QuestionDoesNotBelongToForm
        presenter.raise_question_does_not_belong_to_form.side_effect = BadRequest

        # Act
        with pytest.raises(BadRequest):
            interactor.submit_form_response_wrapper(presenter=presenter)

        # Assert
        storage.get_form.assert_called_once_with(form_id=form_id)
        storage.validate_question_id_with_form.assert_called_once_with(
            form_id=form_id, question_id=question_id)

    def test_when_invalid_answer_given_raise_invalid_user_response(self, live_form):

        # Arrange
        form_id = 1
        question_id = 1
        answer = "Delhi"
        user_id = 1
        valid_answer = "India"

        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = FIBQuestionSubmitFormResponseInteractor(storage=storage,
            form_id=form_id, question_id=question_id, user_id=user_id,
            answer=answer)

        storage.get_form.return_value = live_form
        storage.get_valid_answer_for_question.return_value = valid_answer
        presenter.raise_invalid_user_response.side_effect = BadRequest

        # Act
        with pytest.raises(BadRequest):
            interactor.submit_form_response_wrapper(presenter=presenter)

        # Assert
        storage.get_form.assert_called_once_with(form_id=form_id)
        storage.validate_question_id_with_form.assert_called_once_with(
            form_id=form_id, question_id=question_id)
        storage.get_valid_answer_for_question.assert_called_once_with(
            question_id=question_id)

    def test_create_user_response_for_mcq(self, live_form, user_fib_response):

        # Arrange
        form_id = 1
        question_id = 1
        answer = "India"
        user_id = 1
        valid_answer = "India"
        expected_response_id = 1
        expected_response = {'response_id':1}

        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = FIBQuestionSubmitFormResponseInteractor(storage=storage,
            form_id=form_id, question_id=question_id, user_id=user_id,
            answer=answer)

        storage.get_form.return_value = live_form
        storage.get_valid_answer_for_question.return_value = valid_answer
        storage.create_user_mcq_response.return_value = expected_response_id
        presenter.submit_form_response.return_value = {'response_id':1}

        # Act
        response = interactor.submit_form_response_wrapper(presenter=presenter)

        # Assert
        storage.get_form.assert_called_once_with(form_id=form_id)
        storage.validate_question_id_with_form.assert_called_once_with(
            form_id=form_id, question_id=question_id)
        storage.get_valid_answer_for_question.assert_called_once_with(
            question_id=question_id)
        storage.create_user_fib_response.assert_called_once_with(user_fib_response)
        assert response == expected_response
