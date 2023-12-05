class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start < destination:
            clockwise = sum(distance[start:destination])
        else:
            clockwise = sum(distance[start:]) + sum(distance[:destination])
        ccw= sum(distance) - clockwise
        return min(clockwise, ccw)