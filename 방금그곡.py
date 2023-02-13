def solution(m, musicinfos):
    answer = ''
    musicDatalist = []
    for i in range(len(musicinfos)):
        musicData = musicinfos[i].split(",")
        starttime = musicData[0].split(":")
        endtime = musicData[1].split(":")
        playtime = (int(endtime[0])*60 + int(endtime[1])) - (int(starttime[0])*60 + int(starttime[1]))
        musicData.append(playtime)
        length = 0
        rawlength = len(musicData[3])
        for j in range(len(musicData[3])):
            if musicData[3][j] != '#':
                length += 1
        temp = 0
        index = 0
        if length > playtime:
            temp = 0
            index = 0
            while True:
                if musicData[3][temp] != '#':
                    temp += 1
                    index += 1
                else:
                    temp += 1
                if index == playtime:
                    if temp+1 < rawlength:
                        if musicData[3][temp] == '#':
                            temp += 1
                    break
            musicData[3] = musicData[3][0:temp]
        elif length < playtime:
            temp = 0
            index = 0
            addcnt = playtime - length
            while True:
                if musicData[3][temp] != '#':
                    musicData[3] = musicData[3] + musicData[3][temp]
                    temp += 1
                    index += 1
                else:
                    musicData[3] = musicData[3] + musicData[3][temp]
                    temp += 1
                if temp == rawlength:
                    temp = 0
                if index == addcnt:
                    break
                
        musicDatalist.append(musicData)
        musicData = []
        
    rightmusiclist = []
    print(musicDatalist)
    
    return answer

solution("ABCDEFG",["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"])
solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"])