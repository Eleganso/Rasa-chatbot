#!/usr/bin/env python3
"""
Fix NLU YAML formatting issues
"""

import yaml
import re

def fix_nlu_file():
    """Fix the NLU YAML file formatting"""
    
    # Read the current file
    with open('rasa/data/nlu.yml', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix the examples formatting by removing extra spaces
    # Replace "    - example" with "  - example"
    content = re.sub(r'    - ', '  - ', content)
    
    # Write the fixed content
    with open('rasa/data/nlu.yml', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Fixed NLU YAML formatting - removed extra spaces")

if __name__ == "__main__":
    fix_nlu_file()

