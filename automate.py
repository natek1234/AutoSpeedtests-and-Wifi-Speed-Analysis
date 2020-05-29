#Author: Ketan Vasudeva
#Purpose: Automated speedtest process for graphing and analytics
#Version: 1.1
#Date: May 28th, 2020
#Update Note: Major patch. Graphing functionality fixed, matplotlib now automatically determines tick locations
#             (customizable). The graph now also uses the real time of day (EST).
#             Other customizable features added: customizable runtime. Error handling updated for
#             parsing block. If data cannot be found, previous data point is used as default.
#Known Weaknesses: Occasionally matplotlib or the parsing function will draw a random error due to abnormalities in the
#                  speedtest output. These are handled by skipping over that result.


#Import necessary libraries and modules
import subprocess
import time
import matplotlib.pyplot as plt
import numpy as np
import math

#Initialize arrays
t = []
downloadData = []
uploadData = []
latencyData = []
jitterData = []
t_epoch = 0

#Set your desired time limit here. Default setting runs until manual interrupt in command line.
time_limit = float('inf')

#Run the speedtest for as long as desired.
while(t_epoch < time_limit):
    try:
        #Run and capture the output of the speedtest
        output = subprocess.run(('speedtest.exe'), capture_output=True)

        #Parse the speedtest data
        output = str(output)
        output = output.split()

        #Extract desired components of parsed data, making sure no errors are present.
        #If error is identified, the speed is replaced by the last available reading
        try:
            downloadSpd = output[output.index("Download:") + 1]
        except:
            try: 
                downloadSpd = downloadData[-1]
            except:
                print("Error: Speedtest failed, please try again.")
        try:
            downloadUnit = output[output.index("Download:") + 2]
        except:
            downloadUnit = 'Mbps'
        try:
            uploadSpd = output[output.index("Upload:") + 1]
        except:
            try:
                uploadSpd = uploadData[-1]
            except:
                print("Error: Speedtest failed, please try again.")
        try:
            uploadUnit = output[output.index("Upload:") + 2]
        except:
            uploadUnit = 'Mbps'
        try:
            latency = output[output.index("Latency:") + 1]
        except:
            try:
                latency = latency[-1]
            except:
                print("Error: Speedtest failed, please try again.")
        try:
            latencyUnit = output[output.index("Latency:") + 2]
        except:
            latencyUnit = 'ms'
        try:
            jitter = output[output.index("jitter)\\r\\n\\r") - 2]
            jitter = jitter[1:]
        except:
            try:
                jitter = jitterData[-1]
            except:
                print("Error: Speedtest failed, please try again.")
        try:
            jitterUnit = output[output.index("jitter)\\r\\n\\r") - 1]
        except:
            jitterUnit = 'ms'

        #Output data set to console on ongoing basis
        print("Download Speed: " + downloadSpd + " " + downloadUnit)
        print("Upload Speed: " + uploadSpd + " " + uploadUnit)
        print("Latency: " + latency + " " + latencyUnit)
        print("Jitter: " + jitter + " " + jitterUnit)
        dataUnit = [downloadSpd, uploadSpd, latency, jitter]
        print(dataUnit)

        #Produce timestamp
        ts = time.localtime()
        time_and_date = time.strftime("%x %X", ts)
        real_time = time.strftime("%X", ts)
        print(time_and_date)
        print(real_time)
        t_epoch = time.time()
        print(t_epoch)

        #Update data sets
        t.append(real_time)
        downloadData.append(float(downloadSpd))
        uploadData.append(float(uploadSpd))
        latencyData.append(float(latency))
        jitterData.append(float(jitter))

        #Update plots
        #Download Speed Plot
        figD, main_ax = plt.subplots()
        main_ax.plot(t, downloadData)
        main_ax.set_xlabel('Time (s)')

        #Customizable block to set custom y-axis boundaries. Default setting is set by matplotlib.

        #main_ax.set_ylim(0, 200)
        #main_ax.set_yticks(np.linspace(0,200,40))

        main_ax.set_ylabel('Speed (Mbps)')
        main_ax.set_title('Download Speed')
        figD.savefig('downloadData.png')
        plt.close()

        #Upload Speed Plot
        figD, main_ax = plt.subplots()
        main_ax.plot(t, uploadData)

        #Customizable block to set custom y-axis boundaries. Default setting is set by matplotlib.

        #main_ax.set_ylim(0, 200)
        #main_ax.set_yticks(np.linspace(0,200,40))

        main_ax.set_xlabel('Time (s)')
        main_ax.set_ylabel('Speed (Mbps)')
        main_ax.set_title('Upload Speed')
        figD.savefig('uploadData.png')
        plt.close()


        #Latency Plot
        figD, main_ax = plt.subplots()
        main_ax.plot(t, latencyData)

        #Customizable block to set custom y-axis boundaries. Default setting is set by matplotlib.

        #main_ax.set_ylim(0, 100)
        #main_ax.set_yticks(np.linspace(0,100,20))

        main_ax.set_xlabel('Time (s)')
        main_ax.set_ylabel('Latency (ms)')
        main_ax.set_title('Latency')
        figD.savefig('latencyData.png')
        plt.close()


        #Jitter Plot
        figD, main_ax = plt.subplots()
        main_ax.plot(t, jitterData)

        #Customizable block to set custom y-axis boundaries. Default setting is set by matplotlib.

        #main_ax.set_ylim(0, 100)
        #main_ax.set_yticks(np.linspace(0,100,20))

        main_ax.set_xlabel('Time (s)')
        main_ax.set_ylabel('Jitter (ms)')
        main_ax.set_title('Jitter')
        figD.savefig('jitterData.png')
        plt.close()


        #Waits for one minute between data point collections. This can be changed as desired.
        time.sleep(60)
    except:
        continue



