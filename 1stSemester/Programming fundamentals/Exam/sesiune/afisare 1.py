class A():
    def f(self,a):
        a+=1
    def h(self,l1,l2):
        a = l1[0]
        self.f(a)
        l1[0] = a
        l2 += l1

a = A()
l1 = [1]
l2 = []
a.h(l1, l2)
print(l1, l2)
