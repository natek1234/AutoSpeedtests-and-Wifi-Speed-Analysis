#Author: Ketan Vasudeva
#Purpose: Automated speedtest process for graphing and analystics
#Version: 1.0

#import necessary libraries and modules
import subprocess
import time
import matplotlib.pyplot as plt
import numpy as np

#default plotting values

t = []
downloadData = []
uploadData = []
latencyData = []
jitterData = []

while(True):
    #run and capture the output of the speedtest
    output = subprocess.run(('speedtest.exe'), capture_output=True)
    #print(output)

    #parse the speedtest data
    output = str(output)
    #print(output)
    #print(type(output))
    output = output.split()
    #print(output)

    #extract desired components of parsed data
    downloadSpd = output[output.index("Download:") + 1]
    downloadUnit = output[output.index("Download:") + 2]
    uploadSpd = output[output.index("Upload:") + 1]
    uploadUnit = output[output.index("Upload:") + 2]
    latency = output[output.index("Latency:") + 1]
    latencyUnit = output[output.index("Latency:") + 2]
    jitter = output[output.index("jitter)\\r\\n\\r") - 2]
    jitter = jitter[1:]
    jitterUnit = output[output.index("jitter)\\r\\n\\r") - 1]
    print("Download Speed: " + downloadSpd + " " + downloadUnit)
    print("Upload Speed: " + uploadSpd + " " + uploadUnit)
    print("Latency: " + latency + " " + latencyUnit)
    print("Jitter: " + jitter + " " + jitterUnit)
    dataUnit = [downloadSpd, uploadSpd, latency, jitter]
    print(dataUnit)

    #produce timestamp
    ts = time.localtime()
    print(time.strftime("%x %X", ts))
    t_epoch = time.time()

    #updata data sets
    print(t_epoch)
    print(downloadSpd)
    t.append(t_epoch)
    downloadData.append(downloadSpd)
    uploadData.append(uploadSpd)
    latencyData.append(latency)
    jitterData.append(jitter)

    #update plots

    print(t)
    print(downloadData)

    #Download Speed Plot
    figD, main_ax = plt.subplots()
    main_ax.plot(t, downloadData)
    main_ax.set_xlim(round(min(t)),round(max(t))+1)
    main_ax.set_ylim(0, 200)
    main_ax.set_xlabel('Time (s)')
    main_ax.set_yticks(np.linspace(0,200,40))
    locs, labels = plt.yticks()
    print(locs)
    print(labels)
    main_ax.set_ylabel('Speed (Mbps)')
    main_ax.set_title('Download Speed')
    figD.savefig('downloadData.png')
    plt.close()

    #Upload Speed Plot
    figD, main_ax = plt.subplots()
    main_ax.plot(t, uploadData)
    main_ax.set_xlim(round(min(t)),round(max(t))+1)
    main_ax.set_ylim(0, 200)
    main_ax.set_yticks(np.linspace(0,200,40))
    main_ax.set_xlabel('Time (s)')
    main_ax.set_ylabel('Speed (Mbps)')
    main_ax.set_title('Upload Speed')
    figD.savefig('uploadData.png')
    plt.close()


    #Latency Plot
    figD, main_ax = plt.subplots()
    main_ax.plot(t, latencyData)
    main_ax.set_xlim(round(min(t)),round(max(t))+1)
    main_ax.set_ylim(0, 100)
    main_ax.set_yticks(np.linspace(0,100,20))
    main_ax.set_xlabel('Time (s)')
    main_ax.set_ylabel('Latency (ms)')
    main_ax.set_title('Latency')
    figD.savefig('latencyData.png')
    plt.close()


    #Jitter Plot
    figD, main_ax = plt.subplots()
    main_ax.plot(t, jitterData)
    main_ax.set_xlim(round(min(t)),round(max(t))+1)
    main_ax.set_ylim(0, 100)
    main_ax.set_yticks(np.linspace(0,100,20))
    main_ax.set_xlabel('Time (s)')
    main_ax.set_ylabel('Jitter (ms)')
    main_ax.set_title('Jitter')
    figD.savefig('jitterData.png')
    plt.close()


    #waits for one minute between data point collections
    time.sleep(60)



