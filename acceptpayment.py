import qrcode
#taking upi id as a input 

upi_id=input("Enter your UPI ID = ")

#upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE
#defining payment url based on upi id and payment app
phonepe_url="upi://pay?pa=",{upi_id},"&pn=Recipient%20Name&mc=1234"
paytm_url="upi://pay?pa=",{upi_id},"&pn=Recipient%20Name&mc=1234"
google_pay_url="upi://pay?pa=",{upi_id},"&pn=Recipient%20Name&mc=1234"

#Create QR code for each payment app
phonepe_qr=qrcode.make(phonepe_url)
paytm_qr=qrcode.make(paytm_url)
google_pay_qr=qrcode.make(google_pay_url)

#save images
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

#display qr code (installed pillow library)
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()