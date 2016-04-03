# -*- coding: utf-8 -*-

from django.test import TestCase
from django.template import Template, RequestContext
from django.contrib.auth.models import User, AnonymousUser
from django.test.client import RequestFactory

from django_inline_translations.translate import get_key_hash


class TranslateTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test')
        self.staff_user = User.objects.create_user(username='staff', is_staff=True)

        self.factory = RequestFactory()
        self.request = self.factory.get('/')

    def _render_template(self, string, context=None):

        ctx = RequestContext(self.request)
        if context:
            ctx.push(context)

        return Template(string).render(ctx)

    def test_render_template(self):
        rendered = self._render_template(
            'Hi, {{ name }}!',
            {'name': 'Test'}
        )
        self.assertEqual(rendered, 'Hi, Test!')

    def test_trans(self):
        self.request.user = self.staff_user

        rendered = self._render_template(
            '{% load i18n %}'
            '{% trans "test" %}'
        )
        self.assertEqual(rendered, '<span class="django-inline-translate" data-translate-id="%s">test</span>' % get_key_hash('test'))

    def test_trans_not_auth(self):
        self.request.user = self.user

        rendered = self._render_template(
            '{% load i18n %}'
            '{% trans "test" %}'
        )
        self.assertEqual(rendered, 'test')

    def test_trans_anonymous(self):
        self.request.user = AnonymousUser()

        rendered = self._render_template(
            '{% load i18n %}'
            '{% trans "test" %}'
        )
        self.assertEqual(rendered, 'test')

    def test_blocktrans(self):
        self.request.user = self.staff_user

        rendered = self._render_template(
            '{% load i18n %}'
            '{% blocktrans %}test{% endblocktrans %}'
        )
        self.assertEqual(rendered, '<span class="django-inline-translate" data-translate-id="%s">test</span>' % get_key_hash('test'))

    def test_blocktrans_not_auth(self):
        self.request.user = self.user

        rendered = self._render_template(
            '{% load i18n %}'
            '{% blocktrans %}test{% endblocktrans %}'
        )
        self.assertEqual(rendered, 'test')

    def test_blocktrans_anonymous(self):
        self.request.user = AnonymousUser()

        rendered = self._render_template(
            '{% load i18n %}'
            '{% blocktrans %}test{% endblocktrans %}'
        )
        self.assertEqual(rendered, 'test')
