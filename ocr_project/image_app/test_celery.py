from pathlib import Path
import easyocr
BASE_DIR = Path(__file__).resolve().parent.parent.parent

image = str(BASE_DIR.absolute()) + "/media/" + "images/invoice_test.jpeg"

reader = easyocr.Reader(['ch_sim','en']) # this needs to run only once to load the model into memory
result = reader.readtext(image)
print(result)