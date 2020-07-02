from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json
from .validator_class import ValidatorClass

from gyaan.interactors.leave_a_domain_interactor \
    import LeaveDomainInteractor
from gyaan.storages.domain_storage_implementation \
    import DomainStorageImplementation
from gyaan.presenters.domain_presenter_implementation \
    import DomainPresenterImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user = kwargs['user']
    user_id=user.id
    domain_id = kwargs['domain_d']

    domain_storage = DomainStorageImplementation()
    domain_presenter = DomainPresenterImplementation()
    interactor = LeaveDomainInteractor(
        domain_storage=domain_storage,
        domain_presenter=domain_presenter
    )

    interactor.leave_a_domain(
        user_id=user_id, domain_id=domain_id
    )

    response = HttpResponse(status=200)

    return response