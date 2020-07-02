from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json
from .validator_class import ValidatorClass

from gyaan.interactors.create_post_interactor \
    import CreatePostInteractor
from gyaan.storages.post_storage_implementation \
    import PostStorageImplementation
from gyaan.presenters.post_presenter_implementation \
    import PostPresenterImplementation

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user = kwargs['user']
    user_id=user.id
    request_data = kwargs["request_data"]
    title = request_data["title"]
    content = request_data["content"]
    tag_ids = request_data["tag_ids"]
    domain_id = kwargs["domain_id"]

    post_storage = PostStorageImplementation()
    post_presenter = PostPresenterImplementation()
    interactor = CreatePostInteractor(
        post_storage=post_storage,
        post_presenter=post_presenter,
    )

    interactor.create_post(
        user_id=user_id,
        title=title,
        content=content,
        domain_id=domain_id,
        tag_ids=tag_ids)

    response = HttpResponse(status=201)

    return response