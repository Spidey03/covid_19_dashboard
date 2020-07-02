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

    is_invalid_params = kwargs['request_query_params'] == None

    if is_invalid_params:
        limit = 2
        offset = 0
    else:
        limit = kwargs['request_query_params'].limit
        offset = kwargs['request_query_params'].offset
    domain_id = kwargs['domain_id']

    post_storage = PostStorageImplementation()
    post_presenter = PostPresenterImplementation()
    interactor = GetPostInteractor(
        post_storage=post_storage,
        post_presenter=post_presenter
    )

    get_domain_posts_response = interactor.get_domain_posts(
        user_id=user_id, domain_id=domain_id,
        limit=limit, offset=offset
    )

    # print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    # print(get_domain_posts_response)

    data = json.dumps(get_domain_posts_response)
    response = HttpResponse(data, status=200)

    return response