from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json
from .validator_class import ValidatorClass

from gyaan.interactors.get_post_interactor \
    import GetPostInteractor
from gyaan.storages.post_storage_implementation \
    import PostStorageImplementation
from gyaan.presenters.post_presenter_implementation \
    import PostPresenterImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user = kwargs['user']
    user_id=user.id
    post_id = kwargs['post_id']

    post_storage = PostStorageImplementation()
    post_presenter = PostPresenterImplementation()
    interactor = GetPostInteractor(
        post_storage=post_storage,
        post_presenter=post_presenter
    )

    get_post_response = interactor.get_post(
        user_id=user_id, post_id=post_id
    )
    data = json.dumps(get_post_response)
    response = HttpResponse(data, status=200)

    return response
