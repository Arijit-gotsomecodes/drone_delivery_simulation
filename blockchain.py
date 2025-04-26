# blockchain.py
import datetime, hashlib, json

class Blockchain:
    def __init__(self):
        self.chain = []

    def add_block(self, message):
        previous_hash = self.chain[-1]["hash"] if self.chain else "0"
        block = {
            "index": len(self.chain) + 1,
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "message": message,
            "previous_hash": previous_hash
        }
        # Compute SHA256 hash of the block’s contents
        block_string = json.dumps(block, sort_keys=True).encode()
        block["hash"] = hashlib.sha256(block_string).hexdigest()
        self.chain.append(block)
        return block
    