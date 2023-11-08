import java.awt.image.BufferedImage
import javax.swing.JFrame
import javax.swing.JPanel
import javax.swing.SwingUtilities
import java.awt.*

class BarnsleyFern : JPanel() {
    var img: BufferedImage

    init {
        val dim = 640
        preferredSize = Dimension(dim, dim)
        background = Color.white
        img = BufferedImage(dim, dim, BufferedImage.TYPE_INT_ARGB)
        createFern(dim, dim)
    }

    private fun createFern(w: Int, h: Int) {
        var x = 0.0
        var y = 0.0

        for (i in 0 until 200_000) {
            var tmpx: Double
            var tmpy: Double
            val r = Math.random()

            if (r <= 0.01) {
                tmpx = 0.0
                tmpy = 0.16 * y
            } else if (r <= 0.08) {
                tmpx = 0.2 * x - 0.26 * y
                tmpy = 0.23 * x + 0.22 * y + 1.6
            } else if (r <= 0.15) {
                tmpx = -0.15 * x + 0.28 * y
                tmpy = 0.26 * x + 0.24 * y + 0.44
            } else {
                tmpx = 0.85 * x + 0.04 * y
                tmpy = -0.04 * x + 0.85 * y + 1.6
            }
            x = tmpx
            y = tmpy

            img.setRGB((w / 2 + (x * w / 11)).toInt(), (h - (y * h / 11)).toInt(), 0xFF32CD32.toInt())
        }
    }

    override fun paintComponent(gg: Graphics) {
        super.paintComponent(gg)
        val g = gg as Graphics2D
        g.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON)
        g.drawImage(img, 0, 0, null)
    }

    companion object {
        @JvmStatic
        fun main(args: Array<String>) {
            SwingUtilities.invokeLater {
                val f = JFrame()
                f.defaultCloseOperation = JFrame.EXIT_ON_CLOSE
                f.title = "Barnsley Fern"
                f.isResizable = false
                f.add(BarnsleyFern(), BorderLayout.CENTER)
                f.pack()
                f.setLocationRelativeTo(null)
                f.isVisible = true
            }
        }
    }
}