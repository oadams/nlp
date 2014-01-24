import Test.HUnit

test0 = TestCase (assertString "")
--test1 = TestCase (assertEqual "okies" (1,2) (1 3))

tests = TestList [TestLabel "test0" test0]
