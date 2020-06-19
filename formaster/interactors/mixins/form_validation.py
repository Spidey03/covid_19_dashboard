from formaster.exceptions.exceptions import FormClosed


class FormValidationMixin:

    def validate_for_live_form(self, form_id: int):
        form = self.storage.get_form(form_id)
        is_live = form.is_live
        is_closed = not is_live
        if is_closed:
            raise FormClosed()

