import pytest
from django.urls import reverse
from website.models import SiteInfo, Newsletter
from django.core.exceptions import ValidationError

@pytest.mark.django_db
def test_index_view(client):
    SiteInfo.objects.create(
        nom="Test Site",
        email="test@example.com",
        telephone=1234567890,
        description="Test description",
        logo="logo/test.png",
        status=True
    )
    response = client.get(reverse("index"))
    assert response.status_code == 200
