import Data.Time

checkChristmasSunday :: Integer -> Bool
checkChristmasSunday year = 
    let christmas = fromGregorian year 12 25
        dayOfWeek = dayOfWeek christmas
    in dayOfWeek == Sunday

main :: IO ()
main = do
    let christmasSundays = filter checkChristmasSunday [2008..2121]
    mapM_ print christmasSundays