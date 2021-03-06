from appconf import AppConf

from django.conf import settings  # noqa: F401


class DjangoRestFrameworkRecaptchaConf(AppConf):
    """
    Django REST framework reCAPTCHA settings.
    """

    class Meta:
        prefix = "drf_recaptcha"

    VERIFY_ENDPOINT = "https://www.google.com/recaptcha/api/siteverify"

    SECRET_KEY = None
