from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

if __name__ == "__main__":
    driver = webdriver.Chrome(ChromeDriverManager().install())
