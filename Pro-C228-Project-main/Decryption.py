import wave
song = wave.open("song_embedded.wav", mode='rb')

frame_bytes = bytearray(list(song.readframes(song.getnframes())))


extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
decoded = string.split("###")[0]
-
## it should be [i] not [j] for line 13

#extracted = [frame_bytes[j] & 1 for i in range(len(frame_bytes))]
#string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
#decoded = string.split("###")[0]

-
## no [0] for line 22

#extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
#string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
#decoded = string.split("###")[]

- 
## no .split for string on line 29

#extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
#string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
#decoded = string("###")[0]



print("Sucessfully decoded: "+decoded)
song.close()
