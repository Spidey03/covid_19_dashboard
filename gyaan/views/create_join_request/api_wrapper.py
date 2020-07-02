from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json
from .validator_class import ValidatorClass

from gyaan.interactors.create_domain_join_request_interactor \
    import CreateDomainJoinRequestInteractor
from gyaan.storages.domain_storage_implementation \
    import DomainStorageImplementation
from gyaan.presenters.domain_presenter_implementation \
    import DomainPresenterImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user = kwargs['user']
    user_id=user.id
    domain_id = kwargs['domain_d']
    request_data = kwargs['request_data']
    request_type = request_data['request_type']

    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print(user_id, request_type, domain_id)


    domain_storage = DomainStorageImplementation()
    domain_presenter = DomainPresenterImplementation()
    interactor = CreateDomainJoinRequestInteractor(
        domain_storage=domain_storage,
        domain_presenter=domain_presenter
    )

    response = HttpResponse(status=404)
    if request_type == "follow":
        interactor.create_domain_join_request(
            user_id=user_id, domain_id=domain_id
        )

        response = HttpResponse(status=200)

    return response