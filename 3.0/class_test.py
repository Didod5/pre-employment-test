import requests
import psycopg2
import json
from psycopg2 import Error
from config import db_params
import datetime as dt


class Test:
    def __init__(self, x:int, y:int):
        if not isinstance(x, int) or not isinstance(y, int):
            raise ValueError('Аргументы должны быть целыми числами')
        else:
            self.x = x
            self.y = y

    def parsing_questions(self):
        response = requests.get('https://jservice.io/api/random?count=', {"count": self.x})
        data = response.json()       

        try:
            connection = psycopg2.connect(**db_params)
            cursor = connection.cursor()

            query = "SELECT id FROM Questions"
            cursor.execute(query)
            records_id = [el[0] for el in cursor.fetchall()]
            
            for el in data:
                id = el['id']
                if id not in records_id:
                    category = el['category']['title']
                    question = el['question']
                    answer = el['answer']
                    insert_query = """INSERT INTO Questions (ID, Category, Question, Answer) VALUES (%s, %s, %s, %s)"""
                    data_to_insert = (id, category, question, answer)
                    cursor.execute(insert_query, data_to_insert)
                    connection.commit()
                else:
                    print('Запись с таким идентификатором уже существует')
                    continue
        except (Exception, Error) as error:
            print(error)
        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Соединение с PostgreSQL закрыто")

    def count_questions_from_category(self, category:str):
        if not isinstance(category, str):
            print("Аргумент должен быть строкой")
        else:
            try:
                connection = psycopg2.connect(**db_params)
                cursor = connection.cursor()
                
                query = '''SELECT question FROM Questions WHERE category = %s'''
                cursor.execute(query, (category,))
                data = cursor.fetchall()
                result = (len(data))
                print(result)
                return result
                
            except(Exception, Error) as error:
                print(error)
            finally:
                if connection:
                    cursor.close()
                    connection.close()
                    print("Соединение с PostgreSQL закрыто")

    def get_questions(self):
        try:
            connection = psycopg2.connect(**db_params)
            cursor = connection.cursor()

            query = """SELECT row_to_json(Questions.*) FROM Questions;"""

            cursor.execute(query)
            data = cursor.fetchmany(self.y)
            date = dt.date.today()
            with open(f'3.0/{date}.json', 'w') as file:
                data = [rec[0] for rec in data]
                json.dump(data, file, indent=3)        
            return data    
        except (Exception, Error) as error:
            print(error)
        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Соединение с PostgreSQL закрыто")
