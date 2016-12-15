import threading

class arn_messenger(threading.Thread):
    def run(self):
        for _ in  range(10):
            print(threading.current_thread().getName())


x=arn_messenger(name="send out messages")
y=arn_messenger(name="receive messages")

x.start()
y.start()