import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import math
students_df = pd.read_csv('students.csv')
def draw_hexagon(draw, center, size, color):
    angle = math.pi / 3
    points = [(center[0] + size * math.cos(i * angle), center[1] + size * math.sin(i * angle)) for i in range(6)]
    draw.polygon(points, outline=color, fill=color)
def generate_hexagon_pattern(width, height, hex_size):
    pattern_image = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(pattern_image)
    hex_width = math.sqrt(3) * hex_size
    hex_height = 2 * hex_size
    x_offset = hex_width * 0.75
    y_offset = hex_height * 0.5
    for y in range(0, height, int(hex_height * 0.75)):
        for x in range(0, width, int(hex_width)):
            draw_hexagon(draw, (x + hex_width / 2, y + hex_height / 2), hex_size, (240, 240, 240))
    return pattern_image
def generate_certificate(student_name, student_result, student_time, student_date, student_serial):
    width, height = 1200, 800
    hex_size = 40
    pattern_image = generate_hexagon_pattern(width, height, hex_size)
    image = pattern_image.copy()
    draw = ImageDraw.Draw(image)
    font_path = 'arial.ttf'
    font_handwritten = 'handwritten_font.ttf'
    font_title = ImageFont.truetype(font_path, 80)
    font_name = ImageFont.truetype(font_handwritten, 60)
    font_subtitle = ImageFont.truetype(font_path, 50)
    font_text = ImageFont.truetype(font_path, 40)
    font_serial = ImageFont.truetype(font_path, 30)
    title_text = "\nCertificate of Achievement"
    certifies_text = "\nThis certifies that"
    name_text = f"{student_name}"
    completed_text = "successfully completed the"
    course_text = "Learn Python Course"
    on_date_text = f"on {student_date}"
    score_text = f"with a score of {student_result} in {student_time}."
    serial_text = f"Number: {student_serial}"
    title_position = (width // 2 + 100, 50)
    certifies_position = (width // 2, 180)
    name_position = (width // 2, 280)
    completed_position = (width // 2, 360)
    course_position = (width // 2, 440)
    on_date_position = (width // 2, 520)
    score_position = (width // 2, 600)
    instructor_position = (width // 2, 680)
    instructor_name_position = (width // 2, 760)
    serial_position = (50, height - 50)
    rect_height = 100
    rect_position = (0, 0, width, rect_height + 60)
    draw.rectangle(rect_position, fill=(0, 0, 0))
    python_logo = Image.open("python_logo.png")
    python_logo = python_logo.resize((100, 100))
    image.paste(python_logo, (width // 2 - 525, 40), python_logo)
    shadow_offset = 3
    draw.text((title_position[0] + shadow_offset, title_position[1] + shadow_offset), title_text, font=font_title, fill='gray', anchor='mm')
    draw.text(title_position, title_text, font=font_title, fill='white', anchor='mm')
    draw.text(certifies_position, certifies_text, font=font_text, fill='black', anchor='mm')
    draw.text(name_position, name_text, font=font_name, fill='black', anchor='mm')
    draw.text(completed_position, completed_text, font=font_text, fill='black', anchor='mm')
    draw.text(course_position, course_text, font=font_subtitle, fill='black', anchor='mm')
    draw.text(on_date_position, on_date_text, font=font_text, fill='black', anchor='mm')
    draw.text(score_position, score_text, font=font_text, fill='black', anchor='mm')
    draw.text(serial_position, serial_text, font=font_serial, fill='black')
    certificate_path = f"{student_name.replace('/', '_').replace(' ', '_')}_certificate.png"
    image.save(certificate_path)
    return certificate_path
name_column = 'NAME'
result_column = 'Result'
time_column = 'Form Timer'
date_column = 'Timestamp'
serial_column = 'Serial Number'
for _, student in students_df.iterrows():
    name = student[name_column]
    result = student[result_column]
    time = student[time_column]
    date = student[date_column]
    serial = student[serial_column]
    generate_certificate(name, result, time, date, serial)
print("Certificates have been generated and saved.")