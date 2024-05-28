## Flask Application Design for an Incremental Game

### HTML Files

**index.html:**
- Provides the main interface for the game, including:
    - Display the current game state (e.g., player level, resources, etc.).
    - Actions the player can take (e.g., buttons to upgrade, purchase items, etc.).

**upgrade.html:**
- Allows the player to upgrade specific aspects of the game (e.g., resource generation, attack power).

**purchase.html:**
- Provides a catalog of items or resources that the player can purchase.

### Routes

**@app.route('/')**
- Serves the **index.html** file, which displays the main game interface.

**@app.route('/upgrade')**
- Serves the **upgrade.html** file, allowing the player to upgrade game elements.

**@app.route('/purchase')**
- Serves the **purchase.html** file, where players can buy items or resources.

**@app.route('/process_upgrade', methods=['POST'])**
- Handles form submissions from the **upgrade.html** file, updates the game state, and redirects back to the main page.

**@app.route('/process_purchase', methods=['POST'])**
- Handles form submissions from the **purchase.html** file, processes the purchase, and redirects back to the main page.