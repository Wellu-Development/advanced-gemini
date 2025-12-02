#!/bin/bash

# Script to load a persona profile into the Gemini CLI context.
# Usage: ./load_persona.sh <persona_name>

PERSONA_NAME=$1
AGENTS_DIR="agents"
ROOT_GEMINI_MD="./GEMINI.md"

if [ -z "$PERSONA_NAME" ]; then
    echo "Usage: ./load_persona.sh <persona_name>"
    echo "Available personas in '$AGENTS_DIR/':"
    find "$AGENTS_DIR" -maxdepth 2 -type f -name "GEMINI.md" -printf "%P\n" | sed 's/\/GEMINI.md//g' | sed 's/^/\t- /'
    exit 1
fi

PERSONA_PATH="$AGENTS_DIR/$PERSONA_NAME/GEMINI.md"

if [ ! -f "$PERSONA_PATH" ]; then
    echo "Error: Persona profile '$PERSONA_PATH' not found."
    echo "Available personas in '$AGENTS_DIR/':"
    find "$AGENTS_DIR" -maxdepth 2 -type f -name "GEMINI.md" -printf "%P\n" | sed 's/\/GEMINI.md//g' | sed 's/^/\t- /'
    exit 1
fi

cp "$PERSONA_PATH" "$ROOT_GEMINI_MD"

if [ $? -eq 0 ]; then
    echo "Successfully loaded '$PERSONA_NAME' persona. Context updated in '$ROOT_GEMINI_MD'."
    echo "You can now start gemini-cli: gemini"
else
    echo "Error: Failed to load '$PERSONA_NAME' persona."
fi
