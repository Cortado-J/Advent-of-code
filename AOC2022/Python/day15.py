import os
day = int(os.path.basename(__file__)[-5:-3])
filename = f"input{day:02d}.txt"
lines = open(filename).read().splitlines()
sensors = []
beacons = []
bs = []
for line in lines:
    words = line.split(' ')
    x1 = int(words[2][2:-1])
    y1 = int(words[3][2:-1])
    x2 = int(words[8][2:-1])
    y2 = int(words[9][2:])
    sensors.append((x1,y1))
    beapos = (x2,y2)
    beacons.append(beapos)
    if beapos not in bs:
        bs.append(beapos)
# Sensor at x=20, y=1: closest beacon is at x=15, y=3

def dist(x1,x2):
    if x1 > x2:
        return x1-x2
    else:
        return x2-x1

def man(a,b):
    return dist(a[0], b[0]) + dist(a[1], b[1])

# returns beacon and shortest distance
def nearestBeacon(sen,beas):
    shortestdistancesofar = 100000000
    nearestbeacon = None
    for bea in beas:
        dist = man(sen, bea)
        if dist <= shortestdistancesofar:
            shortestdistancesofar = dist
            nearestbeacon = bea
    result = (nearestbeacon, shortestdistancesofar)
    return result

nearest = [nearestBeacon(sen, beacons) for sen in sensors]

# print(beacons)
print(f"{len(beacons)} beacons", bs)
print(f"{len(sensors)} sensors", sensors)
print(f"{len(nearest)} nearest", nearest)

def ok(newbea):
    newbeacons = beacons + [newbea]
    for index, sen in enumerate(sensors):
        result = nearest[index]
        # print(result)
        currentnearest = result[0]
        shortestdistance = result[1]
        distancenewbeacon = man(sen, newbea)
        if distancenewbeacon <= shortestdistance:
            # print(f"Not ok because for sensor {sen} nearestexisting is {}")
            return False
    return True

# return count and last ok place
def countbad(startx,endx,stepx,starty,endy,stepy):
    lastok = None
    count = 0
    for x in range(startx, endx, stepx):
        for y in range(starty, endy, stepy):
            # print(x, count)
            # if x % 100000 == 0:
            #     print(x,count)
            newbea = (x,y)

            if newbea in beacons:
                # Can't put a sensor where there's a beacon!!
                # print(f"Found beacon at {newbea}")
                continue

            okr = ok(newbea)
            if okr:
                print("OK:", newbea)
                lastok = newbea
            if not okr:
                count += 1
            # print(newbea, okr, count)
    return count, lastok

# counta, lastoka = countbad(-1100000,6000000,1,2000000,2000001,1)
# counta, lastoka = countbad(-10,30,1,10,11,1)
# parta = counta
# print(f"Day {day}: Part A = {parta}")

print("===========================")
countb, lastokb = countbad(0,21,1,0,21,1)
partb = lastokb[0]*4000000 + lastokb[1]
print(f"Day {day}: Part B = {partb}")
