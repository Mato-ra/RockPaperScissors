import os
from socket import *

player=""
yourIp=""
targetIp=""
listeningPort=13000
sendingPort=13001

def UDPListen():
    
    host = ""
    port = listeningPort
    buf = 1024
    addr = (host, port)
    UDPSock = socket(AF_INET, SOCK_DGRAM)
    UDPSock.bind(addr)
    
    message = ""
    
    while True:
        (data, addr) = UDPSock.recvfrom(buf)
        if addr[0] == targetIp:
            break
    UDPSock.close()
    return data.decode("utf-8")

def UDPSend(message):
    host = targetIp
    port = listeningPort
    addr = (host, port)
    UDPSock = socket(AF_INET, SOCK_DGRAM)
    data = message.encode("utf-8")
    UDPSock.sendto(data, addr)
    UDPSock.close()

def SendParallelMessage(message):
    UDPSend(message)
    response = UDPListen()
    UDPSend(message)    
    return response

def PlayRockPaperScissors():
    
    while True:
        SendParallelMessage("hello")
        yourPlay = GetPlay()
        opponentPlay=SendParallelMessage(yourPlay)
        EvaluatePlay(yourPlay, opponentPlay)    
        
        if AskIfAnotherRound() == False:
            return
    
def EvaluatePlay(yourPlay, opponentPlay):
    if (yourPlay == opponentPlay):
        print ("tie")
    elif (yourPlay == "0"):
        if (opponentPlay == "1"):
            print("You lose! Paper covers rock")
        else:
            print("You win! Rock smashes scissors")
    elif (yourPlay == "1"):
        if (opponentPlay == "0"):
            print("You win! Paper covers rock")
        else:
            print("You lose! Scissors cut paper")
    elif (yourPlay == "2"):
        if (opponentPlay == "0"):
            print("You lose! Rock smashes scissors")
        else:
            print("You win! Scissors cut paper")

        
def GetPlay():
    while True:
        play = input("Play 0:Rock 1:Paper or 2:Scissor")
        if (play == "0" or play == "1" or play == "2"):
            return play

def AskIfAnotherRound():
    message = input("Do you want to play again? y/n:")
    response = SendParallelMessage(message)
    if (message == "n" or response == "n"):
        print("game end.")
        return False
    else:
        return True



while True:
    #yourIp=input("Please enter your own IP address:")
    targetIp=input("Please enter the IP address of your opponent:")
    PlayRockPaperScissors()


