import multiprocessing
# import subprocess

# for enabling multithreading
# def startBujji():
#     print("Process 1 is running")
#     from main import start
#     start()
#     # for process 1 to run Bujji
def startBujji():
        # Code for process 1
        print("Process 1 is running.")
        from main import start
        start()

# def listenHotWord():
#     print("Process 2 is running")
#     from engine.features import hotword
#     hotword()
#     # for process 2 to run hot word
    
def listenHotword():
        # Code for process 2
        print("Process 2 is running.")
        from engine.features import hotword
        hotword()

#start both process
# if __name__ == "__main__":
#     p1 = multiprocessing.Process(target=startBujji)
#     p2 = multiprocessing.Process(target=listenHotWord)
#     p1.start()
#     p2.start()
#     p1.join()
#     if p2.is_alive():
#         p2.terminate()
#         p2.join()
#     print("system stop")
    
if __name__ == '__main__':
        p1 = multiprocessing.Process(target=startBujji)
        p2 = multiprocessing.Process(target=listenHotword)
        p1.start()
        # subprocess.call([r'device.bat'])
        p2.start()
        p1.join()

        if p2.is_alive():
            p2.terminate()
            p2.join()

        print("system stop")