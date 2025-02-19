import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_search_by_name(driver):
    driver.get(" https://www.chitai-gorod.ru/ ")
    driver.find_element(By.CLASS_NAME, "header-search__input").send_keys("Ребенок Розмари")
    driver.find_element(By.CLASS_NAME, "header-search__button").click()
    txt = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/p').text
    assert "Показываем результаты по запросу" in txt


def test_search_by_author(driver):
    driver.get(" https://www.chitai-gorod.ru/ ")
    driver.find_element(By.CLASS_NAME, "header-search__input").send_keys("Айра Левин")
    driver.find_element(By.CLASS_NAME, "header-search__button").click()
    txt = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/p').text
    assert "Показываем результаты по запросу" in txt


def test_using_part_of_the_title(driver):
    driver.get(" https://www.chitai-gorod.ru/ ")
    driver.find_element(By.CLASS_NAME, "header-search__input").send_keys("Ребенок Роз")
    driver.find_element(By.CLASS_NAME, "header-search__button").click()
    txt = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/p').text
    assert "Показываем результаты по запросу" in txt


def test_search_by_name_from_numbers(driver):
    driver.get(" https://www.chitai-gorod.ru/ ")
    driver.find_element(By.CLASS_NAME, "header-search__input").send_keys("1984")
    driver.find_element(By.CLASS_NAME, "header-search__button").click()
    txt = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/p').text
    assert "Показываем результаты по запросу" in txt

def test_search_by_name_with_dots(driver):
    driver.get(" https://www.chitai-gorod.ru/ ")
    driver.find_element(By.CLASS_NAME, "header-search__input").send_keys("s.n.u.f.f.")
    driver.find_element(By.CLASS_NAME, "header-search__button").click()
    txt = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/p').text
    assert "Показываем результаты по запросу" in txt