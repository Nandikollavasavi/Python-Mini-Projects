import qrcode
print("===QRcode Generator===")
data=input("Enter Text or URL:")
img=qrcode.make(data)

file_name=input("Enter file name(without .png):")
img.save(file_name+".png")

print("\n✅QRcode Generated Successfully!")
print(f"📁Saved as:{file_name}.png")