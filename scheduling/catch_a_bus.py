# You are given a 0-indexed integer array buses of length n, where buses[i]
# represents the departure time of the ith bus. You are also given a 0-indexed
# integer array passengers of length m, where passengers[j] represents the
# arrival time of the jth passenger. All bus departure times are unique. All
# passenger arrival times are unique.

# You are given an integer capacity, which represents the maximum number of
# passengers that can get on each bus.

# When a passenger arrives, they will wait in line for the next available bus.
# You can get on a bus that departs at x minutes if you arrive at y minutes
# where y <= x, and the bus is not full. Passengers with the earliest arrival times get on the bus first.

# More formally when a bus arrives, either:
# - If capacity or fewer passengers are waiting for a bus, they will all get on
# the bus, or
# - The capacity passengers with the earliest arrival times will get on the bus.

# Return the latest time you may arrive at the bus station to catch a bus.
# You cannot arrive at the same time as another passenger.

# Note: The arrays buses and passengers are not necessarily sorted.

class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        # Sort buses and passengers
        buses = sorted(buses)
        passengers = sorted(passengers)

        last_bus = buses[len(buses) - 1]

        # Find the index of the last seated passenger in the array
        seated_count = 0
        bus_full = False
        for bus in buses:
            seats_used = 0
            bus_full = False

            while seated_count <= len(passengers) - 1 and passengers[seated_count] <= bus and seats_used < capacity:
                seated_count += 1
                seats_used += 1

            if seats_used == capacity:
                bus_full = True

        last_seated_idx = seated_count - 1

        # Find the first open seat on the last bus and return it. Start from last bus time and check that it
        # is not within the passengers array

        if bus_full:
            potential_arrival = passengers[last_seated_idx] - 1

            while last_seated_idx > 0 and passengers[last_seated_idx - 1] == potential_arrival:
                potential_arrival -= 1
                last_seated_idx -= 1

            return potential_arrival
        else:
            potential_arrival = buses[len(buses) - 1]

            while last_seated_idx >= 0 and potential_arrival == passengers[last_seated_idx]:
                potential_arrival -= 1
                last_seated_idx -= 1

            return potential_arrival
