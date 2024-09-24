import pytest

from an_app.models import Foo

pytestmark = pytest.mark.django_db


def test_issue():
    Foo.objects.create()
