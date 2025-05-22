import random
import string
from typing import List, Optional


class UsernameGenerator:
    """A class that provides various methods to generate usernames."""

    def __init__(self):
        self.adjectives = [
            "happy", "clever", "brave", "mighty", "cool", "swift", "amazing",
            "brilliant", "dazzling", "eager", "fantastic", "gentle", "honest",
            "incredible", "jolly", "kind", "lively", "mysterious", "noble",
            "optimistic", "powerful", "quirky", "remarkable", "shining", "talented",
            "unique", "vibrant", "witty", "excellent", "zealous"
        ]
        
        self.nouns = [
            "tiger", "eagle", "panda", "wolf", "dragon", "phoenix", "falcon",
            "dolphin", "lion", "shark", "unicorn", "wizard", "ninja", "robot",
            "pilot", "ranger", "warrior", "hunter", "hero", "champion", "knight",
            "coder", "genius", "explorer", "captain", "commander", "master",
            "scholar", "chief", "leader"
        ]
        
        self.themes = {
            "nature": ["mountain", "river", "ocean", "forest", "sky", "star", 
                      "moon", "sun", "earth", "wind", "fire", "water"],
            "tech": ["cyber", "digital", "pixel", "code", "data", "web", "net", 
                    "tech", "binary", "system", "program", "dev", "hack"],
            "fantasy": ["magic", "mystic", "legend", "myth", "elf", "dwarf", 
                       "wizard", "spell", "potion", "scroll", "realm", "quest"],
            "fiction": ["story", "novel", "chapter", "character", "plot", "writer", 
                       "book", "reader", "author", "tale", "narrative", "hero"],
            "movie": ["actor", "director", "scene", "film", "cinema", "screen", 
                     "script", "drama", "action", "comedy", "thriller", "star"]
        }

    def generate_random(self, length: int = 8) -> str:
        """Generate a completely random username of specified length."""
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(length))

    def generate_adjective_noun(self, with_number: bool = True) -> str:
        """Generate a username with format: adjective + noun + (optional) number."""
        adjective = random.choice(self.adjectives)
        noun = random.choice(self.nouns)
        
        if with_number:
            number = random.randint(1, 999)
            return f"{adjective.capitalize()}{noun.capitalize()}{number}"
        else:
            return f"{adjective.capitalize()}{noun.capitalize()}"

    def generate_themed(self, theme: str, with_number: bool = True) -> str:
        """Generate a username based on a specific theme."""
        if theme not in self.themes:
            raise ValueError(f"Theme '{theme}' not found. Available themes: {list(self.themes.keys())}")
        
        word = random.choice(self.themes[theme])
        adjective = random.choice(self.adjectives)
        
        if with_number:
            number = random.randint(1, 999)
            return f"{adjective.capitalize()}{word.capitalize()}{number}"
        else:
            return f"{adjective.capitalize()}{word.capitalize()}"

    def generate_from_name(self, name: str, with_number: bool = True) -> str:
        """Generate a username based on the user's real name."""
        # Remove spaces and convert to lowercase
        name_processed = name.lower().replace(" ", "")
        
        # Add a random adjective
        adjective = random.choice(self.adjectives)
        
        if with_number:
            number = random.randint(1, 999)
            return f"{name_processed}{adjective.capitalize()}{number}"
        else:
            return f"{name_processed}{adjective.capitalize()}"

    def generate_multiple(self, count: int = 5, method: str = "adjective_noun") -> List[str]:
        """Generate multiple username suggestions."""
        usernames = []
        
        for _ in range(count):
            if method == "random":
                usernames.append(self.generate_random())
            elif method == "adjective_noun":
                usernames.append(self.generate_adjective_noun())
            elif method.startswith("theme_"):
                theme = method.split("_")[1]
                if theme in self.themes:
                    usernames.append(self.generate_themed(theme))
                else:
                    raise ValueError(f"Theme '{theme}' not found.")
            else:
                raise ValueError(f"Method '{method}' not recognized.")
                
        return usernames


if __name__ == "__main__":
    # Example usage
    generator = UsernameGenerator()
    
    print("Random username:", generator.generate_random())
    print("Adjective-noun username:", generator.generate_adjective_noun())
    print("Themed username (nature):", generator.generate_themed("nature"))
    print("Name-based username:", generator.generate_from_name("John Doe"))
    
    print("\nMultiple suggestions:")
    for username in generator.generate_multiple(5):
        print(f"- {username}")