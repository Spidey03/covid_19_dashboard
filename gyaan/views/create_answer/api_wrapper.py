from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json
from .validator_class import ValidatorClass

from gyaan.interactors.mark_as_answer_interactor \
    import MarkAsAnswerInteractor
from gyaan.storages.storage_implementation \
    import StorageImplementation
from gyaan.presenters.presenter_implementation \
    import PresenterImplementaion


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user = kwargs['user']
    user_id=user.id
    comment_id = kwargs['comment_id']

    storage = StorageImplementation()
    presenter = PresenterImplementaion()
    interactor = MarkAsAnswerInteractor(
        storage=storage,
        presenter=presenter
    )

    get_posts_response = interactor.mark_as_answer(
        user_id=user_id, comment_id=comment_id
    )

    response = HttpResponse(status=200)

    return response