import os
import shutil


def count_lines(file_name: str) -> int:
    with open(f'{file_name}', 'r') as f:
        amount_of_lines: int = len(f.readlines())

    return amount_of_lines


def create_list(file_list: list, folder: str) -> int:
    with open('table.txt', 'w') as f:
        num_line: int = 1
        for i in range(len(file_list)):
            amount_of_lines: int = count_lines(f'./{folder}/{file_list[i]}')
            for _ in range(amount_of_lines):
                f.write(f'{num_line}. ({file_list[i].split(".")[0]})\n')
                num_line += 1

    return num_line - 1


def check_correct(guess: str,
                  num_line: int,
                  folder: str,
                  file_name: str,
                  correct_ans: int,
                  already_ans: list,
                  half_ans_list: list) -> int:
    with open(f'./{folder}/{file_name}') as f:
        lines = f.readlines()
        skill_from = file_name.split(".")[0]
        with open('new_table.txt', 'a+') as new_f:
            for line in lines:
                if guess.strip() == line.strip() and num_line in already_ans:
                    new_f.write(f'{num_line}. {guess}\n')
                elif guess.strip() == line.strip():
                    new_f.write(f'{num_line}. {guess}\n')
                    already_ans.append(num_line)
                    correct_ans += 1
                elif guess.strip() in line.strip():
                    new_f.write(f'{num_line}. {guess} ({skill_from})\n')
                    half_ans_list[num_line - 1] = guess

                elif num_line in already_ans:
                    new_f.write(f'{num_line}. {line}')
                elif half_ans_list[num_line - 1] != '':
                    new_f.write(f'{num_line}. {half_ans_list[num_line - 1]} ({skill_from}) \n')

                else:
                    new_f.write(f'{num_line}. ({skill_from})\n')
                num_line += 1

    return num_line, correct_ans, half_ans_list


def game(file_list: str, folder: str, cases: int) -> None:
    correct_ans: int = 0
    already_ans: int = []
    half_ans_list: list = ['' for _ in range(cases)]
    while (correct_ans != cases):
        num_line: int = 1
        guess: str = str(input()).lower()
        for i in range(len(file_list)):
            num_line, correct_ans, half_ans_list = check_correct(guess,
                                                                 num_line,
                                                                 folder,
                                                                 file_list[i],
                                                                 correct_ans,
                                                                 already_ans,
                                                                 half_ans_list)

        os.remove('table.txt')
        os.replace('new_table.txt', 'table.txt')

        print(f'{correct_ans}/{cases}')

        with open('table.txt', 'r') as table:
            print(table.read())

# def create_


if __name__ == '__main__':
    folder: str = './basic_category'
    file_list: list = os.listdir(f'{folder}')
    cases: int = create_list(file_list, f'{folder}')
    game(file_list, folder, cases)
