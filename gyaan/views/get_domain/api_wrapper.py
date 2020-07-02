from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json
from .validator_class import ValidatorClass

from gyaan.interactors.get_domain_metrics_interactor \
    import GetDomainMetricsInteractor
from gyaan.storages.domain_storage_implementation \
    import DomainStorageImplementation
from gyaan.presenters.presenter_implementation \
    import PresenterImplementaion

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user = kwargs['user']
    user_id=user.id
    domain_id = kwargs['domain_id']

    domain_storage = DomainStorageImplementation()
    presenter = PresenterImplementaion()
    interactor = GetDomainMetricsInteractor(
        domain_storage=domain_storage,
        presenter=presenter,
    )

    get_domain_metrics = interactor.get_domain_metrics(
        user_id=user_id,
        domain_id=domain_id
    )

    data = json.dumps(get_domain_metrics)
    response = HttpResponse(data, status=200)

    return response