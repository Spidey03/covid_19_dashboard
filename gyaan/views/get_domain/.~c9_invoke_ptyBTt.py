from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json
from .validator_class import ValidatorClass

from gyaan.interactors.create_reaction_interactor \
    import CreateReactionInteractor
from gyaan.storages.storage_implementation \
    import StorageImplementation
from gyaan.presenters.presenter_implementation \
    import PresenterImplementaion

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user = kwargs['user']
    user_id=user.id
    entity_type = kwargs["entity_type"]
    entity_id = kwargs["entity_id"]

    storage = StorageImplementation()
    presenter = PresenterImplementaion()
    interactor = CreateReactionInteractor(
        storage=storage,
        presenter=presenter,
    )

    interactor.create_reaction(
        user_id=user_id,
        entity_type=entity_type,
        entity_id=entity_id
    )

    response = HttpResponse(status=201)

    return response