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
    limit = kwargs['request_query_params'].limit
    offset = kwargs['request_query_params'].offset

    print(limit, offset)

    is_invalid_limit = limit == None
    if is_invalid_limit:
        limit = 2
    is_invalid_offset = limit == None
    if is_invalid_offset:
        offset = 0

    post_storage = PostStorageImplementation()
    post_presenter = PostPresenterImplementation()
    interactor = GetPostInteractor(
        post_storage=post_storage,
        post_presenter=post_presenter
    )

    get_posts_response = interactor.get_posts(
        user_id=user_id, limit=limit, offset=offset
    )
    print("$"*100)
    print(get_posts_response)
    print("$"*100)
    data = json.dumps(get_posts_response)
    response = HttpResponse(data, status=200)

    return response
