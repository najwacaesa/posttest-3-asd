import os

class Video:
    def _init_(self, title, channel, duration):
        self.title = title
        self.channel = channel
        self.duration = duration
        self.next = None

class Watchlist:
    def _init_(self):
        self.head = None
    
    def add_video(self, title, channel, duration):
        video = Video(title, channel, duration)
        if self.head is None:
            self.head = video
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = video
    
    def remove_video(self, title):
        current = self.head
        previous = None
        while current is not None:
            if current.title == title:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return True
            previous = current
            current = current.next
        return False
    
    def display_watchlist(self):
        current = self.head
        while current is not None:
            print("Title:", current.title)
            print("Channel:", current.channel)
            print("Duration:", current.duration)
            print("-------------------------")
            current = current.next

    def mainmenu(self):
        pilih = "y"
        while (pilih == "y"):
            os.system("cls")
            print("===============================")
            print("|  Menu aplikasi linked list  |")
            print("===============================")
            print("1. Insert data")
            print("2. Delete data")
            print("5. Tampil data")
            print("===============================")
            pilihan=str(input(("Silakan masukan pilihan anda: ")))
            if(pilihan=="1"):
                os.system("cls")
                title    = str(input("Masukan judul yang ingin anda tambahkan  : "))
                channel  = str(input("Masukan channel yang ingin anda tambahkan: "))
                duration = int(input("Masukan durasi yang ingin anda tambahkan : "))
                self.add_video(title, channel, duration)
            elif(pilihan=="2"):
                os.system("cls")
                title    = str(input("Masukan judul yang ingin anda tambahkan: "))
                self.remove_video(title)
                x = input("")
            elif(pilihan=="3"):
                os.system("cls")
                self.display_watchlist()
                x = input("")
            else:
                pilih="n"
 
if __name__ == "__main__":
    l = Watchlist()
    l.mainmenu()

