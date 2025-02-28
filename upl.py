from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Konfigurasi folder untuk menyimpan file yang diunggah
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Pastikan folder 'uploads' ada
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    # Cek jika ada file yang diunggah
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    
    # Jika user tidak memilih file, browser akan mengirimkan file kosong
    if file.filename == '':
        return redirect(request.url)
    
    # Simpan file ke folder uploads
    if file:
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return f'File {filename} berhasil diunggah!'

if __name__ == '__main__':
    app.run(debug=True)