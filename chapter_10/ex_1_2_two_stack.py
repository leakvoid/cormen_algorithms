
# implement two stacks in one array A[1..n]

class TwoStack:
    def __init__(self, l_arr, r_arr, max_size):
        self.base_stack = [0] * max_size
        self.top_left = -1
        self.top_right = -1

        for i in range(len(l_arr)):
            self.push_left(l_arr[i])

        for i in range(len(r_arr)):
            self.push_right(r_arr[i])

    def push_left(self, el):
        self.top_left += 1
        if self.top_left + self.top_right + 2 > len(self.base_stack):
            raise Exception("left stack overflow")
        
        self.base_stack[self.top_left] = el

    def push_right(self, el):
        self.top_right += 1
        if self.top_left + self.top_right + 2 > len(self.base_stack):
            raise Exception("right stack overflow")
        
        self.base_stack[len(self.base_stack) - (self.top_right + 1)] = el

    def stack_empty_left(self):
        if self.top_left == -1:
            return True
        else:
            return False

    def stack_empty_right(self):
        if self.top_right == -1:
            return True
        else:
            return False

    def pop_left(self):
        if self.stack_empty_left():
            raise Exception("left stack underflow")
        else:
            self.top_left -= 1
            return self.base_stack[self.top_left + 1]

    def pop_right(self):
        if self.stack_empty_right():
            raise Exception("right stack underflow")
        else:
            self.top_right -= 1
            return self.base_stack[len(self.base_stack) - (self.top_right + 2)]

    def print_left(self):
        print("left stack:", self.base_stack[0:(self.top_left + 1)])

    def print_right(self):
        print("right stack:", self.base_stack[(len(self.base_stack) - (self.top_right + 1)):len(self.base_stack)][::-1])

ts = TwoStack([1, 2, 3, 4], [10, 20, 30, 40], 10)
ts.print_left()
print("pop_left:", ts.pop_left())
print("push_left 7 and 9")
ts.push_left(7)
ts.push_left(9)
ts.print_left()
print("")
ts.print_right()
print("pop_right:", ts.pop_right())
print("push_right 70 and 90")
ts.push_right(70)
ts.push_right(90)
ts.print_right()
print("")
try:
    ts.push_left(5)
except Exception as e:
    print ("exception:", e)
try:
    ts.push_right(50)
except Exception as e:
    print ("exception:", e)
