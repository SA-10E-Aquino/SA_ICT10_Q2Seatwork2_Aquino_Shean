from js import document, window
from pyodide.ffi import create_proxy

def calculate_average(grades):
    total = sum(grades)
    return total / len(grades)

def calculateAverage(event=None):
    subjects = [
        "science", "math", "english", "filipino", "socialstudies",
        "valueseducation", "musicarts", "pehealth", "tle", "ict", "ltlop"
    ]

    grades = []
    for subject_id in subjects:
        el = document.getElementById(subject_id)
        if el is None:
            message = "Form fields missing or IDs changed."
            document.getElementById("result").innerHTML = message
            window.alert(message)
            return
        raw_value = el.value
        try:
            grade = float(raw_value)
            if grade < 0 or grade > 100:
                raise ValueError
            grades.append(grade)
        except Exception:
            message = "Please enter valid grades between 0 and 100 for all subjects."
            document.getElementById("result").innerHTML = message
            window.alert(message)
            return

    average = calculate_average(grades)

    if 94 <= average <= 100:
        rating = "Excellent"
    elif 87 <= average < 94:
        rating = "Above Satisfactory"
    elif 80 <= average < 87:
        rating = "Satisfactory"
    elif 75 <= average < 80:
        rating = "Needs Improvement"
    elif 70 <= average < 75:
        rating = "Poor"
    else:
        rating = "Failing. Study harder and smarter."

    first_name_el = document.getElementById("first_name")
    last_name_el = document.getElementById("last_name")
    first_name = first_name_el.value.strip() if first_name_el else ""
    last_name = last_name_el.value.strip() if last_name_el else ""
    student = f"{first_name} {last_name}".strip()
    student_prefix = f"Student: <strong>{student}</strong><br>" if student else ""

    subject_labels = [
        "Science", "Mathematics", "English", "Filipino", "Social Studies",
        "Values Education", "Music & Arts", "PE & Health", "TLE", "ICT",
        "Leadership Training / Law on Persons"
    ]

    summary_lines_html = []
    summary_lines_text = []
    for label, grade in zip(subject_labels, grades):
        summary_lines_html.append(f"{label}: <strong>{grade:.2f}</strong>")
        summary_lines_text.append(f"{label}: {grade:.2f}")

    summary_html = "<br>".join(summary_lines_html)
    summary_text = "\n".join(summary_lines_text)

    result_text = (
        f"{student_prefix}"
        f"{summary_html}<br>"
        f"<strong>General Weighted Average: {average:.2f}</strong><br>"
        f"Rating: <strong>{rating}</strong>"
    )
    document.getElementById("result").innerHTML = result_text

    alert_name = f"Student: {student}\n" if student else ""
    window.alert(f"{alert_name}{summary_text}\n\nGeneral Weighted Average: {average:.2f}\nRating: {rating}")

calculateAverage_proxy = create_proxy(calculateAverage)
window.calculateAverage = calculateAverage_proxy

button = document.querySelector("button.btn-success.btn-lg")
if button:
    button.addEventListener("click", calculateAverage_proxy)