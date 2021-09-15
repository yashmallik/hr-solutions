At the annual meeting of Board of Directors of Acme Inc. If everyone attending shakes hands exactly one time with every other attendee, how many handshakes are there?


Function Description

Complete the handshakes function in the editor below.

handshakes has the following parameter:

int n: the number of attendees
  
  -----------x----------------------x---------------------------------x-----------------------------------x----------------------x-------------------------------------
  
  def handshake(n):
    # Write your code here
    shakes = 0
    while(n>1):
        n = (n-1)
        shakes += n
    return shakes
