import Numeric.LinearAlgebra

main = do
    let a = (3><2) [1,2,3,4,5,6]
    putStrLn "Matrix a:"
    disp a
    putStrLn "Transpose of matrix a:"
    disp $ tr a