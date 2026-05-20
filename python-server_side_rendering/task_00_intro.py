#!/usr/bin/python3
"""
A simple string templating program to generate personalized invitations.
"""
import os


def generate_invitations(template, attendees):
    """
    Generates invitation files from a template and a list of attendees.
    """
    # 1. Giriş tiplərinin yoxlanılması
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # 2. Boş şablon yoxlanışı
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # 3. Boş iştirakçı siyahısı yoxlanışı
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # 4. Hər bir iştirakçı üçün şablonun emal edilməsi
    for index, attendee in enumerate(attendees, start=1):
        processed_template = template

        # Şablondakı bütün açarları təyin edirik
        keys = ["name", "event_title", "event_date", "event_location"]

        for key in keys:
            # Əgər açar yoxdursa və ya dəyəri None-dırsa, 'N/A' qoyuruq
            value = attendee.get(key)
            if value is None:
                value = "N/A"

            placeholder = "{" + key + "}"
            processed_template = processed_template.replace(placeholder, str(value))

        # 5. Output faylının yazılması
        filename = "output_{}.txt".format(index)
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(processed_template)
        except Exception as e:
            print("Error writing to file {}: {}".format(filename, e))
