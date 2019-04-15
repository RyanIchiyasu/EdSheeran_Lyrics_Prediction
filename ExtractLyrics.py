import os

dirs = os.listdir('./all lyrics fire fox')

for dir in dirs:
    print("song name = " + dir)
    file = open("./all lyrics fire fox/" + dir, "r", encoding="utf-8")

    recordFlag = 0
    lyrics = list()

    for line in file:
        if "<!-- /SONG LYRICS -->" in line:
            print("Found End Position")
            recordFlag = 0

        if recordFlag == 1:
            line = line.replace("<br />","")
            line = line.replace("</div>","")
            line = line.replace("&#039;","'")
            line = line.replace("&quot","")
            line = line.replace("[Chorus]","")
            line = line.replace("[Verse 1]","")
            line = line.replace("[Verse 2]","")
            line = line.replace("[Pre-Chorus]","")
            line = line.replace("[Chorus:]","")
            line = line.replace("[Bridge:]","")
            line = line.replace("[Verse 2:]","")
            line = line.replace("[Verse:]","")
            line = line.replace("(Chorus)","")
            line = line.replace("[Pre-Chorus 2]","")
            line = line.replace("[Guitar Solo]","")
            line = line.replace("[Pre-Chorus 1]","")
            line = line.replace("[Bridge]","")
            line = line.replace("[Outro]","")
            line = line.replace("[Chorus 2]","")
            line = line.replace("[Break]","")
            line = line.replace("[Bridge]","")
            line = line.replace("[Hook]","")
            line = line.replace("[Pre-Hook]","")
            line = line.replace("[Taylor Swift]","")
            line = line.replace("[Ed Sheeran]","")
            line = line.replace("[Both]","")
            line = line.replace("[Intro]","")
            line = line.replace("[Verse 3]","")
            line = line.replace("[Hook x2]","")
            line = line.replace("[Break x12]","")
            line = line.replace("[Pre-Chrous]","")
            line = line.replace("[Verse 1:]","")
            line = line.replace("[Verse 3:]","")
            line = line.replace("[Verse 4:]","")
            line = line.replace("[Hook:]","")
            line = line.replace("[Accapella]","")
            line = line.replace("[Verse]","")
            line = line.replace("[Rap Verse]","")
            line = line.replace("[Skit]","")
            line = line.replace("[X2]","")
            line = line.replace("[x5]","")
            line = line.replace("    ","")
            line = line.replace("[Pre-chorus]","")
            line = line.replace("[Knock knock]","")
            line = line.replace("[Chorus 2x:]","")
            line = line.replace("[Verse 4]","")
            line = line.replace("[x4]","")
            line = line.replace("[?]","")
            line = line.replace("\n","")

            lyrics.append(line)

        if "<!-- SONG LYRICS -->" in line:
            print("Found Start Position")
            recordFlag = 1

    file.close()
    stringLyrics = ''.join(lyrics[1:])

    file = open("./AllLyrics.txt", "a")
    file.write(stringLyrics)
    file.close()
