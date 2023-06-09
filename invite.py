from PIL import Image, ImageDraw, ImageFont

# Define the wedding invitation information
bride = "Jane Smith"
groom = "John Doe"
date = "Saturday, June 12th"
time = "6:00 PM"
location = "St. Mary's Church"

# Create the wedding invitation text using string formatting and concatenation
invitation_text = f"You are cordially invited to the wedding of\n{bride} and {groom}\n\n{date} at {time}\n{location}\n\nPlease RSVP by May 1st"

# Set the font and text size
font = ImageFont.truetype("arial.ttf", 32)

# Get the bounding box of the text
bbox = font.getbbox(invitation_text)

# Unpack the bounding box tuple into separate variables
x1, y1, x2, y2 = bbox
text_width = x1
