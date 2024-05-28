
# main.py

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialize the game state
player_level = 1
resources = 0

# Routes
@app.route('/')
def index():
    return render_template('index.html', player_level=player_level, resources=resources)


@app.route('/upgrade')
def upgrade():
    return render_template('upgrade.html', player_level=player_level)


@app.route('/purchase')
def purchase():
    return render_template('purchase.html', resources=resources)


@app.route('/process_upgrade', methods=['POST'])
def process_upgrade():
    global player_level, resources
    upgrade_type = request.form['upgrade_type']

    if upgrade_type == 'resource_generation':
        resources += 10
    elif upgrade_type == 'attack_power':
        player_level += 1

    return redirect(url_for('index'))


@app.route('/process_purchase', methods=['POST'])
def process_purchase():
    global resources
    item_type = request.form['item_type']

    if item_type == 'health_potion':
        resources -= 10
    elif item_type == 'attack_upgrade':
        resources -= 20

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
