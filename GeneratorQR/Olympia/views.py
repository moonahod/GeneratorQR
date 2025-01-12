from django.shortcuts import render
import qrcode


def home(request):
    if request.method == 'POST':
        data = request.POST.get('qrdata')
        print('data to code: ', data)
        filename = request.POST.get('filename')
        print('filename: ', filename)
        qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        type(img)
        fileFormat = request.POST.get('fileFormat')
        name = (filename + fileFormat)
        finalcode = img.save('../GeneratorQR/Olympia/static/codes/' + name)
        path = ('/static/codes/' + name)

        if len(data) > 70:
            huge_code_check = True
        else:
            huge_code_check = False

        context = {
            #'code1': img,
            'code1': path,
            'data_check': len(path) > 14,
            'huge_code_check' : huge_code_check,
            #'last_data': data,
            #'last_filename': filename,
            #'last_fileFormat': fileFormat,
        }
        return render(request, 'homepage.html', context)
    else:
        return render(request, 'homepage.html')
