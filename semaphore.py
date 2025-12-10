import threading
import time

examinationroom = threading.Semaphore(1)

def enter_examinationroom(num):
    global examinationroom
    print(fPatient {num} is waiting for his turnn)
    
    examinationroom.acquire()  
    print(fPatient {num} is in the examination roomn)

    time.sleep(2)  

    print(fPatient {num} has left the examination roomn)
    examinationroom.release()  

Patient = []
for i in range(10):
    t = threading.Thread(target=enter_examinationroom, args=(i,))
    Patient.append(t)
    t.start()

for t in Patient:
    t.join()
