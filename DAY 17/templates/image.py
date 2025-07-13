from PIL import Image, ImageDraw

for value in ["10", "20", "50", "100", "200", "500", "2000"]:
    img = Image.new("RGB", (300, 150), color="white")
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 299, 149], outline="black", width=3)
    d.text((100, 60), f"₹{value}", fill="black")
    img.save(f"templates/{value}.jpg")
