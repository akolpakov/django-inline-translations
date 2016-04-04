from django.utils import translation
from django.conf import settings

from .translate import get_key_hash

import polib
import os


def get_po_files():
    language = translation.get_language()

    lc_dirs = (os.path.join(d, language, 'LC_MESSAGES') for d in settings.LOCALE_PATHS)
    po_files = []

    for ldir in lc_dirs:
        for dirpath, dirnames, filenames in os.walk(ldir):
            po_files.extend(polib.pofile(os.path.join(dirpath, f)) for f in filenames if f.endswith('.po'))

    return po_files


def update_po(content):
    po_files = get_po_files()

    for po in po_files:
        for entry in po:
            key = get_key_hash(entry.msgid)
            if key in content:
                entry.msgstr = content[key]

        po.save()
        mo_filepath = po.fpath[:-2] + 'mo'
        po.save_as_mofile(mo_filepath)
