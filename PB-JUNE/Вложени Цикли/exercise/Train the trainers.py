members_in_jury = int(input())
presentation_name = input()
total_sum_result = 0
counter_presentation = 0

while presentation_name != 'Finish':
    avg_grade_presentation = 0
    counter_presentation += 1

    for grade in range(1, members_in_jury + 1):
        member_assessment = float(input())
        avg_grade_presentation += member_assessment / members_in_jury

    print(f"{presentation_name} - {avg_grade_presentation:.2f}.")
    total_sum_result += avg_grade_presentation

    presentation_name = input()

total_avg_result = total_sum_result / counter_presentation
print(f"Student's final assessment is {total_avg_result:.2f}.")
