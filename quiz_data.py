import requests

parameters = {
    "amount": 10,
    "type": "multiple"
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
question_data = response.json()["results"]

{
  "response_code": 0,
  "results": [
    {
      "category": "Entertainment: Video Games",
      "type": "multiple",
      "difficulty": "hard",
      "question": "What was the name of the hero in the 80s animated video game &#039;Dragon&#039;s Lair&#039;?",
      "correct_answer": "Dirk the Daring",
      "incorrect_answers": ["Arthur", "Sir Toby Belch", "Guy of Gisbourne"]
    },
    {
      "category": "Entertainment: Video Games",
      "type": "multiple",
      "difficulty": "medium",
      "question": "Which of these game franchises were made by Namco?",
      "correct_answer": "Tekken",
      "incorrect_answers": ["Street Fighter", "Mortal Kombat", "Dragon Quest"]
    }
  ]
}