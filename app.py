# app.py
from flask import Flask, render_template, jsonify, redirect
from drone import Drone
from blockchain import Blockchain
from simulation import simulate_delivery
import threading, random

app = Flask(__name__)

# Initialize the system
blockchain = Blockchain()
drones = [Drone(i) for i in range(1, 4)]  # e.g., 3 drones

@app.route('/')
def dashboard():
    return render_template('dashboard.html', drones=drones, logs=blockchain.chain)

@app.route('/status')
def status():
    # Send JSON of drone info and logs for AJAX updates
    drones_data = [{
        "id": d.id,
        "status": d.status,
        "battery": round(d.battery, 1),
        "location": d.location
    } for d in drones]
    logs_data = [{
        "index": b["index"],
        "timestamp": b["timestamp"],
        "message": b["message"]
    } for b in blockchain.chain]
    return jsonify({"drones": drones_data, "logs": logs_data})

@app.route('/request_delivery')
def request_delivery():
    available = [d for d in drones if d.status == "Idle"]
    if not available:
        # No idle drone; in a real app we might notify user
        return redirect('/')
    drone = random.choice(available)
    dest = [random.randint(-5, 5), random.randint(-5, 5)]
    thread = threading.Thread(target=simulate_delivery, args=(drone, dest, blockchain))
    thread.daemon = True
    thread.start()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
