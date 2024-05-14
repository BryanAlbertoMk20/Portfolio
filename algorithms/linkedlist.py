class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_begining(self, val):
        node = ListNode(val, self.head)
        self.head = node

    def get_length_of_list(self):
        counter = 0
        head = self.head
        while head:
            counter += 1
            head = head.next
        return counter

    def get_value(self, index):
        if index < 0 or index >= self.get_length_of_list():
            raise Exception("Invalid index")

        if index == 0:
            return self.head.data

        counter = 0
        head = self.head
        while head:
            if counter == index - 1:
                return head.val

            head = head.next
            counter += 1

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        current_node = self.head
        llstr = ''
        while current_node:
            llstr += str(current_node.val) + ' --> '
            current_node = current_node.next

        print(llstr)

    # def middleNode(self, head):
    #     answer = []
    #
    #     length = self.get_length_of_list()
    #
    #     half_length = length / 2
    #
    #     head = self.head
    #
    #     while head:

if __name__ == "__main__":

    linkedlist = LinkedList()

    linkedlist.insert_at_begining(4)
    linkedlist.insert_at_begining(3)
    linkedlist.insert_at_begining(2)
    linkedlist.insert_at_begining(1)

    linkedlist.print()