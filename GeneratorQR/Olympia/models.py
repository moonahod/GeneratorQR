#from django.db import models
#import qrcode

#class CodeQR(models.Model):

    #def __str__(self):
        #return self.name

    #data = request.POST.get('qrdata')
    #filename = request.POST.get('filename')
    #qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    #qr.add_data(data)
    #qr.make(fit=True)
    #img = qr.make_image(fill_color="black", back_color="white")
    #type(img)
    #img.save('../GeneratorQR/Olympia/codes/' + filename + '.jpg')
