from gyaan.interactors.storages.storage_interface \
    import StorageInterface
from gyaan.interactors.presenters.presenter_interface \
    import PresenterInterface
from gyaan.exceptions.exceptions \
    import DomainNotExists, UserIsNotFollwerOfDomain
from gyaan.interactors.storages.dtos import DomainDetailsDto

class GetDomainDetailsInteractor:

    def __init__(self, storage=StorageInterface):

        self.storage = storage

    def get_domain_details_wrapper(self,
            user_id: int, domain_id: int, presenter: PresenterInterface):

        try:
            domain_details_dto = self.get_domain_details(user_id, domain_id)
            response = \
                presenter.get_response_for_domain_details(domain_details_dto)
            return response
        except DomainNotExists:
            presenter.raise_domain_does_not_exists()
        except UserIsNotFollwerOfDomain:
            presenter.raise_user_not_follower()

    def get_domain_details(self, user_id: int, domain_id: int):

        # TODO: CHECK DOMAIN VALID OR NOT
        domain_dto = self.storage.get_domain_details(domain_id)

        # TODO: CHECK USER IS FOLLOWER
        is_user_follower = \
            self.storage.check_user_is_follower_of_domain(user_id, domain_id)
        is_user_not_follower = not is_user_follower
        if is_user_not_follower:
            raise UserIsNotFollwerOfDomain

        # TODO: GET DOMAIN STATS
        domain_stats = self.storage.get_domain_stats(domain_id=domain_id)

        domain_expert_ids = self.storage.get_domain_expert_ids(domain_id)
        domain_experts = self.storage.get_users_details(domain_expert_ids)

        is_user_domain_expert, requested_users_dto = \
            self._get_domain_expert_details(user_id, domain_id)
        domain_details_dto = DomainDetailsDto(
            domain=domain_dto,
            domain_stats=domain_stats,
            domain_experts=domain_experts,
            user_id=user_id,
            is_user_domain_expert=is_user_domain_expert,
            requested_users_dto=requested_users_dto
        )
        return domain_details_dto

    def _get_domain_expert_details(self, user_id: int, domain_id: int):

        print('a;jsfkj')
        is_user_domain_expert = self.storage.is_user_domain_expert(
            user_id=user_id, domain_id=domain_id)
        domain_join_requests_list, requested_users_dto = [], []

        print(is_user_domain_expert)
        if is_user_domain_expert:
            domain_join_requests_list = \
                self.storage.get_domain_join_request(domain_id)
        print(domain_join_requests_list)
        if domain_join_requests_list:
            print('a;jsfkj')
            user_ids = [domain_join_request.user_id \
                for domain_join_request in domain_join_requests_list]
            requested_users_dto = \
                self.storage.get_users_details(user_ids)
            print('a;jsfkj')
        return is_user_domain_expert, requested_users_dto