from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=opts
)

# Ejemplo de uso del driver
driver.get("https://telecom.yul1.qualtrics.com/login")
sleep(5)  # Espera para ver la página cargada

username_field = driver.find_element(By.ID, "UserName")
password_field = driver.find_element(By.ID, "UserPassword")


# Ingresar las credenciales
username_field.send_keys("******")
password_field.send_keys("****")

# Encontrar y hacer clic en el botón de inicio de sesión
login_button = driver.find_element(By.ID, "loginButton")
login_button.click()

# Pausar para permitir que la página de inicio se cargue
sleep(5)

# # Cierra el navegador
# driver.quit()


