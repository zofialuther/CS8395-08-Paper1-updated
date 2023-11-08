import Control.Monad
import System.Exit

main = do
    let problem = True
    when problem (exitSuccess)
    when (not problem) (exitWith (ExitFailure 1))
    exitSuccess
    exitFailure