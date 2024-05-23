import sys

def count_file_content(filename):
        with open(filename) as fn:
            text = fn.read()
        
        # Count characters, lines, and words
        character_count = len(text)
      
        lines = text.split('\n')
        line_count = len(lines)
        
        words = text.split()
        word_count = len(words)
        
        # Print results
        print(f"File: {filename}")
        print(f"Characters: {character_count}")
        print(f"Lines: {line_count}")
        print(f"Words: {word_count}")
