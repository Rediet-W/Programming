class UndergroundSystem:

    def __init__(self):
        self.checkIns = {} # id-> (startstation,time)
        self.totalmap={} # (start, end) -> [totaltime, count]

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkIns[id] = (stationName, t)

    def checkOut(self, id: int, Endstation: str, t: int) -> None:
        start, time = self.checkIns[id]
        route = (start, Endstation)
        if route not in self.totalmap:
            self.totalmap[route] = [0,0]
        self.totalmap[route][0] += t - time
        self.totalmap[route][1] +=1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.totalmap[(startStation, endStation)]
        return total/count
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)