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
        
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python count.py <filename>")
    else:
        print("Arguments received")
        count_file_content(sys.argv[1])