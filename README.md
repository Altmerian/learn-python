# Python Learning Project

This repository contains examples and exercises covering fundamental Python programming concepts.

## Project Structure

```
learn-python/
├── classes/           # Object-oriented programming examples
├── cond_statements/   # Conditional statements examples
├── date_time/         # Date and time manipulation examples
├── dictionaries/      # Dictionary data structure examples
├── exceptions/        # Exception handling examples
├── expressions/       # Python expressions examples
├── functions/         # Function definitions and examples
├── lists/             # List data structure examples
├── loops/             # Loop control structures
├── multithreading/    # Concurrency and parallel execution examples
├── pickle/            # Serialization with pickle
├── sets/              # Set data structure examples
├── strings/           # String manipulation examples
├── tests/             # Test frameworks and test examples
└── zip/               # File compression and decompression
```

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
3. Activate the virtual environment:
   - Windows (PowerShell):
     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```
   - Windows (CMD):
     ```cmd
     .\.venv\Scripts\activate.bat
     ```
   - Unix/MacOS:
     ```bash
     source .venv/bin/activate
     ```

## Topics Covered

- Basic Python Operations
- String Manipulation
- Lists and List Operations
- Loops (for, while)
- Conditional Statements (if, elif, else)
- Functions and Closures
- Dictionaries and Sets
- Object-Oriented Programming
  - Classes and Objects
  - Inheritance
  - Polymorphism
  - Abstraction
- Date and Time Operations
- Concurrent Programming with Threads
- File Operations
  - Pickle Serialization
  - ZIP Compression/Decompression
- Exception Handling
- Testing

## Requirements

- Python 3.x
- No external dependencies required (using only Python standard library)

## Usage

Each directory contains specific examples and exercises. You can run any Python file directly:

```bash
python filename.py
```

For example, to run the serialization example:
```bash
python pickle/Serialization.py
```

Or to run a date operation example:
```bash
python date_time/string_date.py
``` 