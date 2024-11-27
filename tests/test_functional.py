from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
# Fixture pour initialiser et fermer le navigateur
@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# Test du titre de la page d'accueil
def test_homepage_title(browser):
    browser.get("http://localhost:8000")
    assert "El Elenizado - Blog" in browser.title

@pytest.mark.selenium
def test_cours_page_download_link():
    """
    Vérifie que les liens de téléchargement des fichiers sont présents sur la page Cours.
    """
    driver = webdriver.Chrome()
    try:
        # Ouvrir le site principal
        driver.get("http://localhost:8000")

        # Accéder à la page Cours
        driver.get("http://localhost:8000/elenizado/cours")

        # Vérifier qu'un lien de téléchargement spécifique est présent
        download_link = driver.find_element(By.LINK_TEXT, "Descargar")
        href = download_link.get_attribute("href")
        assert "Fiche_Projet_1_1.pdf" in href
    finally:
        driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.mark.selenium
def test_cours_page_title():
    """
    Vérifie que le titre de la page Cours est affiché correctement après navigation.
    """
    driver = webdriver.Chrome()  # Assurez-vous d'avoir configuré ChromeDriver
    try:
        # Ouvrir le site principal
        driver.get("http://localhost:8000")
        
        # Accéder à la page Cours
        driver.get("http://localhost:8000/elenizado/cours")

        # Vérifier le titre de la page
        page_title = driver.find_element(By.CLASS_NAME, "post-list-title").text
        assert page_title == "Cursos"
    finally:
        driver.quit()


@pytest.mark.selenium
def test_contact_form_empty_fields():
    """
    Teste la soumission du formulaire de contact avec des champs vides.
    Vérifie si le message d'erreur 'Veuillez remplir correctement les champs' s'affiche.
    """
    driver = webdriver.Chrome()

    try:
        # Ouvrir la page de contact
        driver.get("http://127.0.0.1:8000/about/contact")

        # Attendre que le bouton de soumission soit visible
        wait = WebDriverWait(driver, 10)
        submit_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "frm-button")))

        # Cliquer sur le bouton sans remplir les champs
        submit_button.click()

        # Attendre le message d'erreur
        error_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.alert.alert-danger")))
        assert "Veuillez remplir correctement les champs" in error_message.text

    finally:
        # Fermer le navigateur
        driver.quit()


@pytest.mark.selenium
def test_contact_form_invalid_email():
    """
    Teste la soumission du formulaire de contact avec un email incorrect.
    Vérifie si le message d'erreur 'email incorrect' s'affiche.
    """
    driver = webdriver.Chrome()

    try:
        # Ouvrir la page de contact
        driver.get("http://127.0.0.1:8000/about/contact")

        # Attendre que les champs du formulaire soient visibles
        wait = WebDriverWait(driver, 10)
        name_input = wait.until(EC.presence_of_element_located((By.NAME, "nname")))
        email_input = wait.until(EC.presence_of_element_located((By.NAME, "eemail")))
        phone_input = wait.until(EC.presence_of_element_located((By.NAME, "wwebsite")))
        subject_input = wait.until(EC.presence_of_element_located((By.NAME, "ssubject")))
        message_input = wait.until(EC.presence_of_element_located((By.NAME, "mmessage")))

        # Remplir les champs avec un email incorrect
        name_input.send_keys("bbbbb")
        email_input.send_keys("bbb@glail.com")
        phone_input.send_keys("bbbbb")
        subject_input.send_keys("bbbbb")
        message_input.send_keys("bbbbb")

        # Soumettre le formulaire
        submit_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "frm-button")))
        submit_button.click()

        # Attendre le message d'erreur
        error_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.alert.alert-danger")))
        assert "email incorrect" in error_message.text

    finally:
        # Fermer le navigateur
        driver.quit()

@pytest.mark.selenium
def test_contact_form_submission():
    """
    Teste la soumission du formulaire de contact.
    Vérifie si le message de confirmation s'affiche après une soumission réussie.
    """
    driver = webdriver.Chrome()

    try:
        # Ouvrir la page de contact
        driver.get("http://127.0.0.1:8000/about/contact")

        # Attendre que les champs du formulaire soient visibles
        wait = WebDriverWait(driver, 10)

        # Localiser et remplir les champs du formulaire
        name_input = wait.until(EC.presence_of_element_located((By.NAME, "nname")))
        name_input.send_keys("Test User")

        email_input = wait.until(EC.presence_of_element_located((By.NAME, "eemail")))
        email_input.send_keys("testuser@example.com")

        phone_input = wait.until(EC.presence_of_element_located((By.NAME, "wwebsite")))
        phone_input.send_keys("123456789")

        subject_input = wait.until(EC.presence_of_element_located((By.NAME, "ssubject")))
        subject_input.send_keys("Test Subject")

        message_input = wait.until(EC.presence_of_element_located((By.NAME, "mmessage")))
        message_input.send_keys("This is a test message.")

        # Soumettre le formulaire
        submit_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "frm-button")))
        submit_button.click()

        # Attendre la confirmation
        success_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.alert.alert-success")))
        assert "l'enregistrement a bien été effectué" in success_message.text

    finally:
        # Fermer le navigateur
        driver.quit()
        