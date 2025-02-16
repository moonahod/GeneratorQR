from django.shortcuts import render, redirect
import qrcode

def lang(request):
    return render(request, 'homepage.html')
    #render(request, 'homepage.html')
    #language = request.POST.get('language')

    #if request.method == 'POST' and language == "EN":
        #return redirect(home_en)
    #elif request.method == 'POST' and language == "BY":
        #return redirect(home_by)


def home_en(request):
    data = request.POST.get('qrdata')
    if not data:
        # for alert later
        no_data = True
        return render(request, 'homepage-en.html')
    else:
        print('eng version code gen')

        data = request.POST.get('qrdata')
        print('data to code: ', data)

        filename = request.POST.get('filename')
        if not filename:
            filename = ("your_qrcode")
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
            img = qr.make_image(fill_color=patternColor, back_color="#f2eddf")
        else:
            img = qr.make_image(fill_color="#000", back_color="#f2eddf")

        type(img)

        name = (filename + fileFormat)
        finalcode = img.save('../GeneratorQR/Olympia/static/codes/' + name)
        path = ('/static/codes/' + name)

        if len(data) > 80:
            huge_code_check = True
        else:
            huge_code_check = False

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
        return render(request, 'homepage-en.html', context)

def home_by(request):
    if request.method == 'POST':
        print('bel version code gen')

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
        else:
            img = qr.make_image(fill_color="#000", back_color="#f2eddf")

        type(img)

        name = (filename + fileFormat)
        finalcode = img.save('../GeneratorQR/Olympia/static/codes/' + name)
        path = ('/static/codes/' + name)

        if len(data) > 80:
            huge_code_check = True
        else:
            huge_code_check = False

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
        return render(request, 'homepage-by.html', context)
    else:
        return render(request, 'homepage-by.html')
