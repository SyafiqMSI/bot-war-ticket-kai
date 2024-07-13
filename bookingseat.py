from seleimp import *
from chromedriver import *
from passenger import *
from time import sleep

def book_seat():
    try:
        # PESAN
        pilih_kursi = WebDriverWait(driver, 3000).until(
            EC.presence_of_element_located((By.CLASS_NAME, "btn-default"))
        )
        pilih_kursi.click()
        print("Memasuki menu pilih kursi")
        
        # GERBONG
        gerbong_dropdown = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "sel1"))
        )
        gerbong_dropdown.click()
        sleep(1)
        gerbong = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, f"//select[@ID='sel1']/option[text()='{GERBONG_KERETA}']"))
        )
        gerbong.click()
        print(f"Gerbong {GERBONG_KERETA} berhasil dipilih")
        
        # P1
        kursi_penumpang1 = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "col-passenger"))
        )
        data_passenger_value = kursi_penumpang1.get_attribute("data-passenger='1'")
        kursi_penumpang1.click()
        sleep(1)
        
        driver.execute_script("arguments[0].scrollIntoView(true);", kursi_penumpang1) 

        # xpath_expression = "//div[@class='box seat numseat-color' and @data-row='3' and @data-gerbang='C']"
        # posisi_penumpang1 = WebDriverWait(driver, 30).until(
        #     EC.presence_of_element_located((By.XPATH, xpath_expression))
        # )
        # posisi_penumpang1 = WebDriverWait(driver, 30).until(
        #     EC.presence_of_element_located((By.XPATH, "//div[@class='box' and @data-row='3' and @data-gerbang='C']"))
        # )
        # driver.execute_script("arguments[0].click();", posisi_penumpang1)
        # posisi_penumpang1.click()
        # print(f"Penumpag {NAMA_PENUMPANG_1} berhasil menempati kursi {KURSI_PENUMPANG_1}")
        
        # # P2
        # kursi_penumpang2 = WebDriverWait(driver, 30).until(
        #     EC.presence_of_element_located((By.CLASS_NAME, "col-passenger"))
        # )
        # data_passenger_value = kursi_penumpang2.get_attribute("data-passenger='2'")
        # kursi_penumpang2.click()
        # print("pass")
        
        # # P3
        # kursi_penumpang3 = WebDriverWait(driver, 30).until(
        #     EC.presence_of_element_located((By.CLASS_NAME, "col-passenger"))
        # )
        # data_passenger_value = kursi_penumpang3.get_attribute("data-passenger='2'")
        # kursi_penumpang3.click()
        # print("pass")
        
        # # P4
        # kursi_penumpang4 = WebDriverWait(driver, 30).until(
        #     EC.presence_of_element_located((By.CLASS_NAME, "col-passenger"))
        # )
        # data_passenger_value = kursi_penumpang4.get_attribute("data-passenger='2'")
        # kursi_penumpang4.click()
        print("Memilih kuri manual waktu 12 detik.")
        hitung_mundur(12)
    except Exception as e:
        print(f"Error abangku: {e}")
        
def hitung_mundur(sekon):
    while sekon > 0:
        print(sekon, end=' ', flush=True)
        sleep(1)
        sekon -= 1

    print("\nHitung mundur selesai...")
   


