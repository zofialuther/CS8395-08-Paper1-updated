import javax.swing.JFrame
import java.awt.Color
import java.awt.Graphics
import java.util.*
import kotlin.math.pow
import kotlin.math.cos
import kotlin.math.sin
import kotlin.math.PI

class DragonCurve(iter: Int) : JFrame("Dragon Curve") {
    private val turns: List<Int>
    private val startingAngle: Double
    private val side: Double

    init {
        setBounds(100, 100, 800, 600)
        defaultCloseOperation = EXIT_ON_CLOSE
        turns = getSequence(iter)
        startingAngle = -iter * (PI / 4)
        side = 400 / 2.0.pow(iter / 2.0)
    }

    private fun getSequence(iterations: Int): List<Int> {
        val turnSequence: MutableList<Int> = ArrayList()
        for (i in 0 until iterations) {
            val copy: List<Int> = ArrayList(turnSequence)
            copy.reverse()
            turnSequence.add(1)
            for (turn in copy) {
                turnSequence.add(-turn)
            }
        }
        return turnSequence
    }

    override fun paint(g: Graphics) {
        g.color = Color.BLACK
        var angle = startingAngle
        var x1 = 230
        var y1 = 350
        var x2 = x1 + (cos(angle) * side).toInt()
        var y2 = y1 + (sin(angle) * side).toInt()
        g.drawLine(x1, y1, x2, y2)
        x1 = x2
        y1 = y2
        for (turn in turns) {
            angle += turn * (PI / 2)
            x2 = x1 + (cos(angle) * side).toInt()
            y2 = y1 + (sin(angle) * side).toInt()
            g.drawLine(x1, y1, x2, y2)
            x1 = x2
            y1 = y2
        }
    }
}

fun main() {
    DragonCurve(14).isVisible = true
}