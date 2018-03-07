def check_exam(arr1,arr2):
    score = 0
    for i in range(len(arr1)):
        if arr2[i] == "":
            score += 0                        
        elif arr2[i] == arr1[i]:
	            score += 4
        elif arr2[i] != arr1[i]:
	            score -= 1
        print(arr1[i], arr2[i], arr1[i] == arr2[i]) 
    if score < 0:
        return 0 
    else: 
        return score 

check_exam(["a", "a", "b", "c"], ["a", "b", "b", "c"])

# Test.it("Basic tests")
# Test.assert_equals(check_exam(["a", "a", "b", "c"], ["a", "a", "b", "c"]), 16)
# Test.assert_equals(check_exam(["b", "c", "b", "a"], ["",  "a", "a", "c"]), 0)
# Test.assert_equals(check_exam(["a", "a", "c", "b"], ["a", "a", "b",  ""]), 7)
# Test.assert_equals(check_exam(["a", "a", "b", "b"], ["a", "c", "b", "d"]), 6)

