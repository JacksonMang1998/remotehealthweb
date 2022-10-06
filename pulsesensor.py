import time
import threading
from MCP3008 import MCP3008

class Pulsesensor:
    def __init__(self, channel = 0, bus = 0, device = 0):
        self.channel = channel
        self.BPM = 0
        self.adc = MCP3008(bus, device)

    def getBPMLoop(self):

        rate = [0] * 10
        sampleCounter = 0
        lastBeatTime = 0
        P = 512
        T = 512
        thresh = 525
        amp = 100
        firstBeat = True
        secondBeat = False

        IBI = 600
        Pulse = False

        lastTime = int(time.time()*1000)

        while not self.thread.stopped:
            Signal = self.adc.read(self.channel)
            currentTime = int(time.time()*1000)

            sampleCounter += currentTime - lastTime
            lastTime = currentTime

            N = sampleCounter - lastBeatTime


            if Signal < thresh and N > (IBI/5.0)*3:     # avoid dichrotic noise by waiting 3/5 of last IBI
                if Signal < T:                          # T is the trough
                    T = Signal                          # keep track of lowest point in pulse wave 

            if Signal > thresh and Signal > P:
                P = Signal


            if N > 250:
                if Signal > thresh and Pulse == False and N > (IBI/5.0)*3:
                    Pulse = True
                    IBI = sampleCounter - lastBeatTime
                    lastBeatTime = sampleCounter

                    if secondBeat:
                       secondBeat = False
                       for i in range(len(rate)):
                        rate[i] = IBI

                    if firstBeat:
                      	 firstBeat = False;
                      	 secondBeat = True;
                      	 continue

                    # keep a running total of the last 10 IBI values
                    rate[:-1] = rate[1:]                # shift data in the rate array
                    rate[-1] = IBI                      # add the latest IBI to the rate array
                    runningTotal = sum(rate)            # add upp oldest IBI values

                    runningTotal /= len(rate)           # average the IBI values 
                    self.BPM = 60000/runningTotal       # how many beats can fit into a minute? that's BPM!

            if Signal < thresh and Pulse == True:       # when the values are going down, the beat is over
               Pulse = False                           # reset the Pulse flag so we can do it again
               amp = P - T                             # get amplitude of the pulse wave
               thresh = amp/2 + T                      # set thresh at 50% of the amplitude
               P = thresh                              # reset these for next time
               T = thresh

            if N > 2500:                                # if 2.5 seconds go by without a beat
                thresh = 512                            # set thresh default
                P = 512                                 # set P default
                T = 512
                lastBeatTime = sampleCounter
                firstBeat = True
                secondBeat = False
                self.BPM = 0

            time.sleep(0.005)

    def startAsyncBPM(self):
        self.thread = threading.Thread(target=self.getBPMLoop)
        self.thread.stopped = False
        self.thread.start()
        return

    def stopAsyncBPM(self):
        self.thread.stopped = True
        self.BPM = 0
        return

