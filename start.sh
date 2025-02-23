#!/bin/sh


# Get the service type from the first argument
SERVICE_TYPE=$1

case $SERVICE_TYPE in
    "bot")
        echo "Starting bot service..."
        uv run bot.py
        ;;
    *)
        echo "Invalid service type. Please use 'bot'"
        exit 1
        ;;
esac

