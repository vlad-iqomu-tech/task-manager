import qrcode
ask_user = input("Enter text or URL:")
ask_user_file = input("Enter the filename:")
img = qrcode.make(ask_user)
img.save(ask_user_file)

print(f"QR code saved as {ask_user_file}")