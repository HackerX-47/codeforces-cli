import requests as req
import click
import json
import re
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types