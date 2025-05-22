# Username Generator

A versatile Python tool for generating creative and unique usernames.

## Features

- Multiple generation methods:
  - Random string generation
  - Adjective + noun combinations
  - Themed usernames (nature, tech, fantasy)
  - Name-based usernames
  - Bulk generation of multiple suggestions

- Command-line interface for easy use
- Web interface built with Flask
- Can be imported as a module in other Python projects

## Installation

Clone this repository:

```
git clone https://github.com/yourusername/username-generator.git
cd username-generator
```

Install dependencies (required for the web interface):

```
pip install -r requirements.txt
```

## Usage

### Command Line

```
python generate_username.py [options]
```

Options:
- `-m, --method`: Generation method (random, adjective_noun, themed, name_based, multiple)
- `-l, --length`: Length of random username (for random method)
- `-t, --theme`: Theme for themed generation (nature, tech, fantasy, fiction, movie)
- `-n, --name`: Your name for name-based generation
- `-c, --count`: Number of suggestions to generate with multiple method
- `--no-number`: Don't append a random number to the username

### Examples

Generate a username with adjective + noun (default method):
```
python generate_username.py
```

Generate a random username of length 10:
```
python generate_username.py -m random -l 10
```

Generate a tech-themed username:
```
python generate_username.py -m themed -t tech
```

Generate a fiction-themed username:
```
python generate_username.py -m themed -t fiction
```

Generate a movie-themed username:
```
python generate_username.py -m themed -t movie
```

Generate a username based on your name:
```
python generate_username.py -m name_based -n "John Doe"
```

Generate 10 username suggestions:
```
python generate_username.py -m multiple -c 10
```

### Web Interface

Start the web server:

```
cd web
python app.py
```

Open your browser and navigate to http://127.0.0.1:5000/

The web interface provides a user-friendly way to generate usernames with all the available methods.

### As a Module

```python
from username_generator import UsernameGenerator

# Create a generator
generator = UsernameGenerator()

# Generate usernames using different methods
random_username = generator.generate_random(length=8)
adjective_noun = generator.generate_adjective_noun()
themed = generator.generate_themed("tech")
name_based = generator.generate_from_name("John Doe")
multiple = generator.generate_multiple(count=5)

print(random_username)
print(adjective_noun)
print(themed)
print(name_based)
print(multiple)
```

## Customization

You can modify the word lists in the `username_generator.py` file to add more adjectives, nouns, or themed words.

## License

MIT