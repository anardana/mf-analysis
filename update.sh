#!/usr/bin/env bash
# Run like 'source update.sh'

ENVIRONMENT_NAME='mf-analysis-env'


echo "Evaluate if virtual environment $ENVIRONMENT_NAME needs to be created ..."
if ! conda info --env | grep -w "$ENVIRONMENT_NAME"; then
    echo "Creating environment: $ENVIRONMENT_NAME"
    conda create -n "$ENVIRONMENT_NAME" python=3.6.3 pip -y
    echo "Environment: $ENVIRONMENT_NAME created"
fi

if source activate "$ENVIRONMENT_NAME"; then
    echo "Environment set to: $ENVIRONMENT_NAME"

    echo "Installing requirements ..."
    pip install -r requirements.txt
    echo "Requirements installed in: $ENVIRONMENT_NAME"
else
    echo "ERROR: Failed to create and load environment $ENVIRONMENT_NAME"
fi
