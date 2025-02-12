# Monty Hall Simulation
This project simulates the famous Monty Hall problem, a counter-intuitive probability puzzle based on a game show scenario. In this simulation:

There are three doors: one hides an "Expensive Car" (the prize) and the other two hide goats.
The contestant makes an initial random choice.
Depending on the strategy chosen, the contestant either sticks with their original door or switches to the other unopened door after the host reveals a goat behind one of the remaining doors.
The simulation demonstrates that switching doors increases the chances of winning the car.

## Code Structure
```
-src
|__dashboard.py
|__main.ipynb
|__manty_hall.py
-test
|___test.py
-README.md
-requirements.txt
```
## requirements
- Python 3.7+
- Streamlit (optional)

Use `pip install -r requirements.txt` to necessary packages.

## Usage
You can use the program directly from the This site: https://montyhallsimulation.streamlit.app/

or

add to `src` directory to the `PYTHONPATH` and run the project's Python script with: `python src/manty_hall.py`
For Streamlit dashboard, run: `streamlit run src/dashboard.py`

## licence
There is no problem using this code for other purposes