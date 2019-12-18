#!/bin/sh
mkdir -p /app/.streamlit/

echo "\
[general]\n\
email = \"user@example.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS = false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
