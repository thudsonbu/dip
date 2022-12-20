class Solution:
    def canVisitAllRooms(self, rooms):
        visited = set()

        self.visitRoom(0, rooms, visited)

        return len(visited) == len(rooms)

    def visitRoom(self, room_index, rooms, visited):
        visited.add(room_index)

        for key in rooms[room_index]:
            if not key in visited:
                self.visitRoom(key, rooms, visited)
