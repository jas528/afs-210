
import random


class Song:
    def __init__(self,title,artist):
        self.title = title
        self.next = None
        self.previous = None
        self.artist = artist
    def getTitle(self):
        return self.title
    def getArtist(self):
        return self.artist
    
    def setTitle(self,title):
        self.title =title
    def setArtist(self,artist):
        self.artist = artist   
    
    def __str__(self):
        return self.title + " by " + self.artist 
    # def __eq__(self, other):
    #     return ((self.title, self.artist) == (other.title, other.artist))
        
    # def __ne__(self, other):
    #     return not (self == other)
    # def __lt__(self, other):
    #     return ((self.title, self.artist) < (other.title, other.artist))
        
    # def __gt__(self, other):
    #     return ((self.title, self.artist) < (other.title, other.artist))
        

class mediaPlayer():
    def __init__(self):
        self.tail = None
        self.head = None
        self.count = 0

    def sizeof(self) -> int:
        return self.count   
    
    def iter(self):
        counting = 0
        listing = self.sizeof()
        playing=self.head
        if listing == 0:
            print ("add a song")
        else:
            while counting  < listing:
                print(counting ,Song.__str__(playing)) 
                playing = playing.next
                counting+=1

    def Add (self, title, artist):
        newsong = Song(title, artist)
        if self.count == 0:
            self.head=newsong
            self.tail=self.head
        else: 
            song1 = self.head 
            self.head = newsong
            song1.previous=self.head 
            newsong.next = song1
            self.head.previous = self.tail
            self.tail.next = self.head
        self.count +=1
        #2.Delete
    def deleteAtIndex(self, index)-> None:
        if (index> (self.count-1)):
            return

        current =self.head
        prev =self.head

        for n in range(index):
            prev= current
            current= current.next

        prev.next = current.next
        current.prev = prev
        self.count -= 1

       
        if (current == self.head):
            self.head = current.next
            current.prev = None
        elif (current == self.tail):
            current.next = None
        else:
            prev.next = current.next
            current.next = prev
        self.count -=1
        return
        prev = current
        current = current.next
    def indexOf(self,data):
        pos =-1

        for node in self.iter():
            pos =+ 1
        if data == node:
            return pos
        return pos


       

        

    def remove (self, index) -> int:
        if (index < 0):
            return 0
        self.playlist.deleteAtindex(index)
        return 1
    #4
    
    def skip(self):
        current =self.head
        forward = self.head.next
        self.tail = current
        self.head =forward
        print(Song.__str__(self.head))

    #5
    def goBack(self):
        back = self.head.previous
        self.tail = back.previous
        self.head = back
        print(Song.__str__(self.head))
    
    def showCurrentSong(self):
        if self.count ==0:
            print("nothing is playing")
        else:
            print(Song.__str__(self.head))
    
    
    def shuffle(self):
        listing = self.sizeof() #how many songs i have
        if listing == 0:#playlist is empty
            print("playlist Empty")
        elif listing == 1:
            print("Cannot Shuffle One Item")
        elif listing == 2:
            self.head, self.tail = self.tail, self.head
        else:
            current = self.head
            counting = 0
            while(counting < listing):
                x = random.randint(0, listing-1)
                swapNode = self.getAtIndex(x)
                temptitle, tempartist = Song.getTitle(swapNode), Song.getArtist(swapNode)
                swapNode.setTitle(Song.getTitle(current))
                swapNode.setArtist(Song.getArtist(current))
                current.setTitle(temptitle)
                current.setArtist(tempartist)
                current = current.next
                counting += 1
       
        print(myMediaPlayer.iter())#how to get the index
    def getAtIndex (self, index):
        if index > self.count-1:
            raise Exception("Index out of Range.")
        current = self.head
        for _ in range(index):
            current = current.next
        return current


       
    def getList(self):
        if self.count==0:
            print("playlist empty")
        else:
            print(Song.__str__(self.head))


myMediaPlayer = mediaPlayer()
myMediaPlayer.Add("Love letter", "Mike")
myMediaPlayer.Add("Dont go", "Mike")
myMediaPlayer.Add("Dont stop the music", "Mike")
myMediaPlayer.Add("keep moving", "Mike")
myMediaPlayer.Add("Crazy in love", "Mike")

def menu():   
    print(20 * "-" , "MENU" , 20 * "-")
    print("1. Add Song to Playlist")
    print("2. Remove song from Playlist")
    print("3. Play")
    print("4. Skip")
    print("5. Go Back")
    print("6. Shuffle")
    print("7. Show Currently Playing Song")
    print("8. Show Current Playlist Order")
    print("0. Exit")
    print(47 * "-")


while True:
    menu()
    choice = int(input())
    if choice == 1:
        newSongTitle = input("enter your song title:")
        newSongArtist = input ("enter the Artist:")
        myMediaPlayer.Add(newSongTitle,newSongArtist)
        print("New Song Playlist")
    elif choice == 2:
        print("YOur play list includes:")
        myMediaPlayer.iter()
        # Add code to prompt user for Song Title and Artist Name
        index = int(input("index:"))
        myMediaPlayer.deleteAtIndex(index)
        print("New Song Added to Playlist")
    elif choice == 2:
        index = int(input("index:"))# Prompt user for Song Title 
        myMediaPlayer.deleteAtIndex(index) # remove song from playlist
        print("Song Removed to Playlist")
    elif choice == 3:
        # Play the playlist from the beginning
        # Display song name that is currently playing
        print("Playing....") 
        myMediaPlayer.getList()     
    elif choice == 4:
        # Skip to the next song on the playlist
        # Display song name that is now playing
        print("Skipping....") 
        myMediaPlayer.skip()                 
    elif choice == 5:
        myMediaPlayer.goBack()
        # Go back to the previous song on the playlist
        # Display song name that is now playing
        print("Replaying....")  
    elif choice == 6:
        print("Shuffling....")          
        myMediaPlayer.shuffle()
        # Randomly shuffle the playlist and play the first song
        # Display song name that is now playing
    elif choice == 7:
        myMediaPlayer.showCurrentSong()
        # Display the song name and artist of the currently playing song
        print("Currently playing: ", end=" ")    
    elif choice == 8:
        print("\nSong list:\n")
        myMediaPlayer.iter() # Show the current song list order
    elif choice == 0:
        print("Goodbye.")
        break
                    