# install library neuralintents
!pip install neuralintents

# import library GenericAssistant dari neuralintents
from neuralintents import GenericAssistant

# ambil data dari file json yang diupload di google drive
assistant = GenericAssistant('kamuskata.json', model_name="test_model")

# proses training
assistant.train_model()
assistant.save_model()

done = False

while not done:
    print("\n")
    message = input("Masukkan Pesan: ")
    if message == "STOP":
        done = True
    else:
        assistant.request(message)