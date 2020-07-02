from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json
from .validator_class import ValidatorClass

from gyaan.interactors.get_user_metrics_interactor \
    import GetUserMetricsInteractor
from gyaan.storages.storage_implementation \
    import StorageImplementation
from gyaan.presenters.presenter_implementation \
    import PresenterImplementaion

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user = kwargs['user']
    user_id=user.id

    storage = StorageImplementation()
    presenter = PresenterImplementaion()
    interactor = GetUserMetricsInteractor(
        storage=storage,
        presenter=presenter,
    )

    get_user_metrics_response = interactor.get_user_metrcis(
        user_id=user_id)
    data = json.dumps(get_user_metrics_response)
    response = HttpResponse(data, status=200)

    return response