#!/usr/bin/env python3

def generate_invitations(template, attendees):
    # Helper function to safely format strings with placeholders
    def safe_format(template, **kwargs):
        class SafeDict(dict):
            def __missing__(self, key):
                return "{%s}" % key
        return template.format_map(SafeDict(**kwargs))

    # Validate input types
    if not isinstance(template, str):
        print("Invalid input type for template.")
        return
    
    if not isinstance(attendees, list) or not all(isinstance(i, dict) for i in attendees):
        print("Invalid input type for attendees.")
        return
    
    # Check for empty inputs
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # Process each attendee and generate personalized invitations
    for index, attendee in enumerate(attendees, start=1):
        # Using safe_format to handle missing keys gracefully
        personal_invitation = safe_format(template, **attendee)
        
        # Constructing filename for each invitation
        filename = f"output_{index}.txt"
        
        # Writing the personalized invitation to a file
        with open(filename, 'w', encoding="utf-8") as file:
            file.write(personal_invitation)
        print(f"Generated {filename}.")