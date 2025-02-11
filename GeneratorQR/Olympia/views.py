from django.shortcuts import render
import qrcode


def home(request):
    if request.method == 'POST':

        print('Hey, new code coming!')

        data = request.POST.get('qrdata')
        print('data to code: ', data)

        filename = request.POST.get('filename')
        print('filename: ', filename)

        errorCorrection = request.POST.get('EC')
        print('EC level: ', errorCorrection)

        patternColor = request.POST.get('color')
        print('pattern color: ', patternColor)

        bgColor = request.POST.get('bg-color')
        print('background color: ', bgColor)

        fileFormat = request.POST.get('fileFormat')
        print('file format: ', fileFormat)
        if not fileFormat:
            fileFormat = '.jpg'

        #win = fpmi.gui.getWindow('MyWindow')
        #width = win.size.width
        #print('window width: ', width)
        #if width <= 420:
        #    mobile = True
        #else:
        #    mobile = False

        # Error Correction Setting
        if errorCorrection == 'L':
            qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
        elif errorCorrection == 'M':
            qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M)
        elif errorCorrection == 'Q':
            qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_Q)
        elif errorCorrection == 'H':
            qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)

        qr.add_data(data)
        qr.make(fit=True)

        # Color Playground
        img = qr.make_image(fill_color=patternColor, back_color=bgColor)
        if not patternColor:
            img = qr.make_image(fill_color="black", back_color=bgColor)
        elif not bgColor:
            img = qr.make_image(fill_color=patternColor, back_color="white")
        elif not patternColor and bgColor:
            img = qr.make_image(fill_color="#000", back_color="#f2eddf")

        type(img)

        name = (filename + fileFormat)
        finalcode = img.save('../GeneratorQR/Olympia/static/codes/' + name)
        path = ('/static/codes/' + name)

        if len(data) > 80:
            huge_code_check = True
        else:
            huge_code_check = False

        #if windowWidth <= 650:
           # mobileVersion = True

        context = {
            #'code1': img,
            'code1': path,
            'data_check': len(path) > 14,
            'huge_code_check' : huge_code_check,
            #'mobile' : mobile,
            #'last_data': data,
            #'last_filename': filename,
            #'last_fileFormat': fileFormat,
        }
        return render(request, 'homepage.html', context)
    else:
        return render(request, 'homepage.html')
