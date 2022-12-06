# import pywhatkit as kit

# kit.image_to_ascii_art("/home/hridoy-pgmr/Downloads/WhatsApp Image 2022-10-25 at 7.00.19 PM.jpeg", "ascii.txt")

# import ascii_magic

# output = ascii_magic.from_image_file("/home/hridoy-pgmr/Downloads/pic.jpg", columns=100,char="#")
# ascii_magic.to_file(output,"/home/hridoy-pgmr/Downloads/asci.txt")
import ascii_magic
my_art = ascii_magic.from_image_file(
    '/home/hridoy-pgmr/Downloads/pic.jpg',
    columns=200,
    width_ratio=2,
    mode=ascii_magic.Modes.HTML
)
ascii_magic.to_html_file('ascii_art.html', my_art)