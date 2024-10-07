
def sjf(soal): 
    #Array ganttchart digunakan untuk membuat ganttchart
    ganttchart = [] 
    burst_times = {} #

    for i in soal:
        burst_times[i[2]] = i[0] 

    completion = {}
    # variabel ini menandakan detik yang sedang berjalan
    seconds = 0 

    # Selama masih ada process yang belum selesai akan terus melakukan looping sampai semua proses telah selesai
    while soal != []: 
        # Available digunakan untuk menyimpan proses yang telah berjalan sebelumnya , proses yang diganggu sebelumnya 
        # akan disimpan dalam array available
        available = [] 

        #Perulangan ini digunakan untuk menyimpan proses yg sedang berjalan ke dalam array variable
        for i in soal : 
            if i[1] <= seconds : 
                available.append(i)
                # print(seconds)
                # print(available)

        # Ini digunakan jika semua proses telah selesai dijalankan
        if available == []: 
            continue
        else:
            # print("------------------------------")
            # print(available)

            # Fungsi disini digunakan untuk mencari burst time paling kecil
            available.sort() 

            # print("-----------Hasil Sort-----------")
            # print(available)

            # variable process disini akan mengambil process yg mempunyai 
            # burst time yang paling kecil hasil dari, available.sort()
            process = available[0] 
            # print(process)
            # print()

            copy_process = available.pop(0)
            # print(copy_process)
            # print()

            #Waktu harus terus berjalan seiring berjalannya proses
            seconds += 1 

            # Fungsi ini yang digunakan untuk membuat ganchart, yang diappend adalah "p ke-n"
            ganttchart.append(process[2]) 
            # Mengurangi burst time dari process yang sedang berjalan saat ini
            process[0] -= 1   
           # print(soal)

           # Function disini digunakan untuk meremove process yang sedang berjalan
            # karena akan di sortir setiap detiknya, apakah ada burst time yang lebih kecil
            # dari burst time sekarang
            soal.remove(copy_process)  
            # print(soal)

            #Jika Process yang sekarang burst time == 0 
            if process[0] == 0: 
                #Variabel ini akan digunakan untuk menyimpan "Process ke-n"
                pro_name = process[2] 
                # print(burst_times)

                # Variabel ini digunakan untuk mengambil burst time 
                burst_time = burst_times[pro_name] 
                # print(burst_time)
                # print(burst_times)

                # completion_time ini menunjukan detik ke berapa process nya selesai
                completion_time = seconds 
                # print(completion_time)
                
                # digunakan untuk mencari berapa lama waktu proses itu selesai, dari datang, 
                # dan detik dia dieksekusi
                turnaround_time = completion_time - process[1] 
                # print(turnaround_time) 

                # digunakan untuk mencari waiting time si process 
                waiting_time = turnaround_time - burst_time 

                #Ini adalah Detail process nya dari urutan yang selesai pertama sampai akhir
                completion[pro_name] = [completion_time,turnaround_time,waiting_time] 
                
                continue
            else:
                soal.append(process) #Dibalikan kedalam soal hasil dari proses yang berjalan , 1 detik, -1 burst time , proses yg skrg
                # print(soal)


    print("Urutan Gannchart :\n",ganttchart) #Untuk Urutan ganchart
    print() 
    print("Detail Proses ^_^") #Detail Proses
    print("Urutan isi proses : [completion time, turnaroundtime, waiting time]")
    print()
    print(completion)

    #Hitung Average Waiting time
    avg = 0
    completion_total = len(completion) 
    for i in completion:
        avg += completion[i][2]
    avgwaitingtime = avg // completion_total
    print()
    print("Average Waiting Time : ",avgwaitingtime)



# Soal = [burst time,arrival time, process]

if __name__ == "__main__" :
    soal = [[7,0,"p1"],
        [4,2,"p2"],
        [1,4,"p3"],
        [4,5,"p4"]]
    sjf(soal)