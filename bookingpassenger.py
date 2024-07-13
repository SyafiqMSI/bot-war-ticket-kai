from seleimp import *
from chromedriver import *
from passenger import *

def book_penumpang():
    # # LOGIN
    # username = WebDriverWait(driver, 20).until(
    #     EC.presence_of_element_located((By.NAME, "username"))
    # )
    # username.send_keys(USERNAME)
    
    # password = WebDriverWait(driver, 20).until(
    #     EC.presence_of_element_located((By.NAME, "password"))
    # )
    # password.send_keys(PASSWORD)
    
    # login = WebDriverWait(driver, 20).until(
    #     EC.presence_of_element_located((By.ID, "btn-login"))
    # )
    # login.click()
    # print(f"USER {USERNAME} berhasil login.")
    
    # LOGIN BYPASS
    login = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn-secondary' and @data-dismiss='modal']"))
    )
    login.click()
    
    #------------DATA PEMESAN ------------
    # NAMA
    nama_penumpang1 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "pemesan_nama"))
    )
    nama_penumpang1.send_keys(NAMA_PENUMPANG_1)
    print(f"Nama pemesan {NAMA_PENUMPANG_1} sudah ditambahkan.")
    
    # NOMOR
    nomor_penumpang1 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "pemesan_nohp"))
    )
    nomor_penumpang1.send_keys(NOMOR_PEMESAN)
    print(f"Nomor pemesan {NOMOR_PEMESAN} sudah ditambahkan.")
    
    # ALAMAT
    alamat_penumpang1 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "pemesan_alamat"))
    )
    alamat_penumpang1.send_keys(ALAMAT_PEMESAN)
    print(f"Alamat pemesan {ALAMAT_PEMESAN} sudah ditambahkan.")
    
    # NIK
    nik_penumpang1 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "pemesan_notandapengenal"))
    )
    nik_penumpang1.send_keys(NIK_PENUMPANG_1)
    print(f"NIK pemesan {NIK_PENUMPANG_1} sudah ditambahkan.")
    
    # EMAIL
    nik_penumpang1 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "pemesan_email"),)
    )
    nik_penumpang1.send_keys(EMAIL_PEMESAN)
    print(f"Email pemesan {EMAIL_PEMESAN} sudah ditambahkan."), print("")
    
    
    
    #------------DATA PENUMPANG 1------------
    # SESUAI DATA LOGIN
    # NAMA
    # nama_penumpang1 = WebDriverWait(driver, 20).until(
    #     EC.presence_of_element_located((By.ID, "penumpang_nama1"))
    # )
    # nama_penumpang1.send_keys(NAMA_PENUMPANG_1)
    # print(f"Nama penumpang {NAMA_PENUMPANG_1} sudah ditambahkan.")

    # # NIK
    # nik_penumpang3 = WebDriverWait(driver, 20).until(
    #     EC.presence_of_element_located((By.ID, "penumpang_notandapengenal1"))
    # )
    # nik_penumpang3.send_keys(NIK_PENUMPANG_1)
    # print(f"NIK penumpang {NIK_PENUMPANG_1} sudah ditambahkan."), print("")
    
    # CASE BYPASS
    
    # CHECKBOX
    chekbox1 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "cbCopy"))
    )
    chekbox1.click()

    #------------DATA PENUMPANG 2------------
    # NYONYA
    select_nyonya = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "penumpang_title2"))
    )   
    select = Select(select_nyonya)
    select.select_by_value("MRS.")
    
    # NAMA
    nama_penumpang2 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "penumpang_nama2"))
    )
    nama_penumpang2.send_keys(NAMA_PENUMPANG_2)
    print(f"Nama penumpang {NAMA_PENUMPANG_2} sudah ditambahkan.")

    # NIK
    nik_penumpang2 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "penumpang_notandapengenal2"))
    )
    nik_penumpang2.send_keys(NIK_PENUMPANG_2)
    print(f"NIK penumpang {NIK_PENUMPANG_2} sudah ditambahkan."), print("")
    
    #------------DATA PENUMPANG 3------------
    # NAMA
    nama_penumpang3 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "penumpang_nama3"))
    )
    nama_penumpang3.send_keys(NAMA_PENUMPANG_3)
    print(f"Nama penumpang {NAMA_PENUMPANG_3} sudah ditambahkan.")

    # NIK
    nik_penumpang3 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "penumpang_notandapengenal3"))
    )
    nik_penumpang3.send_keys(NIK_PENUMPANG_3)
    print(f"NIK penumpang {NIK_PENUMPANG_3} sudah ditambahkan."), print("")
    
    #------------DATA PENUMPANG 4------------
    # NYONYA
    select_nyonya = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "penumpang_title4"))
    )   
    select = Select(select_nyonya)
    select.select_by_value("MRS.")
    # NAMA
    nama_penumpang4 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "penumpang_nama4"))
    )
    nama_penumpang4.send_keys(NAMA_PENUMPANG_4)
    print(f"Nama penumpang {NAMA_PENUMPANG_4} sudah ditambahkan.")

    # NIK
    nik_penumpang3 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "penumpang_notandapengenal4"))
    )
    nik_penumpang3.send_keys(NIK_PENUMPANG_4)
    print(f"NIK penumpang {NIK_PENUMPANG_4} sudah ditambahkan."), print("")
    
    #CHECKBOX
    chekbox2 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "setuju"))
    )
    chekbox2.click()
    try:
        #CAPTCHA
        captcha = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "rc-anchor-center-item.rc-anchor-checkbox-label"))
        )
        # captcha.click()
        captcha_input = captcha.find_element(By.XPATH, ".//input")
        captcha_input.click()
    except :
        print("Captcha harus manual")
        print("Menunggu captcha... ")
        print("")
    
    #! PESAN
    # pesan = WebDriverWait(driver, 20).until(
    #     EC.presence_of_element_located((By.ID, "bayar"))
    # )
    # pesan.click()
    # # if pesan.click() == True:
    # #     pesan = WebDriverWait(driver, 500).until(
    # #     EC.presence_of_element_located((By.ID, "bayar"))
    # # )
    
    # # KONFIRMASI
    # confirm = WebDriverWait(driver, 50).until(
    #     EC.presence_of_element_located((By.ID, "mSubmit"))
    # )
    # confirm.click()
    
    