#!/bin/bash

# Force create the directory structure
mkdir -p /logs/verifier

# Run pytest using the correct --ctrf flag
pytest /tests/test_outputs.py --ctrf /logs/verifier/ctrf.json > /logs/verifier/pytest.log 2>&1
EXIT_CODE=$?

# Always write the reward file
if [ $EXIT_CODE -eq 0 ]; then
    echo "1" > /logs/verifier/reward.txt
    echo "Tests passed! Reward 1 written."
else
    echo "0" > /logs/verifier/reward.txt
    echo "Tests failed! Reward 0 written."
fi

# Explicit exit 0 so Harbor registers a clean grading run
exit 0
