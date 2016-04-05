from django.utils import translation
from django.utils.translation import trans_real, get_language
import gettext


def clean_translation_cache():
    try:

        # Reset gettext.GNUTranslation cache.
        gettext._translations = {}

        # Reset Django by-language translation cache.
        trans_real._translations = {}

        # Delete Django current language translation cache.
        trans_real._default = None

        # Delete translation cache for the current thread,
        # and re-activate the currently selected language (if any)
        translation.activate(get_language())
    except AttributeError:
        pass
