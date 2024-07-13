from seleimp import *
from chromedriver import *
from passenger import *

def book_kereta():
    try:
        # STASIUN_ASAL
        stasiun_asal = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "origination-flexdatalist"))
        )
        stasiun_asal.send_keys(NAMA_STASIUN_ASAL)

        keberangkatan = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, f"//span[text()='{NAMA_STASIUN_ASAL}']"))
        )
        keberangkatan.click()
        print(f"Stasiun Keberangkatan {NAMA_STASIUN_ASAL} berhasil dipilih")
        
        # STASIUN_TUJUAN
        stasiun_tujuan = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "destination-flexdatalist"))
        )
        stasiun_tujuan.send_keys(NAMA_STASIUN_TUJUAN)

        destinasi = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, f"//span[text()='{NAMA_STASIUN_TUJUAN}']"))
        )
        destinasi.click()
        print(f"Stasiun Tujuan {NAMA_STASIUN_TUJUAN} berhasil dipilih.")

        # TANGGAL_KEBERANGKATAN
        tanggal_dropdown = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, "departure_dateh"))
        )
        tanggal_dropdown.click()

        # BULAN_KEBERANGKATAN
        bulan_dropdown = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "ui-datepicker-month"))
        )
        select_bulan = Select(bulan_dropdown)
        select_bulan.select_by_visible_text(BULAN_KEBERANGKATAN)

        # TANGGAL_KEBERANGKATAN
        tanggal = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, f"//a[@class='ui-state-default' and text()='{TANGGAL_KEBERANGKATAN}']"))
        )
        tanggal.click()
        print(f"Tanggal {TANGGAL_KEBERANGKATAN}-{BULAN_KEBERANGKATAN} berhasil diatur.")

        # PENUMPANG
        dewasa = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.NAME, "adult"))
        )
        driver.execute_script("arguments[0].value = arguments[1];", dewasa, PENUMPANG_DEWASA)

        # SUBMIT
        cari = WebDriverWait(driver, 3000).until(
            EC.presence_of_element_located((By.NAME, "submit"))
        )
        cari.click()
        
        # KERETA
        kereta = WebDriverWait(driver, 30).until( 
            EC.presence_of_element_located((By.XPATH, f"//div[contains(@class, 'name') and contains(text(), '{NAMA_KERETA}')]"))
        )
        kereta.click()  
        print("")
    except Exception as e:
        print(f"Error abangku: {e}")
      