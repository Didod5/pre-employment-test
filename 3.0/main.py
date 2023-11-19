from class_test import Test


if __name__ == '__main__':
    test = Test(100, 50)
    test.parsing_questions()
    test.count_questions_from_category('alternative rock')
    test.get_questions()