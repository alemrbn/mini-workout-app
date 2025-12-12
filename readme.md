# Mini Workout App

A command-line application for creating, editing, viewing, and deleting
structured workout routines. Workouts are stored as JSON files, allowing
persistence without the need for a database. The project follows a
modular architecture that keeps components organized, maintainable, and
easy to extend.

## Features

-   Create structured workouts with:
    -   Name
    -   Training days
    -   Exercises with sets and repetition ranges
    -   Optional descriptions with custom line breaks
-   Edit workouts:
    -   Rename workouts
    -   Rename exercises
    -   Edit sets and repetitions
    -   Edit descriptions
-   Delete workouts with confirmation
-   List and view workouts in a clean formatted output
-   JSON-based persistent storage
-   Modular and scalable design

## Project Structure

    mini-workout-app/
    │
    ├── src/
    │   ├── __init__.py
    │   ├── main.py
    │   ├── menu.py
    │   ├── storage.py
    │   ├── utils.py
    │   │
    │   ├── workout_modules/
    │   │   ├── __init__.py
    │   │   ├── create_workout.py
    │   │   ├── delete_workout.py
    │   │   ├── edit_workout.py
    │   │   ├── list_workout.py
    │   │   ├── workout_action.py
    │
    ├── workouts_data/
    │   └── Example.json
    │
    └── .venv (ignored by Git)

## How It Works

### Entry Point: `main.py`

-   Initializes the storage system.
-   Loads all existing workouts from the `workouts_data` directory.
-   Launches the interactive menu.

### Menu System

The `Menu` class provides a loop with options: 

1. Create workout\
2. Edit workout\
3. Delete workout\
4. List workouts\
5. Exit

Users can type either the number or a command keyword (e.g., "create").

### Storage System

Workouts are saved as individual `.json` files.\
The `Storage` class handles: - Loading workouts - Saving new workouts -
Updating edited workouts - Deleting workouts - Renaming workout files

### Utilities

Utility functions include: - Screen clearing - Input validation - Safe
numeric parsing - Custom line-break formatting via `:break:` token

### Workout Modules

Each action is encapsulated: - `CreateWorkout` handles building a
structured workout. - `EditWorkout` handles renaming, adjusting
reps/sets, editing descriptions. - `DeleteWorkout` ensures safe deletion
with confirmation. - `ListWorkout` prints workouts in a formatted
structure. - `WorkoutAction` provides shared selection logic.

## Workout JSON Structure

Example:

    {
        "name": "Example",
        "days": {
            "monday": {
                "exercises": [
                    {
                        "name": "Bench Press",
                        "series": 3,
                        "reps_min": 8,
                        "reps_max": 12
                    }
                ]
            }
        },
        "description": "Example description with line breaks."
    }

## Installation

1.  Clone the repository:

        git clone https://github.com/alemobn/mini-workout-app.git

2.  Enter the project folder:

        cd mini-workout-app

3.  (Optional) Create a virtual environment:

        python -m venv .venv

4.  Activate it:

    -   Windows:

            .venv\Scripts\activate

    -   Linux/macOS:

            source .venv/bin/activate

No external dependencies are required.

## Usage

Run the app:

    python -m src.main

Follow the on-screen instructions to create or manage workouts.

## License

This project is licensed under the Creative Commons Attribution–NonCommercial 4.0 International License (CC BY-NC 4.0).
