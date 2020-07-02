from gyaan.interactors.storages.post_storage_interface \
    import PostStorageInterface

from gyaan.interactors.presenters.post_presenter_interface \
    import PostPresenterInterface

from gyaan.interactors.storages.dtos_v2 import (
    PresenterCommentDto, PresenterReplyDto, PostCompleteDetailsPresenterDto,
    PresenterDomainPostsDto, PostDetailsWithMetricsDto
)

class GetPostInteractor:

    def __init__(self, post_storage: PostStorageInterface,
                 post_presenter: PostPresenterInterface):
        self.post_storage = post_storage
        self.post_presenter = post_presenter

    def get_post(self, user_id: int, post_id: int):

        is_not_valid_post_id = not self.post_storage.validate_post_id(
            post_id=post_id
        )
        if is_not_valid_post_id:
            self.post_presenter.raise_exception_for_invalid_post_id()
            return

        post_details_dto = \
            self.post_storage.get_post_details_dto(post_id=post_id)


        comments_dto = post_details_dto.comments_dto
        reactions_dto = post_details_dto.reactions_dto

        is_user_reacted_to_this_post, post_reactions_count, \
        approved_answer_dto, comments_count, \
        parent_comments_with_replies_dto = \
                self.get_comments_and_reactions_complete_details(
                    user_id, post_id, comments_dto, reactions_dto)

        post_complete_details_dto = PostCompleteDetailsPresenterDto(
                post_details_dto=post_details_dto,
                is_user_reacted=is_user_reacted_to_this_post,
                comments_count=comments_count,
                post_reactions_count=post_reactions_count,
                approved_answer_dto = approved_answer_dto,
                comments_details_dto=parent_comments_with_replies_dto
            )
        # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        # print(post_complete_details_dto)
        # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

        response = self.post_presenter.get_post_response(
            post_complete_details_dto=post_complete_details_dto
        )
        # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        # print(response)
        # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

        return response

    def get_comments_and_reactions_complete_details(
            self, user_id, post_id, comments_dto, reactions_dto):
        is_user_reacted_to_this_post = self._get_user_reaction(
            user_id, reactions_dto)

        post_reactions_count = self._get_post_reactions_count(
            reactions_dto, post_id)


        approved_answer_dto = self._get_approved_answer_dto(
            comments_dto, post_id)

        parent_comments_dto, replies_dto = \
            self._seperate_comments_and_replies(comments_dto, post_id)


        comments_count = len(parent_comments_dto)

        parent_comments_with_replies_dto = \
            self._get_parent_comment_with_replies(
                parent_comments_dto, replies_dto, reactions_dto, user_id)

        return is_user_reacted_to_this_post, post_reactions_count, \
        approved_answer_dto, comments_count, parent_comments_with_replies_dto


    @staticmethod
    def _get_user_reaction(user_id, reactions_dto):
        bool_feild = user_id in [reaction.user_id for reaction in
                                 reactions_dto]
        return bool_feild

    @staticmethod
    def _get_post_reactions_count(reactions_dto, post_id):
        post_reactions_count = len([reaction for reaction in reactions_dto
                                    if reaction.post_id == post_id])
        return post_reactions_count


    def _get_approved_answer_dto(self, comments_dto, post_id):
        approved_answer_dto = [comment for comment in comments_dto
            if comment.is_answer == True and comment.post_id == post_id]
        is_answer = len(approved_answer_dto)
        if is_answer:
            approved_answer_dto = approved_answer_dto[0]
        else:
            approved_answer_dto = None
        return approved_answer_dto


    def _seperate_comments_and_replies(self, comments_dto, post_id):
        parent_comments_dto = []
        replies_dto = []
        for comment in comments_dto:
            is_same_post = comment.post_id == post_id
            if is_same_post:
                is_parent_comment = comment.parent_comment == None
                if is_parent_comment:
                    parent_comments_dto.append(comment)
                else:
                    replies_dto.append(comment)

        return parent_comments_dto, replies_dto


    def _get_parent_comment_with_replies(
            self, parent_comments_dto, replies_dto, reactions_dto, user_id):
        parent_comments_with_replies_dto = []
        for comment in parent_comments_dto:
            presenter_comment_dto = \
                self._get_comment_complete_details(
                    comment, replies_dto, reactions_dto, user_id
                )
            parent_comments_with_replies_dto.append(
                presenter_comment_dto)
        return parent_comments_with_replies_dto


    def _get_comment_complete_details(
            self, comment, replies_dto, reactions_dto, user_id):
        comment_id = comment.comment_id
        comment_replies_dto = []

        for reply in replies_dto:
            is_reply = reply.parent_comment == comment_id
            if is_reply:
                comment_replies_dto.append(
                    self._get_complete_reply_dto(
                        reply, reactions_dto, user_id
                    )
                )

        comment_reactions_count = len([
            reaction for reaction in reactions_dto
            if reaction.comment_id == comment_id])

        is_user_reacted_to_this_comment = \
            self._get_user_reaction_to_this_comment(
                comment, reactions_dto, user_id
            )

        return PresenterCommentDto(
            comment_dto=comment,
            replies_dto=comment_replies_dto,
            is_user_reacted=is_user_reacted_to_this_comment,
            replies_count=len(comment_replies_dto),
            reactions_count=comment_reactions_count
            )

    @staticmethod
    def _get_user_reaction_to_this_comment(comment, reactions_dto, user_id):
        is_same_user = False
        for reaction in reactions_dto:
            is_same_comment_id = reaction.comment_id == comment.comment_id
            if is_same_comment_id:
                is_same_user = reaction.user_id == user_id
                return is_same_user
        return is_same_user

    @staticmethod
    def _get_reply_reactions_count(reply, reactions_dto):
        reply_id = reply.comment_id
        reply_reactions_count = len([reaction for reaction in reactions_dto
                                     if reaction.comment_id == reply_id])
        return reply_reactions_count

    def _get_complete_reply_dto(self, reply, reactions_dto, user_id):
        reply_id = reply.comment_id
        reply_reactions_count = len([reaction for reaction in reactions_dto
                                     if reaction.comment_id == reply_id])

        is_user_reacted_to_this_reply = \
            self._get_user_reaction_to_this_comment(
                reply, reactions_dto, user_id)

        presenter_reply_dto = PresenterReplyDto(
                                reply_dto=reply,
                                is_user_reacted=is_user_reacted_to_this_reply,
                                reactions_count=reply_reactions_count)

        return presenter_reply_dto

    # get_domain_posts_interactor
    def get_domain_posts(self, user_id: int, domain_id: int,
                         limit: int, offset: int):

        is_not_valid_domain_id = not self.post_storage.validate_domain_id(
            domain_id=domain_id
        )
        if is_not_valid_domain_id:
            self.post_presenter.raise_exception_for_invalid_domain_id()
            return

        domain_posts_details_dto = \
            self.post_storage.get_domain_posts_details_dto(
                domain_id=domain_id, limit=limit, offset=offset
            )

        presenter_domain_posts_dto = self._get_all_posts_complete_details(
            domain_posts_details_dto, user_id)

        response = self.post_presenter.get_domain_posts_response(
            presenter_domain_posts_dto=presenter_domain_posts_dto
            )

        return response

    def _get_all_posts_complete_details(self, domain_posts_details_dto,
                                        user_id):
        comments_dto = domain_posts_details_dto.comments_dto
        reactions_dto = domain_posts_details_dto.reactions_dto
        posts_dto = domain_posts_details_dto.posts_dto

        posts_details_with_metrics_dto = []
        for post_dto in posts_dto:
            post_id = post_dto.post_id

            post_complete_details_dto = self._get_post_complete_details(
                user_id, post_id, comments_dto, reactions_dto)
            posts_details_with_metrics_dto.append(
                post_complete_details_dto)

        presenter_domain_posts_dto = PresenterDomainPostsDto(
            domain_posts_details_dto=domain_posts_details_dto,
            posts_details_with_metrics_dto=posts_details_with_metrics_dto
            )
        return presenter_domain_posts_dto


    def _get_post_complete_details(self, user_id, post_id,
                                   comments_dto, reactions_dto):

        is_user_reacted_to_this_post, \
        post_reactions_count, approved_answer_dto, comments_count, \
        parent_comments_with_replies_dto = \
            self.get_comments_and_reactions_complete_details(
                user_id, post_id, comments_dto, reactions_dto)

        post_complete_details_dto = \
            PostDetailsWithMetricsDto(
                post_id=post_id,
                is_user_reacted=is_user_reacted_to_this_post,
                post_reactions_count=post_reactions_count,
                approved_answer_dto=approved_answer_dto,
                comments_count=comments_count,
                parent_comments_with_replies_dto=parent_comments_with_replies_dto
            )

        return post_complete_details_dto


    def get_posts(self, user_id: int, limit: int, offset: int):

        domain_posts_details_dto = \
            self.post_storage.get_user_posts_details_dto(
                user_id=user_id, limit=limit, offset=offset
            )

        presenter_domain_posts_dto = self._get_all_posts_complete_details(
            domain_posts_details_dto, user_id)

        response = self.post_presenter.get_domain_posts_response(
            presenter_domain_posts_dto=presenter_domain_posts_dto
        )

        print("@@"*100)
        print(response)
        return response
