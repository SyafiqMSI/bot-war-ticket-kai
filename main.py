from seleimp import *
from chromedriver import *
from bookingpassenger import *
from bookingtrain import *
from bookingseat import *
from payment import *
from time import sleep

driver.get("https://booking.kai.id/")
print(driver.title)

#def main_program():
try:
    book_kereta()
    sleep(2)
    book_penumpang()
    sleep(1)
    book_seat()
    sleep(2)
    payment_method()
    
except Exception as e:
    print(f"Error: {e}")
    driver.quit()
    raise e

input("\nPress Enter to close the browser...")
driver.quit()