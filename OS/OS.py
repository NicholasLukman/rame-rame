#Simple shell

#Import library yang dibutuhkan

import os #!ntuk berintegrasi dengan sistem operasi
import subprocess #!untuk menjalankan/eksekusi perintah system
import shlex #!Untuk memecah cmmand line menjadi argument

#Definisi fungsi untuk eksekusi perintah yang dimasukan ke shell

def execute_command(command):
    try:
        process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #!Popen untuk ambil command, stdout = untuk output , Stderr= untuk error , PIPE = untuk input ke proses yng lain
    
        output,errors = process.communicate #! untuk mengkomunikasikan output / error , kalo error ke stderr , output ke stderr
        
        if output:
            print(output.decode())
        if errors:
            print(errors.decode())
    except FileNotFoundError:
        print(f"Perintah '{command}' tidak ditemukan ")
        
#!Definisi fungsi untuk mengatasi perintah exit pada shell

def handle_exit():
    print("Anda Telah Keluar dari shell...")
    exit()

#!Definisi fungsi untuk menampilkan pesan-pesan
#!Ketika user input command help

def handle_help():
    print("Perintah-perintah yang dapat digunakan dalam shell ini:")
    print("Exit: Untuk keluar dari shell")
    print("Help: untuk panduan perintah yang dapat digunakan")
    print("cd <directory> : Untuk mengganti direktori")
    print("ls: Untuk menampilkan list file ataupun folder dalam direktori saat ini")
    print("<command> <argument>: Untuk eksekusi perintah lainnya")
    print("mkdir : Untuk Membuat folder baru")
    print("cat: Untuk Membuka File, Hanya Read aja")
    
#!Definisi fungsi utama untuk menjalankan program

def main():
    while True:
        command = input("shell> ")
        if command.lower() == "exit":
            handle_exit()
        elif command.lower() == "help":
            handle_help()
        elif command.startswith("cd"):
            try:
                os.chdir(command.split()[1])
            except FileNotFoundError:
                print("Direktori tidak ditemukan.")
        elif command.startswith("ls"):
            print(os.listdir())
        elif command.startswith("mkdir"):   #! Perintah buat folder baru
            try:
                os.mkdir(command.split()[1])
                print("Folder Telah Dibuat!!!!!!!")
            except FileExistsError:
                print("Direktori Sudah Ada")
        elif command.startswith("cat"): #! Untuk Open file, baca doang karena r
            try:
                with open(command.split()[1],"r") as f:
                    print(f.read())
            except FileNotFoundError:
                print("File tidak ditemukan")
        else:
            execute_command(command)
            

if __name__ == "__main__":
    main()