import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.search_page import SearchPage

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_saucedemo_login_automation(driver):
    login_page = SearchPage(driver)
    login_page.open("https://www.saucedemo.com/")
    
    # Geçerli bir test kullanıcısı ile giriş yap
    login_page.login("standard_user", "secret_sauce")
    
    # Doğrulama: Başarılı giriş yapıldığını URL ve başlık üzerinden kontrol et
    assert "inventory.html" in driver.current_url, f"Hata: Başarılı giriş yapılamadı! Mevcut URL: {driver.current_url}"
