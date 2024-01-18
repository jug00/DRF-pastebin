from allauth.account.adapter import DefaultAccountAdapter
from .tasks import send_allauth_email


class AccountAdapter(DefaultAccountAdapter):
    def send_mail(self, template_prefix, email, context):
        msg = self.render_mail(template_prefix, email, context)
        send_allauth_email.delay(msg.subject, msg.body, msg.from_email, tuple(msg.recipients()))
