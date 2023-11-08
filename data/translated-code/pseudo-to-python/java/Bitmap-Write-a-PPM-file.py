def bitmapToPPM(file, bitmap):
    file.delete()

    try:
        os = open(file, 'wb')
        bw = BufferedOutputStream(os)

        header = "P6\n{} {}\n255\n".format(bitmap.getWidth(), bitmap.getHeight())

        bw.write(header.encode('US-ASCII'))

        for y in range(bitmap.getHeight()):
            for x in range(bitmap.getWidth()):
                pixel = bitmap.getPixel(x, y)
                bw.write(pixel.getRed())
                bw.write(pixel.getGreen())
                bw.write(pixel.getBlue())

    except IOError:
        print("An error occurred while writing the PPM file.")

    finally:
        bw.close()
        os.close()