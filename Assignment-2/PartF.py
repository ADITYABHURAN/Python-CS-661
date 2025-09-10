# Given dataset
records = [
    (101, "Aditya", (85, 90, 92), (88, 91)),
    (102, "Aryan",   (78, 82, 80), (79, 84)),
    (103, "Harshu", (92, 95, 94), (96, 97))
]

# List to store processed results
processed_records = []

# Process each student record
for student_id, name, assignment_scores, exam_scores in records:
    avg_assignment = sum(assignment_scores) / len(assignment_scores)
    avg_exam = sum(exam_scores) / len(exam_scores)
    overall_avg = (avg_assignment + avg_exam) / 2

    # Create new tuple
    new_record = (student_id, name, avg_assignment, avg_exam, overall_avg)
    processed_records.append(new_record)

# Find highest overall average
highest_avg = max(record[4] for record in processed_records)
top_students = [record for record in processed_records if record[4] == highest_avg]

# Print results in tabular format
print(f"{'ID':<5}{'Name':<10}{'Avg Assignment':<15}{'Avg Exam':<12}{'Overall Avg':<12}")
print("-" * 60)
for rec in processed_records:
    print(f"{rec[0]:<5}{rec[1]:<10}{rec[2]:<15.2f}{rec[3]:<12.2f}{rec[4]:<12.2f}")

print("\nTop Student(s):")
for rec in top_students:
    print(f"{rec[1]} with Overall Average = {rec[4]:.2f}")
