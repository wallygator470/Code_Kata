def lostSheep(friday,saturday,total):
    return total - sum(friday+saturday)

print(lostSheep([1,2],[3,4],15))

#Test.describe("Basic Tests")
#test.assert_equals(lostSheep([1,2],[3,4],15),5)
#test.assert_equals(lostSheep([3,1,2],[4,5],21),6)
#test.assert_equals(lostSheep([5,1,4],[5,4],29),10)