#!/usr/bin/env python3
import argparse
import sys
from username_generator import UsernameGenerator


def main():
    parser = argparse.ArgumentParser(
        description="Generate creative usernames for various purposes"
    )
    
    # Add arguments
    parser.add_argument(
        "-m", "--method",
        choices=["random", "adjective_noun", "themed", "name_based", "multiple"],
        default="adjective_noun",
        help="Method to generate username (default: adjective_noun)"
    )
    
    parser.add_argument(
        "-l", "--length",
        type=int,
        default=8,
        help="Length of random username (for random method only, default: 8)"
    )
    
    parser.add_argument(
        "-t", "--theme",
        choices=["nature", "tech", "fantasy", "fiction", "movie"],
        default="nature",
        help="Theme for themed username generation (default: nature)"
    )
    
    parser.add_argument(
        "-n", "--name",
        type=str,
        help="Your name for name-based username generation"
    )
    
    parser.add_argument(
        "-c", "--count",
        type=int,
        default=5,
        help="Number of usernames to generate with multiple method (default: 5)"
    )
    
    parser.add_argument(
        "--no-number",
        action="store_true",
        help="Don't append a random number to the username"
    )
    
    args = parser.parse_args()
    
    # Create the generator
    generator = UsernameGenerator()
    
    # Generate username based on the selected method
    try:
        if args.method == "random":
            username = generator.generate_random(args.length)
            print(f"Random username: {username}")
            
        elif args.method == "adjective_noun":
            username = generator.generate_adjective_noun(not args.no_number)
            print(f"Adjective-noun username: {username}")
            
        elif args.method == "themed":
            username = generator.generate_themed(args.theme, not args.no_number)
            print(f"Themed username ({args.theme}): {username}")
            
        elif args.method == "name_based":
            if not args.name:
                print("Error: --name is required for name-based username generation.")
                sys.exit(1)
            username = generator.generate_from_name(args.name, not args.no_number)
            print(f"Name-based username: {username}")
            
        elif args.method == "multiple":
            method_to_use = "adjective_noun"
            if args.theme:
                method_to_use = f"theme_{args.theme}"
                
            usernames = generator.generate_multiple(args.count, method_to_use)
            print(f"Generated {len(usernames)} username suggestions:")
            for idx, username in enumerate(usernames, 1):
                print(f"{idx}. {username}")
    
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()