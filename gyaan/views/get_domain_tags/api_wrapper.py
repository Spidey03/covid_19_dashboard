from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json
from .validator_class import ValidatorClass

from gyaan.interactors.get_domain_tags_interactor \
    import GetDomainTagsInteractor
from gyaan.storages.domain_storage_implementation \
    import DomainStorageImplementation
from gyaan.presenters.domain_presenter_implementation \
    import DomainPresenterImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    domain_id = kwargs['domain_id']

    domain_storage = DomainStorageImplementation()
    domain_presenter = DomainPresenterImplementation()
    interactor = GetDomainTagsInteractor(
        domain_storage=domain_storage,
        domain_presenter=domain_presenter
    )

    get_domain_tags = interactor.get_domain_tags(
        domain_id=domain_id
    )

    data = json.dumps(get_domain_tags)
    response = HttpResponse(data, status=200)

    return response