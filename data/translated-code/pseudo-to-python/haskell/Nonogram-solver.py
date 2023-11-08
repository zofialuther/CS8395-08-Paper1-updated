```python
import sys
import Control.Applicative
import Control.Monad
import Control.Monad.CSP
import Data.List
import Text.ParserCombinators.ReadP as P
import Text.Printf

main = do
    file <- parseArgs
    printf "reading problem file from %s\n" file
    ps <- parseProblems file
    forM_ ps $ \p -> do
        print p
        putStrLn ""
        printSolution $ solve p
        putStrLn ""

parseArgs = do
    args <- getArgs
    case args of 
        [file] -> return file
        _ -> ioError $ userError "expected exactly one command line argument, the name of the problem file"

data Problem = Problem { rows :: [[Int]], cols :: [[Int]] }

entryP = do
    n <- fromEnum <$> P.get
    if n < 65 || n > 90
        then P.pfail
        else return $ n - 64

blankP = return ' '
eolP = return '\n'

entriesP = ([] <$ blankP) <|> P.many1 entryP

lineP = P.sepBy1 entriesP blankP <* eolP

problemP = Problem <$> lineP <*> lineP

problemsP = P.sepBy1 problemP (P.many blankP <* eolP) <* P.eof

parseProblems file = do
    s <- readFile file
    case P.readP_to_S problemsP s of
        [(ps, "")] -> return ps
        _          -> ioError $ userError ("error parsing file " ++ file)

solve (Problem p) = oneCSPSolution $ problemCSP p

problemCSP (Problem p) = do
    let rowCount = length $ rows p
    let colCount = length $ cols p
    cells <- replicateM rowCount 
        $ replicateM colCount 
        $ mkDV [False, True]

    forM_ (zip cells $ rows p) $ uncurry rowOrColCSP
    forM_ (zip (transpose cells) $ cols p) $ uncurry rowOrColCSP

    return cells

rowOrColCSP (ws, xs) = do
    if null xs
        then forM_ ws $ \w -> constraint1 (not . snd) w
        else do
            let vs = zip [0..] ws
            let n = length ws
            blocks <- forM xs $ \x -> mkDV [(i, i + x - 1) | i <- [0 .. n - x]]
            f blocks
            forM_ blocks $ \x ->
                forM_ vs $ \(i, y) -> constraint2 (\(x1, x2) b -> i < x1 || i > x2 || b) x y
            forM_ vs $ \(i, y) -> constraint2 (\(y', _) b -> i >= y' || not b) (head blocks) y
            forM_ vs $ \(i, y) -> constraint2 (\(_, y') b -> i <= y' || not b) (last blocks) y
            forM_ (zip blocks $ tail blocks) $ \(x, y) ->
                forM_ vs $ \(i, z) -> constraint3 (\(_, x') (y', _) b -> i <= x' || i >= y' || not b) x y z
  where
    f (u : v : bs) = do
        constraint2 (\(_, u') (v', _) -> v' >= u' + 2)  u v
        f $ v : bs
    f _            = return ()

printSolution bss = do
    forM_ bss $ \bs -> do
        forM_ bs $ \b ->
            putChar $ if b then '#' else '.'
        putChar '\n'

```