from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json
from .validator_class import ValidatorClass

from gyaan.interactors.create_comment_interactor \
    import CreateCommentInteractor
from gyaan.storages.storage_implementation \
    import StorageImplementation
from gyaan.presenters.post_presenter_implementation \
    import PostPresenterImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user = kwargs['user']
    user_id=user.id
    entity_type = kwargs['entity_type']
    entity_id = kwargs['entity_id']
    request_data = kwargs['request_data']
    content = request_data['content']

    storage = StorageImplementation()
    post_presenter = PostPresenterImplementation()
    interactor = CreateCommentInteractor(
        storage=storage,
        post_presenter=post_presenter
    )

    get_posts_response = interactor.create_comment(
        user_id=user_id, entity_type=entity_type, entity_id=entity_id,
        content = content
    )

    response = HttpResponse(status=200)

    return response