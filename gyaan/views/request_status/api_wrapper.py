from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json
from .validator_class import ValidatorClass

from gyaan.interactors.approve_or_reject_request_interactor \
    import ApproveOrRejectRequestInteractor
from gyaan.storages.domain_storage_implementation \
    import DomainStorageImplementation
from gyaan.presenters.domain_presenter_implementation \
    import DomainPresenterImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user = kwargs['user']
    user_id=user.id
    request_data = kwargs['request_data']
    request_id = request_data['user_id']
    accept_status = request_data['status']

    domain_storage = DomainStorageImplementation()
    domain_presenter = DomainPresenterImplementation()
    interactor = ApproveOrRejectRequestInteractor(
        domain_storage=domain_storage,
        domain_presenter=domain_presenter
    )

    interactor.approve_or_reject_request(
        user_id=user_id, request_id=request_id, accept_status=accept_status
    )

    response = HttpResponse(status=200)

    return response