from flask import Flask, request, render_template_string
import cv2

app = Flask(__name__)

def analyze_image(image):
    # Perform color analysis using OpenCV
    # (This part would depend on your specific color analysis algorithm)

    # Perform number plate recognition using OpenCV
    # (This part would depend on your specific number plate recognition algorithm)
    # For demonstration purposes, let's assume we have a function called recognize_number_plate
    number_plate_info = recognize_number_plate(image)

    return {
        'color': 'Red',  # Replace with actual color analysis result
        'number_plate': number_plate_info  # Replace with actual number plate recognition result
    }

def recognize_number_plate(image):
    # Dummy function for demonstration purposes
    return "ABC123"  # Replace with actual number plate recognition result

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        # Check if a file was uploaded
        if 'file' not in request.files:
            error = 'No file part'
        else:
            file = request.files['file']

            # Check if the file is empty
            if file.filename == '':
                error = 'No selected file'

            # Check if the file is an image
            elif file and allowed_file(file.filename):
                # Read the uploaded image
                image = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_COLOR)
                # Analyze the image
                analysis_result = analyze_image(image)
                # Display the result to the user
                return render_template_string('''
                    <!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <title>Car Image Analysis Result</title>
                        <style>
                            body {
                                font-family: Arial, sans-serif;
                                margin: 0;
                                padding: 0;
                                background-color: #f0f0f0;
                            }
                            .container {
                                max-width: 800px;
                                margin: 0 auto;
                                padding: 20px;
                            }
                            h1 {
                                text-align: center;
                            }
                            p {
                                text-align: center;
                            }
                            a {
                                display: block;
                                text-align: center;
                                margin-top: 20px;
                                color: #007bff;
                                text-decoration: none;
                            }
                            a:hover {
                                text-decoration: underline;
                            }
                        </style>
                    </head>
                    <body>
                        <div class="container">
                            <h1>Analysis Result</h1>
                            <p>Color: {{ result.color }}</p>
                            <p>Number Plate: {{ result.number_plate }}</p>
                            <a href="/">Upload Another Image</a>
                        </div>
                    </body>
                    </html>
                ''', result=analysis_result)

    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Car Image Analyzer</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f0f0f0;
                }
                .container {
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                }
                h1 {
                    text-align: center;
                }
                form {
                    text-align: center;
                    margin-top: 20px;
                }
                input[type="file"] {
                    display: none;
                }
                button {
                    padding: 10px 20px;
                    background-color: #007bff;
                    color: #fff;
                    border: none;
                    cursor: pointer;
                }
                button:hover {
                    background-color: #0056b3;
                }
                p {
                    text-align: center;
                    color: red;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Upload an Image of a Car</h1>
                {% if error %}
                <p>{{ error }}</p>
                {% endif %}
                <form method="POST" enctype="multipart/form-data">
                    <input type="file" name="file" accept="image/*">
                    <button type="submit">Analyze</button>
                </form>
            </div>
        </body>
        </html>
    ''', error=error)

# Function to check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg'}

if __name__ == '__main__':
    app.run(debug=True)
