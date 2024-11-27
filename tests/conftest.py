import pytest
from website.models import SiteInfo

@pytest.fixture
def create_site_info():
    return SiteInfo.objects.create(
        nom="Test Site",
        email="test@example.com",
        telephone=1234567890,
        description="Test description",
        logo="logo/test.png",
        status=True
    )
