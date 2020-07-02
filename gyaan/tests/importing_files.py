""" import storage implementation"""
from gyaan.storages.post_storage_implementation \
    import PostStorageImplementation
from gyaan.storages.domain_storage_implementation \
    import DomainStorageImplementation

from gyaan.models import *
from django.db.models import Prefetch, Count
from django.db import connection

# importing presenter implementation
from gyaan.presenters.post_presenter_implementation \
    import PostPresenterImplementation
from gyaan.interactors.presenters.post_presenter_interface \
    import PostPresenterInterface
from gyaan.presenters.domain_presenter_implementation \
    import DomainPresenterImplementation

# importing interactors
from gyaan.interactors.get_post_interactor import GetPostInteractor
from gyaan.interactors.get_domain_tags_interactor import GetDomainTagsInteractor

post_storage=PostStorageImplementation()
post_presenter = PostPresenterImplementation()

i = GetPostInteractor(
    post_storage=post_storage,
    post_presenter=post_presenter
)

# output = i.get_post(1,1)
# print(output)
domain_storage = DomainStorageImplementation()
domain_presenter = DomainPresenterImplementation()

tags = GetDomainTagsInteractor(
        domain_storage=domain_storage,
        domain_presenter=domain_presenter
    )