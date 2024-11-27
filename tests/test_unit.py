import pytest
from django.core.exceptions import ValidationError
from website.models import SiteInfo, Newsletter
from about.models import Gallerie
from elenizado.models import Publication
from about.models import Curriculum, Contact
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_newsletter_duplicate_email():
    email = "duplicate@example.com"
    Newsletter.objects.create(email=email)
    with pytest.raises(ValidationError):
        duplicate = Newsletter(email=email)
        duplicate.full_clean()

@pytest.mark.django_db
def test_siteinfo_model():
    site_info = SiteInfo.objects.create(
        nom="Test Site",
        email="test@example.com",
        telephone=1234567890,
        description="Test description",
        logo="logo/test.png",
        status=True
    )
    assert site_info.nom == "Test Site"

@pytest.mark.django_db
def test_gallerie_model_status():
    gallery = Gallerie.objects.create(
        titre="Gallery Test",
        gallerie="path/to/image.jpg",
        status=True
    )
    assert gallery.titre == "Gallery Test"

@pytest.mark.django_db
def test_publication_retrieve():
    publication = Publication.objects.create(
        titre="Test Publication",
        description="Content",
        image="image/path.jpg",
        status=True
    )
    assert publication.titre == "Test Publication"

# Tests pour le modèle Curriculum
@pytest.mark.django_db
def test_curriculum_creation():
    curriculum = Curriculum.objects.create(
        photo='images/curriculum/sample.jpg',
        nom='Test Curriculum',
        description='<p>Description HTML</p>',
        cv='cv/curriculum/sample.pdf',
        status=True,
    )
    assert curriculum.nom == 'Test Curriculum'
    assert curriculum.status is True

@pytest.mark.django_db
def test_curriculum_str_method():
    curriculum = Curriculum.objects.create(
        photo='images/curriculum/sample.jpg',
        nom='Sample Curriculum',
        description='Sample Description',
        cv='cv/curriculum/sample.pdf',
        status=True,
    )
    assert str(curriculum) == 'Sample Curriculum'

# Tests pour le modèle Contact
@pytest.mark.django_db
def test_contact_creation():
    contact = Contact.objects.create(
        nom='John Doe',
        email='johndoe@example.com',
        subject='Test Subject',
        telephone=123456789,
        message='This is a test message.',
        status=True,
    )
    assert contact.nom == 'John Doe'
    assert contact.email == 'johndoe@example.com'

@pytest.mark.django_db
def test_contact_email_validation():
    with pytest.raises(ValidationError):
        contact = Contact(
            nom='Jane Doe',
            email='invalid-email',
            subject='Test Subject',
            telephone=987654321,
            message='Invalid email test.',
        )
        contact.full_clean()

# Test utilisateur (User Model)
@pytest.mark.django_db
def test_user_creation():
    user = User.objects.create_user(username='testuser', password='password123')
    assert user.username == 'testuser'

@pytest.mark.django_db
def test_user_authentication():
    user = User.objects.create_user(username='testuser', password='password123')
    assert user.check_password('password123') is True

# Tests de validation sur des champs
@pytest.mark.django_db
def test_curriculum_field_validation():
    curriculum = Curriculum(
        nom="A" * 256,  # Dépassement de la longueur maximale
        description='<p>Description</p>',
    )
    with pytest.raises(ValidationError):
        curriculum.full_clean()
