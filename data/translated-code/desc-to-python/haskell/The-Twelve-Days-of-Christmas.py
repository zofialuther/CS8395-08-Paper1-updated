gifts = ["a Partridge in a Pear Tree", "Two Turtle Doves", "Three French Hens", "Four Calling Birds", "Five Golden Rings", "Six Geese a Laying", "Seven Swans a Swimming", "Eight Maids a Milking", "Nine Ladies Dancing", "Ten Lords a Leaping", "Eleven Pipers Piping", "Twelve Drummers Drumming"]

days = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]

verseOfTheDay :: Int -> String
verseOfTheDay day = "On the " ++ days !! (day - 1) ++ " day of Christmas my true love sent to me: " ++ gifts !! (day - 1)

main :: IO ()
main = mapM_ (putStrLn . verseOfTheDay) [1..12]