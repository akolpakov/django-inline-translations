from django.templatetags.i18n import TranslateNode, BlockTranslateNode
from django.template import RequestContext

import hashlib


def get_key_hash(key):
    return hashlib.md5(key).hexdigest()


def get_wrapped_content(key, content):
    return '<span class="django-inline-translate" data-translate-id="%s">%s</span>' % (get_key_hash(key), content)


def _replace_render(cls):
    original_render = cls.render

    def render(self, context):
        content = original_render(self, context)

        if isinstance(context, RequestContext) and context.request.user.is_staff:
            if cls == TranslateNode:
                key = str(self.filter_expression.resolve(context))
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
