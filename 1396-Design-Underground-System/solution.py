"""LeetCode Problem 1396 - Design Underground System

An underground railway system is keeping track of customer travel times between
different stations. They are using this data to calculate the average time it takes to
travel from one station to another.

Implement the UndergroundSystem class:

    void checkIn(int id, string stationName, int t)
        * A customer with a card ID equal to id, checks in at the station stationName at
          time t.
        * A customer can only be checked into one place at a time.

    void checkOut(int id, string stationName, int t)
        * A customer with a card ID equal to id, checks out from the station stationName
          at time t.

    double getAverageTime(string startStation, string endStation)
        * Returns the average time it takes to travel from startStation to endStation.
        * The average time is computed from all the previous traveling times from
          startStation to endStation that happened directly, meaning a check in at
          startStation followed by a check out from endStation.
        * The time it takes to travel from startStation to endStation may be different
          from the time it takes to travel from endStation to startStation.
        * There will be at least one customer that has traveled from startStation to
          endStation before getAverageTime is called.

You may assume all calls to the checkIn and checkOut methods are consistent. If a
customer checks in at time t1 then checks out at time t2, then t1 < t2. All events
happen in chronological order.

Constraints
===========
 * 1 <= id, t <= 10^6
 * 1 <= stationName.length, startStation.length, endStation.length <= 10
 * All strings consist of uppercase and lowercase English letters and digits.
 * There will be at most 2 * 10^4 calls in total to checkIn, checkOut, and getAverageTime.
 * Answers within 10^-5 of the actual value will be accepted.

"""

from typing import Text


class UndergroundSystem:
    """Underground System

    Your UndergroundSystem object will be instantiated and called as such:

        obj = UndergroundSystem()
        obj.checkIn(id,stationName,t)
        obj.checkOut(id,stationName,t)
        param_3 = obj.getAverageTime(startStation,endStation)
    """

    def __init__(self) -> None:
        """Underground System Constructor"""
        # Initialize the station travel times dictionary which will track all of the
        # passenger travel times for each station.
        self._stations = {}

        # Initialize the hash_table of passengers which are currently checked in.
        self._passengers = {}

    def checkIn(self, passenger_id: int, station: Text, time: int) -> None:
        """Check Passenger In to the Underground System"""
        # Check whether the station from which the passenger is checking in already
        # exists in the station database. There are no pre-existing stations when the
        # underground system is first initialized, so this is guaranteed to happen if
        # there is at least one passenger checking in.
        if station not in self._stations:
            # Since the station is not already in the stations database, it must be
            # added.
            self._stations[station] = {}

        # Ensure that the passenger is not already checked-in at a different station.
        if passenger_id in self._passengers:
            # Since the passenger is already checked-in, we can't check him in again.
            raise Exception(f"Passenger already checked in. [Passenger ID: {passenger_id:,}]")

        # If the passenger id is not already in the lookup table of passengers who are
        # checked in, go ahead and check in the passenger.
        self._passengers[passenger_id] = (station, time)

    def checkOut(self, passenger_id: int, station: Text, time: int) -> None:
        """Check Passenger Out of the Underground System"""
        # Ensure that the passenger currently trying to check out actually previously
        # checked-in.
        if passenger_id not in self._passengers:
            raise Exception(f"Passenger ID not in system: [{passenger_id:,}]")

        # The passengers lookup table is keyed by the passenger id, and its values are
        # binary tuples containing the starting station where the passenger checked in
        # and the time at which they checked in.
        departure_station, departure_time = self._passengers[passenger_id]

        # Check whether the current station exists as a destination within the stations
        # travel times database.
        if station not in self._stations[departure_station]:
            # If it does not exist, it must be initialized to contain this travel time.
            self._stations[departure_station][station] = [time - departure_time]
        else:
            # If the departure station does exist already, simply add the current time
            # to it.
            self._stations[departure_station][station].append(time - departure_time)

        # Finally, close out the checkout process by removing the current passenger from
        # the passengers table.
        del self._passengers[passenger_id]

    def getAverageTime(self, start_station: Text, end_station: Text) -> float:
        """Get the Average Travel Time of a Passenger From Station A to Station B"""
        # Get the list of travel times between the given starting and ending station in
        # this underground system.
        travel_times = self._stations[start_station][end_station]

        # Return the arithmetic mean of the travel times from the starting station to
        # the ending station.
        return sum(travel_times) / len(travel_times)
