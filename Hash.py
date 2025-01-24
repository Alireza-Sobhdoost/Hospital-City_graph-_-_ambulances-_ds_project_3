class Hash:
    def __init__(self):
        self.hash_value = 0x67452301
        self.magic_prime = 0x1000193

    def update(self, data):
        for char in data:
            self.hash_value ^= ord(char)
            self.hash_value *= self.magic_prime
            self.hash_value &= 0xFFFFFFFF  # Ensure hash_value stays within 32 bits

    def hexdigest(self):
        return hex(self.hash_value)[2:].zfill(8)
