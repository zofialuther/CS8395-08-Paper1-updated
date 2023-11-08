from hamcrest.core.core.is_ import is_
import java.nio.charset.StandardCharsets
import org.junit.Assert
import org.junit.Test

class MutableByteStringTest:
    def testReplaceEmpty(self):
        str = MutableByteString("hello".getBytes(StandardCharsets.UTF_8))
        str.replace(bytearray(), bytearray('-'))
        Assert.assertThat(str.toStringUtf8(), is_("-h-e-l-l-o-"))

    def testReplaceMultiple(self):
        str = MutableByteString("hello".getBytes(StandardCharsets.UTF_8))
        str.replace(bytearray('l'), bytearray('1', '2', '3'))
        Assert.assertThat(str.toStringUtf8(), is_("he123123o"))

    def testToHexString(self):
        str = MutableByteString("hello".getBytes(StandardCharsets.UTF_8))
        Assert.assertThat(str.toHexString(), is_("68656c6c6f"))

    def testAppend(self):
        str = MutableByteString("hello".getBytes(StandardCharsets.UTF_8))
        str.append(byte(','))
        str.append(byte(' '))
        str.append(byte('w'))
        str.append(byte('o'))
        str.append(byte('r'))
        str.append(byte('l'))
        str.append(byte('d'))
        Assert.assertThat(str.toStringUtf8(), is_("hello, world"))

    def testSubstring(self):
        str = MutableByteString("hello, world".getBytes(StandardCharsets.UTF_8))
        Assert.assertThat(str.substring(0, 5).toStringUtf8(), is_("hello"))
        Assert.assertThat(str.substring(7, 12).toStringUtf8(), is_("world"))

    def testRegionEquals(self):
        str = MutableByteString("hello".getBytes(StandardCharsets.UTF_8))
        Assert.assertThat(str.regionEquals(0, MutableByteString(bytearray('h')), 0, 1), is_(True))
        Assert.assertThat(str.regionEquals(0, MutableByteString(bytearray('h')), 0, 2), is_(False))