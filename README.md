# Random-Quiz

The program aims to create 35 random quizzes from 50 US states and their capitals.

The program uses random module

Purpose: The purpose is to create 35 random quiz of 50 state-capital questions to avoid cheating.

Algorithm:

1. Us capitals are stored as keys and their capitals are stored as values in answer_key dictionary.
2. answer_key dictionary is shuffled 35 times to create and store 35 random quiz and their answer keys.
3. Each question paper has header that has Name,Date,Period and a heading i.e State Capitals Quiz (Form No.).
4. Each question has 4 options in which 3 are incorrect and 1 option is correct.
5. 3 Wrong options are randomnly selected and writen to question paper along with correct option in random order.
6. For each unique question paper a unique answer key is created.
