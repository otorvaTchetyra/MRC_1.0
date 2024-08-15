name_of_the_patient = input('ФИО пациента: ')

def get_score(description):
    while True:
        try:
            score = int(input(f"{description} (0-5): "))
            if 0 <= score <= 5:
                return score
            else:
                print("Введите число от 0 до 5.")
        except ValueError:
            print("Пожалуйста, введите корректное число.")

def main():
    print("Оценка мышечной силы (MRC)")
    
    scores = []
    joint_descriptions = [
        "Отведение плеча",
        "Приведение плеча",
        "Сгибание плеча",
        "Сгибание в локтевом суставе",
        "Сгибание запястья",
        "Разгибание запястья",
        "Сгибание пальцев",
        "Разгибание пальцев",
        "Сгибание бедра",
        "Разгибание бедра",
        "Отведение бедра",
        "Приведение бедра",
        "Сгибание в коленном суставе",
        "Разгибание в коленном суставе",
        "Тыльное сгибание стопы",
        "Подошвенное сгибание стопы",
    ]
    
    for description in joint_descriptions:
        score = get_score(description)
        scores.append(score)
    
    total_score = sum(scores)
    average_score = total_score / len(scores)
    
    print(f"\nИтоговая оценка мышечной силы: {total_score}")
    print(f"Средний балл: {average_score:.2f}")
    
    if average_score == 0:
        print("Движение или сокращение мышцы отсутствуют.")
    elif average_score <= 1:
        print("Видимое сокращение мышцы без движения в суставе.")
    elif average_score <= 2:
        print("Движение возможно по всей амплитуде без преодоления силы тяжести")
    elif average_score <= 3:
        print("Движение возможно по всей амплитуде с сопротивлением силы.")
    elif average_score <= 4:
        print("Движение осуществляется при сопротивлении, но сила снижена.")
    else:
        print("Сила в норме")

if __name__ == "__main__":
    main()