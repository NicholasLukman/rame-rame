"""
    Program Simulasi process and thread creation menggunakan python
"""

import os #interaksi dengan sistem operasi
import multiprocessing # untuk create and manage process
import threading #untuk create and manage thread

#buat fungsi untuk create child process
#child process akan menghitung sum/jumlah bilangan
#dari 1 - 10.000

def child_process():
    total = sum(range(1,10001)) #hitung jumlah 1 - 10.000
    
    #ambil PID (PROCESS IDENTIFIER) dari child process dan PID dari parent process
    print(f"Child Process : \nPID = {os.getpid()} \nParent process : PID = {os.getppid()} \nJumlah Bilangan = {total}")
    
    #buat fungsi untuk create Thread
def create_thread(start,end,name):
        partial_sum = sum(range(start,end))
        print(f"Thread {name} : \nJumlah Bilangan dari {start} ke {end-1} = {partial_sum}")
    
    #Buat fungsi utama
def main():
        print(f"Parent Process : PID = {os.getpid()}") #Parent process dicreate oleh OS
        process = multiprocessing.Process(target=child_process)
        process.start() #child proses dimulai
        process.join() #tunggu child process selesai
        
        #membuat thread dan assign task ke thread
        #setiap thread akan menghitung jumlah dengan bagian masing-masing
        
        threads = []
        ranges = [(1,3001),(3001,6001),(6001,10001)]
        
        for i, (start,end) in enumerate(ranges):
            thread = threading.Thread(target=create_thread,args=(start,end,i)) #INI YANG BEKERJA UNTUK MEMBENTUK THREAD DLM PROCESS
            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join() #menunggu thread selesai
        
        print("Process utama selesai.")

if __name__ == "__main__":
    main()
        
    
    