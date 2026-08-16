from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("MOCK_API_KEY")

class MockAIHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        if self.path != "/chat":
            self.send_response(404)
            self.end_headers()
            return

        # Check API key
        authorization = self.headers.get("Authorization")

        if authorization != f"Bearer {API_KEY}":
            self.send_response(401)
            self.end_headers()
            return

        # Read request body
        content_length = int(self.headers["Content-Length"])
        body = self.rfile.read(content_length)

        data = json.loads(body)
        prompt = data.get("prompt", "")

        # Rule-based mock AI
        if "python" in prompt.lower():
            output = "Python is a programming language."

        elif "json" in prompt.lower():
            output = "JSON is a text format commonly used for data exchange."

        else:
            output = f"Mock AI received your question: {prompt}"

        response = {
            "output": output
        }

        response_json = json.dumps(response).encode()

        self.send_response(200)
        self.send_header(
            "Content-Type",
            "application/json"
        )
        self.send_header(
            "Content-Length",
            str(len(response_json))
        )
        self.end_headers()

        self.wfile.write(response_json)


server = HTTPServer(
    ("localhost", 8000),
    MockAIHandler
)

print("Mock AI server running on http://localhost:8000")

server.serve_forever()