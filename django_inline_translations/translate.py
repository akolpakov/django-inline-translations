from django.templatetags.i18n import TranslateNode, BlockTranslateNode
from django.template import RequestContext

import hashlib


def get_key_hash(key):
    return hashlib.md5(key.encode('utf-8')).hexdigest()


def get_wrapped_content(key, content):
    if not key:
        return content
    return '<span class="django-inline-translate" data-translate-id="%s">%s</span>' % (get_key_hash(key), content)


def _replace_render(cls):
    original_render = cls.render

    def render(self, context):
        content = original_render(self, context)

        if isinstance(context, RequestContext) and context.request.user.is_staff:
            if cls == TranslateNode:
                key = self.filter_expression.var.literal
            elif cls == BlockTranslateNode:
                key, vars = self.render_token_list(self.singular)
            else:
                return content
            return get_wrapped_content(key, content)
        else:
            return content

    cls.render = render


_replace_render(TranslateNode)
_replace_render(BlockTranslateNode)
