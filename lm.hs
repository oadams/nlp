import qualified Data.Map as Map

increment :: String -> Map.Map String Integer
increment k map
    | Map.member k map = Map.insert k ((Lookup k map) + 1)

train :: String -> Map.Map String Double
train (x:xs)
    | Map.member x (train xs) = Map.insert x (Lookup x ((train xs) + 1)) (train xs)

--train_unigram :: String -> Model

--p :: Model -> String -> Double
