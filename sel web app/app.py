from flask import Flask, render_template, request, jsonify
import subprocess
import traceback

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route to trigger Selenium script
@app.route('/run-test', methods=['POST'])
def run_test():
    try:
        # Log to check if the route is triggered
        print("Running Selenium Test...")
        
        # Run the Selenium script and capture output
        result = subprocess.run(['python', 'sele.py'], capture_output=True, text=True)

        # Return the output or errors to the frontend
        if result.returncode == 0:
            return jsonify({"status": "success", "output": result.stdout})
        else:
            return jsonify({"status": "error", "message": result.stderr})
    except Exception as e:
        print(traceback.format_exc())  # Logs errors in console
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
