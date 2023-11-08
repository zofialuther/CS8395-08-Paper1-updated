import Graphics.HGL
import Graphics.HGL.Draw.Pen
import Graphics.HGL.Draw.Text
import Graphics.HGL.Draw.Font
import Graphics.HGL.Draw.Region
import Graphics.HGL.Draw.Text
import Graphics.HGL.Draw.Text
import Graphics.HGL.Draw.Text

main :: IO ()
main = runGraphics $ do
  w <- openWindow "Pendulum Animation" (800, 600)
  let pendulumLength = 200

  let drawPendulum :: Double -> Graphic
      drawPendulum angle = do
        let x = 400
            y = 300
            x2 = x + pendulumLength * sin angle
            y2 = y + pendulumLength * cos angle
        drawInWindow w $ withColor Blue $ line (x, y) (x2, y2)
        drawInWindow w $ withColor Black $ ellipse (x2-10, y2-10) (x2+10, y2+10)
        return ()

  let animatePendulum :: Double -> IO ()
      animatePendulum t = do
        drawInWindow w $ withColor White $ text (10, 10) ("Time: " ++ show t)
        drawPendulum (pi/4 * sin (2 * pi * t))
        sync w
        delay 33
        animatePendulum (t + 0.0333)

  animatePendulum 0.0