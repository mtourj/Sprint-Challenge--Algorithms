class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def take_item(self):
        self.set_light_on()
        self.swap_item()

    def drop_item(self):
        self.set_light_off()
        self.swap_item()

    def sort(self):
        """
        Sort the robot's list.
        """
        # Fill this out

        # This robot will implement a bubble sort
        # The 1 bit of memory will be used to track whether we are holding at item
        '''
        Behavior
        Light if we have a number in hand.
        If number is in hand, can't break loop,
        so light ON at end of list means keep looping.
        If we have no number in hand, then we have not
        felt the need to swap anything, so in that case
        end the loop. (Depends on result of compare)
        If you have something in hand and you find a number
        bigger, you swap. If you are at the end of the list
        and you have something in hand, then you are trying
        to replace

        So if light is on:
        Only swap if compare is None or compare is -1

        and if light is off:
        Swap

        and if cannot move right
        Only swap if light is off and compare is None
        If light is on and compare is none, swap
        and end sort


        LIGHT IS ON

        [N, 4, 3]
         5                                                                     
        '''

        # Start with item in hand
        self.set_light_on()
        self.swap_item()

        # If item is in hand, keep looping
        while self.light_is_on():
            # Until we reach end of list...
            while self.can_move_right():

                if self.light_is_on():
                    if  self.compare_item() == None:
                        # If item is in hand, and there is not
                        # an item at this part of the list,
                        # drop the item
                        self.drop_item()
                    elif self.compare_item() == -1:
                        # If item is in hand, and item at this
                        # part of list is larger, swap.
                        self.swap_item()
                else:
                    # If no item in hand, take one.
                    self.take_item()

                self.move_right()
            
            # If we have no item at the end of the list, we
            # take on
            if not self.light_is_on():
                self.take_item()
            # If we have an item and there is no item at end of
            # the list, then we place it there, and this
            # would be the last number we sort, which means the
            # largest number made it to the end of the list
            # The list has been sorted!
            elif self.compare_item() == None and self.light_is_on():
                self.drop_item()
                break
            # If we have an item and the item at the end of list is
            # larger, we swap
            elif self.light_is_on() and self.compare_item() == -1:
                self.swap_item()
            
            # Move all the way back to the left
            while self.can_move_left():
                self.move_left()


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()

    print(robot._item)
    print(robot._list)