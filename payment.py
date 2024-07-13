from seleimp import *
from chromedriver import *
from passenger import *

def payment_method():
    try:
        # PEMBAYARAN
        pembayaran = WebDriverWait(driver, 300).until(
            EC.presence_of_element_located((By.ID, "btnPayment"))
        )
        pembayaran.click()
        print("Posisi Penumpang sudah ditetapkan.\n")
        print("Beralih ke menu pembayaran.")
        
        BRI = WebDriverWait(driver, 300).until(
            EC.element_to_be_clickable((By.XPATH, f"//a[@class='accordion-toggle']/img[@alt='{NAMA_BANK}']"))
        )
        BRI.click()
        print(f"Beralih ke {NAMA_BANK}.")
        
        driver.execute_script("arguments[0].scrollIntoView(true);", BRI) 
        
        bayar = WebDriverWait(driver, 300).until(
            #  EC.element_to_be_clickable((By.XPATH, f"//input[@class='btn btn-primary' and @type='submit' and @value='Bayar dengan '{NAMA_BANK}'']"))
             EC.element_to_be_clickable((By.XPATH, f"//input[@class='btn btn-primary' and @type='submit' and @value='Bayar dengan {NAMA_BANK}']"))
        )
        driver.execute_script("arguments[0].scrollIntoView();", bayar)
        bayar.click()
        print("Menuju menu pembayaran.")
        print("Menunggu pembayaran.")
        
    except Exception as e:
        print(f"Error abangku: {e}")
